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
    name='cargo',
    source='https://github.com/rust-lang/cargo/archive/0.37.0.tar.gz',
    checksum='377e1090e9ce21206270576193746499a26e8ffbd8b89ccd5f8eb1085ca00e3b',
    commands=Command(configuration.src_path + 'cargobootstrap.sh', configuration.install_path)
)
pkg(
    name='chocolate-doom',
    source='https://www.chocolate-doom.org/downloads/3.0.0/chocolate-doom-3.0.0.tar.gz',
    checksum='73aea623930c7d18a7a778eea391e1ddfbe90ad1ac40a91b380afca4b0e1dab8',
    dependencies=('png', 'samplerate', 'sdl2_mixer', 'sdl2_net'),
    commands=Tool()
)
pkg(
    name='cmake',
    source='https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0.tar.gz',
    checksum='aa76ba67b3c2af1946701f847073f4652af5cbd9f141f221c97af99127e75502',
    commands=Tool()
)
