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
    source='https://downloads.xiph.org/releases/flac/flac-1.3.3.tar.xz',
    checksum='213e82bd716c9de6db2f98bcadbc4c24c7e2efe8c75939a1a84e28539c4e1748',
    dependencies='ogg',
    commands=Library()
)
pkg(
    name='fluidsynth',
    source='https://github.com/FluidSynth/fluidsynth/archive/v2.1.1.tar.gz',
    checksum='966d0393591b505d694e51cbf653387007144e9ae0b8705d82ec7d943d31d348',
    dependencies=('glib', 'instpatch', 'sndfile'),
    commands=CMakeInstall(
        '-DCMAKE_BUILD_TYPE=Release',
        '-DCMAKE_EXE_LINKER_FLAGS=-lffi -lpcre -L' + configuration.lib_path,
        '-DBUILD_SHARED_LIBS=NO',
        '-DLIB_SUFFIX=',
        '-Denable-framework=NO',
        '-Denable-readline=NO',
        '-Denable-sdl2=NO'
    )
)
pkg(
    name='freetype',
    source='https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.xz',
    checksum='16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f',
    dependencies='png',
    commands=Library(
        '--enable-freetype-config',
        '--without-harfbuzz',
    )
)
pkg(
    name='ftgl',
    source='https://downloads.sourceforge.net/project/ftgl/FTGL%20Source/2.1.3~rc5/ftgl-2.1.3-rc5.tar.gz',
    checksum='5458d62122454869572d39f8aa85745fc05d5518001bcefa63bd6cbb8d26565b',
    dependencies='freetype',
    commands=Library()
)
