---
name: "draco"
layout: package
next_package: activeharmony
previous_package: xhmm
languages: ['cpp']
---
## 7.6.0
5 / 1182 files match, 4 filtered matches.

 - [src/shared_lib/Shared_Lib.cc](#srcshared_libshared_libcc)
 - [src/shared_lib/dlfcn_support.hh](#srcshared_libdlfcn_supporthh)
 - [src/shared_lib/test/Foo_Base.hh](#srcshared_libtestfoo_basehh)
 - [src/shared_lib/test/Foo.hh](#srcshared_libtestfoohh)

### src/shared_lib/Shared_Lib.cc

```cpp

{% raw %}
86 |   d_handle = dlopen(file_name.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/shared_lib/dlfcn_support.hh

```cpp

{% raw %}
40 | void *dlopen(const char * /*filename*/, int /*flag*/) {
{% endraw %}

```
### src/shared_lib/test/Foo_Base.hh

```cpp

{% raw %}
25 |   For more information, see the "C++ dlopen mini HOWTO" by Aaron Isotton.
{% endraw %}

```
### src/shared_lib/test/Foo.hh

```cpp

{% raw %}
27 |   For more information, see the "C++ dlopen mini HOWTO" by Aaron Isotton.
{% endraw %}

```