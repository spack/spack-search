---
name: "care"
layout: package
next_package: thepeg
previous_package: fltk
languages: ['cpp']
---
## develop
18 / 11464 files match

 - [blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#bltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)
 - [tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt](#tplchaisrctplumpiresrcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342cmakeliststxt)
 - [tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c](#tplchaisrctplumpiresrcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342srccivetwebc)
 - [tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/releases.rst](#tplchaisrctplumpiresrcumpiretplconduitsrcdocssphinxreleasesrst)
 - [tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/building.rst](#tplchaisrctplumpiresrcumpiretplconduitsrcdocssphinxbuildingrst)
 - [tpl/chai/src/tpl/umpire/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#tplchaisrctplumpirebltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)
 - [tpl/chai/src/tpl/raja/src/RuntimePluginLoader.cpp](#tplchaisrctplrajasrcruntimepluginloadercpp)
 - [tpl/chai/src/tpl/raja/src/KokkosPluginLoader.cpp](#tplchaisrctplrajasrckokkospluginloadercpp)
 - [tpl/chai/src/tpl/raja/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#tplchaisrctplrajabltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)
 - [tpl/chai/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#tplchaibltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)
 - [tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt](#tplumpiresrcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342cmakeliststxt)
 - [tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c](#tplumpiresrcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342srccivetwebc)
 - [tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/releases.rst](#tplumpiresrcumpiretplconduitsrcdocssphinxreleasesrst)
 - [tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/building.rst](#tplumpiresrcumpiretplconduitsrcdocssphinxbuildingrst)
 - [tpl/umpire/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#tplumpirebltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)
 - [tpl/raja/src/RuntimePluginLoader.cpp](#tplrajasrcruntimepluginloadercpp)
 - [tpl/raja/src/KokkosPluginLoader.cpp](#tplrajasrckokkospluginloadercpp)
 - [tpl/raja/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#tplrajabltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)

### blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt

```

{% raw %}
70 | # We don't want to rely on dlopen NO_SSL_DL and we don't require a
{% endraw %}

```
### tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c

```cpp

{% raw %}
3837 | /* If SSL is loaded dynamically, dlopen/dlclose is required. */
3848 | dlopen(const char *dll_name, int flags)
11829 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/releases.rst

```

{% raw %}
151 |  * Updated the version of civetweb used to avoid dlopen issues with SSL for static builds
{% endraw %}

```
### tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/building.rst

```

{% raw %}
361 | HDF5 and gtest use runtime features such as ``dlopen``. Because of this, building static on Cray systems commonly yields the following flavor of compiler warning:
{% endraw %}

```
### tpl/chai/src/tpl/umpire/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### tpl/chai/src/tpl/raja/src/RuntimePluginLoader.cpp

```

{% raw %}
88 |   void *plugin = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
91 |     printf("[RuntimePluginLoader]: dlopen failed: %s\n", dlerror());
{% endraw %}

```
### tpl/chai/src/tpl/raja/src/KokkosPluginLoader.cpp

```

{% raw %}
91 |   void *plugin = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
94 |     printf("[KokkosPluginLoader]: dlopen failed: %s\n", dlerror());
{% endraw %}

```
### tpl/chai/src/tpl/raja/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### tpl/chai/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt

```

{% raw %}
70 | # We don't want to rely on dlopen NO_SSL_DL and we don't require a
{% endraw %}

```
### tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c

```cpp

{% raw %}
3837 | /* If SSL is loaded dynamically, dlopen/dlclose is required. */
3848 | dlopen(const char *dll_name, int flags)
11829 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/releases.rst

```

{% raw %}
151 |  * Updated the version of civetweb used to avoid dlopen issues with SSL for static builds
{% endraw %}

```
### tpl/umpire/src/umpire/tpl/conduit/src/docs/sphinx/building.rst

```

{% raw %}
361 | HDF5 and gtest use runtime features such as ``dlopen``. Because of this, building static on Cray systems commonly yields the following flavor of compiler warning:
{% endraw %}

```
### tpl/umpire/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```
### tpl/raja/src/RuntimePluginLoader.cpp

```

{% raw %}
88 |   void *plugin = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
91 |     printf("[RuntimePluginLoader]: dlopen failed: %s\n", dlerror());
{% endraw %}

```
### tpl/raja/src/KokkosPluginLoader.cpp

```

{% raw %}
91 |   void *plugin = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
94 |     printf("[KokkosPluginLoader]: dlopen failed: %s\n", dlerror());
{% endraw %}

```
### tpl/raja/blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```