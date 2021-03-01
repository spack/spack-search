---
name: "libxsmm"
layout: package
next_package: libyogrt
previous_package: libuv
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.6.6
1 / 301 files match, 1 filtered matches.

 - [src/libxsmm_gemm.h](#srclibxsmm_gemmh)

### src/libxsmm_gemm.h

```c

{% raw %}
325 |     if (0 == (ORIGINAL)) { \
326 |       union { const void* pv; LIBXSMM_GEMMFUNCTION_TYPE(TYPE) pf; } libxsmm_gemm_wrapper_dynamic_ = { 0 }; \
327 |       dlerror(); /* clear an eventual error status */ \
328 |       libxsmm_gemm_wrapper_dynamic_.pv = dlsym(RTLD_NEXT, LIBXSMM_STRINGIFY(LIBXSMM_FSYMBOL(LIBXSMM_TPREFIX(TYPE, gemm)))); \
329 |       if (libxsmm_gemm_wrapper_dynamic_.pv != (CALLER)) ORIGINAL = libxsmm_gemm_wrapper_dynamic_.pf; \
330 |       LIBXSMM_GEMM_WRAPPER_BLAS(TYPE, ORIGINAL, CALLER, LIBXSMM_FSYMBOL(LIBXSMM_TPREFIX(TYPE, gemm))); \
{% endraw %}

```