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

from command import Library, CMakeInstall
import repository


pkg = repository.add_package


pkg(
    name='jpeg',
    source='http://www.ijg.org/files/jpegsrc.v9c.tar.gz',
    checksum='650250979303a649e21f87b5ccd02672af1ea6954b911342ea491f351ceb7122',
    commands=Library()
)
pkg(
    name='jpeg-turbo',
    source='https://downloads.sourceforge.net/project/libjpeg-turbo/2.0.2/libjpeg-turbo-2.0.2.tar.gz',
    checksum='acb8599fe5399af114287ee5907aea4456f8f2c1cc96d26c28aebfdf5ee82fed',
    dependencies='nasm',
    commands=CMakeInstall('-DENABLE_SHARED=NO')
)
