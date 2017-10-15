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

from command import Tool
import repository


pkg = repository.add_package


pkg(
    name='yasm',
    source='https://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz',
    checksum='3dce6601b495f5b3d45b59f7d2492a340ee7e84b5beca17e48f862502bd5603f',
    commands=Tool()
)
