---
name: "ncbi-magicblast"
layout: package
next_package: dealii
previous_package: breseq
languages: ['cmake']
---
## 1.5.0
6 / 5879 files match

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
1647 |       # Redundant for programs, but necessary for dlopen-able shared libs,
1726 |       # Redundant for programs, but necessary for dlopen-able shared libs,
4277 |      linux*:ICC   ) ac_cv_search_dlopen="-ldl" ;;
4278 |      solaris*:GCC ) ac_cv_search_dlopen="-ldl" ;;
4288 | NCBI_CHECK_LIBS(DL, dl, dlopen)
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