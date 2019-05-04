#
#    Build Your Mac: Configurable build environment for macOS
#    Copyright (C) 2017-2019 Alexey Lysiuk
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
    source='https://www.nasm.us/pub/nasm/releasebuilds/2.14.02/nasm-2.14.02.tar.xz',
    checksum='e24ade3e928f7253aa8c14aa44726d1edf3f98643f87c9d72ec1df44b26be8f5',
    commands=Tool()
)
pkg(
    name='ninja',
    source='https://github.com/ninja-build/ninja/archive/v1.9.0.tar.gz',
    checksum='5d7ec75828f8d3fd1a0c2f31b5b0cea780cdfe1031359228c428c1a48bfcd5b9',
    dependencies='re2c',
    commands=(
        Command('./configure.py', '--bootstrap'),
        Command('cp', 'ninja', configuration.bin_path)
    )
)
