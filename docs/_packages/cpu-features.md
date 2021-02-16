---
name: "cpu-features"
layout: package
next_package: libxfont2
previous_package: libpam
languages: ['c']
---
## develop
1 / 69 files match, 1 filtered matches.

 - [src/hwcaps.c](#srchwcapsc)

### src/hwcaps.c

```c

{% raw %}
91 |   dlerror();  // Cleaning error state before calling dlopen.
92 |   libc_handle = dlopen("libc.so", RTLD_NOW);
94 |     D("Could not dlopen() C library: %s\n", dlerror());
{% endraw %}

```