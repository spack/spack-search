---
name: "py-pygpu"
layout: package
next_package: py-pyjnius
previous_package: py-pygments
languages: ['c']
---
## 0.6.2
1 / 134 files match, 1 filtered matches.

 - [src/loaders/dyn_load.c](#srcloadersdyn_loadc)

### src/loaders/dyn_load.c

```c

{% raw %}
8 | #include <string.h>
9 | 
10 | void *ga_load_library(const char *name) {
11 |   void *res = dlopen(name, RTLD_LAZY|RTLD_LOCAL);
12 | #ifdef DEBUG
13 |   if (res == NULL)
14 |     warn("dlopen: %s", name);
15 | #endif
16 |   return res;
{% endraw %}

```