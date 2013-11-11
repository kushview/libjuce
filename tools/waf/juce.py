#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, platform, sys, unicodedata
from xml.etree import ElementTree as ET

from waflib import Utils, Logs, Errors
from waflib.Configure import conf


@conf
def check_juce (self):
    self.start_msg ("Checking for JUCE")
    mpath = self.env.JUCE_MODULES_PATH = self.options.juce_modules

    if os.path.exists(mpath):
        minfo = open(mpath + "/juce_core/juce_module_info")
        mdata = json.load(minfo)
        minfo.close()
        self.end_msg(mdata["version"])
    else:
        self.end_msg ("no")

def is_mac():
    return 'Darwin' in platform.system()

def is_linux():
    return 'Linux' in platform.system()

def is_win32():
    return 'Windows' in platform.system()

def get_deps(mod):
    if "juce_audio_basics" == mod:
        return ['juce_core']
    elif "juce_audio_devices" == mod:
        return ['juce_audio_basics', 'juce_audio_formats', 'juce_events']
    elif "juce_audio_formats" == mod:
        return ['juce_audio_basics']
    elif "juce_audio_processors" == mod:
        return ['juce_audio_basics', 'juce_gui_extra']
    elif "juce_audio_utils" == mod:
        return ['juce_gui_basics', 'juce_audio_devices', 'juce_audio_processors', 'juce_audio_formats']
    elif "juce_core" == mod:
        return []
    elif "juce_cryptography" == mod:
        return ['juce_core']
    elif "juce_data_structures" == mod:
        return ['juce_core', 'juce_events']
    elif "juce_events" == mod:
        return ['juce_core']
    elif "juce_events" == mod:
        return ['juce_core']
    elif "juce_graphics" == mod:
        return ['juce_core','juce_events']
    elif "juce_gui_basics" == mod:
        return ['juce_core', 'juce_events', 'juce_graphics', 'juce_data_structures']
    elif "juce_gui_extra" == mod:
        return ['juce_gui_basics']
    elif "juce_opengl" == mod:
        return ['juce_gui_extra']
    elif "juce_video" == mod:
        return ['juce_gui_extra']
    else:
        return []

def get_frameworks(mod):
    if "juce_audio_basics" == mod:
        return ['COCOA', 'ACCELERATE']
    elif "juce_audio_devices" == mod:
        return ['CORE_AUDIO', 'CORE_MIDI', 'DISK_RECORDING']
    elif "juce_audio_formats" == mod:
        return ['CORE_AUDIO', 'CORE_MIDI', 'QUARTZ_CORE', 'AUDIO_TOOLBOX']
    elif "juce_audio_processors" == mod:
        return ['CORE_AUDIO', 'CORE_AUDIO_KIT', 'AUDIO_UNIT', 'CORE_MIDI', 'AUDIO_TOOLBOX']
    elif "juce_audio_utils" == mod:
        return []
    elif "juce_core" == mod:
        return ['COCOA', 'IOKIT']
    elif "juce_events" == mod:
        return ['IOKIT', 'COCOA']
    elif "juce_graphics" == mod:
        return ['COCOA', 'QUARTZ_CORE']
    elif "juce_gui_basics" == mod:
        return ['COCOA', 'CARBON', 'QUARTZ_CORE']
    elif "juce_gui_extra" == mod:
        return ['WEB_KIT']
    elif "juce_opengl" == mod:
        return ['OPENGL']
    else:
        return []

def get_use_libs (mod):
    return get_frameworks (mod)

def options(opt):
    pass

def configure (conf):

    outdir = conf.options.out
    if len (outdir) == 0:
        outdir = "build"

    conf.env.JUCE_MODULE_PATH = "libs/juce/modules"

def extension():
    if platform.system() != "Darwin":
        return ".cpp"
    else:
        return ".mm"

def find (ctx, pattern):
    if len(pattern) <= 0:
        return None
    pattern = '%s/**/%s' % (ctx.env.JUCE_MODULE_PATH, pattern)
    return ctx.path.ant_glob (pattern)

def build_modular_libs (bld, mods, vnum=""):

    libs = []
    mext = extension()

    for mod in mods:
        src = find (bld, mod + mext)
        obj = bld (
            features    = "cxx cxxshlib",
            source      = src,
            name        = mod,
            target      = mod,
            use         = get_use_libs (mod) + get_deps (mod),
            includes    = []
        )
        if len(vnum) > 0:
            obj.vnum = vnum
        libs += [obj]
    return libs

