---
name: "memkind"
layout: package
next_package: nettle
previous_package: dpdk
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.9.0
7 / 482 files match, 2 filtered matches.

 - [src/tbb_wrapper.c](#srctbb_wrapperc)
 - [test/load_tbbmalloc_symbols.c](#testload_tbbmalloc_symbolsc)

### src/tbb_wrapper.c

```c

{% raw %}
51 | void load_tbb_symbols(void)
52 | {
53 |     const char so_name[]="libtbbmalloc.so.2";
54 |     tbb_handle = dlopen(so_name, RTLD_LAZY);
55 |     if(!tbb_handle) {
56 |         log_fatal("%s not found.", so_name);
{% endraw %}

```
### test/load_tbbmalloc_symbols.c

```c

{% raw %}
26 | int load_tbbmalloc_symbols()
27 | {
28 |     const char so_name[]="libtbbmalloc.so.2";
29 |     void *tbb_handle = dlopen(so_name, RTLD_LAZY);
30 |     if(!tbb_handle) {
31 |         printf("Cannot load %s\n", so_name);
{% endraw %}

```