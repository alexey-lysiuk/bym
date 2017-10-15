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

from command import Command, Make, Install, Library, Tool
import configuration
import repository


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
    name='pcre',
    source='https://ftp.pcre.org/pub/pcre/pcre-8.41.tar.bz2',
    checksum='e62c7eac5ae7c0e7286db61ff82912e1c0b7a0c13706616e94a7dd729321b530',
    commands=Library('--enable-unicode-properties')
)
pkg(
    name='pkg-config',
    source='https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
    checksum='6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591',
    commands=Tool('--with-internal-glib')
)
pkg(
    name='png',
    source='https://download.sourceforge.net/libpng/libpng-1.6.32.tar.xz',
    checksum='c918c3113de74a692f0a1526ce881dc26067763eb3915c57ef3a0f7b6886f59b',
    commands=Library()
)

