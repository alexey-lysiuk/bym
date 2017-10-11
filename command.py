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

# import functools
import subprocess

import configuration


# @functools.total_ordering
class Command(object):
    def __init__(self, *args):
        self.args = args
        self.prev = None

    def execute(self, workdir, environment):
        if self.prev:
            self.prev.execute(workdir, environment)

        subprocess.check_call(self.args, cwd=workdir, env=environment)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __ne__(self, other):
        return not self == other

    # def __lt__(self, other):
    #     return self.as_tuple() < other.as_tuple()
    #
    # def __hash__(self):
    #     return hash(self.as_tuple())

    def as_tuple(self):
        return self.args, self.prev

    def is_configure(self):
        return isinstance(self, Configure) or (self.prev.is_configure() if self.prev else False)

    def is_cmake(self):
        return isinstance(self, CMake) or (self.prev.is_cmake() if self.prev else False)


class Configure(Command):
    def __init__(self, *args):
        args = ('./configure', '--prefix=' + configuration.install_path) + configuration.configure_arguments + args
        super(Configure, self).__init__(*args)


class ConfigureStatic(Configure):
    def __init__(self, *args):
        args = ('--enable-static', '--disable-shared') + args
        super(ConfigureStatic, self).__init__(*args)


class CMake(Command):
    def __init__(self, *args):
        args = (configuration.cmake_executable, '-DCMAKE_INSTALL_PREFIX=' + configuration.install_path) \
               + configuration.cmake_arguments + args + ('.',)
        super(CMake, self).__init__(*args)


class Make(Command):
    def __init__(self, *args):
        args = (configuration.make_executable,) + args
        super(Make, self).__init__(*args)


class Install(Make):
    def __init__(self, *args):
        args += ('install',)
        super(Install, self).__init__(*args)


class ConfigureInstall(Install):
    def __init__(self, *args):
        super(ConfigureInstall, self).__init__()
        self.prev = Configure(*args)


class ConfigureStaticInstall(Install):
    def __init__(self, *args):
        super(ConfigureStaticInstall, self).__init__()
        self.prev = ConfigureStatic(*args)


class CMakeInstall(Install):
    def __init__(self, *args):
        super(CMakeInstall, self).__init__()
        self.prev = CMake(*args)


# c1 = ConfigureStatic('lol', '123')
# c2 = CMake('-DSMTH=123')
# c3 = Install('-j2')
#
# c4 = ConfigureInstall('--disable-dependency-tracking')
# c5 = ConfigureStaticInstall('--disable-dependency-tracking')

# import cPickle
# s = cPickle.dumps(c5)
#
# pass
