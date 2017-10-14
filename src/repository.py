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

import os

import command
import configuration
from package import Package


_packages = {}


def package(name):
    # TODO: handle missing package
    return _packages[name]


def pkg(name, source, checksum, commands, dependencies=()):
    _packages[name] = Package(name, source, checksum, commands, dependencies)


def library(*args):
    return command.ConfigureStaticInstall(*args)


def tool(*args):
    return command.ConfigureInstall(*args)


def cmake(*args):
    return command.CMakeInstall(*args)


# TODO: name aliases: 'libogg' -> 'ogg'

pkg(
    name='ao',
    source='http://downloads.xiph.org/releases/ao/libao-1.2.0.tar.gz',
    checksum='03ad231ad1f9d64b52474392d63c31197b0bc7bd416e58b1c10a329a5ed89caf',
    commands=library()
)
pkg(
    name='autoconf',
    source='https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.xz',
    checksum='64ebcec9f8ac5b2487125a86a7760d2591ac9e1d3dbd59489633f9de62a57684',
    commands=tool()
)
pkg(
    name='automake',
    source='https://ftp.gnu.org/gnu/automake/automake-1.15.1.tar.xz',
    checksum='af6ba39142220687c500f79b4aa2f181d9b24e4f8d8ec497cea4ba26c64bedaf',
    commands=tool()
)
pkg(
    name='cmake',
    source='https://cmake.org/files/v3.9/cmake-3.9.1.tar.gz',
    checksum='d768ee83d217f91bb597b3ca2ac663da7a8603c97e1f1a5184bc01e0ad2b12bb',
    commands=tool()
)
pkg(
    name='ffi',
    source='https://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz',
    checksum='d06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37',
    commands=library()
)
pkg(
    name='flac',
    source='https://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz',
    checksum='91cfc3ed61dc40f47f050a109b08610667d73477af6ef36dcad31c31a4a8d53f',
    dependencies='ogg',
    commands=library()
)
pkg(
    name='fluidsynth',
    source='https://downloads.sourceforge.net/project/fluidsynth/fluidsynth-1.1.6/fluidsynth-1.1.6.tar.gz',
    checksum='50853391d9ebeda9b4db787efb23f98b1e26b7296dd2bb5d0d96b5bccee2171c',
    dependencies=('glib', 'sndfile'),
    commands=cmake(
        '-DCMAKE_BUILD_TYPE=Release',
        '-DBUILD_SHARED_LIBS=NO',
        '-DLIB_SUFFIX=',
        '-Denable-framework=NO',
        '-Denable-readline=NO'
    )
)
pkg(
    name='freetype',
    source='https://download.savannah.gnu.org/releases/freetype/freetype-2.8.tar.bz2',
    checksum='a3c603ed84c3c2495f9c9331fe6bba3bb0ee65e06ec331e0a0fb52158291b40b',
    commands=library('--without-harfbuzz')
)
pkg(
    name='gcrypt',
    source='https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.1.tar.bz2',
    checksum='7a2875f8b1ae0301732e878c0cca2c9664ff09ef71408f085c50e332656a78b3',
    dependencies='gpg-error',
    commands=library()
)
pkg(
    name='gettext',
    source='https://ftp.gnu.org/pub/gnu/gettext/gettext-0.19.8.1.tar.xz',
    checksum='105556dbc5c3fbbc2aa0edb46d22d055748b6f5c7cd7a8d99f8e7eb84e938be4',
    commands=library()
)
pkg(
    name='gif',
    source='https://downloads.sourceforge.net/project/giflib/giflib-5.1.4.tar.bz2',
    checksum='df27ec3ff24671f80b29e6ab1c4971059c14ac3db95406884fc26574631ba8d5',
    commands=library()
)
pkg(
    name='glib',
    source='https://download.gnome.org/sources/glib/2.54/glib-2.54.1.tar.xz',
    checksum='50c01b1419324f10fbf9b9709ec2164b18586968bdce7540583bf32302cf47a3',
    dependencies=('ffi', 'gettext', 'pcre'),
    commands=library()
)
pkg(
    name='gpg-error',
    source='https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.27.tar.bz2',
    checksum='4f93aac6fecb7da2b92871bb9ee33032be6a87b174f54abf8ddf0911a22d29d2',
    commands=library()
)
pkg(
    name='jpeg',
    source='http://www.ijg.org/files/jpegsrc.v9b.tar.gz',
    checksum='240fd398da741669bf3c90366f58452ea59041cacc741a489b99f2f6a0bad052',
    commands=library()
)
pkg(
    name='libmikmod',
    source='https://downloads.sourceforge.net/project/mikmod/libmikmod/3.3.11.1/libmikmod-3.3.11.1.tar.gz',
    checksum='ad9d64dfc8f83684876419ea7cd4ff4a41d8bcd8c23ef37ecb3a200a16b46d19',
    commands=library()
)
pkg(
    name='libtool',
    source='https://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.xz',
    checksum='7c87a8c2c8c0fc9cd5019e402bed4292462d00a718a7cd5f11218153bf28b26f',
    commands=tool()
)
pkg(
    name='modplug',
    source='https://downloads.sourceforge.net/modplug-xmms/libmodplug/0.8.8.5/libmodplug-0.8.8.5.tar.gz',
    checksum='77462d12ee99476c8645cb5511363e3906b88b33a6b54362b4dbc0f39aa2daad',
    commands=library()
)
pkg(
    name='mpg123',
    source='https://www.mpg123.de/download/mpg123-1.25.7.tar.bz2',
    checksum='31b15ebcf26111b874732e07c8e60de5053ee555eea15fb70c657a4f9f0344f3',
    commands=library()
)
pkg(
    name='ogg',
    source='https://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.xz',
    checksum='3f687ccdd5ac8b52d76328fbbfebc70c459a40ea891dbf3dccb74a210826e79b',
    commands=library()
)
pkg(
    name='oggz',
    source='https://downloads.xiph.org/releases/liboggz/liboggz-1.1.1.tar.gz',
    checksum='6bafadb1e0a9ae4ac83304f38621a5621b8e8e32927889e65a98706d213d415a',
    dependencies='ogg',
    commands=tool()
)
pkg(
    name='openal',
    source='http://kcat.strangesoft.net/openal-releases/openal-soft-1.18.2.tar.bz2',
    checksum='9f8ac1e27fba15a59758a13f0c7f6540a0605b6c3a691def9d420570506d7e82',
    commands=cmake(
        '-DLIBTYPE=STATIC',
        '-DCMAKE_BUILD_TYPE=Release',
        '-DALSOFT_EMBED_HRTF_DATA=YES'
    )
)
pkg(
    name='opus',
    source='https://archive.mozilla.org/pub/opus/opus-1.2.1.tar.gz',
    checksum='cfafd339ccd9c5ef8d6ab15d7e1a412c054bf4cb4ecbbbcc78c12ef2def70732',
    commands=library()
)
pkg(
    name='opusfile',
    source='https://archive.mozilla.org/pub/opus/opusfile-0.9.tar.gz',
    checksum='f75fb500e40b122775ac1a71ad80c4477698842a8fe9da4a1b4a1a9f16e4e979',
    dependencies=('opus', 'ogg'),
    commands=library('--disable-http')
)
pkg(
    name='opus-tools',
    source='https://archive.mozilla.org/pub/opus/opus-tools-0.1.10.tar.gz',
    checksum='a2357532d19471b70666e0e0ec17d514246d8b3cb2eb168f68bb0f6fd372b28c',
    dependencies=('opus', 'ogg', 'flac'),
    commands=tool()
)
pkg(
    name='p7zip',
    source='https://downloads.sourceforge.net/project/p7zip/p7zip/16.02/p7zip_16.02_src_all.tar.bz2',
    checksum='5eb20ac0e2944f6cb9c2d51dd6c4518941c185347d4089ea89087ffdd6e2341f',
    commands=(
        command.Command('cp', 'makefile.macosx_llvm_64bits', 'makefile.machine'),
        command.Make('all3'),
        command.Install('DEST_HOME=' + configuration.install_path)
    )
)
pkg(
    name='pcre',
    source='https://ftp.pcre.org/pub/pcre/pcre-8.41.tar.bz2',
    checksum='e62c7eac5ae7c0e7286db61ff82912e1c0b7a0c13706616e94a7dd729321b530',
    commands=library('--enable-unicode-properties')
)
pkg(
    name='pkg-config',
    source='https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
    checksum='6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591',
    commands=tool('--with-internal-glib')
)
pkg(
    name='png',
    source='https://download.sourceforge.net/libpng/libpng-1.6.32.tar.xz',
    checksum='c918c3113de74a692f0a1526ce881dc26067763eb3915c57ef3a0f7b6886f59b',
    commands=library()
)
pkg(
    name='samplerate',
    source='http://www.mega-nerd.com/SRC/libsamplerate-0.1.9.tar.gz',
    checksum='0a7eb168e2f21353fb6d84da152e4512126f7dc48ccb0be80578c565413444c1',
    commands=library()
)
pkg(
    name='sdl',
    # The latest stable version 1.2.15 has way too many bugs
    source='http://hg.libsdl.org/SDL/archive/2c67e7e5a106.tar.bz2',
    checksum='fb48367773b1699fc84b71aafc3df066baff270adcadafd885ee0877d31bebaf',
    commands=(
        command.Autogen(),
        library('--without-x')
    )
)
pkg(
    name='sdl_gfx',
    source='http://www.ferzkopp.net/Software/SDL_gfx-2.0/SDL_gfx-2.0.26.tar.gz',
    checksum='7ceb4ffb6fc63ffba5f1290572db43d74386cd0781c123bc912da50d34945446',
    dependencies='sdl',
    commands=library()
)
pkg(
    name='sdl_image',
    source='https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz',
    checksum='0b90722984561004de84847744d566809dbb9daf732a9e503b91a1b5a84e5699',
    dependencies=('sdl', 'jpeg', 'png', 'tiff', 'webp'),
    commands=library(
        '--disable-jpg-shared',
        '--disable-png-shared',
        '--disable-tif-shared',
        '--disable-webp-shared'
    )
)
pkg(
    name='sdl_mixer',
    source='https://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-1.2.12.tar.gz',
    checksum='1644308279a975799049e4826af2cfc787cad2abb11aa14562e402521f86992a',
    dependencies=('sdl', 'vorbis', 'flac', 'libmikmod', 'fluidsynth', 'smpeg'),
    commands=library(
        '--disable-music-ogg-shared',
        '--disable-music-flac-shared',
        '--disable-music-fluidsynth-shared',
        '--disable-music-mod-shared',
        '--disable-music-mp3-shared'
    )
)
pkg(
    name='sdl_net',
    source='https://www.libsdl.org/projects/SDL_net/release/SDL_net-1.2.8.tar.gz',
    checksum='5f4a7a8bb884f793c278ac3f3713be41980c5eedccecff0260411347714facb4',
    dependencies='sdl',
    commands=library()
),
pkg(
    name='sdl_ttf',
    source='https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.11.tar.gz',
    checksum='724cd895ecf4da319a3ef164892b72078bd92632a5d812111261cde248ebcdb7',
    dependencies=('sdl', 'freetype'),
    commands=library()
)
pkg(
    name='sdl2',
    source='https://www.libsdl.org/release/SDL2-2.0.6.tar.gz',
    checksum='03658b5660d16d7b31263a691e058ed37acdab155d68dabbad79998fb552c5df',
    commands=library('--without-x')
)
pkg(
    name='sdl2_gfx',
    source='http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.3.tar.gz',
    checksum='a4066bd467c96469935a4b1fe472893393e7d74e45f95d59f69726784befd8f8',
    dependencies='sdl2',
    commands=library()
)
pkg(
    name='sdl2_image',
    source='https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.1.tar.gz',
    checksum='3a3eafbceea5125c04be585373bfd8b3a18f259bd7eae3efc4e6d8e60e0d7f64',
    dependencies=('sdl2', 'jpeg', 'png', 'tiff', 'webp'),
    commands=library(
        '--disable-jpg-shared',
        '--disable-png-shared',
        '--disable-tif-shared',
        '--disable-webp-shared'
    )
)
pkg(
    name='sdl2_mixer',
    source='https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.1.tar.gz',
    checksum='5a24f62a610249d744cbd8d28ee399d8905db7222bf3bdbc8a8b4a76e597695f',
    dependencies=('sdl2', 'vorbis', 'flac', 'libmikmod', 'modplug', 'fluidsynth', 'smpeg2'),
    commands=library(
        '--enable-music-mod-mikmod',
        '--disable-music-ogg-shared',
        '--disable-music-flac-shared',
        '--disable-music-midi-fluidsynth-shared',
        '--disable-music-mod-mikmod-shared',
        '--disable-music-mod-modplug-shared',
        '--disable-music-mp3-smpeg-shared'
    )
)
pkg(
    name='sdl2_net',
    source='https://www.libsdl.org/projects/SDL_net/release/SDL2_net-2.0.1.tar.gz',
    checksum='15ce8a7e5a23dafe8177c8df6e6c79b6749a03fff1e8196742d3571657609d21',
    dependencies='sdl2',
    commands=library()
)
pkg(
    name='sdl2_ttf',
    source='https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.14.tar.gz',
    checksum='34db5e20bcf64e7071fe9ae25acaa7d72bdc4f11ab3ce59acc768ab62fe39276',
    dependencies=('sdl2', 'freetype'),
    commands=library()
)
pkg(
    name='smpeg',
    source='https://github.com/alexey-lysiuk/bym/releases/download/sources/smpeg-0.4.5.tar.xz',
    checksum='1635cde79660440defa6b6641e1a7465ce8886b535dc123069adc31e65e947be',
    dependencies='sdl',
    commands=(
        command.Autogen(),
        library(),
    )
)
pkg(
    name='smpeg2',
    source='https://www.libsdl.org/projects/smpeg/release/smpeg2-2.0.0.tar.gz',
    checksum='979a65b211744a44fa641a9b6e4d64e64a12ff703ae776bafe3c4c4cd85494b3',
    dependencies='sdl2',
    commands=library()
)
pkg(
    name='sndfile',
    source='http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz',
    checksum='1ff33929f042fa333aed1e8923aa628c3ee9e1eb85512686c55092d1e5a9dfa9',
    dependencies=('ogg', 'vorbis', 'flac'),
    commands=library()
)
pkg(
    name='speex',
    source='http://downloads.xiph.org/releases/speex/speex-1.2.0.tar.gz',
    checksum='eaae8af0ac742dc7d542c9439ac72f1f385ce838392dc849cae4536af9210094',
    dependencies='ogg',
    commands=library()
)
pkg(
    name='tiff',
    source='http://download.osgeo.org/libtiff/tiff-4.0.8.tar.gz',
    checksum='59d7a5a8ccd92059913f246877db95a2918e6c04fb9d43fd74e5c3390dac2910',
    dependencies=('jpeg', 'xz'),
    commands=library()
)
pkg(
    name='timidity',
    source='https://downloads.sourceforge.net/project/timidity/TiMidity++/TiMidity++-2.14.0/TiMidity++-2.14.0.tar.bz2',
    checksum='f97fb643f049e9c2e5ef5b034ea9eeb582f0175dce37bc5df843cc85090f6476',
    dependencies=('vorbis', 'flac', 'speex', 'ao'),
    commands=tool('--enable-audio=darwin,vorbis,flac,speex,ao',),
)
pkg(
    name='vorbis',
    source='https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.xz',
    checksum='54f94a9527ff0a88477be0a71c0bab09a4c3febe0ed878b24824906cd4b0e1d1',
    dependencies='ogg',
    commands=library()
)
pkg(
    name='vorbis-tools',
    source='https://downloads.xiph.org/releases/vorbis/vorbis-tools-1.4.0.tar.gz',
    checksum='a389395baa43f8e5a796c99daf62397e435a7e73531c9f44d9084055a05d22bc',
    dependencies=('vorbis', 'flac', 'ao'),
    commands=tool()
)
pkg(
    name='webp',
    source='http://downloads.webmproject.org/releases/webp/libwebp-0.6.0.tar.gz',
    checksum='c928119229d4f8f35e20113ffb61f281eda267634a8dc2285af4b0ee27cf2b40',
    dependencies=('png', 'jpeg', 'tiff', 'gif'),
    commands=library()
)
pkg(
    name='xz',
    source='https://downloads.sourceforge.net/project/lzmautils/xz-5.2.3.tar.gz',
    checksum='71928b357d0a09a12a4b4c5fafca8c31c19b0e7d3b8ebb19622e96f26dbf28cb',
    commands=library()
)
pkg(
    name='zlib',
    source='https://zlib.net/zlib-1.2.11.tar.gz',
    checksum='c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1',
    commands=(
        command.Configure('--static'),
        command.Install()
    )
)


_custom_filename = __name__ + '.custom.py'

if os.path.exists(_custom_filename):
    execfile(_custom_filename)
