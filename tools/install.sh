#!/bin/bash

set -ex
./waf configure clean build --introjucer --juce-demo
./waf install
./waf clean configure build --debug
./waf install --no-headers
./waf distclean
