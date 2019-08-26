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

#pragma once

#include <juce/config.h>
#define JUCE_GLOBAL_MODULE_SETTINGS_INCLUDED 1

#if JUCE_MODULE_AVAILABLE_juce_analytics
  #include <juce_analytics/juce_analytics.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_core
  #include <juce_core/juce_core.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_cryptography
  #include  <juce_cryptography/juce_cryptography.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_events
  #include  <juce_events/juce_events.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_data_structures
  #include  <juce_data_structures/juce_data_structures.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_basics
 #include  <juce_audio_basics/juce_audio_basics.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_devices
  #include  <juce_audio_devices/juce_audio_devices.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_formats
  #include  <juce_audio_formats/juce_audio_formats.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_processors
  #include  <juce_audio_processors/juce_audio_processors.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_audio_utils
  #include  <juce_audio_utils/juce_audio_utils.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_graphics
  #include  <juce_graphics/juce_graphics.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_box2d
  #include  <juce_box2d/juce_box2d.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_gui_basics
  #include  <juce_gui_basics/juce_gui_basics.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_gui_extra
  #include  <juce_gui_extra/juce_gui_extra.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_open_gl
  #include  <juce_opengl/juce_opengl.h>
#endif

#if JUCE_MODULE_AVAILABLE_juce_video
  #include  <juce_video/juce_video.h>
#endif
