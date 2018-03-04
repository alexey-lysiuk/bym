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

import os

import configuration
from package import Package


_packages = {}


def package(name):
    # TODO: handle missing package
    return _packages[name]


def add_package(name, source, checksum, commands, dependencies=()):
    _packages[name] = Package(name, source, checksum, commands, dependencies)


def _load_packages():
    self_path = os.path.dirname(os.path.abspath(__file__))
    filenames = os.listdir(self_path)

    for filename in filenames:
        if filename.startswith('_pkg_') and filename.endswith('.py'):
            execfile(self_path + os.sep + filename)


_load_packages()

# TODO: name aliases: 'libogg' -> 'ogg'

try:
    # noinspection PyUnresolvedReferences
    import repository_user
except ImportError:
    pass

