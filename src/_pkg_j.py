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
    name='jpeg',
    source='http://www.ijg.org/files/jpegsrc.v9c.tar.gz',
    checksum='1f3a3f610f57e88ff3f1f9db530c605f3949ee6e78002552e324d493cf086ad4',
    commands=Library()
)
pkg(
    name='jpeg-turbo',
    source='https://sourceforge.net/projects/libjpeg-turbo/files/2.0.0/libjpeg-turbo-2.0.0.tar.gz',
    checksum='778876105d0d316203c928fd2a0374c8c01f755d0a00b12a1c8934aeccff8868',
    dependencies='nasm',
    commands=CMakeInstall('-DENABLE_SHARED=NO')
)
