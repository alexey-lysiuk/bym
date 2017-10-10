#
#    Build Your Mac: Configurable build environment for macOS
#    Copyright (C) 2017 Alexey Lysiuk
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

import cPickle
import hashlib
import os
import shutil
import subprocess
import sys
import urllib2

# import command
import configuration
import patch


class Package(object):
    def __init__(self, name, source, checksum, commands, dependencies=None, environment=None):
        self.name = name
        self.source = source
        self.checksum = checksum
        self.commands = commands
        self.dependencies = dependencies
        self.environment = environment

        self._patch_path = configuration.patches_path + self.name + '.diff'
        self._work_path = None
        self._settings_path = None
        self._filename = None

    def build(self):
        self._filename = self.source.rsplit('/', 1)[1]

        if os.path.exists(self._filename):
            checksum = _calculate_checksum(self._filename)
        else:
            checksum = self._download()

        if checksum != self.checksum:
            os.unlink(self._filename)
            raise Exception("Checksum for %s doesn't match!" % self._filename)

        self._work_path = self._guess_work_path()
        self._settings_path = self._work_path + os.sep + '~bym_cached_settings.txt'

        if not os.path.exists(self._work_path):
            self._extract()

            if os.path.exists(self._patch_path):
                patch_set = patch.fromfile(self._patch_path)

                if not patch_set.apply(root=self._work_path):
                    raise Exception('Failed to apply patch %s' % self._patch_path)

        environment = configuration.environment.copy()
        _merge_environment(environment, self.environment)

        current_settings = self._make_settings(environment)
        previous_setting = self._read_settings()
        up_to_date = current_settings == previous_setting

        if up_to_date and not configuration.force_build:
            return

        if isinstance(self.commands, tuple) or isinstance(self.commands, list):
            for command in self.commands:
                command.execute(self._work_path, environment)
        else:
            self.commands.execute(self._work_path, environment)

        with open(self._settings_path, 'wb') as f:
            cPickle.dump(current_settings, f)

    def _download(self):
        response = urllib2.urlopen(self.source)
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

    def _extract(self):
        try:
            subprocess.check_call(['tar', '-xf', self._filename])
        except (IOError, subprocess.CalledProcessError):
            shutil.rmtree(self._work_path, ignore_errors=True)
            raise

    def _guess_work_path(self):
        files = subprocess.check_output(['tar', '-tf', self._filename])
        result = ''
        shortest = sys.maxint

        guess_filenames = (
            'configure',
            'Makefile',
            'makefile',
            'autogen.sh',
            'CMakeLists.txt'
        )

        for name in files.split('\n'):
            parts = name.split('/')
            parts_count = len(parts)

            if parts[-1] in guess_filenames:
                if parts_count < shortest:
                    result = '/'.join(parts[:-1])
                    shortest = parts_count

        return result

    def _make_settings(self, environment):
        stripped_environment = {}

        # Store important environment variables only
        for var in environment:
            if var in configuration.environment_variables:
                stripped_environment[var] = environment[var]

        settings = {
            'ver': 2,
            'chk': self.checksum,
            'cmd': self.commands,
            'dep': self.dependencies,
            'env': stripped_environment,
        }

        patch_path = self._patch_path

        if os.path.exists(patch_path):
            settings['patch'] = _calculate_checksum(patch_path)

        return settings

    def _read_settings(self):
        try:
            with open(self._settings_path, 'rb') as f:
                return cPickle.load(f)
        except IOError, cPickle.UnpicklingError:
            return {}


def _calculate_checksum(filename):
    checksum = hashlib.sha256()

    with open(filename, 'rb') as f:
        data = True

        while data:
            data = f.read(64 * 1024)
            checksum.update(data)

    return checksum.hexdigest()


def _merge_environment(merged, source):
    for var in source:
        if var in merged:
            merged[var] += ' ' + source[var]
        else:
            merged[var] = source[var]