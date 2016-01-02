#!/bin/bash
set -ex
dllroot=/usr/lib/gcc/i686-w64-mingw32/4.9-win32
cp "${dllroot}/libgcc_s_sjlj-1.dll" build/
cp "${dllroot}/libstdc++-6.dll" build/
chmod +x build/*.dll
exit 0
