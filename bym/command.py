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

import os
import subprocess

from . import configuration


class Command(object):
    def __init__(self, *arguments):
        self._arguments = arguments
        self._previous = None
        self._prerequisites = ()

    def execute(self, workdir, environment):
        if self._previous:
            self._previous.execute(workdir, environment)

        subprocess.check_call(self._arguments, cwd=workdir, env=environment)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple() if isinstance(other, Command) else False

    def __ne__(self, other):
        return not self == other

    def as_tuple(self):
        return self._arguments, self._previous, self._prerequisites

    def prerequisites(self):
        return (self._previous.prerequisites() if self._previous else ()) + self._prerequisites


class CreateDirectories(Command):
    def execute(self, workdir, environment):
        if self._previous:
            self._previous.execute(workdir, environment)

        # TODO: handle OSError, IOError

        prev_workdir = os.getcwd()
        os.chdir(workdir)

        for dirname in self._arguments:
            if not os.path.exists(dirname):
                os.makedirs(dirname)

        os.chdir(prev_workdir)


class CreateFile(Command):
    def execute(self, workdir, environment):
        if self._previous:
            self._previous.execute(workdir, environment)

        # TODO: handle OSError, IOError

        prev_workdir = os.getcwd()
        os.chdir(workdir)

        filename, content = self._arguments

        with open(filename, 'w') as f:
            f.write(content)

        os.chdir(prev_workdir)


class Autogen(Command):
    def __init__(self, *arguments):
        arguments = ('./autogen.sh',) + arguments
        super(Autogen, self).__init__(*arguments)
        self._prerequisites = configuration.autogen_prerequisites


class Configure(Command):
    def __init__(self, *arguments):
        arguments = ('./configure', '--prefix=' + configuration.install_path) + configuration.configure_arguments + arguments
        super(Configure, self).__init__(*arguments)


class ConfigureStatic(Configure):
    def __init__(self, *arguments):
        arguments = ('--enable-static', '--disable-shared') + arguments
        super(ConfigureStatic, self).__init__(*arguments)


class CMake(Command):
    def __init__(self, *arguments):
        prefix_arg = '-DCMAKE_INSTALL_PREFIX=' + configuration.install_path
        arguments = (configuration.cmake_executable, prefix_arg, '-DCMAKE_BUILD_TYPE=Release') \
            + configuration.cmake_arguments + arguments + ('.',)
        super(CMake, self).__init__(*arguments)
        self._prerequisites = configuration.cmake_prerequisites


class Make(Command):
    def __init__(self, *arguments):
        arguments = (configuration.make_executable,) + configuration.make_arguments + arguments
        super(Make, self).__init__(*arguments)


class Install(Make):
    def __init__(self, *arguments):
        arguments += ('install',)
        super(Install, self).__init__(*arguments)


class ConfigureInstall(Install):
    def __init__(self, *arguments):
        super(ConfigureInstall, self).__init__()
        self._previous = Configure(*arguments)


class ConfigureStaticInstall(Install):
    def __init__(self, *arguments):
        super(ConfigureStaticInstall, self).__init__()
        self._previous = ConfigureStatic(*arguments)


class CMakeInstall(Install):
    def __init__(self, *arguments):
        super(CMakeInstall, self).__init__()
        self._previous = CMake(*arguments)


class PythonVenv(Command):
    def execute(self, workdir, environment):
        if self._previous:
            self._previous.execute(workdir, environment)

        python_path = configuration.bin_path + os.sep + 'python3'

        if not os.path.exists(python_path):
            Command('python3', '-Em', 'venv', configuration.install_path).execute(workdir, environment)

        args = (python_path, '-E') + self._arguments
        Command(*args).execute(workdir, environment)


class PythonSetupTools(PythonVenv):
    def __init__(self, *arguments):
        arguments = ('setup.py', '--no-user-cfg', 'install') + arguments
        super(PythonVenv, self).__init__(*arguments)


class Meson(Command):
    def __init__(self, *arguments):
        super(Meson, self).__init__(*arguments)
        self._prerequisites = ('meson', 'ninja')

    def execute(self, workdir, environment):
        build_dir = '_bym_build'
        CreateDirectories(build_dir).execute(workdir, environment)
        workdir += os.sep + build_dir

        configure_args = (
            configuration.bin_path + os.sep + 'meson',
            '--prefix=' + configuration.install_path,
            '--buildtype=release',
            '--default-library=static',
            '..'
        )
        Command(*configure_args).execute(workdir, environment)
        Command('ninja', 'install').execute(workdir, environment)


Library = ConfigureStaticInstall
Tool = ConfigureInstall
