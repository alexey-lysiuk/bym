#!/usr/bin/env python

#
#    Build Your Mac: Hackable build environment for macOS
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

import config
import hacking


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


def _extract(filename, work_dir):
    try:
        subprocess.check_call(['tar', '-xf', filename])
    except:
        shutil.rmtree(work_dir, ignore_errors=True)
        raise


_GUESS_FILENAMES = (
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

        if parts[-1] in _GUESS_FILENAMES:
            if parts_count < shortest:
                result = '/'.join(parts[:-1])
                shortest = parts_count

    return result


def _merge_environ(dst, src):
    for e in src:
        if e in dst:
            dst[e] += ' ' + src[e]
        else:
            dst[e] = src[e]


def _prefix_environ(environ):
    compile_flag = ' -I' + config.INSTALL_PATH + '/include'
    environ['CPPFLAGS'] += compile_flag
    environ['CFLAGS'] += compile_flag
    environ['CXXFLAGS'] += compile_flag
    environ['OBJCFLAGS'] += compile_flag
    environ['OBJCXXFLAGS'] += compile_flag
    environ['LDFLAGS'] += ' -L' + config.INSTALL_PATH + '/lib'
    environ['PATH'] = config.INSTALL_PATH + '/bin:' + environ['PATH']


def _is_configure(command):
    return command[0].endswith('configure')


def _is_cmake(command):
    return command[0].endswith('cmake')


def _prefix_command(command):
    if _is_configure(command):
        return command + ('--prefix=' + config.INSTALL_PATH, )
    elif _is_cmake(command):
        return command + ('-DCMAKE_INSTALL_PREFIX=' + config.INSTALL_PATH, )
    else:
        return command


def _settings_filepath(work_dir):
    return work_dir + os.sep + '~bym_cached_settings.txt'


def _make_settings(target, environ):
    stripped_environ = {}

    # Store important environment variables only
    for var in environ:
        if var in config.ENVIRON:
            stripped_environ[var] = environ[var]

    return {
        'ver': 1,
        'chk': target['chk'],
        'cmd': target['cmd'],
        'env': stripped_environ,
    }


def _read_settings(work_dir):
    try:
        with open(_settings_filepath(work_dir), 'rb') as f:
            return cPickle.load(f)
    except IOError, cPickle.UnpicklingError:
        return {}


def _build(name):
    target = config.TARGETS[name]
    url = target['url']
    splitted = url.rsplit('/', 1)
    filename = splitted[1]

    if not os.path.exists(filename):
        checksum = _download(url, filename)

        if checksum != target['chk']:
            os.unlink(filename)
            raise Exception("Checksum for %s doesn't match!" % filename)

    work_dir = _guess_work_dir(filename)

    if not os.path.exists(work_dir):
        _extract(filename, work_dir)

    environ = os.environ.copy()
    _merge_environ(environ, config.ENVIRON)
    _merge_environ(environ, _dict_value(target, 'env', {}))
    _prefix_environ(environ)

    current_settings = _make_settings(target, environ)
    previous_setting = _read_settings(work_dir)
    up_to_date = current_settings == previous_setting

    for command in target['cmd']:
        # avoid overhead of running configure without changes
        # in source code, build commands and environment
        if up_to_date and _is_configure(command):
            continue

        command = _prefix_command(command)
        subprocess.check_call(command, cwd=work_dir, env=environ)

    with open(_settings_filepath(work_dir), 'wb') as f:
        cPickle.dump(current_settings, f)


def _main():
    if len(sys.argv) < 2:
        print('Usage: bym.py [target ...]')
        sys.exit(1)

    hacking.main()

    to_build = []

    def add_deps(root):
        if root in to_build:
            return

        deps = _dict_value(config.TARGETS[root], 'dep', ())

        for dep in deps:
            add_deps(dep)

        to_build.append(root)

    for name in sys.argv[1:]:
        add_deps(name)

    if not os.path.exists(config.BUILD_PATH):
        os.makedirs(config.BUILD_PATH)

    os.chdir(config.BUILD_PATH)

    for name in to_build:
        _build(name)


if __name__ == '__main__':
    _main()
