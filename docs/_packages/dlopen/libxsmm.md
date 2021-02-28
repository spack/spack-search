---
name: "libxsmm"
layout: package
next_package: ace
previous_package: gmake
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.16.1
1 / 875 files match, 1 filtered matches.

 - [src/libxsmm_malloc.c](#srclibxsmm_mallocc)

### src/libxsmm_malloc.c

```c

{% raw %}
1137 | # if defined(LIBXSMM_MALLOC_HOOK_QKMALLOC)
1138 |   void* handle_qkmalloc = NULL;
1139 |   dlerror(); /* clear an eventual error status */
1140 |   handle_qkmalloc = dlopen("libqkmalloc.so", RTLD_LAZY);
1141 |   if (NULL != handle_qkmalloc) {
1142 |     libxsmm_malloc_fn.memalign.ptr = internal_memalign_malloc;
1208 |     if (NULL == libxsmm_malloc_fn.free.ptr) {
1209 |       void* handle_libc = NULL;
1210 |       dlerror(); /* clear an eventual error status */
1211 |       handle_libc = dlopen("libc.so." LIBXSMM_STRINGIFY(LIBXSMM_MALLOC_GLIBC), RTLD_LAZY);
1212 |       if (NULL != handle_libc) {
1213 |         libxsmm_malloc_fn.memalign.dlsym = dlsym(handle_libc, "__libc_memalign");
{% endraw %}

```