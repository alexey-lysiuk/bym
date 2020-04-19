#
#    Build Your Mac: Configurable build environment for macOS
#    Copyright (C) 2017-2019 Alexey Lysiuk
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pickle
import hashlib
import os
import shutil
import ssl
import subprocess
import sys
import urllib.error
import urllib.request

import configuration
import patch


class BuildState(object):
    def __init__(self, package):
        patch_path = package.patch_path()

        self.version = 1
        self.name = package.name
        self.checksum = package.checksum
        self.commands = package.commands
        self.dependencies = package.dependencies
        self.environment = _stripped_environment()
        self.patch_checksum = _calculate_checksum(patch_path) if os.path.exists(patch_path) else None

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __ne__(self, other):
        return not self == other

    def as_tuple(self):
        return (
            self.version,
            self.name,
            self.checksum,
            self.commands,
            self.dependencies,
            self.environment,
            self.patch_checksum
        )

    def uptodate(self):
        try:
            with self._open('rb') as f:
                other = pickle.load(f)

                # compare versions explicitly to avoid potential reference to undefined member
                return self.version == other.version and self == other

        except (IOError, pickle.UnpicklingError):
            return False

    def save(self):
        # TODO: handle errors
        with self._open('wb') as f:
            pickle.dump(self, f)

    def _open(self, mode):
        return open(configuration.state_path + self.name + '.p', mode)


class Package(object):
    def __init__(self, name, source, checksum, commands, dependencies=()):
        self.name = name
        self.source = source
        self.checksum = checksum
        self.commands = commands
        self.dependencies = dependencies

        self._filename = None
        self._work_path = None

    def build(self):
        state = BuildState(self)

        if not configuration.force_build and state.uptodate():
            return

        print('=' * 80 + '\n Building ' + self.name + '\n' + '=' * 80)

        self._setup_workdir()

        if isinstance(self.commands, tuple) or isinstance(self.commands, list):
            for command in self.commands:
                command.execute(self._work_path, configuration.environment)
        else:
            self.commands.execute(self._work_path, configuration.environment)

        state.save()

        self._work_path = None
        self._filename = None

    def _setup_workdir(self):
        assert not self._filename
        self._filename = self.source.rsplit('/', 1)[1]

        if os.path.exists(self._filename):
            checksum = _calculate_checksum(self._filename)
        else:
            retry = 0

            while retry <= configuration.download_retries:
                try:
                    checksum = self._download()

                    if checksum != self.checksum:
                        os.unlink(self._filename)
                        raise Exception("Checksum for %s doesn't match!" % self._filename)
                    else:
                        break

                except Exception as e:
                    print(e)
                    retry += 1

            if retry > configuration.download_retries:
                raise Exception("Download of {self._filename} failed after {configuration.download_retries} retries")

        assert not self._work_path
        self._work_path = self._guess_work_path()

        if not os.path.exists(self._work_path):
            self._extract()
            self._apply_patch()

    def _download(self):
        try:
            response = urllib.request.urlopen(self.source, context=_ssl_context)
        except (urllib.error.HTTPError, urllib.error.URLError):
            request = urllib.request.Request(self.source)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0')
            opener = urllib.request.build_opener()
            response = opener.open(request)

        checksum = hashlib.sha256()
        step = 64 * 1024
        total = 0

        try:
            with open(self._filename, 'wb') as f:
                while True:
                    data = response.read(step)
                    total += len(data)

                    if not data:
                        sys.stdout.write('\n')
                        return checksum.hexdigest()

                    f.write(data)
                    checksum.update(data)

                    sys.stdout.write('\rDownloading %s: %i bytes' % (self._filename, total))
                    sys.stdout.flush()
        except IOError:
            os.unlink(self._filename)
            raise

    def _guess_work_path(self):
        files = subprocess.check_output(['tar', '-tf', self._filename]).decode("utf-8")
        files = files.split('\n')

        for filename in files:
            if '/' in filename:
                return filename[:filename.find('/')]

        raise Exception("Failed to guess work path for " + self._filename)

    def _extract(self):
        print("Extracting %s..." % self._filename)

        try:
            subprocess.check_call(['tar', '-xf', self._filename])
        except (IOError, subprocess.CalledProcessError):
            shutil.rmtree(self._work_path, ignore_errors=True)
            raise

    def _apply_patch(self):
        patch_path = self.patch_path()

        if not os.path.exists(patch_path):
            return

        patch_set = patch.fromfile(patch_path)

        if not patch_set or not patch_set.apply(root=self._work_path):
            raise Exception('Failed to apply patch %s' % patch_path)

    def patch_path(self):
        return configuration.patch_path + self.name + '.diff'


def _calculate_checksum(filename):
    checksum = hashlib.sha256()

    with open(filename, 'rb') as f:
        data = True

        while data:
            data = f.read(64 * 1024)
            checksum.update(data)

    return checksum.hexdigest()


def _stripped_environment():
    # Store important environment variables only
    environment = configuration.environment
    stripped_environment = {}

    for var in environment:
        if var in configuration.environment_variables:
            stripped_environment[var] = environment[var]

    return stripped_environment


_ssl_context = ssl.create_default_context(cafile=configuration.src_path + 'cacert.pem')
