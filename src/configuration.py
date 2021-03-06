#
#    Build Your Mac: Configurable build environment for macOS
#    Copyright (C) 2017-2020 Alexey Lysiuk
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
import platform
import shlex
import subprocess


src_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
root_path = os.path.realpath(src_path + os.pardir) + os.sep

patch_path = root_path + 'patch' + os.sep

# Parse command line

_parser = argparse.ArgumentParser(description='Build Your Mac: Configurable build environment for macOS')
_parser.add_argument('packages', metavar='package', nargs='+',
                     help='list of package names to build')

_parser.add_argument('--build-path', default=root_path + 'build',
                     help='directory for source code and intermediate files')
_parser.add_argument('--cache-path', default=root_path + 'cache',
                     help='directory for downloaded source code packages')
_parser.add_argument('--install-path', default=root_path + 'install',
                     help='installation directory also knows as prefix')

_parser.add_argument('--arch', default=platform.machine(),
                     help='target architecture')

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

_parser.add_argument('--download-retries', default=3,
                     help='Number of source code download retries')

_arguments = _parser.parse_args()


targets = _arguments.packages
architecture = _arguments.arch


def _append_arch(path: str) -> str:
    if not path.endswith(os.sep):
        path = path + os.sep

    return path.endswith(architecture) and path or (path + architecture)


# Setup configuration options

build_path = _append_arch(_arguments.build_path)
cache_path = _arguments.cache_path
install_path = _append_arch(_arguments.install_path)
bin_path = install_path + os.sep + 'bin'
native_bin_path = bin_path.replace(architecture, platform.machine())
include_path = install_path + os.sep + 'include'
lib_path = install_path + os.sep + 'lib'
state_path = _append_arch(root_path + 'state') + os.sep


make_executable = _arguments.make_exe
make_arguments = tuple(shlex.split(_arguments.make_args))

configure_arguments = tuple(shlex.split(_arguments.configure_args))

cmake_executable = _arguments.cmake_exe
cmake_arguments = tuple(shlex.split(_arguments.cmake_args))

extra_flags = _arguments.extra_flags

force_build = _arguments.force_build

download_retries = _arguments.download_retries


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
    'CARGO_HOME',
    'LDFLAGS',
    'PATH',
)

for variable in _compilation_environment_variables:
    _append_flags(variable, '-I' + include_path)
    _append_flags(variable, extra_flags)

_append_flags('LDFLAGS', '-L' + lib_path)
_append_flags('LDFLAGS', '-lc++ -lc++abi')
_append_flags('LDFLAGS', extra_flags)

_append_flags('CARGO_HOME', install_path + '/share/cargo')

_prepend_path(native_bin_path)

_cmake_dir = os.path.dirname(cmake_executable)

if len(_cmake_dir) > 0:
    _prepend_path(_cmake_dir)


try:
    # noinspection PyUnresolvedReferences
    import configuration_user
except ImportError:
    pass
