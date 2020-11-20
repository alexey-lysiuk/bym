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
    source='https://downloads.sourceforge.net/project/lzmautils/xz-5.2.5.tar.gz',
    checksum='f6f4910fd033078738bd82bfba4f49219d03b17eb0794eb91efbae419f4aba10',
    commands=Library()
)
