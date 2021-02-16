---
name: "musl"
layout: package
next_package: mvapich2
previous_package: multiverso
languages: ['c']
---
## 1.1.20
3 / 2392 files match, 3 filtered matches.

 - [src/ldso/dlopen.c](#srcldsodlopenc)
 - [include/dlfcn.h](#includedlfcnh)
 - [ldso/dynlink.c](#ldsodynlinkc)

### src/ldso/dlopen.c

```c

{% raw %}
6 | static void *stub_dlopen(const char *file, int mode)
12 | weak_alias(stub_dlopen, dlopen);
{% endraw %}

```
### include/dlfcn.h

```c

{% raw %}
23 | void  *dlopen(const char *, int);
{% endraw %}

```
### ldso/dynlink.c

```c

{% raw %}
1752 | void *dlopen(const char *file, int mode)
{% endraw %}

```