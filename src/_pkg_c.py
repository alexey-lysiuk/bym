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
    name='cmake',
    source='https://cmake.org/files/v3.9/cmake-3.9.1.tar.gz',
    checksum='d768ee83d217f91bb597b3ca2ac663da7a8603c97e1f1a5184bc01e0ad2b12bb',
    commands=Tool()
)

pkg(
    name='chocolate-doom',
    source='https://www.chocolate-doom.org/downloads/3.0.0/chocolate-doom-3.0.0.tar.gz',
    checksum='73aea623930c7d18a7a778eea391e1ddfbe90ad1ac40a91b380afca4b0e1dab8',
    dependencies=('png', 'samplerate', 'sdl2_mixer', 'sdl2_net'),
    commands=Tool()
)
