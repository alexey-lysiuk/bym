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

from command import Command, Tool
import configuration
import repository


pkg = repository.add_package


pkg(
    name='nasm',
    source='https://www.nasm.us/pub/nasm/releasebuilds/2.15.05/nasm-2.15.05.tar.xz',
    checksum='3caf6729c1073bf96629b57cee31eeb54f4f8129b01902c73428836550b30a3f',
    commands=Tool()
)
pkg(
    name='ninja',
    source='https://github.com/ninja-build/ninja/archive/v1.10.0.tar.gz',
    checksum='3810318b08489435f8efc19c05525e80a993af5a55baa0dfeae0465a9d45f99f',
    commands=(
        Command('./configure.py', '--bootstrap'),
        Command('cp', 'ninja', configuration.bin_path)
    )
)
