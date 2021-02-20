---
name: "apex"
layout: package
next_package: apr
previous_package: aomp
languages: ['c']
---
## 0.1
1 / 266 files match, 1 filtered matches.

 - [src/wrappers/pthread_wrapper.c](#srcwrapperspthread_wrapperc)

### src/wrappers/pthread_wrapper.c

```c

{% raw %}
43 |   // #defines in Profiler.h, -Wl,-wrap on the link line, and LD_PRELOAD.
44 |   if (handle == caller) {
45 |     RESET_DLERROR();
46 |     void * syms = dlopen(NULL, RTLD_NOW);
47 |     CHECK_DLERROR();
48 |     do {
{% endraw %}

```