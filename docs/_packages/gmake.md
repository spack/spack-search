---
name: "gmake"
layout: package
next_package: boost
previous_package: gawk
languages: ['c']
---
## 4.2.1
6 / 204 files match

 - [load.c](#loadc)
 - [w32/compat/posixfcn.c](#w32compatposixfcnc)
 - [w32/include/dlfcn.h](#w32includedlfcnh)

### load.c

```c

{% raw %}
55 |       global_dl = dlopen (NULL, RTLD_NOW|RTLD_GLOBAL);
75 |         dlp = dlopen (concat (2, "./", ldname), RTLD_LAZY|RTLD_GLOBAL);
79 |         dlp = dlopen (ldname, RTLD_LAZY|RTLD_GLOBAL);
{% endraw %}

```
### w32/compat/posixfcn.c

```c

{% raw %}
371 | dlopen (const char *file, int mode)
{% endraw %}

```
### w32/include/dlfcn.h

```c

{% raw %}
23 | extern void *dlopen (const char *, int);
{% endraw %}

```