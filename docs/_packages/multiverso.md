---
name: "multiverso"
layout: package
next_package: stinger
previous_package: tfel
languages: ['cpp']
---
## 143187
1 / 255 files match

 - [include/multiverso/net/mpi_net.h](#includemultiversonetmpi_neth)

### include/multiverso/net/mpi_net.h

```cpp

{% raw %}
37 |   static void dlopen_libmpi()
51 |     if (!handle) handle = dlopen("libmpi_cxx.so",   mode);
103 |       dlopen_libmpi();
{% endraw %}

```