---
name: "cpu-features"
layout: package
next_package: cpuinfo
previous_package: cpprestsdk
languages: ['c']
---
## develop
1 / 69 files match, 1 filtered matches.

 - [src/hwcaps.c](#srchwcapsc)

### src/hwcaps.c

```c

{% raw %}
88 |   void *libc_handle = NULL;
89 |   getauxval_func_t *func = NULL;
90 | 
91 |   dlerror();  // Cleaning error state before calling dlopen.
92 |   libc_handle = dlopen("libc.so", RTLD_NOW);
93 |   if (!libc_handle) {
94 |     D("Could not dlopen() C library: %s\n", dlerror());
95 |     return 0;
96 |   }
{% endraw %}

```