---
name: "conduit"
layout: package
next_package: libxp
previous_package: boinc-client
languages: ['cpp']
---
## 0.5.1
5 / 1108 files match

 - [CHANGELOG.md](#changelogmd)
 - [src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt](#srcthirdparty_builtincivetweb-0a95342cmakeliststxt)
 - [src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c](#srcthirdparty_builtincivetweb-0a95342srccivetwebc)
 - [src/docs/sphinx/releases.rst](#srcdocssphinxreleasesrst)
 - [src/docs/sphinx/building.rst](#srcdocssphinxbuildingrst)

### CHANGELOG.md

```

{% raw %}
263 | - Updated the version of civetweb used to avoid dlopen issues with SSL for static builds
{% endraw %}

```
### src/thirdparty_builtin/civetweb-0a95342/CMakeLists.txt

```

{% raw %}
70 | # We don't want to rely on dlopen NO_SSL_DL and we don't require a
{% endraw %}

```
### src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c

```cpp

{% raw %}
3837 | /* If SSL is loaded dynamically, dlopen/dlclose is required. */
3848 | dlopen(const char *dll_name, int flags)
11829 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/docs/sphinx/releases.rst

```

{% raw %}
336 |  * Updated the version of civetweb used to avoid dlopen issues with SSL for static builds
{% endraw %}

```
### src/docs/sphinx/building.rst

```

{% raw %}
420 | HDF5 and gtest use runtime features such as ``dlopen``. Because of this, building static on Cray systems commonly yields the following flavor of compiler warning:
{% endraw %}

```