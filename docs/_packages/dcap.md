---
name: "dcap"
layout: package
next_package: onednn
previous_package: meep
languages: ['c']
---
## 2.47.12
7 / 166 files match, 4 filtered matches.

 - [src/win32_libdl.c](#srcwin32_libdlc)
 - [src/tunnelManager.c](#srctunnelmanagerc)
 - [src/win32_libdl.h](#srcwin32_libdlh)
 - [src/system_io.c](#srcsystem_ioc)

### src/win32_libdl.c

```c

{% raw %}
12 | void *dlopen(const char *name, int mode)
{% endraw %}

```
### src/tunnelManager.c

```c

{% raw %}
101 | 	handle = dlopen( libname, RTLD_NOW);
108 | 		handle = dlopen(fullpath, RTLD_NOW);
{% endraw %}

```
### src/win32_libdl.h

```c

{% raw %}
23 | extern void  *dlopen(const char *, int);
{% endraw %}

```
### src/system_io.c

```c

{% raw %}
237 | 		handle = dlopen( libname, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```