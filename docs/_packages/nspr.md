---
name: "nspr"
layout: package
next_package: libatomic-ops
previous_package: llvm-openmp
languages: ['c']
---
## 4.13.1
7 / 635 files match, 6 filtered matches.

 - [nspr/pr/src/linking/prlink.c](#nsprprsrclinkingprlinkc)
 - [nspr/pr/src/malloc/prmem.c](#nsprprsrcmallocprmemc)
 - [nspr/pr/src/pthreads/ptio.c](#nsprprsrcpthreadsptioc)
 - [nspr/pr/src/md/unix/aix.c](#nsprprsrcmdunixaixc)
 - [nspr/pr/src/md/unix/irix.c](#nsprprsrcmdunixirixc)
 - [nspr/pr/src/md/unix/uxproces.c](#nsprprsrcmdunixuxprocesc)

### nspr/pr/src/linking/prlink.c

```c

{% raw %}
168 |     h = dlopen(0, RTLD_LAZY);
799 |             h = dlopen(name, dl_flags);
802 |     h = dlopen(name, dl_flags);
{% endraw %}

```
### nspr/pr/src/malloc/prmem.c

```c

{% raw %}
97 |     h = dlopen(0, RTLD_LAZY);
{% endraw %}

```
### nspr/pr/src/pthreads/ptio.c

```c

{% raw %}
2106 |     void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
2496 |     handle = dlopen("libsendfile.so", RTLD_LAZY | RTLD_GLOBAL);
2498 |         ("dlopen(libsendfile.so) returns %p", handle));
2506 |         handle = dlopen(0, RTLD_LAZY | RTLD_GLOBAL);
2508 |             ("dlopen(0) returns %p", handle));
{% endraw %}

```
### nspr/pr/src/md/unix/aix.c

```c

{% raw %}
77 |     main_app_handle = dlopen(NULL, RTLD_NOW);
195 | 	aix_handle = dlopen("/unix", RTLD_NOW);
218 | 	aix_handle = dlopen("/unix", RTLD_NOW);
{% endraw %}

```
### nspr/pr/src/md/unix/irix.c

```c

{% raw %}
997 | 				libc_handle = dlopen("libc.so",RTLD_NOW);
1506 | 	libc_handle = dlopen("libc.so",RTLD_NOW);
{% endraw %}

```
### nspr/pr/src/md/unix/uxproces.c

```c

{% raw %}
716 |         void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```