---
name: "gromacs"
layout: package
next_package: None
previous_package: tar
languages: ['cmake', 'cpp']
---
## 5.1.2
9 / 4523 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [src/external/vmd_molfile/vmddlopen.c](#srcexternalvmd_molfilevmddlopenc)
 - [src/external/vmd_molfile/vmdplugin.h](#srcexternalvmd_molfilevmdpluginh)
 - [src/external/vmd_molfile/vmddlopen.h](#srcexternalvmd_molfilevmddlopenh)
 - [src/gromacs/fileio/vmdio.c](#srcgromacsfileiovmdioc)
 - [src/gromacs/fileio/CMakeLists.txt](#srcgromacsfileiocmakeliststxt)
 - [cmake/TestVMD.c](#cmaketestvmdc)
 - [cmake/gmxTestdlopen.cmake](#cmakegmxtestdlopencmake)
 - [docs/manual/special.tex](#docsmanualspecialtex)

### CMakeLists.txt

```

{% raw %}
675 |     # Native Windows does not have, nor need dlopen
676 |     include(gmxTestdlopen)
677 |     gmx_test_dlopen(HAVE_DLOPEN)
681 |   if(WIN32 OR (HAVE_DLOPEN AND BUILD_SHARED_LIBS))
689 |     list(APPEND GMX_EXTRA_LIBRARIES ${CMAKE_DL_LIBS}) # magic cross-platform pre-set variable for dlopen library
{% endraw %}

```
### src/external/vmd_molfile/vmddlopen.c

```cpp

{% raw %}
59 |  *      $RCSfile: vmddlopen.c,v $
73 | #include "vmddlopen.h"
81 | void *vmddlopen( const char *path) {
109 | void *vmddlopen( const char *path) {
159 | void *vmddlopen(const char *fname) {
167 |   sprintf(szBuf, "vmddlopen failed: GetLastError returned %lu\n", dw);
185 | void *vmddlopen(const char *fname) {
186 |   return dlopen(fname, RTLD_NOW);
{% endraw %}

```
### src/external/vmd_molfile/vmdplugin.h

```cpp

{% raw %}
97 |  *  and fini routines via dlopen() or similar operating system interfaces.
226 |  * This API is optional; if found by dlopen, it will be called after first
{% endraw %}

```
### src/external/vmd_molfile/vmddlopen.h

```cpp

{% raw %}
59 |  *      $RCSfile: vmddlopen.h,v $
75 |  * vmddlopen: thin multi-platform wrapper around dlopen/LoadLibrary
78 | #ifndef VMD_DLOPEN__
87 | void *vmddlopen(const char *fname);
{% endraw %}

```
### src/gromacs/fileio/vmdio.c

```cpp

{% raw %}
97 | #include "external/vmd_molfile/vmddlopen.h"
138 |     handle = vmddlopen(fullpath);
363 |             printf("Compiled with dlopen?\n");
{% endraw %}

```
### src/gromacs/fileio/CMakeLists.txt

```

{% raw %}
37 |   set(FILEIO_SOURCES ${FILEIO_SOURCES} ${CMAKE_SOURCE_DIR}/src/external/vmd_molfile/vmddlopen.c)
{% endraw %}

```
### cmake/TestVMD.c

```cpp

{% raw %}
1 | #include "vmddlopen.c"
12 | /*run: gcc TestVMD.c -DGMX_USE_PLUGINS -Wall -ldl src/gmxlib/vmddlopen.c -I src/gmxlib && ./a.out .../xyzplugin.so ; echo $?*/
18 |     handle = vmddlopen(argv[1]);
{% endraw %}

```
### cmake/gmxTestdlopen.cmake

```cmake

{% raw %}
34 | # - Define macro to check if DLOPEN is defined
36 | #  GMX_TEST_DLOPEN(VARIABLE)
38 | #  VARIABLE will be set if dlopen is present in dlfcn.h
41 | MACRO(GMX_TEST_DLOPEN VARIABLE)
43 |     MESSAGE(STATUS "Checking for dlopen")
50 |   dlopen(0,0);
55 |       MESSAGE(STATUS "Checking for dlopen - found")
56 |       set(${VARIABLE} 1 CACHE INTERNAL "Result of test for dlopen" FORCE)
58 |       MESSAGE(STATUS "Checking for dlopen - not found")
59 |       set(${VARIABLE} 0 CACHE INTERNAL "Result of test for dlopen" FORCE)
{% endraw %}

```
### docs/manual/special.tex

```

{% raw %}
2086 | system provides the dlopen function so that programs can determine at
2181 | % LocalWords:  CMake homepage DEV overclocking GT dlopen vmd VMDDIR
{% endraw %}

```