#include "demolib.h"

void print() {
  #ifdef _WIN32
    puts("Hello World, Windows!");
  #elif defined __linux__
    puts("Hello World, Linux!");
  #elif defined TARGET_OS_MAC
    puts("Hello World, MacOS!");
  #else
  #error "unknown platform"
  #endif
}
