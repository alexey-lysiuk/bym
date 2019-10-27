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

from command import ConfigureStaticInstall, Library
import configuration
import repository


pkg = repository.add_package


pkg(
    name='mad',
    source='https://downloads.sourceforge.net/project/mad/libmad/0.15.1b/libmad-0.15.1b.tar.gz',
    checksum='bbfac3ed6bfbc2823d3775ebb931087371e142bb0e9bb1bee51a76a6e0078690',
    commands=Library()
)
pkg(
    name='mc',
    source='https://www.midnight-commander.org/downloads/mc-4.8.19.tar.xz',
    checksum='eb9e56bbb5b2893601d100d0e0293983049b302c5ab61bfb544ad0ee2cc1f2df',
    dependencies=('glib', 'slang', 'ssh2'),
    commands=ConfigureStaticInstall(
        'LDFLAGS=-framework CoreServices ' + configuration.environment['LDFLAGS'],
        'ac_cv_func_utimensat=no'
    )
)
pkg(
    name='modplug',
    source='https://downloads.sourceforge.net/modplug-xmms/libmodplug/0.8.8.5/libmodplug-0.8.8.5.tar.gz',
    checksum='77462d12ee99476c8645cb5511363e3906b88b33a6b54362b4dbc0f39aa2daad',
    commands=Library()
)
pkg(
    name='mpg123',
    source='https://sourceforge.net/projects/mpg123/files/mpg123/1.25.13/mpg123-1.25.13.tar.bz2',
    checksum='90306848359c793fd43b9906e52201df18775742dc3c81c06ab67a806509890a',
    commands=Library()
)
