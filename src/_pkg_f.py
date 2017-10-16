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

from command import CMakeInstall, Library
import repository


pkg = repository.add_package


pkg(
    name='ffi',
    source='https://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz',
    checksum='d06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37',
    commands=Library()
)
pkg(
    name='flac',
    source='https://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz',
    checksum='91cfc3ed61dc40f47f050a109b08610667d73477af6ef36dcad31c31a4a8d53f',
    dependencies='ogg',
    commands=Library()
)
pkg(
    name='fluidsynth',
    source='https://downloads.sourceforge.net/project/fluidsynth/fluidsynth-1.1.6/fluidsynth-1.1.6.tar.gz',
    checksum='50853391d9ebeda9b4db787efb23f98b1e26b7296dd2bb5d0d96b5bccee2171c',
    dependencies=('glib', 'sndfile'),
    commands=CMakeInstall(
        '-DCMAKE_BUILD_TYPE=Release',
        '-DBUILD_SHARED_LIBS=NO',
        '-DLIB_SUFFIX=',
        '-Denable-framework=NO',
        '-Denable-readline=NO'
    )
)
pkg(
    name='freetype',
    source='https://download.savannah.gnu.org/releases/freetype/freetype-2.8.tar.bz2',
    checksum='a3c603ed84c3c2495f9c9331fe6bba3bb0ee65e06ec331e0a0fb52158291b40b',
    commands=Library('--without-harfbuzz')
)