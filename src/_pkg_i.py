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

from command import CMakeInstall
import configuration
import repository


pkg = repository.add_package


pkg(
    name='instpatch',
    source='https://github.com/swami/libinstpatch/archive/v1.1.4.tar.gz',
    checksum='e529b15055b7341ab7a75885338d0a9b84859e3f6ca3ed3c363e7f3521329c9c',
    dependencies=('glib', 'sndfile'),
    commands=CMakeInstall(
        '-DCMAKE_EXE_LINKER_FLAGS=-framework Carbon -framework CoreFoundation -framework Foundation'
        ' -lffi -lpcre -L' + configuration.lib_path,
        '-DBUILD_SHARED_LIBS=NO',
        '-DLIB_SUFFIX=',
    )
)