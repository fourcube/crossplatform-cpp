# crossplatform-cpp

## Build

Inside the project directory:

### Win32 (VS 2013)

```
> gyp build --depth . build.gyp
> cmd.exe "C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.com" "build.sln" /Build "Debug|Win32"

> Debug\crossplatform-demo.exe

Hello World, Windows!
```

### Linux

```
> gyp build --depth . build.gyp
> make

> ./out/Debug/crossplatform-demo

Hello World, Linux!
```

### MacOS

```
> gyp --depth . build.gyp
> xcodebuild -project build.xcodeproj/ -target crossplatform-demo

> ./build/Debug/crossplatform-demo

Hello World, MacOS!
```

#### With tests

```
> xcodebuild -project build.xcodeproj/ -alltargets

# For all tests
> ./build/Debug/crossplatform-demo-test

# Individual test
> ./demolib/build/Debug/demolib_test_bin

===============================================================================
All tests passed (3 assertions in 1 test case)

```
