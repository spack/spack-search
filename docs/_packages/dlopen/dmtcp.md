---
name: "dmtcp"
layout: package
next_package: dotconf
previous_package: dimemas
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['python', 'c']
---
## 2.5.2
23 / 648 files match, 7 filtered matches.

 - [src/syscallsreal.c](#srcsyscallsrealc)
 - [src/syscallwrappers.h](#srcsyscallwrappersh)
 - [include/trampolines.h](#includetrampolinesh)
 - [test/dlopen1.c](#testdlopen1c)
 - [test/autotest.py](#testautotestpy)
 - [test/plugin/sleep2/sleep2.c](#testpluginsleep2sleep2c)
 - [contrib/infiniband/infinibandwrappers.c](#contribinfinibandinfinibandwrappersc)

### src/syscallsreal.c

```c

{% raw %}
364 | }
365 | 
366 | LIB_PRIVATE
367 | void *_real_dlopen(const char *filename, int flag) {
368 |   REAL_FUNC_PASSTHROUGH_TYPED (void*, dlopen) (filename, flag);
369 | }
370 | 
{% endraw %}

```
### src/syscallwrappers.h

```c

{% raw %}
104 | 
105 | extern int dmtcp_wrappers_initializing;
106 | 
107 | LIB_PRIVATE extern __thread int thread_performing_dlopen_dlsym;
108 | 
109 | #define FOREACH_GLIBC_MALLOC_FAMILY_WRAPPERS(MACRO)\
118 |   MACRO(munmap)
119 | 
120 | #define FOREACH_GLIBC_WRAPPERS(MACRO)       \
121 |   MACRO(dlopen)                             \
122 |   MACRO(dlclose)                            \
123 |   MACRO(getpid)                             \
408 |   ssize_t _real_readlink(const char *path, char *buf, size_t bufsiz);
409 |   void * _real_dlsym (void *handle, const char *symbol);
410 | 
411 |   void *_real_dlopen(const char *filename, int flag);
412 |   int _real_dlclose(void *handle);
413 | 
{% endraw %}

```
### include/trampolines.h

```c

{% raw %}
109 | {
110 |   /* Find libc func
111 |      We assume that no one is wrapping func yet. */
112 |   void *handle = dlopen(LIBC_FILENAME, RTLD_NOW);
113 |   if (handle == NULL) {
114 |     fprintf(stderr, "*** %s:%d DMTCP Internal Error: dlopen() failed.\n",
115 |             __FILE__, __LINE__);
116 |     abort();
{% endraw %}

```
### test/dlopen1.c

```c

{% raw %}
24 |       dlclose(handle);
25 | 
26 |     if (lib == 1) {
27 |       handle = dlopen("libdlopen-lib1.so", RTLD_NOW);
28 |       if (handle == NULL) {
29 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
30 |         exit(1);
31 |       }
34 |     }
35 | 
36 |     if (lib == 2) {
37 |       handle = dlopen("libdlopen-lib2.so", RTLD_LAZY);
38 |       if (handle == NULL) {
39 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
40 |         exit(1);
41 |       }
{% endraw %}

```
### test/autotest.py

```python

{% raw %}
896 |                                    "/test:" + os.getenv("PWD")
897 | else:
898 |   os.environ['LD_LIBRARY_PATH'] = os.getenv("PWD") + "/test:" + os.getenv("PWD")
899 | runTest("dlopen1",        1, ["./test/dlopen1"])
900 | # Disable the dlopen2 test until we can figure out a way to handle calls to
901 | # fork/exec/wait during library intialization with dlopen().
{% endraw %}

```
### test/plugin/sleep2/sleep2.c

```c

{% raw %}
21 |   static void *handle = NULL;
22 | 
23 |   if (! handle)
24 |     handle = dlopen("libc.so.6", RTLD_NOW);
25 |   if (! real_fnc)
26 |     real_fnc = (__typeof__(real_fnc)) dlsym(handle, "sleep");
{% endraw %}

```
### contrib/infiniband/infinibandwrappers.c

```c

{% raw %}
11 | #include "debug.h"
12 | #include <infiniband/verbs.h>
13 | 
14 | void *dlopen(const char *filename, int flag) {
15 |   if (filename) {
16 |     if (strstr(filename, "libibverbs.so")) {
17 |       void *handle = NEXT_FNC(dlopen)("libdmtcp_infiniband.so", flag);
18 |       if (handle == NULL) {
19 |         fprintf(stderr,
25 |       return handle;
26 |     }
27 |   }
28 |   return NEXT_FNC(dlopen)(filename, flag);
29 | }
30 | 
{% endraw %}

```