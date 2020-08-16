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

from command import CMakeInstall, Library
import configuration
import repository


pkg = repository.add_package


pkg(
    name='iconv',
    source='https://ftp.gnu.org/gnu/libiconv/libiconv-1.16.tar.gz',
    checksum='e6a1b1b589654277ee790cce3734f07876ac4ccfaecbee8afa0b649cf529cc04',
    commands=Library('--enable-extra-encodings')
)
pkg(
    name='instpatch',
    source='https://github.com/swami/libinstpatch/archive/v1.1.5.tar.gz',
    checksum='5fd01cd2ba7377e7a72caaf3b565d8fe088b5c8a14e0ea91516f0c87524bcf8a',
    dependencies=('glib', 'sndfile'),
    commands=CMakeInstall(
        '-DCMAKE_EXE_LINKER_FLAGS=-framework Carbon -framework CoreFoundation -framework Foundation'
        ' -lffi -lpcre -L' + configuration.lib_path,
        '-DBUILD_SHARED_LIBS=NO',
        '-DLIB_SUFFIX=',
    )
)
