#crossplatform-cpp

## Build

### Win32 (VS 2013)

Inside the project directory:

```
> gyp build --depth 2 build.gyp
> cmd.exe "C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\devenv.com" "build.sln" /Build "Debug|Win32"

> Debug\crossplatform-demo.exe
Hello World, Windows!
```
