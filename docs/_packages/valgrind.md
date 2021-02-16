---
name: "valgrind"
layout: package
next_package: libpciaccess
previous_package: libidn2
languages: ['c']
---
## 3.14.0
26 / 5760 files match

 - [perf/tinycc.c](#perftinyccc)
 - [cachegrind/tests/dlclose.c](#cachegrindtestsdlclosec)
 - [memcheck/tests/linux/dlclose_leak.c](#memchecktestslinuxdlclose_leakc)
 - [exp-sgcheck/tests/preen_invars_so.c](#exp-sgchecktestspreen_invars_soc)
 - [exp-sgcheck/tests/preen_invars.c](#exp-sgchecktestspreen_invarsc)
 - [drd/tests/dlopen_main.c](#drdtestsdlopen_mainc)
 - [none/tests/solaris/mmap_noreserve.c](#nonetestssolarismmap_noreservec)

### perf/tinycc.c

```c

{% raw %}
1360 | 					   by rld on dlopen() calls.  */
6584 | void *dlopen(const char *filename, int flag)
{% endraw %}

```
### cachegrind/tests/dlclose.c

```c

{% raw %}
18 |    handle = dlopen ("./myprint.so", RTLD_LAZY);
{% endraw %}

```
### memcheck/tests/linux/dlclose_leak.c

```c

{% raw %}
17 |         void* handle = dlopen("./dlclose_leak_so.so", RTLD_NOW);
19 |             printf("FAILURE to dlopen dlclose_leak_so.so\n");
{% endraw %}

```
### exp-sgcheck/tests/preen_invars_so.c

```c

{% raw %}
2 |    which is dlopened by preen_invar.c.  That then accesses the global
{% endraw %}

```
### exp-sgcheck/tests/preen_invars.c

```c

{% raw %}
12 |   void* hdl = dlopen("./preen_invars_so.so", RTLD_NOW);
{% endraw %}

```
### drd/tests/dlopen_main.c

```c

{% raw %}
12 |   handle = dlopen(lib, RTLD_NOW);
{% endraw %}

```
### none/tests/solaris/mmap_noreserve.c

```c

{% raw %}
26 | static void *do_dlopen(const char *pathname)
29 |    void *handle = dlopen(pathname, mode);
31 |       fprintf(stderr, "dlopen failed for %s: %s",
42 |    do_dlopen("libm.so");
46 |    do_dlopen("liby.so");
52 |    do_dlopen("libz.so");
67 |       do_dlopen("libw.so");
{% endraw %}

```