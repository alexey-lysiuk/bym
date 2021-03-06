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

from command import CMakeInstall, Command, Library, Install, Tool
import configuration
import repository


pkg = repository.add_package


pkg(
    name='ogg',
    source='https://downloads.xiph.org/releases/ogg/libogg-1.3.4.tar.gz',
    checksum='fe5670640bd49e828d64d2879c31cb4dde9758681bb664f9bdbf159a01b0c76e',
    commands=Library()
)
pkg(
    name='oggz',
    source='https://downloads.xiph.org/releases/liboggz/liboggz-1.1.1.tar.gz',
    checksum='6bafadb1e0a9ae4ac83304f38621a5621b8e8e32927889e65a98706d213d415a',
    dependencies='ogg',
    commands=Tool()
)
pkg(
    name='openal',
    source='https://openal-soft.org/openal-releases/openal-soft-1.21.0.tar.bz2',
    checksum='2916b4fc24e23b0271ce0b3468832ad8b6d8441b1830215b28cc4fee6cc89297',
    commands=CMakeInstall(
        '-DLIBTYPE=STATIC',
        '-DALSOFT_EXAMPLES=NO'
    )
)
pkg(
    name='openssl',
    source='https://www.openssl.org/source/openssl-1.1.1h.tar.gz',
    checksum='5c9ca8774bd7b03e5784f26ae9e9e6d749c9da2438545077e6b3d755a06595d9',
    commands=(
        Command('./Configure', 'no-shared', '--prefix=' + configuration.install_path, 'darwin64-x86_64-cc'),
        Install()
    )
)
pkg(
    name='opus',
    source='https://archive.mozilla.org/pub/opus/opus-1.3.1.tar.gz',
    checksum='65b58e1e25b2a114157014736a3d9dfeaad8d41be1c8179866f144a2fb44ff9d',
    commands=Library()
)
pkg(
    name='opusfile',
    source='https://downloads.xiph.org/releases/opus/opusfile-0.12.tar.gz',
    checksum='118d8601c12dd6a44f52423e68ca9083cc9f2bfe72da7a8c1acb22a80ae3550b',
    dependencies=('opus', 'ogg'),
    commands=Library('--disable-http')
)
pkg(
    name='opus-tools',
    source='https://archive.mozilla.org/pub/opus/opus-tools-0.1.10.tar.gz',
    checksum='a2357532d19471b70666e0e0ec17d514246d8b3cb2eb168f68bb0f6fd372b28c',
    dependencies=('opus', 'ogg', 'flac'),
    commands=Tool()
)
