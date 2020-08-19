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

from command import Command, Install, Library, Make, Meson
import configuration
import repository


pkg = repository.add_package


pkg(
    name='gcrypt',
    source='https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.4.tar.bz2',
    checksum='f638143a0672628fde0cad745e9b14deb85dffb175709cacc1f4fe24b93f2227',
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
    source='https://ftp.gnu.org/gnu/gettext/gettext-0.21.tar.xz',
    checksum='d20fcbb537e02dcf1383197ba05bd0734ef7bf5db06bdb241eb69b7d16b73192',
    commands=Library('--disable-java', '--disable-csharp')
)
pkg(
    name='gif',
    source='https://downloads.sourceforge.net/project/giflib/giflib-5.2.1.tar.gz',
    checksum='31da5562f44c5f15d63340a09a4fd62b48c45620cd302f77a6d9acf0077879bd',
    commands=(
        Make(),
        Install('PREFIX=' + configuration.install_path),
    )
)
pkg(
    name='glib',
    source='https://download.gnome.org/sources/glib/2.64/glib-2.64.4.tar.xz',
    checksum='f7e0b325b272281f0462e0f7fff25a833820cac19911ff677251daf6d87bce50',
    dependencies=('ffi', 'gettext', 'pcre'),
    commands=Meson()
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
    source='https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.36.tar.bz2',
    checksum='babd98437208c163175c29453f8681094bcaf92968a15cafb1a276076b33c97c',
    commands=Library()
)
