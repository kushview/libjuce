#!/bin/bash

set -ex

./waf distclean
./waf configure $@
./waf build 
sudo ./waf install 

./waf clean 
./waf configure --debug $@
./waf build
sudo ./waf install --no-headers
./waf distclean
