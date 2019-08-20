#!/bin/bash

compiler="$1"
destdir="$2"

if [ -z "$compiler" ]; then
  echo "Didn't specify a compiler"
  exit 1
fi

if [ -z "$destdir" ]; then
  destdir="`pwd`/build/lib"
fi

set -ex
mkdir -p "${destdir}"
cp -f "`${compiler} -print-file-name=libgcc_s_sjlj-1.dll`" "${destdir}/"
cp -f "`${compiler} -print-file-name=libstdc++-6.dll`" "${destdir}/"

exit 0
