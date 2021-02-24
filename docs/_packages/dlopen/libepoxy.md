---
name: "libepoxy"
layout: package
next_package: xdm
previous_package: tulip
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.4.3
9 / 82 files match, 4 filtered matches.

 - [src/dispatch_common.c](#srcdispatch_commonc)
 - [test/dlwrap.h](#testdlwraph)
 - [test/egl_without_glx.c](#testegl_without_glxc)
 - [test/dlwrap.c](#testdlwrapc)

### src/dispatch_common.c

```c

{% raw %}
282 | }
283 | 
284 | static bool
285 | get_dlopen_handle(void **handle, const char *lib_name, bool exit_on_fail)
286 | {
287 |     if (*handle)
289 | 
290 |     if (!library_initialized) {
291 |         fprintf(stderr,
292 |                 "Attempting to dlopen() while in the dynamic linker.\n");
293 |         abort();
294 |     }
321 |     void *result;
322 |     const char *error = "";
323 | 
324 |     if (!get_dlopen_handle(handle, lib_name, exit_on_fail))
325 |         return NULL;
326 | 
727 |      * non-X11 ES2 context from loading a bunch of X11 junk).
728 |      */
729 | #if PLATFORM_HAS_EGL
730 |     get_dlopen_handle(&api.egl_handle, EGL_LIB, false);
731 |     if (api.egl_handle) {
732 |         switch (epoxy_egl_get_current_gl_context_api()) {
738 |              * us.  Try the GLES2 implementation first, and fall back
739 |              * to GLES1 otherwise.
740 |              */
741 |             get_dlopen_handle(&api.gles2_handle, GLES2_LIB, false);
742 |             if (api.gles2_handle)
743 |                 return epoxy_gles2_dlsym(name);
{% endraw %}

```
### test/dlwrap.h

```c

{% raw %}
30 |  * thing to call is dlwrap_real_dlopen.
31 |  */
32 | void *
33 | dlwrap_real_dlopen(const char *filename, int flag);
34 | 
35 | /* Perform a dlopen on the libfips library itself.
42 |  * The returned handle can be passed to dlwrap_real_dlsym for the
43 |  * lookups. */
44 | void *
45 | dlwrap_dlopen_libfips(void);
46 | 
47 | /* Call the *real* dlsym. We have our own wrapper for dlsym that, of
54 | 
55 | #define DEFER_TO_GL(library, func, name, args)                          \
56 | ({                                                                      \
57 |     void *lib = dlwrap_real_dlopen(library, RTLD_LAZY | RTLD_LOCAL);    \
58 |     typeof(&func) real_func = dlwrap_real_dlsym(lib, name);             \
59 |     /* gcc extension -- func's return value is the return value of      \
{% endraw %}

```
### test/egl_without_glx.c

```c

{% raw %}
49 |  * system.
50 |  */
51 | void *
52 | dlopen(const char *filename, int flag)
53 | {
54 |     void * (*dlopen_unwrapped)(const char *filename, int flag);
55 | 
56 |     if (!strcmp(filename, "libGL.so.1"))
63 |         return NULL;
64 | #endif
65 | 
66 |     dlopen_unwrapped = dlsym(RTLD_NEXT, "dlopen");
67 |     assert(dlopen_unwrapped);
68 | 
69 |     return dlopen_unwrapped(filename, flag);
70 | }
71 | 
80 | static EGLBoolean
81 | override_eglBindAPI(EGLenum api)
82 | {
83 |     void *egl = dlopen("libEGL.so.1", RTLD_LAZY | RTLD_LOCAL);
84 |     EGLBoolean (*real_eglBindAPI)(EGLenum api) = dlsym(egl, "eglBindAPI");
85 | 
101 | static EGLint
102 | override_eglGetError(void)
103 | {
104 |     void *egl = dlopen("libEGL.so.1", RTLD_LAZY | RTLD_LOCAL);
105 |     EGLint (*real_eglGetError)(void) = dlsym(egl, "eglGetError");
106 | 
{% endraw %}

```
### test/dlwrap.c

```c

{% raw %}
50 | 
51 | void *libfips_handle;
52 | 
53 | typedef void *(*fips_dlopen_t)(const char *filename, int flag);
54 | typedef void *(*fips_dlsym_t)(void *handle, const char *symbol);
55 | 
97 |  * wrapper here and redirect it to our library.
98 |  */
99 | void *
100 | dlopen(const char *filename, int flag)
101 | {
102 |     void *ret;
107 |      * expected side-effects from loading the intended library are
108 |      * resolved. Below, we may still return a handle pointing to
109 |      * our own library, and not what is opened here. */
110 |     ret = dlwrap_real_dlopen(filename, flag);
111 | 
112 |     /* If filename is not a wrapped library, just return real dlopen */
136 | }
137 | 
138 | void *
139 | dlwrap_real_dlopen(const char *filename, int flag)
140 | {
141 |     static fips_dlopen_t real_dlopen = NULL;
142 | 
143 |     if (!real_dlopen) {
144 |         real_dlopen = (fips_dlopen_t) dlwrap_real_dlsym(RTLD_NEXT, "dlopen");
145 |         if (!real_dlopen) {
146 |             fprintf(stderr, "Error: Failed to find symbol for dlopen.\n");
147 |             exit(1);
148 |         }
149 |     }
150 | 
151 |     return real_dlopen(filename, flag);
152 | }
153 | 
{% endraw %}

```