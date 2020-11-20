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
    name='theora',
    source='https://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.bz2',
    checksum='b6ae1ee2fa3d42ac489287d3ec34c5885730b1296f0801ae577a35193d3affbc',
    dependencies='vorbis',
    commands=Library()
)
pkg(
    name='tiff',
    source='https://download.osgeo.org/libtiff/tiff-4.1.0.tar.gz',
    checksum='5d29f32517dadb6dbcd1255ea5bbc93a2b54b94fbf83653b4d65c7d6775b8634',
    dependencies=('jpeg', 'xz'),
    commands=Library()
)
pkg(
    name='timidity',
    source='https://downloads.sourceforge.net/project/timidity/TiMidity++/TiMidity++-2.14.0/TiMidity++-2.14.0.tar.bz2',
    checksum='f97fb643f049e9c2e5ef5b034ea9eeb582f0175dce37bc5df843cc85090f6476',
    dependencies=('vorbis', 'flac', 'speex', 'ao'),
    commands=Tool('--enable-audio=darwin,vorbis,flac,speex,ao',),
)
