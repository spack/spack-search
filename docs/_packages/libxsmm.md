---
name: "libxsmm"
layout: package
next_package: libyogrt
previous_package: libxslt
languages: ['c']
---
## 1.16.1
1 / 875 files match, 1 filtered matches.

 - [src/libxsmm_malloc.c](#srclibxsmm_mallocc)

### src/libxsmm_malloc.c

```c

{% raw %}
1140 |   handle_qkmalloc = dlopen("libqkmalloc.so", RTLD_LAZY);
1211 |       handle_libc = dlopen("libc.so." LIBXSMM_STRINGIFY(LIBXSMM_MALLOC_GLIBC), RTLD_LAZY);
{% endraw %}

```