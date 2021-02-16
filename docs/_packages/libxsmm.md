---
name: "libxsmm"
layout: package
next_package: otf2
previous_package: llvm-amdgpu
languages: ['c']
---
## 1.16.1
1 / 875 files match

 - [src/libxsmm_malloc.c](#srclibxsmm_mallocc)

### src/libxsmm_malloc.c

```c

{% raw %}
1140 |   handle_qkmalloc = dlopen("libqkmalloc.so", RTLD_LAZY);
1211 |       handle_libc = dlopen("libc.so." LIBXSMM_STRINGIFY(LIBXSMM_MALLOC_GLIBC), RTLD_LAZY);
{% endraw %}

```