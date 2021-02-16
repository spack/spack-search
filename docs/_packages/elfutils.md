---
name: "elfutils"
layout: package
next_package: expat
previous_package: fastdb
languages: ['c']
---
## 0.180
9 / 1398 files match, 3 filtered matches.

 - [libelf/elf.h](#libelfelfh)
 - [src/elfclassify.c](#srcelfclassifyc)
 - [libdwfl/debuginfod-client.c](#libdwfldebuginfod-clientc)

### libelf/elf.h

```c

{% raw %}
1958 | 					   by rld on dlopen() calls.  */
{% endraw %}

```
### src/elfclassify.c

```c

{% raw %}
604 |      can dlopen it just fine.  */
{% endraw %}

```
### libdwfl/debuginfod-client.c

```c

{% raw %}
103 |   void *debuginfod_so = dlopen("libdebuginfod-" VERSION ".so", RTLD_LAZY);
106 |     debuginfod_so = dlopen("libdebuginfod.so", RTLD_LAZY);
{% endraw %}

```