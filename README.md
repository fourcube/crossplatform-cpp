# crossplatform-cpp

## Build

Inside the project directory. The default build steps only build the main project.
"With tests" will include a binary which contains all tests as well as separate binaries
for each module.

### Win32 (VS 2013)

```

# Only include "crossplatform-demo" target and it's dependencies
$ gyp build.gyp --depth . -R crossplatform-demo
$ cmd.exe "C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.com" "build.sln" /Build "Debug|Win32"

$ Debug\crossplatform-demo.exe

Hello World, Windows!
```

#### With tests

```
$ gyp build --depth . build.gyp
$ cmd.exe "C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.com" "build.sln" /Build "Debug|Win32"

# For all tests
$ Debug\crossplatform-demo-test.exe

# Individual test
$ Debug\demolib_test_bin.exe

===============================================================================
All tests passed (3 assertions in 1 test case)

```

### Linux

```
$ gyp build --depth . build.gyp
$ make crossplatform-demo

$ ./out/Debug/crossplatform-demo

Hello World, Linux!
```

#### With tests

```
$ gyp build --depth . build.gyp
$ make all

# For all tests
$ ./out/Debug/crossplatform-demo-test

# Individual test
$ ./out/Debug/demolib_test_bin

===============================================================================
All tests passed (3 assertions in 1 test case)

```

### MacOS

```
$ gyp --depth . build.gyp
$ xcodebuild -project build.xcodeproj/ -target crossplatform-demo

$ ./build/Debug/crossplatform-demo

Hello World, MacOS!
```

#### With tests

```
$ xcodebuild -project build.xcodeproj/ -alltargets

# For all tests
$ ./build/Debug/crossplatform-demo-test

# Individual test
$ ./demolib/build/Debug/demolib_test_bin

===============================================================================
All tests passed (3 assertions in 1 test case)

```
