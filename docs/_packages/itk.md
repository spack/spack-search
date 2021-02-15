---
name: "itk"
layout: package
next_package: process-in-process
previous_package: libpmemobj-cpp
languages: ['cmake', 'cpp']
---
## 5.1.1
13 / 15831 files match

 - [Wrapping/Generators/Java/JavaBase/javaBase.i](#wrappinggeneratorsjavajavabasejavabasei)
 - [CMake/InsightValgrind-Ubuntu1804.supp](#cmakeinsightvalgrind-ubuntu1804supp)
 - [CMake/InsightValgrind-RHEL6.supp](#cmakeinsightvalgrind-rhel6supp)
 - [CMake/InsightValgrind-CentOS7.supp](#cmakeinsightvalgrind-centos7supp)
 - [CMake/InsightValgrind.supp](#cmakeinsightvalgrindsupp)
 - [Documentation/ReleaseNotes/2.8.md](#documentationreleasenotes28md)
 - [Documentation/ReleaseNotes/2.6.md](#documentationreleasenotes26md)
 - [Modules/ThirdParty/GoogleTest/src/itkgoogletest/googletest/cmake/libgtest.la.in](#modulesthirdpartygoogletestsrcitkgoogletestgoogletestcmakelibgtestlain)
 - [Modules/ThirdParty/HDF5/src/itkhdf5/config/cmake_ext_mod/ConfigureChecks.cmake](#modulesthirdpartyhdf5srcitkhdf5configcmake_ext_modconfigurecheckscmake)
 - [Modules/ThirdParty/HDF5/src/itkhdf5/src/H5PLpkg.h](#modulesthirdpartyhdf5srcitkhdf5srch5plpkgh)
 - [Modules/ThirdParty/KWSys/src/KWSys/DynamicLoader.cxx](#modulesthirdpartykwsyssrckwsysdynamicloadercxx)
 - [Modules/ThirdParty/KWSys/src/KWSys/DynamicLoader.hxx.in](#modulesthirdpartykwsyssrckwsysdynamicloaderhxxin)
 - [Modules/ThirdParty/KWSys/src/KWSys/testDynamicLoader.cxx](#modulesthirdpartykwsyssrckwsystestdynamicloadercxx)

### Wrapping/Generators/Java/JavaBase/javaBase.i

```

{% raw %}
31 |     dlopen(lib, RTLD_GLOBAL|RTLD_NOW);
{% endraw %}

```
### CMake/InsightValgrind-Ubuntu1804.supp

```

{% raw %}
4 |    dlopen
9 |    fun:dlopen@@GLIBC_2.?.?
{% endraw %}

```
### CMake/InsightValgrind-RHEL6.supp

```

{% raw %}
176 |    dlopen
180 |    fun:dlopen@@GLIBC_2.?.?
{% endraw %}

```
### CMake/InsightValgrind-CentOS7.supp

```

{% raw %}
4 |    dlopen
9 |    fun:dlopen@@GLIBC_2.?.?
{% endraw %}

```
### CMake/InsightValgrind.supp

```

{% raw %}
1014 |    dlopen leak1
1018 |    fun:dlopen*
1022 |    dlopen leak2
1026 |    fun:dlopen*
1029 |    dlopen leak3
1033 |    fun:dlopen
1353 |    fun:__libc_dlopen_mode
1462 |    fun:dlopen
1489 |    fun:dlopen
1516 |    fun:dlopen
1554 |    fun:dlopen
1622 |    fun:dlopen
{% endraw %}

```
### Documentation/ReleaseNotes/2.8.md

```

{% raw %}
3546 |         BUG: Trying to get testDynamicLoader to work on Solaris and SunOS, where current directory is not lookup when doing dlopen
3663 |         BUG: Trying to get testDynamicLoader to work on Solaris and SunOS, where current directory is not lookup when doing dlopen
{% endraw %}

```
### Documentation/ReleaseNotes/2.6.md

```

{% raw %}
2696 |         BUG: Trying to get testDynamicLoader to work on Solaris and SunOS, where current directory is not lookup when doing dlopen
2717 |         BUG: Trying to get testDynamicLoader to work on Solaris and SunOS, where current directory is not lookup when doing dlopen
{% endraw %}

```
### Modules/ThirdParty/GoogleTest/src/itkgoogletest/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### Modules/ThirdParty/HDF5/src/itkhdf5/config/cmake_ext_mod/ConfigureChecks.cmake

```cmake

{% raw %}
120 |   CHECK_LIBRARY_EXISTS_CONCAT ("dl" dlopen     ${HDF_PREFIX}_HAVE_LIBDL)
{% endraw %}

```
### Modules/ThirdParty/HDF5/src/itkhdf5/src/H5PLpkg.h

```cpp

{% raw %}
96 | #   define H5PL_OPEN_DLIB(S) dlopen(S, RTLD_LAZY)
105 | #   define H5PL_CLR_ERROR HERROR(H5E_PLUGIN, H5E_CANTGET, "can't dlopen:%s", dlerror())
{% endraw %}

```
### Modules/ThirdParty/KWSys/src/KWSys/DynamicLoader.cxx

```

{% raw %}
27 | //   later) which use dlopen
452 | // later) which use dlopen
462 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### Modules/ThirdParty/KWSys/src/KWSys/DynamicLoader.hxx.in

```

{% raw %}
32 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### Modules/ThirdParty/KWSys/src/KWSys/testDynamicLoader.cxx

```

{% raw %}
96 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
106 |   // This one is actually fun to test, since dlopen is by default
108 |   res += TestDynamicLoader("foobar.lib", "dlopen", 0, 1, 0);
109 |   res += TestDynamicLoader("libdl.so", "dlopen", 1, 1, 1);
{% endraw %}

```