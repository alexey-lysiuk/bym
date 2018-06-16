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
    source='https://github.com/FluidSynth/fluidsynth/archive/v1.1.11.tar.gz',
    checksum='da8878ff374d12392eecf87e96bad8711b8e76a154c25a571dd8614d1af80de8',
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
    source='https://download.savannah.gnu.org/releases/freetype/freetype-2.9.tar.bz2',
    checksum='e6ffba3c8cef93f557d1f767d7bc3dee860ac7a3aaff588a521e081bc36f4c8a',
    dependencies='png',
    commands=Library('--without-harfbuzz')
)
