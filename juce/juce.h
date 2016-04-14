/*
    juce.h - This file is part of libjuce
    Copyright (C) 2015  Kushview, LLC. All rights reserved.

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
*/

#ifndef LIBJUCE_H
#define LIBJUCE_H

#include "modules/config.h"
#define JUCE_GLOBAL_MODULE_SETTINGS_INCLUDED 1

#if JUCE_MODULE_AVAILABLE_juce_core
  #include "modules/juce_core/juce_core.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_cryptography
  #include "modules/juce_cryptography/juce_cryptography.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_events
  #include "modules/juce_events/juce_events.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_data_structures
  #include "modules/juce_data_structures/juce_data_structures.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_basics
 #include "modules/juce_audio_basics/juce_audio_basics.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_devices
  #include "modules/juce_audio_devices/juce_audio_devices.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_formats
  #include "modules/juce_audio_formats/juce_audio_formats.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_processors
  #include "modules/juce_audio_processors/juce_audio_processors.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_utils
  #include "modules/juce_audio_utils/juce_audio_utils.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_graphics
  #include "modules/juce_graphics/juce_graphics.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_box2d
  #include "modules/juce_box2d/juce_box2d.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_gui_basics
  #include "modules/juce_gui_basics/juce_gui_basics.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_gui_extra
  #include "modules/juce_gui_extra/juce_gui_extra.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_open_gl
  #include "modules/juce_opengl/juce_opengl.h"
#endif

#if JUCE_MODULE_AVAILABLE_juce_video
  #include "modules/juce_video/juce_video.h"
#endif

#if ! DONT_SET_USING_JUCE_NAMESPACE
  using namespace juce;
#endif

#endif
