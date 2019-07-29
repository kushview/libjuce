#include <juce/juce.h>
int main() {
    juce::String hello ("hello world");
    std::cout << hello.toStdString();
    return 0;
}
