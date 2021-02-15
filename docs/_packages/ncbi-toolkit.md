---
name: "ncbi-toolkit"
layout: package
next_package: r-httpuv
previous_package: kitty
languages: ['cmake']
---
## 22_0_0
6 / 15650 files match

 - [src/corelib/ncbifile.cpp](#srccorelibncbifilecpp)
 - [src/corelib/ncbidll.cpp](#srccorelibncbidllcpp)
 - [src/build-system/configure.ac](#srcbuild-systemconfigureac)
 - [src/build-system/cmake/CMake.NCBIComponentsUNIX.cmake](#srcbuild-systemcmakecmakencbicomponentsunixcmake)
 - [include/corelib/ncbidll.hpp](#includecorelibncbidllhpp)
 - [scripts/common/check/valgrind.supp](#scriptscommoncheckvalgrindsupp)

### src/corelib/ncbifile.cpp

```

{% raw %}
4723 |             void* handle = dlopen(kNcbiPanfsDLL, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/corelib/ncbidll.cpp

```

{% raw %}
171 |     void* handle = dlopen(m_Name.c_str(), flags);
{% endraw %}

```
### src/build-system/configure.ac

```

{% raw %}
1645 |       # Redundant for programs, but necessary for dlopen-able shared libs,
1724 |       # Redundant for programs, but necessary for dlopen-able shared libs,
4275 |      linux*:ICC   ) ac_cv_search_dlopen="-ldl" ;;
4276 |      solaris*:GCC ) ac_cv_search_dlopen="-ldl" ;;
4286 | NCBI_CHECK_LIBS(DL, dl, dlopen)
{% endraw %}

```
### src/build-system/cmake/CMake.NCBIComponentsUNIX.cmake

```cmake

{% raw %}
27 | check_library_exists(dl dlopen "" HAVE_LIBDL)
{% endraw %}

```
### include/corelib/ncbidll.hpp

```

{% raw %}
123 |         /// UNIX specific (see 'man dlopen'), ignored on all other platforms.
{% endraw %}

```
### scripts/common/check/valgrind.supp

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