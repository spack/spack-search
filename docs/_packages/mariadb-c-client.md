---
name: "mariadb-c-client"
layout: package
next_package: fish
previous_package: spades
languages: ['cmake', 'cpp']
---
## 2.3.1
4 / 200 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [include/my_global.h](#includemy_globalh)
 - [libmariadb/client_plugin.c](#libmariadbclient_pluginc)
 - [cmake/CheckFunctions.cmake](#cmakecheckfunctionscmake)

### CMakeLists.txt

```

{% raw %}
130 |   SEARCH_LIBRARY(LIBDL dlopen "dl")
150 |   ADD_DEFINITIONS(-DHAVE_DLOPEN)
{% endraw %}

```
### include/my_global.h

```cpp

{% raw %}
1080 | #ifdef HAVE_DLOPEN
1083 | #define dlopen(libname, unused) LoadLibraryEx(libname, NULL, 0)
{% endraw %}

```
### libmariadb/client_plugin.c

```cpp

{% raw %}
130 |   @param dlhandle       a handle to the shared object (returned by dlopen)
374 |   if (!(dlhandle= dlopen((const char *)dlpath, RTLD_NOW)))
{% endraw %}

```
### cmake/CheckFunctions.cmake

```cmake

{% raw %}
27 | CHECK_FUNCTION_EXISTS (dlopen HAVE_DLOPEN)
{% endraw %}

```