---
name: "verrou"
layout: package
next_package: vim
previous_package: veclibfort
languages: ['c']
---
## 2.0.0
21 / 5652 files match, 6 filtered matches.

 - [valgrind-3.13.0/perf/tinycc.c](#valgrind-3130perftinyccc)
 - [valgrind-3.13.0/cachegrind/tests/dlclose.c](#valgrind-3130cachegrindtestsdlclosec)
 - [valgrind-3.13.0/exp-sgcheck/tests/preen_invars_so.c](#valgrind-3130exp-sgchecktestspreen_invars_soc)
 - [valgrind-3.13.0/exp-sgcheck/tests/preen_invars.c](#valgrind-3130exp-sgchecktestspreen_invarsc)
 - [valgrind-3.13.0/drd/tests/dlopen_main.c](#valgrind-3130drdtestsdlopen_mainc)
 - [valgrind-3.13.0/none/tests/solaris/mmap_noreserve.c](#valgrind-3130nonetestssolarismmap_noreservec)

### valgrind-3.13.0/perf/tinycc.c

```c

{% raw %}
1360 | 					   by rld on dlopen() calls.  */
6584 | void *dlopen(const char *filename, int flag)
{% endraw %}

```
### valgrind-3.13.0/cachegrind/tests/dlclose.c

```c

{% raw %}
18 |    handle = dlopen ("./myprint.so", RTLD_LAZY);
{% endraw %}

```
### valgrind-3.13.0/exp-sgcheck/tests/preen_invars_so.c

```c

{% raw %}
2 |    which is dlopened by preen_invar.c.  That then accesses the global
{% endraw %}

```
### valgrind-3.13.0/exp-sgcheck/tests/preen_invars.c

```c

{% raw %}
12 |   void* hdl = dlopen("./preen_invars_so.so", RTLD_NOW);
{% endraw %}

```
### valgrind-3.13.0/drd/tests/dlopen_main.c

```c

{% raw %}
12 |   handle = dlopen(lib, RTLD_NOW);
{% endraw %}

```
### valgrind-3.13.0/none/tests/solaris/mmap_noreserve.c

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