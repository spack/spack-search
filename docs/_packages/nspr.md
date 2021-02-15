---
name: "nspr"
layout: package
next_package: libatomic-ops
previous_package: llvm-openmp
languages: ['cpp']
---
## 4.13.1
7 / 635 files match

 - [nspr/configure.in](#nsprconfigurein)
 - [nspr/pr/src/linking/prlink.c](#nsprprsrclinkingprlinkc)
 - [nspr/pr/src/malloc/prmem.c](#nsprprsrcmallocprmemc)
 - [nspr/pr/src/pthreads/ptio.c](#nsprprsrcpthreadsptioc)
 - [nspr/pr/src/md/unix/aix.c](#nsprprsrcmdunixaixc)
 - [nspr/pr/src/md/unix/irix.c](#nsprprsrcmdunixirixc)
 - [nspr/pr/src/md/unix/uxproces.c](#nsprprsrcmdunixuxprocesc)

### nspr/configure.in

```

{% raw %}
2520 |     AC_CHECK_LIB(dl, dlopen,
{% endraw %}

```
### nspr/pr/src/linking/prlink.c

```cpp

{% raw %}
167 | #if defined(USE_DLFCN) && !defined(NO_DLOPEN_NULL)
168 |     h = dlopen(0, RTLD_LAZY);
183 | #elif defined(USE_MACH_DYLD) || defined(NO_DLOPEN_NULL)
795 |     /* DARWIN's dlopen ignores the provided path and checks for the */
799 |             h = dlopen(name, dl_flags);
802 |     h = dlopen(name, dl_flags);
811 |      * dlopen().
{% endraw %}

```
### nspr/pr/src/malloc/prmem.c

```cpp

{% raw %}
87 | #if defined(USE_DLFCN) && !defined(NO_DLOPEN_NULL)
97 |     h = dlopen(0, RTLD_LAZY);
120 | #elif defined(USE_MACH_DYLD) || defined(NO_DLOPEN_NULL)
{% endraw %}

```
### nspr/pr/src/pthreads/ptio.c

```cpp

{% raw %}
42 | #include <dlfcn.h>  /* for dlopen */
64 | #include <dlfcn.h>  /* for dlopen */
2106 |     void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
2496 |     handle = dlopen("libsendfile.so", RTLD_LAZY | RTLD_GLOBAL);
2498 |         ("dlopen(libsendfile.so) returns %p", handle));
2502 |          * The dlopen(0, mode) call is to allow for the possibility that
2506 |         handle = dlopen(0, RTLD_LAZY | RTLD_GLOBAL);
2508 |             ("dlopen(0) returns %p", handle));
{% endraw %}

```
### nspr/pr/src/md/unix/aix.c

```cpp

{% raw %}
77 |     main_app_handle = dlopen(NULL, RTLD_NOW);
175 |  * On AIX 4.2, we use dlopen("/unix", RTLD_NOW) and dlsym() to get
195 | 	aix_handle = dlopen("/unix", RTLD_NOW);
218 | 	aix_handle = dlopen("/unix", RTLD_NOW);
{% endraw %}

```
### nspr/pr/src/md/unix/irix.c

```cpp

{% raw %}
997 | 				libc_handle = dlopen("libc.so",RTLD_NOW);
1506 | 	libc_handle = dlopen("libc.so",RTLD_NOW);
{% endraw %}

```
### nspr/pr/src/md/unix/uxproces.c

```cpp

{% raw %}
14 | #include <dlfcn.h>  /* For dlopen, dlsym, dlclose */
716 |         void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```