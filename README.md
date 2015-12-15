## libJUCE

A standardized build/install [JUCE](http://www.juce.com). This is done by compiling upstream [JUCE](http://www.juce.com)
modules as shared libraries and installing them to the system using the
[Waf meta build system](https://waf.io)

_**Note:** This is NOT the [official JUCE codebase](https://github.com/julianstorer/JUCE.git). This is just a waf build
centered around upstream JUCE via a submodule._

### Building/Installing libJUCE
Since this uses waf, installation is easy. From the command line:

__Installing JUCE modules__
```
cd path/to/libjuce
./waf configure build
./waf install # may require sudo
```

__Installing Introjucer and the JUCE demo__
```
cd path/to/libjuce
./waf configure --introjucer --juce-demo build
./waf install
```

__Installing debuggable modules__
```
./waf configure --debug build
./waf install --no-headers
```
