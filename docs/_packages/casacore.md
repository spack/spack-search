---
name: "casacore"
layout: package
next_package: audacity
previous_package: libfontenc
languages: ['cmake', 'cpp']
---
## 3.3.0
3 / 3213 files match

 - [casa/OS/DynLib.cc](#casaosdynlibcc)
 - [casa/OS/DynLib.h](#casaosdynlibh)
 - [cmake/FindDL.cmake](#cmakefinddlcmake)

### casa/OS/DynLib.cc

```cpp

{% raw %}
27 | //# For the time being assume that all systems have dlopen.
28 | #ifndef HAVE_DLOPEN
29 | # define HAVE_DLOPEN
40 | #ifdef HAVE_DLOPEN
94 | #ifdef HAVE_DLOPEN
108 | #ifdef HAVE_DLOPEN
109 |     itsHandle = dlopen (name.c_str(), RTLD_NOW | RTLD_GLOBAL);
119 | #ifdef HAVE_DLOPEN
{% endraw %}

```
### casa/OS/DynLib.h

```cpp

{% raw %}
45 |   //    <li> Basic knowledge of the dlopen function family
64 |   // It is a wrapper around functions dlopen, dlsym, and dlclose.
65 |   // If dlopen and so are not supported on a platform, the class acts as if
80 |   // dlopen is a standard UNIX system call, but some operating systems
{% endraw %}

```
### cmake/FindDL.cmake

```cmake

{% raw %}
0 | # - find where dlopen and friends are located.
3 | # DL_LIBRARIES - libraries needed to use dlopen
12 |   check_function_exists(dlopen DL_FOUND)
13 |   # If dlopen can be found without linking in dl then dlopen is part
{% endraw %}

```