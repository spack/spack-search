---
name: "vsearch"
layout: package
next_package: vt
previous_package: vim
languages: ['cpp']
---
## 2.4.3
2 / 120 files match, 1 filtered matches.

 - [src/dynlibs.cc](#srcdynlibscc)

### src/dynlibs.cc

```cpp

{% raw %}
119 |   gz_lib = dlopen(gz_libname, RTLD_LAZY);
137 |   bz2_lib = dlopen(bz2_libname, RTLD_LAZY);
{% endraw %}

```