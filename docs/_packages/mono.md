---
name: "mono"
layout: package
next_package: mpich
previous_package: mivisionx
languages: ['c']
---
## 5.10.1.57
46 / 82201 files match, 7 filtered matches.

 - [mono/utils/mono-dl-posix.c](#monoutilsmono-dl-posixc)
 - [mono/mini/mini-darwin.c](#monominimini-darwinc)
 - [mono/eglib/gmodule-unix.c](#monoeglibgmodule-unixc)
 - [libgc/threadlibs.c](#libgcthreadlibsc)
 - [libgc/dyn_load.c](#libgcdyn_loadc)
 - [libgc/gc_dlopen.c](#libgcgc_dlopenc)
 - [libgc/include/gc_pthread_redirects.h](#libgcincludegc_pthread_redirectsh)

### mono/utils/mono-dl-posix.c

```c

{% raw %}
68 | 	return dlopen (file, flags);
{% endraw %}

```
### mono/mini/mini-darwin.c

```c

{% raw %}
73 | void* dlopen(const char* path, int mode);
87 | 		void *handle = dlopen ("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation", RTLD_LAZY);
{% endraw %}

```
### mono/eglib/gmodule-unix.c

```c

{% raw %}
59 | 	handle = dlopen (file, f);
{% endraw %}

```
### libgc/threadlibs.c

```c

{% raw %}
7 | 	printf("-Wl,--wrap -Wl,dlopen "
{% endraw %}

```
### libgc/dyn_load.c

```c

{% raw %}
39 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
152 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
227 | 	--> fix mutual exclusion with dlopen
{% endraw %}

```
### libgc/gc_dlopen.c

```c

{% raw %}
48 |   static void disable_gc_for_dlopen()
65 |   void * __wrap_dlopen(const char *path, int mode)
67 |   void * GC_dlopen(path, mode)
75 |       disable_gc_for_dlopen();
78 |       result = (void *)__real_dlopen(path, mode);
80 |       result = dlopen(path, mode);
83 |       GC_enable(); /* undoes disable_gc_for_dlopen */
{% endraw %}

```
### libgc/include/gc_pthread_redirects.h

```c

{% raw %}
23 |   void * GC_dlopen(const char *path, int mode);
{% endraw %}

```