#!/usr/bin/env python

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

try:
    # Python 2
    # noinspection PyUnresolvedReferences
    from urllib2 import urlopen
except ImportError:
    # Python 3
    # noinspection PyUnresolvedReferences
    from urllib.request import urlopen

import configuration
import repository
import patch


def _dict_value(dictionary, key, default):
    return key in dictionary and dictionary[key] or default


def _download(url, filename):
    response = urlopen(url)
    checksum = hashlib.sha256()
    step = 4096
    total = 0

    try:
        with open(filename, 'wb') as f:
            while True:
                data = response.read(step)
                total += step

                if not data:
                    sys.stdout.write('\n')
                    return checksum.hexdigest()

                f.write(data)
                checksum.update(data)

                sys.stdout.write('\rDownloading %s: %i bytes' % (filename, total))
                sys.stdout.flush()
    except IOError:
        os.unlink(filename)
        raise


def _calculate_checksum(filename):
    checksum = hashlib.sha256()

    with open(filename, 'rb') as f:
        data = True

        while data:
            data = f.read(4096)
            checksum.update(data)

    return checksum.hexdigest()


def _extract(filename, work_dir):
    try:
        subprocess.check_call(['tar', '-xf', filename])
    except:
        shutil.rmtree(work_dir, ignore_errors=True)
        raise


_guess_filenames = (
    'configure',
    'Makefile',
    'autogen.sh',
    'CMakeLists.txt'
)


def _guess_work_dir(filename):
    files = subprocess.check_output(['tar', '-tf', filename])
    result = ''
    shortest = sys.maxint

    for name in files.split('\n'):
        parts = name.split('/')
        parts_count = len(parts)

        if parts[-1] in _guess_filenames:
            if parts_count < shortest:
                result = '/'.join(parts[:-1])
                shortest = parts_count

    return result


def _settings_filepath(work_dir):
    return work_dir + os.sep + '~bym_cached_settings.txt'


def _make_settings(package, environment):
    stripped_environment = {}

    # Store important environment variables only
    for var in environment:
        if var in configuration.environment_variables:
            stripped_environment[var] = environment[var]

    return {
        'ver': 1,
        'chk': package['chk'],
        'cmd': package['cmd'],
        'env': stripped_environment,
    }


def _read_settings(work_dir):
    try:
        with open(_settings_filepath(work_dir), 'rb') as f:
            return cPickle.load(f)
    except IOError, cPickle.UnpicklingError:
        return {}


def _build(target):
    print('-' * 80)
    print('- Processing package: %s' % target)
    print('-' * 80)

    package = repository.packages[target]

    url = package['src']
    filename = url.rsplit('/', 1)[1]

    if os.path.exists(filename):
        checksum = _calculate_checksum(filename)
    else:
        checksum = _download(url, filename)

    if checksum != package['chk']:
        os.unlink(filename)
        raise Exception("Checksum for %s doesn't match!" % filename)

    work_dir = _guess_work_dir(filename)

    if not os.path.exists(work_dir):
        _extract(filename, work_dir)

        if target in repository.patches:
            patch_set = patch.fromstring(repository.patches[target])
            patch_set.apply(root=work_dir)

    current_settings = _make_settings(package, configuration.environment)
    previous_setting = _read_settings(work_dir)

    if current_settings == previous_setting:
        # package is up-to-date
        return

    for command in package['cmd']:
        subprocess.check_call(command, cwd=work_dir, env=configuration.environment)

    with open(_settings_filepath(work_dir), 'wb') as f:
        cPickle.dump(current_settings, f)


def _make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def _add_dependencies(target, packages):
    if target in packages:
        return

    dependencies = _dict_value(repository.packages[target], 'dep', ())

    for dependency in dependencies:
        _add_dependencies(dependency, packages)

    packages.append(target)


def _main():
    targets = list(repository.prerequisites)

    for target in configuration.targets:
        _add_dependencies(target, targets)

    _make_directory(configuration.build_path)
    _make_directory(configuration.bin_path)
    _make_directory(configuration.include_path)
    _make_directory(configuration.lib_path)

    os.chdir(configuration.build_path)

    for target in targets:
        _build(target)


if __name__ == '__main__':
    _main()
