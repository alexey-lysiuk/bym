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


# Parse command line

_self_path = os.path.dirname(os.path.abspath(__file__))

_parser = argparse.ArgumentParser(description='Build Your Mac: Configurable build environment for macOS')
_parser.add_argument('packages', metavar='package', nargs='+',
                     help='list of package names to build')

_parser.add_argument('--build-path', default=_self_path + '/build',
                     help='directory for source code and intermediate files')
_parser.add_argument('--install-path', default=_self_path + '/install',
                     help='installation directory also knows as prefix')

_parser.add_argument('--make-exe', default='make',
                     help='path to make executable')
_parser.add_argument('--make-args', default='',
                     help='additional arguments for make')

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

cmake_executable = _arguments.cmake_exe
cmake_arguments = tuple(shlex.split(_arguments.cmake_args))

extra_flags = _arguments.extra_flags

force_build = _arguments.force_build


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
