#
#    Build Your Mac: Hackable build environment for macOS
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
import subprocess

import config


# Mount disk image to /usr/local and use it as install directory a.k.a. prefix
_USR_LOCAL_DISK_IMAGE = False

# String appended to all ...FLAGS environment variables
_EXTRA_FLAGS = ''
# _EXTRA_FLAGS = ' -mmacosx-version-min=10.7 -isysroot /Volumes/Storage/Work/devbuilds/macos_sdk/MacOSX10.7.sdk'

# String prepended to PATH environment variable
_EXTRA_PATH = ''
# _EXTRA_PATH = '/Applications/CMake.app/Contents/bin:'


def _mount_usr_local():
    basename = 'usr.local'
    filename = basename + '.sparseimage'
    filepath = config.BUILD_PATH + os.sep + filename

    if not os.path.exists(config.BUILD_PATH):
        os.makedirs(config.BUILD_PATH)

    if not os.path.exists(filename):
        subprocess.check_call(['hdiutil', 'create', '-size', '2g', '-type', 'SPARSE',
                               '-fs', 'HFS+', '-volname', basename, filepath])

    hdi_info = subprocess.check_output(['hdiutil', 'info'])

    if -1 == hdi_info.find(filename):
        subprocess.check_call(['sudo', '-k', 'hdiutil', 'attach', '-mountpoint', '/usr/local', filepath])


def main():
    if _USR_LOCAL_DISK_IMAGE:
        _mount_usr_local()

        config.INSTALL_PATH = '/usr/local'

    env = config.ENVIRON

    if len(_EXTRA_FLAGS) > 0:
        env['CPPFLAGS'] += _EXTRA_FLAGS
        env['CPPFLAGS'] += _EXTRA_FLAGS
        env['CFLAGS'] += _EXTRA_FLAGS
        env['CXXFLAGS'] += _EXTRA_FLAGS
        env['OBJCFLAGS'] += _EXTRA_FLAGS
        env['OBJCXXFLAGS'] += _EXTRA_FLAGS
        env['LDFLAGS'] += _EXTRA_FLAGS

    if len(_EXTRA_PATH) > 0:
        env['PATH'] = _EXTRA_PATH + env['PATH']

    # Other specific hacks
    # # The last version of GLib that supports Mac OS X 10.7 Lion is 2.44.1
    # glib = config.TARGETS['glib']
    # glib['url'] = 'https://download.gnome.org/sources/glib/2.44/glib-2.44.1.tar.xz'
    # glib['chk'] = '8811deacaf8a503d0a9b701777ea079ca6a4277be10e3d730d2112735d5eca07'
