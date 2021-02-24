---
name: "gmake"
layout: package
next_package: casacore
previous_package: whizard
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.2.1
5 / 204 files match, 3 filtered matches.

 - [load.c](#loadc)
 - [w32/compat/posixfcn.c](#w32compatposixfcnc)
 - [w32/include/dlfcn.h](#w32includedlfcnh)

### load.c

```c

{% raw %}
60 |         }
61 |     }
62 | 
63 |   symp = (load_func_t) dlsym (global_dl, symname);
64 |   if (! symp)
65 |     {
90 |         }
91 | 
92 |       /* Assert that the GPL license symbol is defined.  */
93 |       symp = (load_func_t) dlsym (dlp, "plugin_is_GPL_compatible");
94 |       if (! symp)
95 |         OS (fatal, flocp,
96 |              _("Loaded object %s is not declared to be GPL compatible"),
97 |              ldname);
98 | 
99 |       symp = (load_func_t) dlsym (dlp, symname);
100 |       if (! symp)
101 |         {
{% endraw %}

```
### w32/compat/posixfcn.c

```c

{% raw %}
422 | }
423 | 
424 | void *
425 | dlsym (void *handle, const char *name)
426 | {
427 |   FARPROC addr = NULL;
{% endraw %}

```
### w32/include/dlfcn.h

```c

{% raw %}
21 | #define RTLD_GLOBAL 4
22 | 
23 | extern void *dlopen (const char *, int);
24 | extern void *dlsym (void *, const char *);
25 | extern char *dlerror (void);
26 | extern int   dlclose (void *);
{% endraw %}

```