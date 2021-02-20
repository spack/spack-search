---
name: "draco"
layout: package
next_package: dyninst
previous_package: dpdk
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
83 | 
84 |   // RTLD_LAZY means symbols are resolved as they're needed.  We might want
85 |   // to make this an option, in the future.
86 |   d_handle = dlopen(file_name.c_str(), RTLD_LAZY);
87 | 
88 |   d_file_name = file_name;
{% endraw %}

```
### src/shared_lib/dlfcn_support.hh

```cpp

{% raw %}
37 | 
38 | static const int RTLD_LAZY = 1; // or whatever.
39 | 
40 | void *dlopen(const char * /*filename*/, int /*flag*/) {
41 |   Insist(0, "Serious Shared_Lib error.");
42 |   void *dummy(0);
{% endraw %}

```
### src/shared_lib/test/Foo_Base.hh

```cpp

{% raw %}
22 |   This class may act as an abstract base class for derived classes that are
23 |   defined within a shared library.
24 |   
25 |   For more information, see the "C++ dlopen mini HOWTO" by Aaron Isotton.
26 |  */
27 | //============================================================================//
{% endraw %}

```
### src/shared_lib/test/Foo.hh

```cpp

{% raw %}
24 |   When loaded as a shared lib, objects of this class are created and
25 |   destroyed via the functions defined in creator_destroyer.cc.
26 |   
27 |   For more information, see the "C++ dlopen mini HOWTO" by Aaron Isotton.
28 |  */
29 | //============================================================================//
{% endraw %}

```