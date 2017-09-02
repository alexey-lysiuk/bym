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

import configuration


_cmake_dependency = () if os.path.exists(configuration.cmake_executable) else ('cmake',)

_no_dep_track = ('--disable-dependency-tracking',)

_configure = (
    './configure',
    '--prefix=' + configuration.install_path
)

_configure_static = _configure + (
    '--enable-static',
    '--disable-shared',
)
_configure_static += _no_dep_track

_cmake = (
    configuration.cmake_executable,
    '-DCMAKE_INSTALL_PREFIX=' + configuration.install_path
)
_cmake += configuration.cmake_arguments

_install = (configuration.make_executable,)
_install += configuration.make_arguments
_install += ('install',)


# TODO: name aliases: 'libogg' -> 'ogg'

packages = {
    'ao': {
        'url': 'http://downloads.xiph.org/releases/ao/libao-1.2.0.tar.gz',
        'chk': '03ad231ad1f9d64b52474392d63c31197b0bc7bd416e58b1c10a329a5ed89caf',
        # 'url': 'https://github.com/xiph/libao/archive/1.2.2.tar.gz',
        # 'chk': 'df8a6d0e238feeccb26a783e778716fb41a801536fe7b6fce068e313c0e2bf4d',
        'cmd': (
            _configure_static,
            _install
        )
    },

    'autoconf': {
        'url': 'https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.xz',
        'chk': '64ebcec9f8ac5b2487125a86a7760d2591ac9e1d3dbd59489633f9de62a57684',
        'cmd': (
            _configure,
            _install
        )
    },

    'automake': {
        'url': 'https://ftp.gnu.org/gnu/automake/automake-1.15.1.tar.xz',
        'chk': 'af6ba39142220687c500f79b4aa2f181d9b24e4f8d8ec497cea4ba26c64bedaf',
        'cmd': (
            _configure,
            _install
        )
    },

    'cmake': {
        'url': 'https://cmake.org/files/v3.9/cmake-3.9.1.tar.gz',
        'chk': 'd768ee83d217f91bb597b3ca2ac663da7a8603c97e1f1a5184bc01e0ad2b12bb',
        'cmd': (
            _configure,
            _install
        )
    },

    'ffi': {
        'url': 'https://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz',
        'chk': 'd06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37',
        'cmd': (
            _configure_static,
            _install
        )
    },

    'flac': {
        'url': 'https://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz',
        'chk': '91cfc3ed61dc40f47f050a109b08610667d73477af6ef36dcad31c31a4a8d53f',
        'dep': ('ogg',),
        'cmd': (
            _configure_static,
            _install
        )
    },

    'fluidsynth': {
        'url': 'https://downloads.sourceforge.net/project/fluidsynth/fluidsynth-1.1.6/fluidsynth-1.1.6.tar.gz',
        'chk': '50853391d9ebeda9b4db787efb23f98b1e26b7296dd2bb5d0d96b5bccee2171c',
        'dep': _cmake_dependency + ('pkg-config', 'glib', 'sndfile'),
        'cmd': (
            _cmake + (
                '-DCMAKE_BUILD_TYPE=Release', '-DBUILD_SHARED_LIBS=NO', '-DLIB_SUFFIX=',
                '-Denable-framework=NO', '-Denable-readline=NO', '.',
                '-DCMAKE_EXE_LINKER_FLAGS=-logg -lvorbis -lvorbisenc -lFLAC -L' + configuration.lib_path +
                ' -framework AudioToolbox -framework AudioUnit -framework CoreAudio'
            ),
            _install
        )
    },

    'gettext': {
        'url': 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.19.8.1.tar.xz',
        'chk': '105556dbc5c3fbbc2aa0edb46d22d055748b6f5c7cd7a8d99f8e7eb84e938be4',
        'cmd': (
            _configure_static,
            _install
        )
    },

    'glib': {
        'url': 'https://download.gnome.org/sources/glib/2.52/glib-2.52.3.tar.xz',
        'chk': '25ee7635a7c0fcd4ec91cbc3ae07c7f8f5ce621d8183511f414ded09e7e4e128',
        'dep': ('ffi', 'gettext', 'pcre'),
        'cmd': (
            _configure_static,
            _install
        )
    },

    'libtool': {
        'url': 'http://ftp-gnu-org.ip-connect.vn.ua/libtool/libtool-2.4.6.tar.xz',
        'chk': '7c87a8c2c8c0fc9cd5019e402bed4292462d00a718a7cd5f11218153bf28b26f',
        'cmd': (
            _configure,
            _install
        )
    },

    'mpg123': {
        'url': 'https://www.mpg123.de/download/mpg123-1.25.6.tar.bz2',
        'chk': '0f0458c9b87799bc2c9bf9455279cc4d305e245db43b51a39ef27afe025c5a8e',
        'cmd': (
            _configure_static,
            _install
        )
    },

    'ogg': {
        'url': 'https://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.xz',
        'chk': '3f687ccdd5ac8b52d76328fbbfebc70c459a40ea891dbf3dccb74a210826e79b',
        'cmd': (
            _configure_static,
            _install
        )
    },

    'oggz': {
        'url': 'https://downloads.xiph.org/releases/liboggz/liboggz-1.1.1.tar.gz',
        'chk': '6bafadb1e0a9ae4ac83304f38621a5621b8e8e32927889e65a98706d213d415a',
        'dep': ('ogg',),
        'cmd': (
            _configure + _no_dep_track,
            _install
        )
    },

    'openal': {
        'url': 'http://kcat.strangesoft.net/openal-releases/openal-soft-1.18.1.tar.bz2',
        'chk': '2d51a6529526ef22484f51567e31a5c346a599767991a3dc9d4dcd9d9cec71dd',
        'dep': _cmake_dependency,
        'cmd': (
            _cmake + (
                '-DLIBTYPE=STATIC',
                '-DCMAKE_BUILD_TYPE=Release',
                '-DALSOFT_EMBED_HRTF_DATA=YES',
                '.'
            ),
            _install
        )
    },

    'opus': {
        'url': 'https://archive.mozilla.org/pub/opus/opus-1.2.1.tar.gz',
        'chk': 'cfafd339ccd9c5ef8d6ab15d7e1a412c054bf4cb4ecbbbcc78c12ef2def70732',
        'cmd': (
            _configure + _no_dep_track,
            _install
        )
    },

    'opusfile': {
        'url': 'https://archive.mozilla.org/pub/opus/opusfile-0.9.tar.gz',
        'chk': 'f75fb500e40b122775ac1a71ad80c4477698842a8fe9da4a1b4a1a9f16e4e979',
        'dep': ('pkg-config', 'opus', 'ogg'),
        'cmd': (
            _configure + ('--disable-http',) + _no_dep_track,
            _install
        )
    },

    'opus-tools': {
       'url': 'https://archive.mozilla.org/pub/opus/opus-tools-0.1.10.tar.gz',
       'chk': 'a2357532d19471b70666e0e0ec17d514246d8b3cb2eb168f68bb0f6fd372b28c',
       'dep': ('pkg-config', 'opus', 'ogg', 'flac'),
       'cmd': (
           _configure + _no_dep_track,
           _install
       )
    },

    'pcre': {
        'url': 'https://ftp.pcre.org/pub/pcre/pcre-8.41.tar.bz2',
        'chk': 'e62c7eac5ae7c0e7286db61ff82912e1c0b7a0c13706616e94a7dd729321b530',
        'cmd': (
            _configure_static + ('--enable-unicode-properties',),
            _install
        )
    },

    'pkg-config': {
        'url': 'https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
        'chk': '6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591',
        'cmd': (
            _configure + ('--with-internal-glib',),
            _install
        )
    },

    'sdl2': {
        'url': 'https://libsdl.org/release/SDL2-2.0.5.tar.gz',
        'chk': '442038cf55965969f2ff06d976031813de643af9c9edc9e331bd761c242e8785',
        'cmd': (
            _configure_static,
            _install
        )
    },

    'sdl2_net': {
        'url': 'https://www.libsdl.org/projects/SDL_net/release/SDL2_net-2.0.1.tar.gz',
        'chk': '15ce8a7e5a23dafe8177c8df6e6c79b6749a03fff1e8196742d3571657609d21',
        'dep': ('sdl2',),
        'cmd': (
            _configure_static,
            _install
        )
    },

    'sndfile': {
        'url': 'http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz',
        'chk': '1ff33929f042fa333aed1e8923aa628c3ee9e1eb85512686c55092d1e5a9dfa9',
        'dep': ('pkg-config', 'ogg', 'vorbis', 'flac'),
        'cmd': (
            _configure_static,
            _install
        )
    },

    'speex': {
        'url': 'http://downloads.xiph.org/releases/speex/speex-1.2.0.tar.gz',
        'chk': 'eaae8af0ac742dc7d542c9439ac72f1f385ce838392dc849cae4536af9210094',
        'dep': ('ogg',),
        'cmd': (
            _configure_static,
            _install
        )
    },

    'timidity': {
        'url': 'https://downloads.sourceforge.net/project/timidity/'
               'TiMidity++/TiMidity++-2.14.0/TiMidity++-2.14.0.tar.bz2',
        'chk': 'f97fb643f049e9c2e5ef5b034ea9eeb582f0175dce37bc5df843cc85090f6476',
        'dep': ('vorbis', 'flac', 'speex', 'ao'),
        'cmd': (
            _configure + ('--enable-audio=darwin,vorbis,flac,speex,ao',) + _no_dep_track,
            _install
        )
    },

    'vorbis': {
        'url': 'https://downloads.xiph.org/releases/vorbis/libvorbis-1.3.5.tar.xz',
        'chk': '54f94a9527ff0a88477be0a71c0bab09a4c3febe0ed878b24824906cd4b0e1d1',
        'dep': ('ogg',),
        'cmd': (
            _configure_static,
            _install
        )
    },

    'vorbis-tools': {
        'url': 'https://downloads.xiph.org/releases/vorbis/vorbis-tools-1.4.0.tar.gz',
        'chk': 'a389395baa43f8e5a796c99daf62397e435a7e73531c9f44d9084055a05d22bc',
        'dep': ('vorbis', 'flac', 'ao'),
        'cmd': (
            _configure + _no_dep_track,
            _install
        )
    },
}


