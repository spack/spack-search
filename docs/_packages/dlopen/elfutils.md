---
name: "elfutils"
layout: package
next_package: emacs
previous_package: dyninst
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
1955 | #define DT_MIPS_RLD_TEXT_RESOLVE_ADDR 0x7000002d /* Address of rld_text_rsolve
1956 | 						    function stored in GOT.  */
1957 | #define DT_MIPS_PERF_SUFFIX  0x7000002e /* Default suffix of dso to be added
1958 | 					   by rld on dlopen() calls.  */
1959 | #define DT_MIPS_COMPACT_SIZE 0x7000002f /* (O32)Size of compact rel section. */
1960 | #define DT_MIPS_GP_VALUE     0x70000030 /* GP value for aux GOTs.  */
{% endraw %}

```
### src/elfclassify.c

```c

{% raw %}
601 |     return false;
602 | 
603 |   /* It could still (also) be a (PIE) executable, but most likely you
604 |      can dlopen it just fine.  */
605 |   return true;
606 | }
{% endraw %}

```
### libdwfl/debuginfod-client.c

```c

{% raw %}
100 | void __attribute__ ((constructor))
101 | __libdwfl_debuginfod_init (void)
102 | {
103 |   void *debuginfod_so = dlopen("libdebuginfod-" VERSION ".so", RTLD_LAZY);
104 | 
105 |   if (debuginfod_so == NULL)
106 |     debuginfod_so = dlopen("libdebuginfod.so", RTLD_LAZY);
107 | 
108 |   if (debuginfod_so != NULL)
{% endraw %}

```