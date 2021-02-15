---
name: "ncbi-rmblastn"
layout: package
next_package: r-np
previous_package: powerapi
languages: ['cmake']
---
## 2.9.0
6 / 5772 files match

 - [c++/src/corelib/ncbifile.cpp](#c++srccorelibncbifilecpp)
 - [c++/src/corelib/ncbidll.cpp](#c++srccorelibncbidllcpp)
 - [c++/src/build-system/configure.ac](#c++srcbuild-systemconfigureac)
 - [c++/src/build-system/cmake/CMake.NCBIComponentsUNIX.cmake](#c++srcbuild-systemcmakecmakencbicomponentsunixcmake)
 - [c++/include/corelib/ncbidll.hpp](#c++includecorelibncbidllhpp)
 - [c++/scripts/common/check/valgrind.supp](#c++scriptscommoncheckvalgrindsupp)

### c++/src/corelib/ncbifile.cpp

```

{% raw %}
4723 |             void* handle = dlopen(kNcbiPanfsDLL, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### c++/src/corelib/ncbidll.cpp

```

{% raw %}
171 |     void* handle = dlopen(m_Name.c_str(), flags);
{% endraw %}

```
### c++/src/build-system/configure.ac

```

{% raw %}
1645 |       # Redundant for programs, but necessary for dlopen-able shared libs,
1724 |       # Redundant for programs, but necessary for dlopen-able shared libs,
4275 |      linux*:ICC   ) ac_cv_search_dlopen="-ldl" ;;
4276 |      solaris*:GCC ) ac_cv_search_dlopen="-ldl" ;;
4286 | NCBI_CHECK_LIBS(DL, dl, dlopen)
{% endraw %}

```
### c++/src/build-system/cmake/CMake.NCBIComponentsUNIX.cmake

```cmake

{% raw %}
27 | check_library_exists(dl dlopen "" HAVE_LIBDL)
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
766 |     libc/dlopen
773 |     libc/dlopen
779 |     libc/dlopen
786 |     libc/dlopen
792 |     libc/dlopen
798 |     libc/dlopen
804 |     libc/dlopen
811 |     libc/dlopen
{% endraw %}

```