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

import argparse
import os
import shlex
import subprocess


_self_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
_root_path = os.path.realpath(_self_path + os.pardir) + os.sep

patch_path = _root_path + 'patch' + os.sep
state_path = _root_path + 'state' + os.sep

# Parse command line

_parser = argparse.ArgumentParser(description='Build Your Mac: Configurable build environment for macOS')
_parser.add_argument('packages', metavar='package', nargs='+',
                     help='list of package names to build')

_parser.add_argument('--build-path', default=_root_path + 'build',
                     help='directory for source code and intermediate files')
_parser.add_argument('--install-path', default=_root_path + 'install',
                     help='installation directory also knows as prefix')

_parser.add_argument('--make-exe', default='make',
                     help='path to make executable')
_parser.add_argument('--make-args', default='',
                     help='additional arguments for make')

_parser.add_argument('--configure-args', default='',
                     help='additional arguments for ./configure')

_parser.add_argument('--cmake-exe', default='cmake',
                     help='path to cmake executable')
_parser.add_argument('--cmake-args', default='',
                     help='additional arguments for cmake')

_parser.add_argument('--extra-flags', default='',
                     help='string appended to all ...FLAGS environment variables')

_parser.add_argument('--force-build', action='store_true',
                     help='Do all build steps even if package is up-to-date')

_arguments = _parser.parse_args()


targets = _arguments.packages

# Setup configuration options

build_path = _arguments.build_path
install_path = _arguments.install_path
bin_path = install_path + '/bin'
include_path = install_path + '/include'
lib_path = install_path + '/lib'

make_executable = _arguments.make_exe
make_arguments = tuple(shlex.split(_arguments.make_args))

configure_arguments = tuple(shlex.split(_arguments.configure_args))

cmake_executable = _arguments.cmake_exe
cmake_arguments = tuple(shlex.split(_arguments.cmake_args))

extra_flags = _arguments.extra_flags

force_build = _arguments.force_build


# Prerequisites

def _check_cmake(exe_path):
    try:
        subprocess.check_output([exe_path, '--version'])
    except (OSError, subprocess.CalledProcessError):
        return False

    return True


def _have_cmake():
    global cmake_executable

    if _check_cmake(cmake_executable):
        return True

    if 'cmake' != cmake_executable:
        # Do not proceed with CMake.app check if custom executable is specified
        return False

    cmake_app_exe = '/Applications/CMake.app/Contents/bin/cmake'

    if _check_cmake(cmake_app_exe):
        cmake_executable = cmake_app_exe
        return True

    return False


prerequisites = (
    'pkg-config',
)

autogen_prerequisites = (
    'autoconf',
    'automake'
)

cmake_prerequisites = () if _have_cmake() else ('cmake',)


# Setup environment variables

def _append_flags(name, value):
    environment[name] = name in environment and (environment[name] + ' ' + value) or value


def _prepend_path(value):
    environment['PATH'] = 'PATH' in environment and (value + ':' + environment['PATH']) or value


environment = os.environ.copy()

_compilation_environment_variables = (
    'CPPFLAGS',
    'CFLAGS',
    'CXXFLAGS',
    'OBJCFLAGS',
    'OBJCXXFLAGS',
)

environment_variables = _compilation_environment_variables + (
    'LDFLAGS',
    'PATH',
)

for variable in _compilation_environment_variables:
    _append_flags(variable, '-I' + include_path)
    _append_flags(variable, extra_flags)

_append_flags('LDFLAGS', '-L' + lib_path)
_append_flags('LDFLAGS', extra_flags)

_prepend_path(bin_path)


_custom_filename = __name__ + '.custom.py'

if os.path.exists(_custom_filename):
    execfile(_custom_filename)
