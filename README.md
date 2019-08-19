## libJUCE

[![Build Status](https://travis-ci.org/kushview/libjuce.svg?branch=master)](https://travis-ci.org/kushview/libjuce)

A standardized build of [JUCE](http://www.juce.com). This is done by compiling upstream [JUCE](http://www.juce.com) modules as shared libraries and installing them to the system using the [Waf meta build system](https://waf.io)

_**Note:** This is NOT the [official JUCE codebase](https://github.com/WeAreROLI/JUCE.git). This project includes the official source as a submodule_ 

### Building/Installing libJUCE
Since this uses waf, installation is easy. From the command line:

__Installing JUCE modules__
```
cd path/to/libjuce
./waf configure build
./waf install # may require sudo
```

__Installing Debuggable Libraries__
```
./waf configure --debug build
./waf install --no-headers
```

__Complete Installation__

_See:_ [tools/install.sh](tools/install.sh)

Any options added after the script will be appended to `./waf configure`. For example...

```
tools/install.sh --prefix=/opt/sdk
```
