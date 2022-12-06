# Problem with cross building package with tools

## Profiles

default:
```conf
[settings]
os=Linux
os_build=Linux
arch=x86_64
arch_build=x86_64
compiler=gcc
compiler.version=11
compiler.libcxx=libstdc++11
compiler.cppstd=20
build_type=Release
[options]
[build_requires]
[env]
CONAN_CMAKE_GENERATOR=Ninja
[conf]
tools.system.package_manager:mode=install
tools.system.package_manager:sudo=True
tools.system.package_manager:tool=apt-get
```

android:
```conf
[settings]
os=Android
os.api_level=29
arch=armv8
compiler=clang
compiler.version=14
compiler.libcxx=c++_shared
compiler.cppstd=20
build_type=Release
[options]
[build_requires]
*: android-ndk/r25, cmake/3.24.1, ninja/1.10.1
[env]
CONAN_CMAKE_GENERATOR=Ninja
```


## Build logs
<details>
<summary>Logs from successful build without cross building</summary>

```
[I] ⋊> ~/C/t/conan_tool_cross_build on main ◦ conan create . @some/test -pr:h default -pr:b default --build missing                                                                                   
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'url'. It is recommended to add it as attribute
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'license'. It is recommended to add it as attribute
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'description'. It is recommended to add it as attribute
Exporting package recipe
example/1.0.0@some/test exports_sources: Copied 3 '.txt' files: CMakeLists.txt, CMakeLists.txt, CMakeLists.txt
example/1.0.0@some/test exports_sources: Copied 2 '.cpp' files: example-lib.cpp, example-generator.cpp
example/1.0.0@some/test exports_sources: Copied 1 '.hpp' file: example-lib.hpp
example/1.0.0@some/test exports_sources: Copied 1 '.cmake' file: ExampleGeneratorToolTarget.cmake
example/1.0.0@some/test: A new conanfile.py version was exported
example/1.0.0@some/test: Folder: /home/xandox/.conan/data/example/1.0.0/some/test/export
example/1.0.0@some/test: Using the exported files summary hash as the recipe revision: 31996aa025b3f8089d88673e4e5ecbff 
example/1.0.0@some/test: Exported revision: 31996aa025b3f8089d88673e4e5ecbff
Configuration (profile_host):
[settings]
arch=x86_64
arch_build=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=11
os=Linux
os_build=Linux
[options]
[build_requires]
[env]
CONAN_CMAKE_GENERATOR=Ninja
[conf]
tools.system.package_manager:mode=install
tools.system.package_manager:sudo=True
tools.system.package_manager:tool=apt-get

Configuration (profile_build):
[settings]
arch=x86_64
arch_build=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=11
os=Linux
os_build=Linux
[options]
[build_requires]
[env]
CONAN_CMAKE_GENERATOR=Ninja
[conf]
tools.system.package_manager:mode=install
tools.system.package_manager:sudo=True
tools.system.package_manager:tool=apt-get

example/1.0.0@some/test (test package): Installing package
Requirements
    example/1.0.0@some/test from local cache - Cache
    zlib/1.2.13 from 'conan' - Cache
Packages
    example/1.0.0@some/test:ff2e458a6cce6dd891cd1be6801c354c450cd846 - Build
    zlib/1.2.13:dfbe50feef7f3c6223a476cd5aeadb687084a646 - Cache
Build requirements
    example/1.0.0@some/test from local cache - Cache
    zlib/1.2.13 from 'conan' - Cache
Build requirements packages
    example/1.0.0@some/test:ff2e458a6cce6dd891cd1be6801c354c450cd846 - Build
    zlib/1.2.13:dfbe50feef7f3c6223a476cd5aeadb687084a646 - Cache

Installing (downloading, building) binaries...
zlib/1.2.13: Already installed!
example/1.0.0@some/test: Configuring sources in /home/xandox/.conan/data/example/1.0.0/some/test/source/.
example/1.0.0@some/test: Copying sources to build folder
example/1.0.0@some/test: Building your package in /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846
example/1.0.0@some/test: Generator 'CMakeToolchain' calling 'generate()'
example/1.0.0@some/test: Preset 'release' added to CMakePresets.json. Invoke it manually using 'cmake --preset release'
example/1.0.0@some/test: If your CMake version is not compatible with CMakePresets (<3.19) call cmake like: 'cmake <path> -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release'
example/1.0.0@some/test: Generator 'CMakeDeps' calling 'generate()'
example/1.0.0@some/test: Calling generate()
example/1.0.0@some/test: Preset 'release' added to CMakePresets.json. Invoke it manually using 'cmake --preset release'
example/1.0.0@some/test: If your CMake version is not compatible with CMakePresets (<3.19) call cmake like: 'cmake <path> -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release'
example/1.0.0@some/test: Aggregating env generators
example/1.0.0@some/test: Calling build()
example/1.0.0@some/test: CMake command: cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake" -DCMAKE_INSTALL_PREFIX="/home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846" -DCMAKE_POLICY_DEFAULT_CMP0091="NEW" -DCMAKE_BUILD_TYPE="Release" "/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/."
-- Using Conan toolchain: /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake
-- Conan toolchain: C++ Standard 20 with extensions OFF
-- The C compiler identification is GNU 11.3.0
-- The CXX compiler identification is GNU 11.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Conan: Target declared 'ZLIB::ZLIB'
-- Configuring done
-- Generating done
CMake Warning:
Manually-specified variables were not used by the project:

    CMAKE_POLICY_DEFAULT_CMP0091


-- Build files have been written to: /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/Release
example/1.0.0@some/test: CMake command: cmake --build "/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/Release" '--' '-j16'
[ 25%] Building CXX object lib/CMakeFiles/example-lib.dir/example-lib.cpp.o
[ 50%] Building CXX object tool/CMakeFiles/example-generator.dir/example-generator.cpp.o
[ 75%] Linking CXX static library libexample-lib.a
[ 75%] Built target example-lib
[100%] Linking CXX executable example-generator
[100%] Built target example-generator
example/1.0.0@some/test: Package 'ff2e458a6cce6dd891cd1be6801c354c450cd846' built
example/1.0.0@some/test: Build folder /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/Release
example/1.0.0@some/test: Generated conaninfo.txt
example/1.0.0@some/test: Generated conanbuildinfo.txt
example/1.0.0@some/test: Generating the package
example/1.0.0@some/test: Package folder /home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846
example/1.0.0@some/test: Calling package()
example/1.0.0@some/test: CMake command: cmake --install "/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/Release" --prefix "/home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846"
-- Install configuration: "Release"
-- Installing: /home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846/include/example-lib.hpp
-- Installing: /home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846/lib/libexample-lib.a
-- Installing: /home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846/bin/example-generator
example/1.0.0@some/test: Copied 1 '.cmake' file: ExampleGeneratorToolTarget.cmake
example/1.0.0@some/test package(): Packaged 1 '.a' file: libexample-lib.a
example/1.0.0@some/test package(): Packaged 1 '.cmake' file: ExampleGeneratorToolTarget.cmake
example/1.0.0@some/test package(): Packaged 1 file: example-generator
example/1.0.0@some/test package(): Packaged 1 '.hpp' file: example-lib.hpp
example/1.0.0@some/test: Package 'ff2e458a6cce6dd891cd1be6801c354c450cd846' created
example/1.0.0@some/test: Created package revision d1326e959254ee7b1df13d1edc88dc71
example/1.0.0@some/test: Appending PATH environment variable: /home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846/bin
example/1.0.0@some/test: Appending PATH environment variable: /home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846/bin
example/1.0.0@some/test (test package): Applying build-requirement: example/1.0.0@some/test
example/1.0.0@some/test (test package): Applying build-requirement: zlib/1.2.13
example/1.0.0@some/test (test package): Generator 'CMakeToolchain' calling 'generate()'
example/1.0.0@some/test (test package): Preset 'release' added to CMakePresets.json. Invoke it manually using 'cmake --preset release'
example/1.0.0@some/test (test package): If your CMake version is not compatible with CMakePresets (<3.19) call cmake like: 'cmake <path> -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=/home/xandox/Code/temp/conan_tool_cross_build/test_package/build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release'
example/1.0.0@some/test (test package): Generator txt created conanbuildinfo.txt
example/1.0.0@some/test (test package): Generator 'CMakeDeps' calling 'generate()'
example/1.0.0@some/test (test package): Calling generate()
example/1.0.0@some/test (test package): Preset 'release' added to CMakePresets.json. Invoke it manually using 'cmake --preset release'
example/1.0.0@some/test (test package): If your CMake version is not compatible with CMakePresets (<3.19) call cmake like: 'cmake <path> -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=/home/xandox/Code/temp/conan_tool_cross_build/test_package/build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release'
example/1.0.0@some/test (test package): Aggregating env generators
example/1.0.0@some/test (test package): Generated conaninfo.txt
example/1.0.0@some/test (test package): Generated graphinfo
Using lockfile: '/home/xandox/Code/temp/conan_tool_cross_build/test_package/build/generators/conan.lock'
Using cached profile from lockfile
example/1.0.0@some/test (test package): Calling build()
example/1.0.0@some/test (test package): CMake command: cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="/home/xandox/Code/temp/conan_tool_cross_build/test_package/build/generators/conan_toolchain.cmake" -DCMAKE_POLICY_DEFAULT_CMP0091="NEW" -DCMAKE_BUILD_TYPE="Release" "/home/xandox/Code/temp/conan_tool_cross_build/test_package/."
-- Using Conan toolchain: /home/xandox/Code/temp/conan_tool_cross_build/test_package/build/generators/conan_toolchain.cmake
-- Conan toolchain: C++ Standard 20 with extensions OFF
-- The C compiler identification is GNU 11.3.0
-- The CXX compiler identification is GNU 11.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Conan: Target declared 'example::example'
-- Conan: Target declared 'ZLIB::ZLIB'
-- Conan: Including build module from '/home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846/lib/cmake/ExampleGeneratorToolTarget.cmake'
-- Configuring done
-- Generating done
CMake Warning:
Manually-specified variables were not used by the project:

    CMAKE_POLICY_DEFAULT_CMP0091


-- Build files have been written to: /home/xandox/Code/temp/conan_tool_cross_build/test_package/build/Release
example/1.0.0@some/test (test package): CMake command: cmake --build "/home/xandox/Code/temp/conan_tool_cross_build/test_package/build/Release" '--' '-j16'
[ 25%] Generating generated.cpp, generated.h
[ 50%] Building CXX object CMakeFiles/test_package.dir/test_package.cpp.o
[ 50%] Generating generated.cpp, generated.h
[ 75%] Building CXX object CMakeFiles/test_package.dir/generated.cpp.o
[100%] Linking CXX executable test_package
[100%] Built target test_package
example/1.0.0@some/test (test package): Running test()
Hello, world!
Hello from generated!
```
</details>


