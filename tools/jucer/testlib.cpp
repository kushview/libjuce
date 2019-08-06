#include <juce/juce.h>

int main()
{
    juce::String hello ("hello world");
    juce::Logger::writeToLog (hello);
    return 0;
}
