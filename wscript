# encoding: utf-8

NAME = 'xf86-input-xwiimote'
DATE = '11/07/2012'
VERSION = '0.2'
WEBSITE = 'http://hg.pysoy.org/xf86-input-wiimote'
LICENSE = '''
    XInput Module for Wii Remote
    Copyright (C) 2012 Copyleft Games Group
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import os
top = '.'
out = 'build'

def options(opt) :
    opt.tool_options('gcc gxx')
    opt.load('compiler_c')

def configure(conf) :
    if not conf.env.PKGCONFIG :
        conf.find_program('pkg-config', var='PKGCONFIG')
    conf.env['PACKAGE'] = 'xf86-input-xwiimote'
    conf.load('compiler_c')   
    conf.define('PACKAGE', NAME)
    conf.define('PACKAGE_VERSION_MAJOR',0)
    conf.define('PACKAGE_VERSION_MINOR',2)
    conf.define('PACKAGE_VERSION_PATCHLEVEL',0)
    conf.check_cfg(package='bluez', uselib_store='BLUEZ', mandatory=True,
                   args='--cflags --libs')
    conf.check_cfg(package='xorg-server', uselib_store='XORG', mandatory=True,
                   atleast_version='1.10', args='--cflags --libs')
    conf.check_cfg(package='xproto', uselib_store='XPROTO', mandatory=True, args='--cflags --libs')
    conf.check_cfg(package='inputproto', uselib_store='INPUTPROTO', mandatory=True, args='--cflags --libs')
    conf.check_cfg(package='libudev', uselib_store='UDEV', mandatory=True, args='--cflags --libs')

    conf.write_config_header ('config.h')
    xorgserverlibdir = conf.cmd_and_log("pkg-config xorg-server --variable=moduledir").strip()
    conf.env.LIBDIR = xorgserverlibdir + '/input/'
    conf.env.cshlib_PATTERN = '%s.so'
def build(bld) :
    bld.define('PACKAGE', NAME)
    bld.define('VERSION', VERSION)
    bld.add_subdirs('src')
    bld.add_group ()

