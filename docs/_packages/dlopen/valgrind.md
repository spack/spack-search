---
name: "valgrind"
layout: package
next_package: vim
previous_package: unixodbc
library_name: dlopen
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## 3.14.0
26 / 5760 files match, 7 filtered matches.

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
1357 | #define DT_MIPS_RLD_TEXT_RESOLVE_ADDR 0x7000002d /* Address of rld_text_rsolve
1358 | 						    function stored in GOT.  */
1359 | #define DT_MIPS_PERF_SUFFIX  0x7000002e /* Default suffix of dso to be added
1360 | 					   by rld on dlopen() calls.  */
1361 | #define DT_MIPS_COMPACT_SIZE 0x7000002f /* (O32)Size of compact rel section. */
1362 | #define DT_MIPS_GP_VALUE     0x70000030 /* GP value for aux GOTs.  */
6581 | #define RTLD_DEFAULT    NULL
6582 | 
6583 | /* dummy function for profiling */
6584 | void *dlopen(const char *filename, int flag)
6585 | {
6586 |     return NULL;
{% endraw %}

```
### cachegrind/tests/dlclose.c

```c

{% raw %}
15 |    void (*myprint)(void);
16 |    char *error;
17 | 
18 |    handle = dlopen ("./myprint.so", RTLD_LAZY);
19 |    if (!handle) {
20 |        fputs (dlerror(), stderr);
{% endraw %}

```
### memcheck/tests/linux/dlclose_leak.c

```c

{% raw %}
14 |     {
15 |         char* memToLeak;
16 |         char x __attribute__((unused));
17 |         void* handle = dlopen("./dlclose_leak_so.so", RTLD_NOW);
18 |         if(!handle) {
19 |             printf("FAILURE to dlopen dlclose_leak_so.so\n");
20 |             return EXIT_FAILURE;
21 |         }
{% endraw %}

```
### exp-sgcheck/tests/preen_invars_so.c

```c

{% raw %}
1 | /* This file contains a global array.  It is compiled into a .so,
2 |    which is dlopened by preen_invar.c.  That then accesses the global
3 |    array, hence generating Inv_Global invariants in sg_main.c.
4 | 
{% endraw %}

```
### exp-sgcheck/tests/preen_invars.c

```c

{% raw %}
9 | {
10 |   int i, r, sum = 0;
11 |   char* im_a_global_array;
12 |   void* hdl = dlopen("./preen_invars_so.so", RTLD_NOW);
13 |   assert(hdl);
14 |   im_a_global_array = dlsym(hdl, "im_a_global_array");
{% endraw %}

```
### drd/tests/dlopen_main.c

```c

{% raw %}
9 |   void (*function)();
10 |   const char *error;
11 | 
12 |   handle = dlopen(lib, RTLD_NOW);
13 |   if (!handle) {
14 |     fputs (dlerror(), stderr);
{% endraw %}

```
### none/tests/solaris/mmap_noreserve.c

```c

{% raw %}
23 |    }
24 | }
25 | 
26 | static void *do_dlopen(const char *pathname)
27 | {
28 |    int mode = RTLD_LAZY | RTLD_LOCAL;
29 |    void *handle = dlopen(pathname, mode);
30 |    if (handle == NULL) {
31 |       fprintf(stderr, "dlopen failed for %s: %s",
32 |               pathname, dlerror());
33 |       exit(1);
39 | int main(int argc, const char *argv[])
40 | {
41 |    do_map(MAP_NORESERVE);
42 |    do_dlopen("libm.so");
43 |    do_map(0);
44 |    do_map(0);
45 |    do_map(MAP_NORESERVE);
46 |    do_dlopen("liby.so");
47 |    do_map(MAP_NORESERVE);
48 |    do_map(0);
49 |    do_map(0);
50 |    do_map(MAP_NORESERVE);
51 |    do_map(MAP_NORESERVE);
52 |    do_dlopen("libz.so");
53 |    do_map(MAP_NORESERVE);
54 |    do_map(MAP_NORESERVE);
64 |       do_map(MAP_NORESERVE);
65 |       do_map(0);
66 |       do_map(0);
67 |       do_dlopen("libw.so");
68 |       do_map(0);
69 |       do_map(MAP_NORESERVE);
{% endraw %}

```