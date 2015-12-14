/*
    JuceHeader.h - This file is part of libjuce
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

/*
    Compatibility for thirdpart juce modules and introjucer projects

    This file is here so that projects and thirdparty juce modules will
    compile with or without libjuce and not worry about handling the logic
    of including libjuce or the regular JuceHeader.h

    This header simply includes <juce/juce.h>
*/

#ifndef LIBJUCE_JUCE_HEADER_H
#define LIBJUCE_JUCE_HEADER_H

#include "./juce.h"

#endif
