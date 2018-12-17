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

from command import Library, CMakeInstall
import repository


pkg = repository.add_package


pkg(
    name='webp',
    source='https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-0.6.1.tar.gz',
    checksum='06503c782d9f151baa325591c3579c68ed700ffc62d4f5a32feead0ff017d8ab',
    dependencies=('png', 'jpeg', 'tiff', 'gif'),
    commands=Library()
)
pkg(
    name='wxwidgets',
    source='https://github.com/wxWidgets/wxWidgets/releases/download/v3.1.2/wxWidgets-3.1.2.tar.bz2',
    checksum='4cb8d23d70f9261debf7d6cfeca667fc0a7d2b6565adb8f1c484f9b674f1f27a',
    dependencies=('xz'),
    commands=CMakeInstall('-DwxBUILD_SHARED=NO', '-DwxUSE_LIBLZMA=YES', '-DwxUSE_LIBSDL=NO')
)
