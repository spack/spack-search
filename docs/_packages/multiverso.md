---
name: "multiverso"
layout: package
next_package: stinger
previous_package: tfel
languages: ['c']
---
## 143187
1 / 255 files match, 1 filtered matches.

 - [include/multiverso/net/mpi_net.h](#includemultiversonetmpi_neth)

### include/multiverso/net/mpi_net.h

```c

{% raw %}
37 |   static void dlopen_libmpi()
51 |     if (!handle) handle = dlopen("libmpi_cxx.so",   mode);
103 |       dlopen_libmpi();
{% endraw %}

```