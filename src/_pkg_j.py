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
    name='jpeg',
    source='http://www.ijg.org/files/jpegsrc.v9c.tar.gz',
    checksum='650250979303a649e21f87b5ccd02672af1ea6954b911342ea491f351ceb7122',
    commands=Library()
)
pkg(
    name='jpeg-turbo',
    source='https://downloads.sourceforge.net/project/libjpeg-turbo/2.0.6/libjpeg-turbo-2.0.6.tar.gz',
    checksum='d74b92ac33b0e3657123ddcf6728788c90dc84dcb6a52013d758af3c4af481bb',
    dependencies='nasm',
    commands=CMakeInstall('-DENABLE_SHARED=NO')
)
