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

from command import Library, CMakeInstall
import repository


pkg = repository.add_package


pkg(
    name='webp',
    source='https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.1.0.tar.gz',
    checksum='98a052268cc4d5ece27f76572a7f50293f439c17a98e67c4ea0c7ed6f50ef043',
    dependencies=('png', 'jpeg', 'tiff', 'gif'),
    commands=Library()
)
pkg(
    name='wxwidgets',
    source='https://github.com/wxWidgets/wxWidgets/releases/download/v3.1.3/wxWidgets-3.1.3.tar.bz2',
    checksum='fffc1d34dac54ff7008df327907984b156c50cff5a2f36ee3da6052744ab554a',
    dependencies=('jpeg', 'png', 'tiff'),
    commands=CMakeInstall(
        '-DwxBUILD_SHARED=NO',
        '-DwxUSE_LIBLZMA=YES',
        '-DwxUSE_LIBSDL=NO',
        '-DwxUSE_LIBJPEG=sys',
        '-DwxUSE_LIBPNG=sys',
        '-DwxUSE_LIBTIFF=sys',
    )
)
