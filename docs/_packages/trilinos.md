---
name: "trilinos"
layout: package
next_package: libsodium
previous_package: optipng
languages: ['cpp']
---
## xsdk-0.2.0
8 / 46265 files match

 - [packages/kokkos/core/src/impl/Kokkos_Profiling_Interface.cpp](#packageskokkoscoresrcimplkokkos_profiling_interfacecpp)
 - [packages/PyTrilinos/ReleaseNotes.txt](#packagespytrilinosreleasenotestxt)
 - [packages/PyTrilinos/src/PyTrilinos/__init__.py.in](#packagespytrilinossrcpytrilinos__init__pyin)
 - [packages/stk/stk_util/stk_util/diag/UserPlugin.cpp](#packagesstkstk_utilstk_utildiaguserplugincpp)
 - [packages/stk/stk_util/stk_util/util/FeatureTest.hpp](#packagesstkstk_utilstk_utilutilfeaturetesthpp)
 - [packages/stk/stk_classic/stk_util/stk_util/diag/UserPlugin.cpp](#packagesstkstk_classicstk_utilstk_utildiaguserplugincpp)
 - [packages/stk/stk_classic/stk_util/stk_util/util/FeatureTest.hpp](#packagesstkstk_classicstk_utilstk_utilutilfeaturetesthpp)
 - [packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C](#packagesseacaslibrariesiosssrcvisualizationiovs_databaseioc)

### packages/kokkos/core/src/impl/Kokkos_Profiling_Interface.cpp

```

{% raw %}
151 |             firstProfileLibrary = dlopen(profileLibraryName, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### packages/PyTrilinos/ReleaseNotes.txt

```

{% raw %}
327 |   * Changed PyTrilinos/__init__.py to alter the python dlopen flags so
{% endraw %}

```
### packages/PyTrilinos/src/PyTrilinos/__init__.py.in

```

{% raw %}
61 | # the flags values are.  After all this, the sys module setdlopenflags()
72 |     dlopenflags = dl.RTLD_NOW | dl.RTLD_GLOBAL
75 |     dlopenflags = 258
77 | sys.setdlopenflags(dlopenflags)
{% endraw %}

```
### packages/stk/stk_util/stk_util/diag/UserPlugin.cpp

```

{% raw %}
42 | #ifdef SIERRA_DLOPEN_ENABLED
180 | #ifdef SIERRA_DLOPEN_ENABLED
182 |   void *dl = dlopen(so_path, RTLD_NOW);
221 | #ifdef SIERRA_DLOPEN_ENABLED
223 |   void *dl = dlopen(nullptr, RTLD_LAZY);
{% endraw %}

```
### packages/stk/stk_util/stk_util/util/FeatureTest.hpp

```

{% raw %}
94 | /// @def SIERRA_DLOPEN_ENABLED
95 | /// SIERRA_DLOPEN_ENABLED -- The dlopen functionality is built into the sierra
{% endraw %}

```
### packages/stk/stk_classic/stk_util/stk_util/diag/UserPlugin.cpp

```

{% raw %}
16 | #ifdef SIERRA_DLOPEN_ENABLED
154 | #ifdef SIERRA_DLOPEN_ENABLED
156 |   void *dl = dlopen(so_path, RTLD_NOW);
195 | #ifdef SIERRA_DLOPEN_ENABLED
197 |   void *dl = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### packages/stk/stk_classic/stk_util/stk_util/util/FeatureTest.hpp

```

{% raw %}
65 | /// @def SIERRA_DLOPEN_ENABLED
66 | /// SIERRA_DLOPEN_ENABLED -- The dlopen functionality is built into the sierra
{% endraw %}

```
### packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C

```cpp

{% raw %}
32 | #ifdef SIERRA_DLOPEN_ENABLED
263 |           //it is necessary to do this call because the dlopen() in
267 | #ifdef SIERRA_DLOPEN_ENABLED
268 |           void *dl = dlopen(plugin_library_path.c_str(), RTLD_NOW | RTLD_GLOBAL);
276 |           //we must make the extra dlopen call to make it have
280 |           //void *dl = dlopen("~/libParaViewCatalystSierraAdaptor.so",
295 | #if SIERRA_DLOPEN_ENABLED
{% endraw %}

```