patches = {
    # https://sourceforge.net/p/timidity/git/ci/6e189f6073e979ceccaf05c3bb5f495a1b9ed87e/tree/timidity/mfi.c?diff=7eaa3a5e7782cfa741e7f4642156ccd08218deb4
    'timidity': '''
--- a/timidity/mfi.c
+++ b/timidity/mfi.c
@@ -344,7 +344,7 @@
 #define SEND_LASTNOTEINFO(lni, ch)				if (LASTNOTEINFO_HAS_DATA((lni)[ch])) SendLastNoteInfo(lni, ch);
 #define SEND_AND_CLEAR_LASTNOTEINFO(lni, ch)	if (LASTNOTEINFO_HAS_DATA((lni)[ch])) { SendLastNoteInfo(lni, ch); (lni)[ch].on = NO_LAST_NOTE_INFO; }

-inline void StoreLastNoteInfo(LastNoteInfo *info, int channel, int time, int duration, int note, int velocity)
+static inline void StoreLastNoteInfo(LastNoteInfo *info, int channel, int time, int duration, int note, int velocity)
 {
 \tinfo[channel].on = time;
 \tinfo[channel].off = time + duration;
@@ -352,7 +352,7 @@
 \tinfo[channel].velocity = velocity;
 }

-inline void SendLastNoteInfo(const LastNoteInfo *info, int channel)
+static inline void SendLastNoteInfo(const LastNoteInfo *info, int channel)
 {
 \tNOTE_BUF_EV_DEBUGSTR(channel, info[channel].on, note_name[info[channel].note % 12], info[channel].note / 12, info[channel].velocity, info[channel].off);
 \tMIDIEVENT(info[channel].on, ME_NOTEON, channel, info[channel].note, info[channel].velocity);
''',
}
