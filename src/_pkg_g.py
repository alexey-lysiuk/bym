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

from command import Autogen, Command, Library, Make
import configuration
import repository


pkg = repository.add_package


pkg(
    name='gcrypt',
    source='https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.1.tar.bz2',
    checksum='7a2875f8b1ae0301732e878c0cca2c9664ff09ef71408f085c50e332656a78b3',
    dependencies='gpg-error',
    commands=Library()
)
pkg(
    name='gdbm',
    source='https://ftp.gnu.org/gnu/gdbm/gdbm-1.18.1.tar.gz',
    checksum='86e613527e5dba544e73208f42b78b7c022d4fa5a6d5498bf18c8d6f745b91dc',
    dependencies='readline',
    commands=Library()
)
pkg(
    name='gettext',
    source='https://ftp.gnu.org/pub/gnu/gettext/gettext-0.19.8.1.tar.xz',
    checksum='105556dbc5c3fbbc2aa0edb46d22d055748b6f5c7cd7a8d99f8e7eb84e938be4',
    commands=Library()
)
pkg(
    name='gif',
    source='https://downloads.sourceforge.net/project/giflib/giflib-5.1.4.tar.bz2',
    checksum='df27ec3ff24671f80b29e6ab1c4971059c14ac3db95406884fc26574631ba8d5',
    commands=Library()
)
pkg(
    name='glib',
    source='https://download.gnome.org/sources/glib/2.58/glib-2.58.1.tar.xz',
    checksum='97d6a9d926b6aa3dfaadad3077cfb43eec74432ab455dff14250c769d526d7d6',
    dependencies=('autoconf', 'automake', 'ffi', 'gettext', 'libtool', 'pcre'),
    commands=(
        Autogen(),
        Library()
    )
)
pkg(
    name='glew',
    source='https://downloads.sourceforge.net/project/glew/glew/2.1.0/glew-2.1.0.tgz',
    checksum='04de91e7e6763039bc11940095cd9c7f880baba82196a7765f727ac05a993c95',
    commands=(
        Make('GLEW_DEST=' + configuration.install_path, 'glew.lib.static', 'install.include', 'install.pkgconfig'),
        Command('cp', 'lib/libGLEW.a', configuration.lib_path),
    )
)
pkg(
    name='gpg-error',
    source='https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.27.tar.bz2',
    checksum='4f93aac6fecb7da2b92871bb9ee33032be6a87b174f54abf8ddf0911a22d29d2',
    commands=Library()
)
