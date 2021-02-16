---
name: "tcl"
layout: package
next_package: exciting
previous_package: libxcursor
languages: ['c']
---
## 8.6.6
9 / 1481 files match

 - [compat/dlfcn.h](#compatdlfcnh)
 - [pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c](#pkgssqlite3130compatsqlite3sqlite3c)
 - [unix/tclLoadDyld.c](#unixtclloaddyldc)
 - [unix/tclLoadDl.c](#unixtclloaddlc)
 - [unix/tclUnixInit.c](#unixtclunixinitc)
 - [unix/tclLoadAix.c](#unixtclloadaixc)

### compat/dlfcn.h

```c

{% raw %}
48 | void *dlopen (const char *path, int mode);
{% endraw %}

```
### pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c

```c

{% raw %}
35273 |   return dlopen(zFilename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### unix/tclLoadDyld.c

```c

{% raw %}
174 |     int dlopenflags = 0;
193 |     	dlopenflags |= RTLD_GLOBAL;
195 |     	dlopenflags |= RTLD_LOCAL;
198 |     	dlopenflags |= RTLD_LAZY;
200 |     	dlopenflags |= RTLD_NOW;
202 |     dlHandle = dlopen(nativePath, dlopenflags);
210 | 	dlHandle = dlopen(nativeFileName, dlopenflags);
{% endraw %}

```
### unix/tclLoadDl.c

```c

{% raw %}
77 |     int dlopenflags = 0;
90 |     	dlopenflags |= RTLD_GLOBAL;
92 |     	dlopenflags |= RTLD_LOCAL;
95 |     	dlopenflags |= RTLD_LAZY;
97 |     	dlopenflags |= RTLD_NOW;
99 |     handle = dlopen(native, dlopenflags);
114 | 	handle = dlopen(native, dlopenflags);
{% endraw %}

```
### unix/tclUnixInit.c

```c

{% raw %}
409 |     (void) dlopen(NULL, RTLD_NOW);			/* INTL: Native. */
{% endraw %}

```
### unix/tclLoadAix.c

```c

{% raw %}
96 | dlopen(
149 | 	strcpy(errbuf, "dlopen: ");
{% endraw %}

```