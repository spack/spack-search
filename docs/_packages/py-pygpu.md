---
name: "py-pygpu"
layout: package
next_package: ntirpc
previous_package: fish
languages: ['c']
---
## 0.6.2
1 / 134 files match, 1 filtered matches.

 - [src/loaders/dyn_load.c](#srcloadersdyn_loadc)

### src/loaders/dyn_load.c

```c

{% raw %}
11 |   void *res = dlopen(name, RTLD_LAZY|RTLD_LOCAL);
14 |     warn("dlopen: %s", name);
{% endraw %}

```