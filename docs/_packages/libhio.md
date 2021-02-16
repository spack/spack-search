---
name: "libhio"
layout: package
next_package: libiberty
previous_package: libhbaapi
languages: ['c']
---
## 1.4.1.0
7 / 114 files match, 3 filtered matches.

 - [src/hio_component.c](#srchio_componentc)
 - [test/xexec/xexec.c](#testxexecxexecc)
 - [test/xexec/xexec_base.c](#testxexecxexec_basec)

### src/hio_component.c

```c

{% raw %}
81 |       dl_ctx = dlopen (path, RTLD_LAZY);
85 |         hioi_log (context, HIO_VERBOSE_DEBUG_LOW, "Failed to dlopen() plugin. Reason: %s", strerror (errno));
{% endraw %}

```
### test/xexec/xexec.c

```c

{% raw %}
73 |   " dlopen and related actions can be enabled by building with -DDLFCN.\n"
{% endraw %}

```
### test/xexec/xexec_base.c

```c

{% raw %}
69 |   "  dlo <name>    Issue dlopen for specified file name\n"
548 |   S.dl_handle[++S.dl_num] = dlopen(name, RTLD_NOW);
549 |   VERB3("%s; dlopen(%s) returns %p", A.desc, name, S.dl_handle[S.dl_num]);
551 |     VERB0("%s; dlopen failed: %s", A.desc, dlerror());
{% endraw %}

```