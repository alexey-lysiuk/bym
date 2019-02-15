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

from command import Library, Tool, Make
import configuration
import repository


pkg = repository.add_package


pkg(
    name='libxmp',
    source='https://downloads.sourceforge.net/project/xmp/libxmp/4.4.1/libxmp-4.4.1.tar.gz',
    checksum='353535cc84c8cddae8decec4e65fa4c51fc64f22eb0891bc3dae6eaf25f9cccf',
    commands=Library()
)
pkg(
    name='libmikmod',
    source='https://downloads.sourceforge.net/project/mikmod/libmikmod/3.3.11.1/libmikmod-3.3.11.1.tar.gz',
    checksum='ad9d64dfc8f83684876419ea7cd4ff4a41d8bcd8c23ef37ecb3a200a16b46d19',
    commands=Library()
)
pkg(
    name='libtool',
    source='https://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.xz',
    checksum='7c87a8c2c8c0fc9cd5019e402bed4292462d00a718a7cd5f11218153bf28b26f',
    commands=Tool()
)
pkg(
    name='luajit',
    source='https://luajit.org/download/LuaJIT-2.0.5.tar.gz',
    checksum='874b1f8297c697821f561f9b73b57ffd419ed8f4278c82e05b48806d30c1e979',
    commands=Make('amalg', 'install', 'BUILDMODE=static', 'PREFIX=' + configuration.install_path)
)
