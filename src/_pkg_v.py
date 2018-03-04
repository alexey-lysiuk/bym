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

from command import Library, Tool
import repository


pkg = repository.add_package


pkg(
    name='vorbis',
    source='https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.xz',
    checksum='54f94a9527ff0a88477be0a71c0bab09a4c3febe0ed878b24824906cd4b0e1d1',
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
