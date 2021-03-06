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

from command import CMakeInstall, Library, Make
import repository


pkg = repository.add_package


pkg(
    name='ffi',
    source='https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz',
    checksum='72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056',
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
    source='https://github.com/FluidSynth/fluidsynth/archive/v2.1.5.tar.gz',
    checksum='b539b7c65a650b56f01cd60a4e83c6125c217c5a63c0c214ef6274894a677d00',
    dependencies=('glib', 'instpatch', 'sndfile'),
    commands=CMakeInstall(
        '-DCMAKE_EXE_LINKER_FLAGS=-framework Foundation -lffi -lpcre -L' + configuration.lib_path,
        '-DBUILD_SHARED_LIBS=NO',
        '-DLIB_SUFFIX=',
        '-Denable-framework=NO',
        '-Denable-readline=NO',
        '-Denable-sdl2=NO'
    )
)
pkg(
    name='fmt',
    source='https://github.com/fmtlib/fmt/archive/6.2.1.tar.gz',
    checksum='5edf8b0f32135ad5fafb3064de26d063571e95e8ae46829c2f4f4b52696bbff0',
    commands=CMakeInstall('-DBUILD_SHARED_LIBS=NO', '-DFMT_TEST=NO')
)
pkg(
    name='freeimage',
    source='https://downloads.sourceforge.net/project/freeimage/Source%20Distribution/3.18.0/FreeImage3180.zip',
    checksum='f41379682f9ada94ea7b34fe86bf9ee00935a3147be41b6569c9605a53e438fd',
    commands=Make(
        'INCDIR=' + configuration.include_path,
        'INSTALLDIR=' + configuration.lib_path,
        'install'
    )
)
pkg(
    name='freetype',
    source='https://download.savannah.gnu.org/releases/freetype/freetype-2.10.4.tar.xz',
    checksum='86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784',
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
