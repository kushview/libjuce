#!/bin/bash
set -ex
here="`pwd`"
cd "${here}/src/doxygen" && make
mkdir -p "${here}/build/doc"
rsync -ar --delete ${here}/src/doxygen/doc/ ${here}/build/doc/
cd "${here}/src/doxygen" && make clean
exit 0
