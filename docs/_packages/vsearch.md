---
name: "vsearch"
layout: package
next_package: vtable-dumper
previous_package: vpic
languages: ['cpp']
---
## 2.4.3
2 / 120 files match, 1 filtered matches.

 - [src/dynlibs.cc](#srcdynlibscc)

### src/dynlibs.cc

```cpp

{% raw %}
116 | #ifdef _WIN32
117 |   gz_lib = LoadLibraryA(gz_libname);
118 | #else
119 |   gz_lib = dlopen(gz_libname, RTLD_LAZY);
120 | #endif
121 |   if (gz_lib)
134 | #ifdef _WIN32
135 |   bz2_lib = LoadLibraryA(bz2_libname);
136 | #else
137 |   bz2_lib = dlopen(bz2_libname, RTLD_LAZY);
138 | #endif
139 |   if (bz2_lib)
{% endraw %}

```