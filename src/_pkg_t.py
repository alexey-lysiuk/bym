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
    name='tiff',
    source='http://download.osgeo.org/libtiff/tiff-4.0.8.tar.gz',
    checksum='59d7a5a8ccd92059913f246877db95a2918e6c04fb9d43fd74e5c3390dac2910',
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