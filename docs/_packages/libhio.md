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
78 |         break;
79 |       }
80 | 
81 |       dl_ctx = dlopen (path, RTLD_LAZY);
82 |       free (path);
83 |       if (NULL == dl_ctx) {
84 |         rc = hioi_err_errno (errno);
85 |         hioi_log (context, HIO_VERBOSE_DEBUG_LOW, "Failed to dlopen() plugin. Reason: %s", strerror (errno));
86 |         continue;
87 |       }
{% endraw %}

```
### test/xexec/xexec.c

```c

{% raw %}
70 |   "\n"
71 |   #endif // MPI
72 |   #ifndef DLFCN
73 |   " dlopen and related actions can be enabled by building with -DDLFCN.\n"
74 |   "\n"
75 |   #endif // DLFCN
{% endraw %}

```
### test/xexec/xexec_base.c

```c

{% raw %}
66 |   "                a multiple of <stride>.\n"
67 |   "  nf            Free allocated blocks\n"
68 |   #ifdef DLFCN
69 |   "  dlo <name>    Issue dlopen for specified file name\n"
70 |   "  dls <symbol>  Issue dlsym for specified symbol in most recently opened library\n"
71 |   "  dlc           Issue dlclose for most recently opened library\n"
545 | 
546 | ACTION_RUN(dlo_run) {
547 |   char * name = V0.s;
548 |   S.dl_handle[++S.dl_num] = dlopen(name, RTLD_NOW);
549 |   VERB3("%s; dlopen(%s) returns %p", A.desc, name, S.dl_handle[S.dl_num]);
550 |   if (!S.dl_handle[S.dl_num]) {
551 |     VERB0("%s; dlopen failed: %s", A.desc, dlerror());
552 |     S.dl_num--;
553 |   }
{% endraw %}

```