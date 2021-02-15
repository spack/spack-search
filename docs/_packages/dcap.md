---
name: "dcap"
layout: package
next_package: onednn
previous_package: meep
languages: ['cpp']
---
## 2.47.12
7 / 166 files match

 - [specs/sl6/dcap-fedora.spec](#specssl6dcap-fedoraspec)
 - [specs/sl6/dcap-epel.spec](#specssl6dcap-epelspec)
 - [src/win32_libdl.c](#srcwin32_libdlc)
 - [src/tunnelManager.c](#srctunnelmanagerc)
 - [src/win32_libdl.h](#srcwin32_libdlh)
 - [src/system_io.c](#srcsystem_ioc)
 - [patches/2.47.6/dcap-dlopen.patch](#patches2476dcap-dlopenpatch)

### specs/sl6/dcap-fedora.spec

```

{% raw %}
163 | - Drop patch dcap-dlopen.patch - merged upstream
{% endraw %}

```
### specs/sl6/dcap-epel.spec

```

{% raw %}
16 | Patch0:		%{name}-dlopen.patch
{% endraw %}

```
### src/win32_libdl.c

```cpp

{% raw %}
12 | void *dlopen(const char *name, int mode)
{% endraw %}

```
### src/tunnelManager.c

```cpp

{% raw %}
101 | 	handle = dlopen( libname, RTLD_NOW);
108 | 		handle = dlopen(fullpath, RTLD_NOW);
{% endraw %}

```
### src/win32_libdl.h

```cpp

{% raw %}
23 | extern void  *dlopen(const char *, int);
{% endraw %}

```
### src/system_io.c

```cpp

{% raw %}
237 | 		handle = dlopen( libname, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### patches/2.47.6/dcap-dlopen.patch

```

{% raw %}
13 |  	handle = dlopen( libname, RTLD_NOW);
19 | +		handle = dlopen(fullpath, RTLD_NOW);
{% endraw %}

```