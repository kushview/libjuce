#!/bin/bash
destdir="$1"
if [ -z "$destdir" ]; then
  destdir="`pwd`/build"
fi

set -e
dllroot=/usr/lib/gcc/i686-w64-mingw32/4.9-win32
cp -f "${dllroot}/libgcc_s_sjlj-1.dll" "${destdir}/"
cp -f "${dllroot}/libstdc++-6.dll" "${destdir}/"

exit 0
