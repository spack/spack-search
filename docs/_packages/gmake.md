---
name: "gmake"
layout: package
next_package: gmt
previous_package: glusterfs
languages: ['c']
---
## 4.2.1
6 / 204 files match, 3 filtered matches.

 - [load.c](#loadc)
 - [w32/compat/posixfcn.c](#w32compatposixfcnc)
 - [w32/include/dlfcn.h](#w32includedlfcnh)

### load.c

```c

{% raw %}
52 | 
53 |   if (! global_dl)
54 |     {
55 |       global_dl = dlopen (NULL, RTLD_NOW|RTLD_GLOBAL);
56 |       if (! global_dl)
57 |         {
72 |           && ! strchr (ldname, '\\')
73 | #endif
74 |          )
75 |         dlp = dlopen (concat (2, "./", ldname), RTLD_LAZY|RTLD_GLOBAL);
76 | 
77 |       /* If we haven't opened it yet, try the default search path.  */
78 |       if (! dlp)
79 |         dlp = dlopen (ldname, RTLD_LAZY|RTLD_GLOBAL);
80 | 
81 |       /* Still no?  Then fail.  */
{% endraw %}

```
### w32/compat/posixfcn.c

```c

{% raw %}
368 | static DWORD last_err;
369 | 
370 | void *
371 | dlopen (const char *file, int mode)
372 | {
373 |   char dllfn[MAX_PATH], *p;
{% endraw %}

```
### w32/include/dlfcn.h

```c

{% raw %}
20 | #define RTLD_NOW    2
21 | #define RTLD_GLOBAL 4
22 | 
23 | extern void *dlopen (const char *, int);
24 | extern void *dlsym (void *, const char *);
25 | extern char *dlerror (void);
{% endraw %}

```