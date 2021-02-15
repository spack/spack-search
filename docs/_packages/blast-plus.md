---
name: "blast-plus"
layout: package
next_package: e2fsprogs
previous_package: libvorbis
languages: ['cmake']
---
## 2.2.30
5 / 4581 files match

 - [c++/src/corelib/ncbidll.cpp](#c++srccorelibncbidllcpp)
 - [c++/src/build-system/configure.ac](#c++srcbuild-systemconfigureac)
 - [c++/src/build-system/cmake/CMakeChecks.cmake](#c++srcbuild-systemcmakecmakecheckscmake)
 - [c++/include/corelib/ncbidll.hpp](#c++includecorelibncbidllhpp)
 - [c++/scripts/common/check/valgrind.supp](#c++scriptscommoncheckvalgrindsupp)

### c++/src/corelib/ncbidll.cpp

```

{% raw %}
173 |     void* handle = dlopen(m_Name.c_str(), flags);
{% endraw %}

```
### c++/src/build-system/configure.ac

```

{% raw %}
1404 |       # Redundant for programs, but necessary for dlopen-able shared libs,
1483 |       # Redundant for programs, but necessary for dlopen-able shared libs,
3863 |      solaris*:GCC ) ac_cv_search_dlopen="-ldl" ;;
3866 | NCBI_CHECK_LIBS(DL, dl, dlopen)
{% endraw %}

```
### c++/src/build-system/cmake/CMakeChecks.cmake

```cmake

{% raw %}
104 | check_library_exists(dl dlopen "" HAVE_LIBDL)
{% endraw %}

```
### c++/include/corelib/ncbidll.hpp

```

{% raw %}
123 |         /// UNIX specific (see 'man dlopen'), ignored on all other platforms.
{% endraw %}

```
### c++/scripts/common/check/valgrind.supp

```

{% raw %}
460 |     libc/dlopen
467 |     libc/dlopen
473 |     libc/dlopen
480 |     libc/dlopen
486 |     libc/dlopen
492 |     libc/dlopen
498 |     libc/dlopen
505 |     libc/dlopen
{% endraw %}

```