---
name: "apr"
layout: package
next_package: arrayfire
previous_package: aomp
languages: ['c']
---
## 1.7.0
8 / 467 files match, 4 filtered matches.

 - [include/arch/aix/apr_arch_dso.h](#includearchaixapr_arch_dsoh)
 - [dso/unix/dso.c](#dsounixdsoc)
 - [dso/aix/dso.c](#dsoaixdsoc)
 - [dso/netware/dso.c](#dsonetwaredsoc)

### include/arch/aix/apr_arch_dso.h

```c

{% raw %}
27 | void *dlopen(const char *path, int mode);
{% endraw %}

```
### dso/unix/dso.c

```c

{% raw %}
122 |     void *os_handle = dlopen((char *)path, RTLD_NOW | RTLD_GLOBAL);
138 |     os_handle = dlopen(path, flags);
{% endraw %}

```
### dso/aix/dso.c

```c

{% raw %}
130 |     void *os_handle = dlopen((char *)path, RTLD_NOW | RTLD_GLOBAL);
241 | void *dlopen(const char *path, int mode)
285 | 	strcpy(errbuf, "dlopen: ");
{% endraw %}

```
### dso/netware/dso.c

```c

{% raw %}
80 |     os_handle = dlopen(fullpath, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```