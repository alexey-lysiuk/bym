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

from command import CreateDirectories, CreateFile, Install
import configuration
import repository


pkg = repository.add_package


pkg(
    name='dumb',
    source='https://downloads.sourceforge.net/project/dumb/dumb/0.9.3/dumb-0.9.3.tar.gz',
    checksum='8d44fbc9e57f3bac9f761c3b12ce102d47d717f0dd846657fb988e0bb5d1ea33',
    commands=(
        CreateDirectories(
            'lib/unix',
            'obj/unix/debug',
            'obj/unix/release'
        ),
        CreateFile(
            'make/config.txt',
            'include make/unix.inc\n'
            'ALL_TARGETS := core core-headers\n'
            'PREFIX := %s\n' % configuration.install_path),
        Install()
    )
)
