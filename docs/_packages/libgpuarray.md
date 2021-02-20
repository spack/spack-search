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
9 | #include <string.h>
10 | 
11 | void *ga_load_library(const char *name, error *e) {
12 |   void *res = dlopen(name, RTLD_LAZY|RTLD_LOCAL);
13 |   if (res == NULL)
14 |     error_fmt(e, GA_LOAD_ERROR, "Could not load \"%s\": %s", name, dlerror());
{% endraw %}

```