def create_unified_lib (bld, tgt, mods, feats="cxx cxxshlib"):

    mext = extension()

    mod_path = bld.env.JUCE_MODULE_PATH
    src = []
    ug  = []

    for mod in mods:
        src += [mod_path + "/" + mod + "/" + mod + mext]
        ug += get_use_libs (mod)

    # strip out duplicate use libs
    us = []
    for u in ug:
        if not u in us:
            us += [u]

    obj = bld (
        features    = feats,
        source      = src,
        includes    = ["element/juce"],
        name        = tgt,
        target      = tgt,
        use         = us
    )

    return obj

def module_path (ctx):
    return ctx.env.JUCE_MODULE_PATH

def available_modules (ctx):
    return os.listdir (module_path (ctx))

def display_msg (conf, msg, status = None, color = None):
    color = 'CYAN'
    if type(status) == bool and status or status == "True":
        color = 'GREEN'
    elif type(status) == bool and not status or status == "False":
        color = 'YELLOW'
    Logs.pprint('BOLD', " *", sep='')
    Logs.pprint('NORMAL', "%s" % msg.ljust(conf.line_just - 3), sep='')
    Logs.pprint('BOLD', ":", sep='')
    Logs.pprint(color, status)


def module_source(bld, m):
        code = '%s/juce_%s/juce_%s.cpp' % (bld.env.JUCE_MODULES_PATH, m, m)
        if os.path.isabs(code):
                return bld.root.find_resource(code)

        return bld.path.find_resource(code)

# this will eventually be used in a custom task generator
class IntrojucerProject:
    data = None
    proj = None
    root = None

    def __init__ (self, project):
        if os.path.exists (project):
            self.proj = project
            data = ET.parse (self.proj)

            if data.getroot().tag == "JUCERPROJECT":
                self.data = data
                self.root = data.getroot()
            else:
                self.data = None

    def isValid (self):
        return self.data != None and self.name != None

    def getProperty (self, prop):
        return self.root.attrib[prop]

    def getId (self):
        return self.getProperty ("id")

    def getName (self):
        return self.getProperty ("name")

    def getVersion (self):
        return self.getProperty ("version")

    def getJucerVersion (self):
        return self.getProperty ("jucerVersion")

    def getProjectType(self):
        return self.getProperty ("projectType")

    def getBundleIdentifier (self):
        return self.getProperty ("bundleIdentifier")

    def getModules(self):
        mods = []
        for mod in self.root.iter ("MODULE"):
            mods += [mod.attrib ["id"]]
        return mods

    def getProjectDir(self):
         return os.path.relpath (os.path.join(self.proj, ".."))

    def getProjectCode(self):
        code = []
        for c in self.root.iter("FILE"):
            if "compile" in c.attrib and c.attrib["compile"] == "1":
                f = "%s" % (c.attrib["file"])
                #f = os.path.relpath(unicodedata.normalize("NFKD", f).encode('ascii','ignore'))
                parent = os.path.join (self.proj, "..")
                code.append (os.path.join (parent, os.path.relpath(f)))
        return code

    def getLibraryCode (self, module_path):
        code = []
        for mod in self.getModules():
            infofile = os.path.join (module_path, mod, "juce_module_info")
            if os.path.exists(infofile):
                res = open(infofile)
                data = json.load(res)
                res.close()

                if "compile" in data:
                    for i in data["compile"]:
                        if "target" in i and i["target"] == "! xcode":
                            f = "%s/%s/%s" % (module_path, mod, i["file"])
                            f = os.path.relpath(unicodedata.normalize("NFKD", f).encode('ascii','ignore'))
                            code.append(f)

        # Add binary data file if it exists
        bd = os.path.join (self.getProjectDir(), "JuceLibraryCode/BinaryData.cpp")
        if os.path.exists(bd): code.append (bd)

        return code

    def getLibraryCodePath (self):
        return os.path.join (self.getProjectDir(), "JuceLibraryCode")

    def getBuildableCode (self, module_path):
        return self.getProjectCode() + self.getLibraryCode(module_path)
