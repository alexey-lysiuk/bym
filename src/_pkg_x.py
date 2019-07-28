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

from command import Library
import repository


pkg = repository.add_package


pkg(
    name='xdelta',
    source='https://github.com/jmacd/xdelta-gpl/releases/download/v3.1.0/xdelta3-3.1.0.tar.gz',
    checksum='114543336ab6cee3764e3c03202701ef79d7e5e8e4863fe64811e4d9e61884dc',
    dependencies='xz',
    commands=Library()
)
pkg(
    name='xz',
    source='https://downloads.sourceforge.net/project/lzmautils/xz-5.2.4.tar.gz',
    checksum='b512f3b726d3b37b6dc4c8570e137b9311e7552e8ccbab4d39d47ce5f4177145',
    commands=Library()
)
