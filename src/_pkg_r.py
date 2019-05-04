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

from command import Library, Tool
import repository


pkg = repository.add_package


pkg(
    name='re2c',
    source='https://github.com/skvadrik/re2c/releases/download/1.1.1/re2c-1.1.1.tar.gz',
    checksum='856597337ea00b24ce91f549f79e6eece1b92ba5f8b63292cad66c14ac7451cf',
    commands=Library()
)
pkg(
    name='readline',
    source='https://ftp.gnu.org/gnu/readline/readline-8.0.tar.gz',
    checksum='e339f51971478d369f8a053a330a190781acb9864cf4c541060f12078948e461',
    commands=Library()
)
pkg(
    name='rust',
    source='https://static.rust-lang.org/dist/rustc-1.33.0-src.tar.gz',
    checksum='5a01a8d7e65126f6079042831385e77485fa5c014bf217e9f3e4aff36a485d94',
    dependencies=('openssl', 'ssh2'),
    commands=Tool()
)
