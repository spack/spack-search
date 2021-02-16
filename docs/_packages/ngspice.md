---
name: "ngspice"
layout: package
next_package: mpileaks
previous_package: libhio
languages: ['c']
---
## 33
5 / 3566 files match, 2 filtered matches.

 - [src/spicelib/devices/dev.c](#srcspicelibdevicesdevc)
 - [visualc/ng_shared_xspice_v/src/main_xspice.c](#visualcng_shared_xspice_vsrcmain_xspicec)

### src/spicelib/devices/dev.c

```c

{% raw %}
50 | void *dlopen(const char *, int);
318 |   lib = dlopen(libname,RTLD_NOW);
418 |     lib = dlopen(name, RTLD_NOW);
510 | void *dlopen(const char *name, int type)
{% endraw %}

```
### visualc/ng_shared_xspice_v/src/main_xspice.c

```c

{% raw %}
43 | void *dlopen (const char *, int);
136 |     ngdllhandle = dlopen(loadstring, RTLD_NOW);
645 |    Add functions dlopen, dlsym, dlerror, dlclose to Windows by
650 | void *dlopen(const char *name,int type)
{% endraw %}

```