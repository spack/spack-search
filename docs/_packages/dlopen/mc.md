---
name: "mc"
layout: package
next_package: valgrind
previous_package: openmpi
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.8.23
6 / 1128 files match, 1 filtered matches.

 - [lib/tty/key.c](#libttykeyc)

### lib/tty/key.c

```c

{% raw %}
920 |             /* QNX 6.x has no support for RTLD_LAZY */
921 |             void *ph_handle;
922 | 
923 |             ph_handle = dlopen ("/usr/lib/libph.so", RTLD_NOW);
924 |             if (ph_handle != NULL)
925 |             {
{% endraw %}

```