## libJUCE

A standardized build/install [JUCE](http://www.juce.com). This is done by compiling upstream [JUCE](http://www.juce.com)
modules as shared libraries and installing them to the system using the
[Waf meta build system](https://waf.io)

_**Note:** This is NOT the [official JUCE codebase](https://github.com/WeAreROLI/JUCE.git). It is a Waf build
centered around upstream JUCE via a submodule._

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

The PREFIX envronment variable can be used to determine the install location

```
PREFIX=/opt/mydir bash tools/install.sh
```
