---
name: "vsearch"
layout: package
next_package: libxtrap
previous_package: musl
languages: ['cpp']
---
## 2.4.3
2 / 120 files match

 - [src/dynlibs.cc](#srcdynlibscc)

### src/dynlibs.cc

```cpp

{% raw %}
119 |   gz_lib = dlopen(gz_libname, RTLD_LAZY);
137 |   bz2_lib = dlopen(bz2_libname, RTLD_LAZY);
{% endraw %}

```