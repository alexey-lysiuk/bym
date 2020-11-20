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

from .command import Command, Make, Install, CMakeInstall, Library, Tool
from . import configuration
from . import repository


pkg = repository.add_package


pkg(
    name='p7zip',
    source='https://downloads.sourceforge.net/project/p7zip/p7zip/16.02/p7zip_16.02_src_all.tar.bz2',
    checksum='5eb20ac0e2944f6cb9c2d51dd6c4518941c185347d4089ea89087ffdd6e2341f',
    commands=(
        Command('cp', 'makefile.macosx_llvm_64bits', 'makefile.machine'),
        Make('all3'),
        Install('DEST_HOME=' + configuration.install_path)
    )
)
pkg(
    name='pbzx',
    source='https://github.com/NiklasRosenstein/pbzx/archive/v1.0.2.tar.gz',
    checksum='33db3cf9dc70ae704e1bbfba52c984f4c6dbfd0cc4449fa16408910e22b4fd90',
    dependencies='xz',
    commands=Command(
        'clang',
        '-I' + configuration.include_path,
        '-L' + configuration.lib_path, '-llzma', '-lxar',
        'pbzx.c',
        '-o', configuration.bin_path + '/pbzx'
    )
)
pkg(
    name='pcre',
    source='https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.bz2',
    checksum='19108658b23b3ec5058edc9f66ac545ea19f9537234be1ec62b714c84399366d',
    commands=Library('--enable-unicode-properties')
)
pkg(
    name='physfs',
    source='https://icculus.org/physfs/downloads/physfs-3.0.0.tar.bz2',
    checksum='f2617d6855ea97ea42e4a8ebcad404354be99dfd8a274eacea92091b27fd7324',
    commands=CMakeInstall('-DPHYSFS_BUILD_SHARED=NO')
)
pkg(
    name='pkg-config',
    source='https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
    checksum='6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591',
    commands=Tool('--with-internal-glib')
)
pkg(
    name='png',
    source='https://downloads.sourceforge.net/libpng/libpng-1.6.37.tar.xz',
    checksum='505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca',
    commands=Library()
)
pkg(
    name='python',
    source='https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz',
    checksum='75894117f6db7051c1b34f37410168844bbb357c139a8a10a352e9bf8be594e8',
    dependencies=('gdbm', 'gettext', 'openssl', 'sqlite', 'xz'),
    commands=Tool(
        'LDFLAGS=-lintl -liconv ' + configuration.environment['LDFLAGS'],
        '--enable-optimizations')
)
