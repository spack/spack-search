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
3 | __attribute__((__visibility__("hidden")))
4 | void __dl_seterr(const char *, ...);
5 | 
6 | static void *stub_dlopen(const char *file, int mode)
7 | {
8 | 	__dl_seterr("Dynamic loading not supported");
9 | 	return 0;
10 | }
11 | 
12 | weak_alias(stub_dlopen, dlopen);
13 | 
{% endraw %}

```
### include/dlfcn.h

```c

{% raw %}
20 | 
21 | int    dlclose(void *);
22 | char  *dlerror(void);
23 | void  *dlopen(const char *, int);
24 | void  *dlsym(void *__restrict, const char *__restrict);
25 | 
{% endraw %}

```
### ldso/dynlink.c

```c

{% raw %}
1749 | 	lazy_head = p;
1750 | }
1751 | 
1752 | void *dlopen(const char *file, int mode)
1753 | {
1754 | 	struct dso *volatile p, *orig_tail, *orig_syms_tail, *orig_lazy_head, *next;
{% endraw %}

```