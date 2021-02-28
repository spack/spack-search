---
name: "darshan-util"
layout: package
next_package: vim
previous_package: cpuinfo
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.2.0
2 / 277 files match, 1 filtered matches.

 - [darshan-runtime/darshan.h](#darshan-runtimedarshanh)

### darshan-runtime/darshan.h

```c

{% raw %}
47 | #define MAP_OR_FAIL(__func) \
48 |     if (!(__real_ ## __func)) \
49 |     { \
50 |         __real_ ## __func = dlsym(RTLD_NEXT, #__func); \
51 |         if(!(__real_ ## __func)) { \
52 |             darshan_core_fprintf(stderr, "Darshan failed to map symbol: %s\n", #__func); \
{% endraw %}

```