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

from command import CMakeInstall, Library, Tool
import repository


pkg = repository.add_package


pkg(
    name='ogg',
    source='https://downloads.xiph.org/releases/ogg/libogg-1.3.3.tar.xz',
    checksum='4f3fc6178a533d392064f14776b23c397ed4b9f48f5de297aba73b643f955c08',
    commands=Library()
)
pkg(
    name='oggz',
    source='https://downloads.xiph.org/releases/liboggz/liboggz-1.1.1.tar.gz',
    checksum='6bafadb1e0a9ae4ac83304f38621a5621b8e8e32927889e65a98706d213d415a',
    dependencies='ogg',
    commands=Tool()
)
pkg(
    name='openal',
    source='http://kcat.strangesoft.net/openal-releases/openal-soft-1.19.0.tar.bz2',
    checksum='f1adf3a6e73e2f9270a0fd00887ea23793968fa787f60dcdec41a3b2f42a0ed6',
    commands=CMakeInstall(
        '-DLIBTYPE=STATIC',
        '-DCMAKE_BUILD_TYPE=Release',
    )
)
pkg(
    name='opus',
    source='https://archive.mozilla.org/pub/opus/opus-1.2.1.tar.gz',
    checksum='cfafd339ccd9c5ef8d6ab15d7e1a412c054bf4cb4ecbbbcc78c12ef2def70732',
    commands=Library()
)
pkg(
    name='opusfile',
    source='https://archive.mozilla.org/pub/opus/opusfile-0.9.tar.gz',
    checksum='f75fb500e40b122775ac1a71ad80c4477698842a8fe9da4a1b4a1a9f16e4e979',
    dependencies=('opus', 'ogg'),
    commands=Library('--disable-http')
)
pkg(
    name='opus-tools',
    source='https://archive.mozilla.org/pub/opus/opus-tools-0.1.10.tar.gz',
    checksum='a2357532d19471b70666e0e0ec17d514246d8b3cb2eb168f68bb0f6fd372b28c',
    dependencies=('opus', 'ogg', 'flac'),
    commands=Tool()
)
