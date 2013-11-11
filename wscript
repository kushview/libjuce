#!/usr/bin/evn python
# encoding: utf-8
# Copyright (C) 2012 Michael Fisher <mfisher31@gmail.com>

''' This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public Licence as published by
the Free Software Foundation, either version 3 of the Licence, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
file COPYING for more details. '''

import sys, os, platform
from subprocess import call

sys.path.insert(0, "tools/waf")
import juce
from juce import IntrojucerProject as Project


JUCE_VERSION  ="2.1.8"
EXTRA_VERSION =""

PKG_VERSION   ="2.0"

LIBJUCE_VERSION=JUCE_VERSION+EXTRA_VERSION
LIBJUCE_MAJOR_VERSION=2
LIBJUCE_MINOR_VERSION=1
LIBJUCE_MICRO_VERSION=8
LIBJUCE_EXTRA_VERSION=EXTRA_VERSION

# For waf dist
APPNAME = 'libjuce'
VERSION = LIBJUCE_VERSION

# Waf wants these as well
top = '.'
out = 'build'

def options(opts):
    opts.load("compiler_c compiler_cxx juce")

    opts.add_option('--introjucer', default=False, action="store_true", \
        dest="introjucer", help="Disable Jucer Builds [ Default: False ]")
    opts.add_option('--juce-demo', default=False, action="store_true", \
        dest="juce_demo", help="Build the JUCE Demo [ Default: False ]")
    opts.add_option('--static', default=False, action="store_true", \
        dest="static", help="Build Static Libraries [ Default: False ]")
    opts.add_option('--ziptype', default='gz', type='string', \
        dest='ziptype', help="Zip type for waf dist (gz/bz2/zip) [ Default: gz ]")

def configure(conf):
    conf.load("compiler_c compiler_cxx")

    # Put some defines in a header file
    conf.define ("LIBJUCE_VERSION", VERSION)
    conf.define ("LIBJUCE_MAJOR_VERSION",LIBJUCE_MAJOR_VERSION)
    conf.define ("LIBJUCE_MINOR_VERSION",LIBJUCE_MINOR_VERSION)
    conf.define ("LIBJUCE_MICRO_VERSION",LIBJUCE_MICRO_VERSION)
    conf.define ("LIBJUCE_EXTRA_VERSION",LIBJUCE_EXTRA_VERSION)
    conf.define ("UPSTREAM_VERSION", JUCE_VERSION);
    conf.write_config_header ("Version.h")

    conf.check_inline()

    conf.env.DATADIR    = conf.env.PREFIX + '/share'
    conf.env.LIBDIR     = conf.env.PREFIX + '/lib'
    conf.env.BINDIR     = conf.env.PREFIX + '/bin'
    conf.env.INCLUDEDIR = conf.env.PREFIX + '/include'

    conf.load ('juce')
    # override a few juce.py environment vars
    conf.env.JUCE_MODULE_PATH = 'src/modules'

    # Export version to the environment
    conf.env.LIBJUCE_MAJOR_VERSION = LIBJUCE_MAJOR_VERSION
    conf.env.LIBJUCE_MINOR_VERSION = LIBJUCE_MINOR_VERSION
    conf.env.LIBJUCE_MICRO_VERSION = LIBJUCE_MICRO_VERSION
    conf.env.APPNAME               = APPNAME

    # Store options in environment
    conf.env.BUILD_INTROJUCER  = conf.options.introjucer
    conf.env.BUILD_JUCE_DEMO   = conf.options.juce_demo
    conf.env.BUILD_STATIC      = conf.options.static

    conf.check_cfg (package='x11',  uselib_store='X11',  args=['--libs', '--cflags'], mandatory=False)
    conf.check_cfg (package='xext', uselib_store='XEXT', args=['--libs', '--cflags'], mandatory=False)
    conf.check_cfg (package='gl',   uselib_store='GL',   args=['--libs', '--cflags'], mandatory=False)
    conf.check_cfg (package='alsa', uselib_store='ALSA', args=['--libs', '--cflags'], mandatory=False)
    conf.check_cfg (package='jack', uselib_store='JACK', args=['--libs', '--cflags'], mandatory=False)
    conf.check_cfg (package='freetype2', uselib_store='FREETYPE2', args=['--libs', '--cflags'], mandatory=True)

def make_desktop (bld, slug):
    location = 'data'
    src = "data/%s.desktop.in" % (slug)
    tgt = "%s.desktop" % (slug)

    if os.path.exists(src):
        bld (features = "subst",
            source    = src,
            target    = tgt,
            name      = tgt,
            JUCE_DATA = "%s/juce" % (bld.env.DATADIR),
            install_path = bld.env.DATADIR + "/applications"
        )

library_modules = '''
    juce_audio_basics
    juce_audio_devices
    juce_audio_formats
    juce_audio_processors
    juce_audio_utils
    juce_box2d
    juce_core
    juce_cryptography
    juce_data_structures
    juce_events
    juce_graphics
    juce_gui_basics
    juce_gui_extra
    juce_opengl
    juce_video
'''.split()

def install_module_headers (bld, modules):
    for mod in modules:
        bld.install_files (bld.env.INCLUDEDIR + '/juce-2', bld.path.ant_glob ("src/modules/" + mod + "/**/*.h"), \
            relative_trick=True, cwd=bld.path.find_dir ("src"))

def build (bld):

    modules = juce.build_modular_libs (bld, library_modules, JUCE_VERSION)
    for module in modules:
        module.includes += ['project/JuceLibraryCode']
    install_module_headers (bld, library_modules)
    bld.add_group()

    if bld.env.BUILD_INTROJUCER:
        introjucer = juce.IntrojucerProject ('src/extras/Introjucer/Introjucer.jucer')
        make_desktop (bld, "Introjucer")
        bld.program (
            source    = introjucer.getBuildableCode (bld.env.JUCE_MODULE_PATH),
            includes  = [introjucer.getLibraryCodePath()],
            name      = 'Introjucer',
            target    = 'Introjucer',
            use       = ['X11', 'XEXT', 'FREETYPE2'],
            linkflags = ['-lpthread', '-lrt', '-ldl']
        )
        bld.add_group()

    if bld.env.BUILD_JUCE_DEMO:
        demo = juce.IntrojucerProject ('src/extras/JuceDemo/Juce Demo.jucer')
        make_desktop (bld, "JuceDemo")
        bld.program (
            source    = demo.getBuildableCode (bld.env.JUCE_MODULE_PATH),
            includes  = [demo.getLibraryCodePath()],
            name      = 'JuceDemo',
            target    = 'JuceDemo',
            use       = ['X11', 'XEXT', 'FREETYPE2', 'ALSA', 'GL'],
            linkflags = ['-lpthread', '-lrt', '-ldl']
        )
        bld.add_group()

    # Install common juce data
    bld.install_files (bld.env.DATADIR + '/juce/icons', 'data/juce_icon.xpm')
    bld.install_files (bld.env.INCLUDEDIR + '/juce-2', 'project/JuceLibraryCode/AppConfig.h')
    bld.install_files (bld.env.INCLUDEDIR + '/juce-2', 'project/JuceLibraryCode/JuceHeader.h')

def dist(ctx):
    z=ctx.options.ziptype
    if 'zip' in z:
        ziptype = z
    else:
        ziptype = "tar." + z
    ctx.algo       = ziptype
