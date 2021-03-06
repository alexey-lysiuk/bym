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

from command import Autogen, Make, CMakeInstall, Configure, Library, Tool
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
    source='https://hg.libsdl.org/SDL/archive/ab7529cb9558.tar.bz2',
    checksum='5059e831b56fe43a08859d4696a4dcfc1be6a8e826e7a214e114cd7f14cbefd4',
    dependencies='iconv',
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
    source='https://libsdl.org/release/SDL2-2.0.12.tar.gz',
    checksum='349268f695c02efbc9b9148a70b85e58cefbbf704abd3e91be654db7f1e2c863',
    dependencies='iconv',
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
    source='https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.5.tar.gz',
    checksum='bdd5f6e026682f7d7e1be0b6051b209da2f402a2dd8bd1c4bd9c25ad263108d0',
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
    dependencies=('sdl2', 'vorbis', 'flac', 'libmikmod', 'modplug', 'fluidsynth', 'opusfile', 'mpg123'),
    commands=Library(
        # LDFLAGS variable is needed for FluidSynth detection and linking of samples
        'LDFLAGS=-framework AudioUnit -framework CoreAudio -framework CoreAudio -framework CoreFoundation '
        ' -framework CoreMIDI -framework CoreServices -framework Foundation -liconv'
        ' -lintl -lglib-2.0 -lgobject-2.0 -lffi -lpcre -linstpatch-1.0'
        ' -logg -lvorbis -lvorbisenc -lvorbisfile -lFLAC -lsndfile '
        + configuration.environment['LDFLAGS'],
        '--enable-music-mod-mikmod',
        '--enable-music-mp3-mpg123',
        '--disable-music-ogg-shared',
        '--disable-music-flac-shared',
        '--disable-music-midi-fluidsynth-shared',
        '--disable-music-mod-mikmod-shared',
        '--disable-music-mod-modplug-shared',
        '--disable-music-opus-shared'
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
    source='https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.tar.gz',
    checksum='a9eceb1ad88c1f1545cd7bd28e7cbc0b2c14191d40238f531a15b01b1b22cd33',
    dependencies=('sdl2', 'freetype'),
    commands=Library()
)
pkg(
    name='sfml',
    source='https://www.sfml-dev.org/files/SFML-2.5.1-sources.zip',
    checksum='bf1e0643acb92369b24572b703473af60bac82caf5af61e77c063b779471bb7f',
    dependencies=('vorbis', 'flac', 'openal', 'freetype'),
    commands=CMakeInstall(
        '-DBUILD_SHARED_LIBS=NO',
        '-DSFML_USE_SYSTEM_DEPS=YES',
        '-DSFML_MISC_INSTALL_PREFIX=' + configuration.install_path + '/share/SFML',
        # Use OpenAL Soft instead of Apple's framework
        '-DOPENAL_INCLUDE_DIR=' + configuration.include_path + '/AL',
        '-DOPENAL_LIBRARY=' + configuration.lib_path + '/libopenal.a',
    )
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
    name='smartmontools',
    source='https://downloads.sourceforge.net/project/smartmontools/smartmontools/7.1/smartmontools-7.1.tar.gz',
    checksum='3f734d2c99deb1e4af62b25d944c6252de70ca64d766c4c7294545a2e659b846',
    commands=Tool(
        '--sbindir=' + configuration.bin_path,
        '--with-nvme-devicescan',
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
    source='https://github.com/libsndfile/libsndfile/releases/download/v1.0.30/libsndfile-1.0.30.tar.bz2',
    checksum='9df273302c4fa160567f412e10cc4f76666b66281e7ba48370fb544e87e4611a',
    dependencies=('ogg', 'vorbis', 'flac', 'opus'),
    commands=CMakeInstall('-DBUILD_REGTEST=NO')
)
pkg(
    name='sodium',
    source='https://github.com/jedisct1/libsodium/archive/1.0.18-RELEASE.tar.gz',
    checksum='b7292dd1da67a049c8e78415cd498ec138d194cfdb302e716b08d26b80fecc10',
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
    source='https://sqlite.org/2020/sqlite-autoconf-3310100.tar.gz',
    checksum='62284efebc05a76f909c580ffa5c008a7d22a1287285d68b7825a2b6b51949ae',
    dependencies='readline',
    commands=Library()
)
pkg(
    name='ssh2',
    source='https://libssh2.org/download/libssh2-1.9.0.tar.gz',
    checksum='d5fb8bd563305fd1074dda90bd053fb2d29fc4bce048d182f96eaa466dfadafd',
    dependencies=('zlib', 'openssl'),
    commands=Library(
        '--with-libssl-prefix=' + configuration.install_path,
        '--disable-examples-build'
    )
)
