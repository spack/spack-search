---
name: "libepoxy"
layout: package
next_package: xts
previous_package: eccodes
languages: ['c']
---
## 1.4.3
9 / 82 files match

 - [src/dispatch_common.c](#srcdispatch_commonc)
 - [test/dlwrap.h](#testdlwraph)
 - [test/egl_without_glx.c](#testegl_without_glxc)
 - [test/dlwrap.c](#testdlwrapc)

### src/dispatch_common.c

```c

{% raw %}
285 | get_dlopen_handle(void **handle, const char *lib_name, bool exit_on_fail)
292 |                 "Attempting to dlopen() while in the dynamic linker.\n");
324 |     if (!get_dlopen_handle(handle, lib_name, exit_on_fail))
730 |     get_dlopen_handle(&api.egl_handle, EGL_LIB, false);
741 |             get_dlopen_handle(&api.gles2_handle, GLES2_LIB, false);
{% endraw %}

```
### test/dlwrap.h

```c

{% raw %}
33 | dlwrap_real_dlopen(const char *filename, int flag);
45 | dlwrap_dlopen_libfips(void);
57 |     void *lib = dlwrap_real_dlopen(library, RTLD_LAZY | RTLD_LOCAL);    \
{% endraw %}

```
### test/egl_without_glx.c

```c

{% raw %}
52 | dlopen(const char *filename, int flag)
54 |     void * (*dlopen_unwrapped)(const char *filename, int flag);
66 |     dlopen_unwrapped = dlsym(RTLD_NEXT, "dlopen");
67 |     assert(dlopen_unwrapped);
69 |     return dlopen_unwrapped(filename, flag);
83 |     void *egl = dlopen("libEGL.so.1", RTLD_LAZY | RTLD_LOCAL);
104 |     void *egl = dlopen("libEGL.so.1", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### test/dlwrap.c

```c

{% raw %}
53 | typedef void *(*fips_dlopen_t)(const char *filename, int flag);
100 | dlopen(const char *filename, int flag)
110 |     ret = dlwrap_real_dlopen(filename, flag);
139 | dlwrap_real_dlopen(const char *filename, int flag)
141 |     static fips_dlopen_t real_dlopen = NULL;
143 |     if (!real_dlopen) {
144 |         real_dlopen = (fips_dlopen_t) dlwrap_real_dlsym(RTLD_NEXT, "dlopen");
145 |         if (!real_dlopen) {
146 |             fprintf(stderr, "Error: Failed to find symbol for dlopen.\n");
151 |     return real_dlopen(filename, flag);
{% endraw %}

```