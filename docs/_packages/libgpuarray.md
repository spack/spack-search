---
name: "libgpuarray"
layout: package
next_package: mpich
previous_package: guile
languages: ['c']
---
## 0.7.0
1 / 200 files match

 - [src/loaders/dyn_load.c](#srcloadersdyn_loadc)

### src/loaders/dyn_load.c

```c

{% raw %}
12 |   void *res = dlopen(name, RTLD_LAZY|RTLD_LOCAL);
{% endraw %}

```