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

from command import Autogen, Make, Configure, Library
import configuration
import repository


pkg = repository.add_package


pkg(
    name='samplerate',
    source='http://www.mega-nerd.com/SRC/libsamplerate-0.1.9.tar.gz',
    checksum='0a7eb168e2f21353fb6d84da152e4512126f7dc48ccb0be80578c565413444c1',
    commands=Library()
)
pkg(
    name='sdl',
    # The latest stable version 1.2.15 has way too many bugs
    source='http://hg.libsdl.org/SDL/archive/2c67e7e5a106.tar.bz2',
    checksum='fb48367773b1699fc84b71aafc3df066baff270adcadafd885ee0877d31bebaf',
    commands=(
        Autogen(),
        Library('--without-x')
    )
)
pkg(
    name='sdl_gfx',
    source='http://www.ferzkopp.net/Software/SDL_gfx-2.0/SDL_gfx-2.0.26.tar.gz',
    checksum='7ceb4ffb6fc63ffba5f1290572db43d74386cd0781c123bc912da50d34945446',
    dependencies='sdl',
    commands=Library()
)
pkg(
    name='sdl_image',
    source='https://www.libsdl.org/projects/SDL_image/release/SDL_image-1.2.12.tar.gz',
    checksum='0b90722984561004de84847744d566809dbb9daf732a9e503b91a1b5a84e5699',
    dependencies=('sdl', 'jpeg', 'png', 'tiff', 'webp'),
    commands=Library(
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
    commands=Library(
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
    commands=Library()
),
pkg(
    name='sdl_ttf',
    source='https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.11.tar.gz',
    checksum='724cd895ecf4da319a3ef164892b72078bd92632a5d812111261cde248ebcdb7',
    dependencies=('sdl', 'freetype'),
    commands=Library()
)
pkg(
    name='sdl2',
    source='https://www.libsdl.org/release/SDL2-2.0.9.tar.gz',
    checksum='255186dc676ecd0c1dbf10ec8a2cc5d6869b5079d8a38194c2aecdff54b324b1',
    commands=Library('--without-x')
)
pkg(
    name='sdl2_gfx',
    source='http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.3.tar.gz',
    checksum='a4066bd467c96469935a4b1fe472893393e7d74e45f95d59f69726784befd8f8',
    dependencies='sdl2',
    commands=Library()
)
pkg(
    name='sdl2_image',
    source='https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.4.tar.gz',
    checksum='e74ec49c2402eb242fbfa16f2f43a19582a74c2eabfbfb873f00d4250038ceac',
    dependencies=('sdl2', 'jpeg', 'png', 'tiff', 'webp'),
    commands=Library(
        '--disable-jpg-shared',
        '--disable-png-shared',
        '--disable-tif-shared',
        '--disable-webp-shared'
    )
)
pkg(
    name='sdl2_mixer',
    source='https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.4.tar.gz',
    checksum='b4cf5a382c061cd75081cf246c2aa2f9df8db04bdda8dcdc6b6cca55bede2419',
    dependencies=('sdl2', 'vorbis', 'flac', 'libmikmod', 'modplug', 'fluidsynth', 'smpeg2'),
    commands=Library(
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
    commands=Library()
)
pkg(
    name='sdl2_ttf',
    source='https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.14.tar.gz',
    checksum='34db5e20bcf64e7071fe9ae25acaa7d72bdc4f11ab3ce59acc768ab62fe39276',
    dependencies=('sdl2', 'freetype'),
    commands=Library()
)
pkg(
    name='slang',
    source='http://www.jedsoft.org/releases/slang/slang-2.3.1a.tar.bz2',
    checksum='54f0c3007fde918039c058965dffdfd6c5aec0bad0f4227192cc486021f08c36',
    dependencies=('pcre', 'png'),
    commands=(
        Configure(),
        Make('install-static')
    )
)
pkg(
    name='smpeg',
    source='https://github.com/alexey-lysiuk/bym/releases/download/sources/smpeg-0.4.5.tar.xz',
    checksum='1635cde79660440defa6b6641e1a7465ce8886b535dc123069adc31e65e947be',
    dependencies='sdl',
    commands=(
        Autogen(),
        Library(),
    )
)
pkg(
    name='smpeg2',
    source='https://www.libsdl.org/projects/smpeg/release/smpeg2-2.0.0.tar.gz',
    checksum='979a65b211744a44fa641a9b6e4d64e64a12ff703ae776bafe3c4c4cd85494b3',
    dependencies='sdl2',
    commands=Library()
)
pkg(
    name='sndfile',
    source='http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz',
    checksum='1ff33929f042fa333aed1e8923aa628c3ee9e1eb85512686c55092d1e5a9dfa9',
    dependencies=('ogg', 'vorbis', 'flac'),
    commands=Library()
)
pkg(
    name='speex',
    source='http://downloads.xiph.org/releases/speex/speex-1.2.0.tar.gz',
    checksum='eaae8af0ac742dc7d542c9439ac72f1f385ce838392dc849cae4536af9210094',
    dependencies='ogg',
    commands=Library()
)
pkg(
    name='sqlite',
    source='https://sqlite.org/2019/sqlite-autoconf-3270200.tar.gz',
    checksum='50c39e85ea28b5ecfdb3f9e860afe9ba606381e21836b2849efca6a0bfe6ef6e',
    dependencies='readline',
    commands=Library()
)
pkg(
    name='ssh2',
    source='https://libssh2.org/download/libssh2-1.8.0.tar.gz',
    checksum='39f34e2f6835f4b992cafe8625073a88e5a28ba78f83e8099610a7b3af4676d4',
    dependencies=('zlib', 'gcrypt'),
    commands=Library(
        '--with-libgcrypt=' + configuration.install_path,
        '--disable-examples-build'
    )
)
