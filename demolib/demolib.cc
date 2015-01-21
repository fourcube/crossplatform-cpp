#include "demolib.h"

void print() {
  #ifdef _WIN32
    printf("Hello World, Windows!");
  #elif defined __linux__
    printf("Hello World, Linux!");
  #elif defined TARGET_OS_MAC
    printf("Hello World, MacOS!");
  #else
  #error "unknown platform"
  #endif
}
