---
name: "fipscheck"
layout: package
next_package: petsc
previous_package: r-rgraphviz
languages: ['cpp']
---
## 7.0.0.398
2 / 18 files match

 - [configure.ac](#configureac)
 - [src/library.c](#srclibraryc)

### configure.ac

```

{% raw %}
89 | AC_CHECK_LIB([dl], [dlopen], LIBDL="-ldl", LIBDL="")
{% endraw %}

```
### src/library.c

```cpp

{% raw %}
74 |         dl = dlopen(libname, RTLD_NODELETE|RTLD_NOLOAD|RTLD_LAZY);
{% endraw %}

```