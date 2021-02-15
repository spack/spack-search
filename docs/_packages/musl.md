---
name: "musl"
layout: package
next_package: vsearch
previous_package: py-awkward1
languages: ['cpp']
---
## 1.1.20
3 / 2392 files match

 - [src/ldso/dlopen.c](#srcldsodlopenc)
 - [include/dlfcn.h](#includedlfcnh)
 - [ldso/dynlink.c](#ldsodynlinkc)

### src/ldso/dlopen.c

```cpp

{% raw %}
6 | static void *stub_dlopen(const char *file, int mode)
12 | weak_alias(stub_dlopen, dlopen);
{% endraw %}

```
### include/dlfcn.h

```cpp

{% raw %}
23 | void  *dlopen(const char *, int);
{% endraw %}

```
### ldso/dynlink.c

```cpp

{% raw %}
807 | 		 * (either system paths or a call to dlopen). */
1291 | 	 * dlopen from one of its constructors, but block any
1350 | 	 * at program startup or by an already-completed call to dlopen. */
1752 | void *dlopen(const char *file, int mode)
{% endraw %}

```