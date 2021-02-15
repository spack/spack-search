---
name: "vsearch"
layout: package
next_package: libxtrap
previous_package: musl
languages: ['cpp']
---
## 2.4.3
2 / 120 files match

 - [configure.ac](#configureac)
 - [src/dynlibs.cc](#srcdynlibscc)

### configure.ac

```

{% raw %}
26 | AC_CHECK_LIB([dl], [dlopen])
{% endraw %}

```
### src/dynlibs.cc

```cpp

{% raw %}
119 |   gz_lib = dlopen(gz_libname, RTLD_LAZY);
137 |   bz2_lib = dlopen(bz2_libname, RTLD_LAZY);
{% endraw %}

```