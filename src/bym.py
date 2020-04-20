#!/usr/bin/env python3

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

import configuration
import repository
from ordered_set import OrderedSet


def _make_directory(path):
    if not os.path.exists(path):
        # todo: handle errors
        os.makedirs(path)


def _add_dependencies(target, packages):
    if target in packages:
        return

    dependencies = repository.package(target).dependencies

    if isinstance(dependencies, (tuple, list)):
        for dependency in dependencies:
            _add_dependencies(dependency, packages)
    else:
        _add_dependencies(dependencies, packages)

    packages.append(target)


def _add_prerequisites(targets):
    prerequisites = OrderedSet(configuration.prerequisites)

    for target in targets:
        commands = repository.package(target).commands

        if isinstance(commands, (tuple, list)):
            for cmd in commands:
                prerequisites.update(cmd.prerequisites())
        else:
            prerequisites.update(commands.prerequisites())

    targets[0:0] = list(prerequisites)


def _main():
    # Resolve dependencies
    targets = []

    for target in configuration.targets:
        _add_dependencies(target, targets)

    _add_prerequisites(targets)

    # Prepare build directories
    _make_directory(configuration.state_path)
    _make_directory(configuration.build_path)
    _make_directory(configuration.bin_path)
    _make_directory(configuration.include_path)
    _make_directory(configuration.lib_path)

    # Do build
    os.chdir(configuration.build_path)

    for target in targets:
        # todo: handle errors
        repository.package(target).build()


if __name__ == '__main__':
    _main()
