---
name: "dmtcp"
layout: package
next_package: dpdk
previous_package: dealii
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
367 | void *_real_dlopen(const char *filename, int flag) {
368 |   REAL_FUNC_PASSTHROUGH_TYPED (void*, dlopen) (filename, flag);
{% endraw %}

```
### src/syscallwrappers.h

```c

{% raw %}
107 | LIB_PRIVATE extern __thread int thread_performing_dlopen_dlsym;
121 |   MACRO(dlopen)                             \
411 |   void *_real_dlopen(const char *filename, int flag);
{% endraw %}

```
### include/trampolines.h

```c

{% raw %}
112 |   void *handle = dlopen(LIBC_FILENAME, RTLD_NOW);
114 |     fprintf(stderr, "*** %s:%d DMTCP Internal Error: dlopen() failed.\n",
{% endraw %}

```
### test/dlopen1.c

```c

{% raw %}
27 |       handle = dlopen("libdlopen-lib1.so", RTLD_NOW);
29 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
37 |       handle = dlopen("libdlopen-lib2.so", RTLD_LAZY);
39 |         fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### test/autotest.py

```python

{% raw %}
899 | runTest("dlopen1",        1, ["./test/dlopen1"])
{% endraw %}

```
### test/plugin/sleep2/sleep2.c

```c

{% raw %}
24 |     handle = dlopen("libc.so.6", RTLD_NOW);
{% endraw %}

```
### contrib/infiniband/infinibandwrappers.c

```c

{% raw %}
14 | void *dlopen(const char *filename, int flag) {
17 |       void *handle = NEXT_FNC(dlopen)("libdmtcp_infiniband.so", flag);
28 |   return NEXT_FNC(dlopen)(filename, flag);
{% endraw %}

```