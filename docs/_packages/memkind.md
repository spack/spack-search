---
name: "memkind"
layout: package
next_package: mount-point-attributes
previous_package: gosam-contrib
languages: ['c']
---
## 1.9.0
7 / 482 files match

 - [src/tbb_wrapper.c](#srctbb_wrapperc)
 - [test/load_tbbmalloc_symbols.c](#testload_tbbmalloc_symbolsc)

### src/tbb_wrapper.c

```c

{% raw %}
54 |     tbb_handle = dlopen(so_name, RTLD_LAZY);
{% endraw %}

```
### test/load_tbbmalloc_symbols.c

```c

{% raw %}
29 |     void *tbb_handle = dlopen(so_name, RTLD_LAZY);
{% endraw %}

```