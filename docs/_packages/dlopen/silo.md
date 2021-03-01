---
name: "silo"
layout: package
next_package: slurm
previous_package: scorep
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.10.2-bsd
5 / 388 files match, 1 filtered matches.

 - [tests/ioperf.c](#testsioperfc)

### tests/ioperf.c

```c

{% raw %}
349 |         {
350 |             char libfilename[256];
351 |             sprintf(libfilename, "%s/ioperf_%s.so", dirs[d], ifacename);
352 |             dlhandle = dlopen(libfilename, RTLD_LAZY);
353 |             if (!dlhandle) continue;
354 | 
{% endraw %}

```