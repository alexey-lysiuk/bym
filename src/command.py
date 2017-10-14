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

import subprocess

import configuration


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
        arguments = (configuration.cmake_executable, '-DCMAKE_INSTALL_PREFIX=' + configuration.install_path) \
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
