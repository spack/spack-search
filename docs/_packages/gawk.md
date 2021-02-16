---
name: "gawk"
layout: package
next_package: gcc
previous_package: g2o
languages: ['c']
---
## 5.1.0
18 / 1886 files match, 3 filtered matches.

 - [ext.c](#extc)
 - [nonposix.h](#nonposixh)
 - [pc/dlfcn.h](#pcdlfcnh)

### ext.c

```c

{% raw %}
58 | 	if ((dl = dlopen(lib_name, flags)) == NULL)
{% endraw %}

```
### nonposix.h

```c

{% raw %}
93 | void *os2_dlopen(const char *file, int mode);
{% endraw %}

```
### pc/dlfcn.h

```c

{% raw %}
6 | extern void *dlopen (const char *, int);
{% endraw %}

```