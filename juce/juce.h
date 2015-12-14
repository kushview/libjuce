
#ifndef LIBJUCE_H
#define LIBJUCE_H

#include "modules/config.h"

#define JUCE_MODULE_AVAILABLE_juce_audio_basics          1
#define JUCE_MODULE_AVAILABLE_juce_audio_devices         1
#define JUCE_MODULE_AVAILABLE_juce_audio_formats         1
#define JUCE_MODULE_AVAILABLE_juce_audio_processors      1
#define JUCE_MODULE_AVAILABLE_juce_audio_utils           1
#define JUCE_MODULE_AVAILABLE_juce_box2d                 1
#define JUCE_MODULE_AVAILABLE_juce_core                  1
#define JUCE_MODULE_AVAILABLE_juce_cryptography          1
#define JUCE_MODULE_AVAILABLE_juce_data_structures       1
#define JUCE_MODULE_AVAILABLE_juce_events                1
#define JUCE_MODULE_AVAILABLE_juce_graphics              1
#define JUCE_MODULE_AVAILABLE_juce_gui_basics            1
#define JUCE_MODULE_AVAILABLE_juce_gui_extra             1
#define JUCE_MODULE_AVAILABLE_juce_opengl                1
#define JUCE_MODULE_AVAILABLE_juce_video                 1

#include "modules/juce_audio_basics/juce_audio_basics.h"
#include "modules/juce_audio_devices/juce_audio_devices.h"
#include "modules/juce_audio_formats/juce_audio_formats.h"
#include "modules/juce_audio_processors/juce_audio_processors.h"
#include "modules/juce_audio_utils/juce_audio_utils.h"
#include "modules/juce_box2d/juce_box2d.h"
#include "modules/juce_core/juce_core.h"
#include "modules/juce_cryptography/juce_cryptography.h"
#include "modules/juce_data_structures/juce_data_structures.h"
#include "modules/juce_events/juce_events.h"
#include "modules/juce_graphics/juce_graphics.h"
#include "modules/juce_gui_basics/juce_gui_basics.h"
#include "modules/juce_gui_extra/juce_gui_extra.h"
#include "modules/juce_opengl/juce_opengl.h"
#include "modules/juce_video/juce_video.h"

#if ! DONT_SET_USING_JUCE_NAMESPACE
 using namespace juce;
#endif

#endif
