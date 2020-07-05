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

from command import Library, Tool
import repository


pkg = repository.add_package


pkg(
    name='vorbis',
    source='https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.xz',
    checksum='b33cc4934322bcbf6efcbacf49e3ca01aadbea4114ec9589d1b1e9d20f72954b',
    dependencies='ogg',
    commands=Library()
)
pkg(
    name='vorbis-tools',
    source='https://downloads.xiph.org/releases/vorbis/vorbis-tools-1.4.0.tar.gz',
    checksum='a389395baa43f8e5a796c99daf62397e435a7e73531c9f44d9084055a05d22bc',
    dependencies=('vorbis', 'flac', 'ao'),
    commands=Tool()
)
pkg(
    name='vpx',
    source='https://github.com/webmproject/libvpx/archive/v1.8.2.tar.gz',
    checksum='8735d9fcd1a781ae6917f28f239a8aa358ce4864ba113ea18af4bb2dc8b474ac',
    dependencies='yasm',
    commands=Library('--disable-examples', '--disable-unit-tests')
)
