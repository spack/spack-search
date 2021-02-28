---
name: "silo"
layout: package
next_package: libxslt
previous_package: nicstat
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.10.2-bsd
4 / 388 files match, 1 filtered matches.

 - [tests/ioperf.c](#testsioperfc)

### tests/ioperf.c

```c

{% raw %}
352 |             dlhandle = dlopen(libfilename, RTLD_LAZY);
353 |             if (!dlhandle) continue;
354 | 
355 |             CreateInterfaceFunc createFunc = (CreateInterfaceFunc) dlsym(dlhandle, "CreateInterface");
356 |             if (!createFunc) continue;
357 | 
{% endraw %}

```