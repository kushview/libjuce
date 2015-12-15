## libJUCE

A standardized build/install of the official JUCE. This is done by compiling
upstream juce modules as shared libraries and installing them to the system
using the [Waf meta build system](https://waf.io)

### Building/Installing JUCE
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
