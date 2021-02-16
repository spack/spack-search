---
name: "libgpuarray"
layout: package
next_package: libgssglue
previous_package: libfuse
languages: ['c']
---
## 0.7.0
1 / 200 files match, 1 filtered matches.

 - [src/loaders/dyn_load.c](#srcloadersdyn_loadc)

### src/loaders/dyn_load.c

```c

{% raw %}
12 |   void *res = dlopen(name, RTLD_LAZY|RTLD_LOCAL);
{% endraw %}

```