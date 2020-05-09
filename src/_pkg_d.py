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

from command import Autogen, CMakeInstall, Tool
import configuration
import repository


pkg = repository.add_package


pkg(
    name='dumb',
    source='https://github.com/kode54/dumb/archive/2.0.3.tar.gz',
    checksum='99bfac926aeb8d476562303312d9f47fd05b43803050cd889b44da34a9b2a4f9',
    commands=CMakeInstall(
        '-DBUILD_EXAMPLES=OFF',
        '-DBUILD_ALLEGRO4=OFF',
    )
)
pkg(
    name='dosbox-staging',
    source='https://github.com/dosbox-staging/dosbox-staging/archive/v0.75.0.tar.gz',
    checksum='6279690a05b9cc134484b8c7d11e9c1cb53b50bdb9bf32bdf683bd66770b6658',
    dependencies=('sdl2_net', 'opusfile'),
    commands=(
        Autogen(),
        Tool()
    )
)
