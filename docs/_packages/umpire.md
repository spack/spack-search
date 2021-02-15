---
name: "umpire"
layout: package
next_package: libxfixes
previous_package: chapel
languages: ['cpp']
---
## 0.3.1
4 / 2034 files match

 - [src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt](#srcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342cmakeliststxt)
 - [src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c](#srcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342srccivetwebc)
 - [src/umpire/tpl/conduit/src/docs/sphinx/releases.rst](#srcumpiretplconduitsrcdocssphinxreleasesrst)
 - [src/umpire/tpl/conduit/src/docs/sphinx/building.rst](#srcumpiretplconduitsrcdocssphinxbuildingrst)

### src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt

```

{% raw %}
70 | # We don't want to rely on dlopen NO_SSL_DL and we don't require a
{% endraw %}

```
### src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c

```cpp

{% raw %}
3837 | /* If SSL is loaded dynamically, dlopen/dlclose is required. */
3848 | dlopen(const char *dll_name, int flags)
11829 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/umpire/tpl/conduit/src/docs/sphinx/releases.rst

```

{% raw %}
151 |  * Updated the version of civetweb used to avoid dlopen issues with SSL for static builds
{% endraw %}

```
### src/umpire/tpl/conduit/src/docs/sphinx/building.rst

```

{% raw %}
361 | HDF5 and gtest use runtime features such as ``dlopen``. Because of this, building static on Cray systems commonly yields the following flavor of compiler warning:
{% endraw %}

```