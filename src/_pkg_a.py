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

from command import Library, Tool, CMakeInstall
import repository


pkg = repository.add_package


pkg(
    name='allegro',
    source='https://github.com/liballeg/allegro5/releases/download/5.2.3.0/allegro-5.2.3.0.tar.gz',
    checksum='5a4d40601899492b697ad5cfdf11d8265fe554036a2c912c86a6e6d23001f905',
    dependencies=('vorbis', 'flac', 'opusfile', 'theora', 'openal', 'webp', 'dumb', 'freetype', 'physfs', 'enet'),
    commands=CMakeInstall(
        '-DSHARED=NO',
        '-DWANT_DOCS=NO',
        '-DWANT_EXAMPLES=NO',
        '-DWANT_TESTS=NO',
        '-DFREETYPE_ZLIB=YES',
        '-DFREETYPE_BZIP2=YES',
        '-DFREETYPE_PNG=YES'
    )
)
pkg(
    name='ao',
    source='http://downloads.xiph.org/releases/ao/libao-1.2.0.tar.gz',
    checksum='03ad231ad1f9d64b52474392d63c31197b0bc7bd416e58b1c10a329a5ed89caf',
    commands=Library()
)
pkg(
    name='autoconf',
    source='https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.xz',
    checksum='64ebcec9f8ac5b2487125a86a7760d2591ac9e1d3dbd59489633f9de62a57684',
    commands=Tool()
)
pkg(
    name='automake',
    source='https://ftp.gnu.org/gnu/automake/automake-1.15.1.tar.xz',
    checksum='af6ba39142220687c500f79b4aa2f181d9b24e4f8d8ec497cea4ba26c64bedaf',
    commands=Tool()
)