<details>
<summary>Logs from unsuccessful build with cross building</summary>

```
[I] ⋊> ~/C/t/conan_tool_cross_build on main ◦ rm -rf ~/.conan/data/example/
[I] ⋊> ~/C/t/conan_tool_cross_build on main ◦ conan create . @some/test -pr:h android -pr:b default --build missing                                                                                   
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'url'. It is recommended to add it as attribute
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'license'. It is recommended to add it as attribute
[HOOK - attribute_checker.py] pre_export(): WARN: Conanfile doesn't have 'description'. It is recommended to add it as attribute
Exporting package recipe
example/1.0.0@some/test exports_sources: Copied 3 '.txt' files: CMakeLists.txt, CMakeLists.txt, CMakeLists.txt
example/1.0.0@some/test exports_sources: Copied 2 '.cpp' files: example-lib.cpp, example-generator.cpp
example/1.0.0@some/test exports_sources: Copied 1 '.hpp' file: example-lib.hpp
example/1.0.0@some/test exports_sources: Copied 1 '.cmake' file: ExampleGeneratorToolTarget.cmake
example/1.0.0@some/test: A new conanfile.py version was exported
example/1.0.0@some/test: Folder: /home/xandox/.conan/data/example/1.0.0/some/test/export
example/1.0.0@some/test: Using the exported files summary hash as the recipe revision: 31996aa025b3f8089d88673e4e5ecbff 
example/1.0.0@some/test: Exported revision: 31996aa025b3f8089d88673e4e5ecbff
Configuration (profile_host):
[settings]
arch=armv8
build_type=Release
compiler=clang
compiler.cppstd=20
compiler.libcxx=c++_shared
compiler.version=14
os=Android
os.api_level=29
[options]
[build_requires]
*: android-ndk/r25, cmake/3.24.1, ninja/1.10.1
[env]
CONAN_CMAKE_GENERATOR=Ninja
Configuration (profile_build):
[settings]
arch=x86_64
arch_build=x86_64
build_type=Release
compiler=gcc
compiler.cppstd=20
compiler.libcxx=libstdc++11
compiler.version=11
os=Linux
os_build=Linux
[options]
[build_requires]
[env]
CONAN_CMAKE_GENERATOR=Ninja
[conf]
tools.system.package_manager:mode=install
tools.system.package_manager:sudo=True
tools.system.package_manager:tool=apt-get

example/1.0.0@some/test (test package): Installing package
Requirements
    example/1.0.0@some/test from local cache - Cache
    zlib/1.2.13 from 'conan' - Cache
Packages
    example/1.0.0@some/test:4eefe19e0c78eaba4d7e6dca79fde88bbb9f58f9 - Build
    zlib/1.2.13:39f1a94c0802f35481ae4244b07fb2551f3be9ab - Cache
Build requirements
    android-ndk/r25 from 'conan' - Cache
    cmake/3.24.1 from 'conan' - Cache
    example/1.0.0@some/test from local cache - Cache
    ninja/1.10.1 from 'conan' - Cache
    openssl/1.1.1s from 'conan' - Cache
    zlib/1.2.13 from 'conan' - Cache
Build requirements packages
    android-ndk/r25:4db1be536558d833e52e862fd84d64d75c2b3656 - Cache
    cmake/3.24.1:5c09c752508b674ca5cb1f2d327b5a2d582866c8 - Cache
    example/1.0.0@some/test:ff2e458a6cce6dd891cd1be6801c354c450cd846 - Build
    ninja/1.10.1:24647d9fe8ec489125dfbae4b3ebefaf7581674c - Cache
    openssl/1.1.1s:dfbe50feef7f3c6223a476cd5aeadb687084a646 - Cache
    zlib/1.2.13:dfbe50feef7f3c6223a476cd5aeadb687084a646 - Cache

Cross-build from 'Linux:x86_64' to 'Android:armv8'
Installing (downloading, building) binaries...
android-ndk/r25: Already installed!
ninja/1.10.1: Already installed!
openssl/1.1.1s: Already installed!
zlib/1.2.13: Already installed!
zlib/1.2.13: Already installed!
cmake/3.24.1: Already installed!
cmake/3.24.1: Appending PATH environment variable: /home/xandox/.conan/data/cmake/3.24.1/_/_/package/5c09c752508b674ca5cb1f2d327b5a2d582866c8/bin
cmake/3.24.1: Appending PATH environment variable: /home/xandox/.conan/data/cmake/3.24.1/_/_/package/5c09c752508b674ca5cb1f2d327b5a2d582866c8/bin
example/1.0.0@some/test: Configuring sources in /home/xandox/.conan/data/example/1.0.0/some/test/source/.
example/1.0.0@some/test: Copying sources to build folder
example/1.0.0@some/test: Building your package in /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846
example/1.0.0@some/test: Generator 'CMakeDeps' calling 'generate()'
example/1.0.0@some/test: Generator 'CMakeToolchain' calling 'generate()'
example/1.0.0@some/test: Preset 'release' added to CMakePresets.json. Invoke it manually using 'cmake --preset release'
example/1.0.0@some/test: If your CMake version is not compatible with CMakePresets (<3.19) call cmake like: 'cmake <path> -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release'
example/1.0.0@some/test: Calling generate()
example/1.0.0@some/test: Preset 'release' added to CMakePresets.json. Invoke it manually using 'cmake --preset release'
example/1.0.0@some/test: If your CMake version is not compatible with CMakePresets (<3.19) call cmake like: 'cmake <path> -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release'
example/1.0.0@some/test: Aggregating env generators
example/1.0.0@some/test: Calling build()
example/1.0.0@some/test: CMake command: cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake" -DCMAKE_INSTALL_PREFIX="/home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846" -DCMAKE_POLICY_DEFAULT_CMP0091="NEW" -DCMAKE_BUILD_TYPE="Release" "/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/."
-- Using Conan toolchain: /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake
-- Conan toolchain: C++ Standard 20 with extensions OFF
-- The C compiler identification is GNU 11.3.0
-- The CXX compiler identification is GNU 11.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at tool/CMakeLists.txt:4 (find_package):
Could not find a package configuration file provided by "ZLIB" with any of
the following names:

    ZLIBConfig.cmake
    zlib-config.cmake

Add the installation prefix of "ZLIB" to CMAKE_PREFIX_PATH or set
"ZLIB_DIR" to a directory containing one of the above files.  If "ZLIB"
provides a separate development package or SDK, be sure it has been
installed.


-- Configuring incomplete, errors occurred!
See also "/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/Release/CMakeFiles/CMakeOutput.log".
example/1.0.0@some/test: 
example/1.0.0@some/test: ERROR: Package 'ff2e458a6cce6dd891cd1be6801c354c450cd846' build failed
example/1.0.0@some/test: WARN: Build folder /home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/Release
ERROR: example/1.0.0@some/test: Error in build() method, line 25
    cmake.configure()
    ConanException: Error 1 while executing cmake -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/build/generators/conan_toolchain.cmake" -DCMAKE_INSTALL_PREFIX="/home/xandox/.conan/data/example/1.0.0/some/test/package/ff2e458a6cce6dd891cd1be6801c354c450cd846" -DCMAKE_POLICY_DEFAULT_CMP0091="NEW" -DCMAKE_BUILD_TYPE="Release" "/home/xandox/.conan/data/example/1.0.0/some/test/build/ff2e458a6cce6dd891cd1be6801c354c450cd846/."
```

</details>
