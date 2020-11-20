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

from command import Command, Make
import configuration
import repository


pkg = repository.add_package


pkg(
    name='unrar',
    source='https://www.rarlab.com/rar/unrarsrc-5.9.4.tar.gz',
    checksum='3d010d14223e0c7a385ed740e8f046edcbe885e5c22c5ad5733d009596865300',
    commands=(
        Make(),
        Command('cp', 'unrar', configuration.bin_path)
    )
)
