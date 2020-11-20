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
import typing


class Configuration:
    def __init__(self, arguments: typing.Iterable[str]):
        self.module_path = os.path.dirname(os.path.abspath(__file__)) + os.sep
        self.root_path = os.path.realpath(self.module_path + os.pardir) + os.sep

        args = self._parse(arguments)
        assert args

        self.targets = args.packages
        self.architecture = args.arch

        # Paths
        self.build_path = self._append_arch_to_path(args.build_path)
        self.cache_path = args.cache_path
        self.install_path = self._append_arch_to_path(args.install_path)
        self.patch_path = self._append_arch_to_path(self.root_path + 'patch') + os.sep
        self.state_path = self._append_arch_to_path(self.root_path + 'state') + os.sep

        self.bin_path = self.install_path + os.sep + 'bin'
        self.include_path = self.install_path + os.sep + 'include'
        self.lib_path = self.install_path + os.sep + 'lib'

        # Build options
        self.configure_arguments = tuple(shlex.split(args.configure_args))
        self.make_executable = args.make_exe
        self.make_arguments = tuple(shlex.split(args.make_args))
        self.extra_flags = args.extra_flags

        self.cmake_executable = args.cmake_exe
        self.cmake_arguments = tuple(shlex.split(args.cmake_args))

        self.force_build = args.force_build
        self.download_retries = args.download_retries

        # Prerequisites
        self.prerequisites = (
            'pkg-config',
        )
        self.autogen_prerequisites = (
            'autoconf',
            'automake'
        )
        self.cmake_prerequisites = () if self._have_cmake() else ('cmake',)

        # Setup environment variables
        self.environment = os.environ.copy()

        compilation_environment_variables = (
            'CPPFLAGS',
            'CFLAGS',
            'CXXFLAGS',
            'OBJCFLAGS',
            'OBJCXXFLAGS',
        )

        self.environment_variables = compilation_environment_variables + (
            'CARGO_HOME',
            'LDFLAGS',
            'PATH',
        )

        for variable in compilation_environment_variables:
            self._append_flags(variable, '-I' + self.include_path)
            self._append_flags(variable, self.extra_flags)

        self._append_flags('LDFLAGS', '-L' + self.lib_path)
        self._append_flags('LDFLAGS', '-lc++ -lc++abi')
        self._append_flags('LDFLAGS', self.extra_flags)

        self._append_flags('CARGO_HOME', self.install_path + '/share/cargo')

        # Executable search paths
        self._prepend_path(self.bin_path)

        cmake_dir = os.path.dirname(self.cmake_executable)

        if len(cmake_dir) > 0:
            self._prepend_path(cmake_dir)

    def _parse(self, arguments):
        _parser = argparse.ArgumentParser(description='Build Your Mac: Configurable build environment for macOS')
        _parser.add_argument('packages', metavar='package', nargs='+',
                             help='list of package names to build')

        assert self.root_path

        _parser.add_argument('--build-path', default=self.root_path + 'build',
                             help='directory for source code and intermediate files')
        _parser.add_argument('--cache-path', default=self.root_path + 'cache',
                             help='directory for downloaded source code packages')
        _parser.add_argument('--install-path', default=self.root_path + 'install',
                             help='installation directory also knows as prefix')

        _parser.add_argument('--arch', default=platform.machine(),
                             help='target architecture, can be specified more than once')

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

        return _parser.parse_args(args=arguments)

    def _append_arch_to_path(self, path: str) -> str:
        if not path.endswith(os.sep):
            path = path + os.sep

        assert self.architecture
        return path + self.architecture

    @staticmethod
    def _check_cmake(exe_path):
        try:
            subprocess.check_output([exe_path, '--version'])
        except (OSError, subprocess.CalledProcessError):
            return False

        return True

    def _have_cmake(self):
        if Configuration._check_cmake(self.cmake_executable):
            return True

        if 'cmake' != self.cmake_executable:
            # Do not proceed with CMake.app check if custom executable is specified
            return False

        cmake_app_exe = '/Applications/CMake.app/Contents/bin/cmake'

        if Configuration._check_cmake(cmake_app_exe):
            self.cmake_executable = cmake_app_exe
            return True

        return False

    def _append_flags(self, name, value):
        self.environment[name] = name in self.environment and (self.environment[name] + ' ' + value) or value

    def _prepend_path(self, value):
        self.environment['PATH'] = 'PATH' in self.environment and (value + ':' + self.environment['PATH']) or value
