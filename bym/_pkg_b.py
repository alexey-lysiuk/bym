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

from command import Install
import repository


pkg = repository.add_package


pkg(
    name='bzip2',
    source='https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz',
    checksum='ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269',
    commands=Install('PREFIX=' + configuration.install_path),
)
