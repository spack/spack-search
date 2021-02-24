---
name: "valgrind"
layout: package
next_package: rocfft
previous_package: mc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.14.0
11 / 5760 files match, 5 filtered matches.

 - [perf/tinycc.c](#perftinyccc)
 - [cachegrind/tests/dlclose.c](#cachegrindtestsdlclosec)
 - [memcheck/tests/linux/dlclose_leak.c](#memchecktestslinuxdlclose_leakc)
 - [exp-sgcheck/tests/preen_invars.c](#exp-sgchecktestspreen_invarsc)
 - [drd/tests/dlopen_main.c](#drdtestsdlopen_mainc)

### perf/tinycc.c

```c

{% raw %}
6628 | void *resolve_sym(TCCState *s1, const char *sym, int type)
6629 | {
6630 |   assert(0);
6631 |   return 0; //dlsym(RTLD_DEFAULT, sym);
6632 |   // jrs: remove need for dlsym
6633 | }
{% endraw %}

```
### cachegrind/tests/dlclose.c

```c

{% raw %}
21 |        exit(1);
22 |    }
23 | 
24 |    myprint = dlsym(handle, "myprint");
25 |    if ((error = dlerror()) != NULL)  {
26 |        fprintf (stderr, "%s\n", error);
{% endraw %}

```
### memcheck/tests/linux/dlclose_leak.c

```c

{% raw %}
19 |             printf("FAILURE to dlopen dlclose_leak_so.so\n");
20 |             return EXIT_FAILURE;
21 |         }
22 |         jmp_on_uninit = dlsym(handle,"jmp_on_uninit");
23 |         //fprintf(stderr, "jmp_on_uninit: %p\n", jmp_on_uninit);
24 |         assert(jmp_on_uninit);
25 |         alloc_1_byte = dlsym(handle,"alloc_1_byte");
26 |         //fprintf(stderr, "alloc_1_byte: %p\n", alloc_1_byte);
27 |         assert(alloc_1_byte);
{% endraw %}

```
### exp-sgcheck/tests/preen_invars.c

```c

{% raw %}
11 |   char* im_a_global_array;
12 |   void* hdl = dlopen("./preen_invars_so.so", RTLD_NOW);
13 |   assert(hdl);
14 |   im_a_global_array = dlsym(hdl, "im_a_global_array");
15 |   assert(im_a_global_array);
16 |   /* printf("%p %p\n", im_a_global_array, me_too_me_too); */
{% endraw %}

```
### drd/tests/dlopen_main.c

```c

{% raw %}
15 |     exit(1);
16 |   }
17 | 
18 |   function = dlsym(handle, "foo");
19 |   error = dlerror();
20 |   if (error)  {
{% endraw %}

```