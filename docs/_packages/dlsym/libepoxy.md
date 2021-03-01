---
name: "libepoxy"
layout: package
next_package: libfabric
previous_package: libcanberra
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['python', 'c']
---
## 1.4.3
16 / 82 files match, 13 filtered matches.

 - [src/dispatch_glx.c](#srcdispatch_glxc)
 - [src/egl_generated_dispatch.c](#srcegl_generated_dispatchc)
 - [src/dispatch_common.h](#srcdispatch_commonh)
 - [src/dispatch_common.c](#srcdispatch_commonc)
 - [src/glx_generated_dispatch.c](#srcglx_generated_dispatchc)
 - [src/dispatch_egl.c](#srcdispatch_eglc)
 - [src/gl_generated_dispatch.c](#srcgl_generated_dispatchc)
 - [src/wgl_generated_dispatch.c](#srcwgl_generated_dispatchc)
 - [src/gen_dispatch.py](#srcgen_dispatchpy)
 - [test/glx_static.c](#testglx_staticc)
 - [test/dlwrap.h](#testdlwraph)
 - [test/egl_without_glx.c](#testegl_without_glxc)
 - [test/dlwrap.c](#testdlwrapc)

### src/dispatch_glx.c

```c

{% raw %}
160 |     Bool (* pf_glXQueryExtension) (Display *, int *, int *);
161 |     int error_base, event_base;
162 | 
163 |     pf_glXQueryExtension = epoxy_conservative_glx_dlsym("glXQueryExtension", false);
164 |     if (pf_glXQueryExtension && pf_glXQueryExtension(dpy, &error_base, &event_base))
165 |         return true;
{% endraw %}

```
### src/egl_generated_dispatch.c

```c

{% raw %}
3337 |         switch (providers[i]) {
3338 |         case EGL_10:
3339 |             if (true)
3340 |                 return epoxy_egl_dlsym(entrypoint_strings + entrypoints[i]);
3341 |             break;
3342 |         case EGL_11:
3343 |             if (epoxy_conservative_egl_version() >= 11)
3344 |                 return epoxy_egl_dlsym(entrypoint_strings + entrypoints[i]);
3345 |             break;
3346 |         case EGL_12:
3347 |             if (epoxy_conservative_egl_version() >= 12)
3348 |                 return epoxy_egl_dlsym(entrypoint_strings + entrypoints[i]);
3349 |             break;
3350 |         case EGL_14:
3351 |             if (epoxy_conservative_egl_version() >= 14)
3352 |                 return epoxy_egl_dlsym(entrypoint_strings + entrypoints[i]);
3353 |             break;
3354 |         case EGL_15:
3355 |             if (epoxy_conservative_egl_version() >= 15)
3356 |                 return epoxy_egl_dlsym(entrypoint_strings + entrypoints[i]);
3357 |             break;
3358 |         case EGL_extension_EGL_ANDROID_blob_cache:
{% endraw %}

```
### src/dispatch_common.h

```c

{% raw %}
144 |     GEN_DISPATCH_TABLE_REWRITE_PTR_RET(ret, name, args, passthrough) \
145 |     GEN_DISPATCH_TABLE_THUNK_RET(ret, name, args, passthrough)
146 | 
147 | void *epoxy_egl_dlsym(const char *name);
148 | void *epoxy_glx_dlsym(const char *name);
149 | void *epoxy_gl_dlsym(const char *name);
150 | void *epoxy_gles1_dlsym(const char *name);
151 | void *epoxy_gles2_dlsym(const char *name);
152 | void *epoxy_gles3_dlsym(const char *name);
153 | void *epoxy_get_proc_address(const char *name);
154 | void *epoxy_get_core_proc_address(const char *name, int core_version);
161 | int epoxy_conservative_egl_version(void);
162 | bool epoxy_conservative_has_egl_extension(const char *name);
163 | bool epoxy_conservative_has_wgl_extension(const char *name);
164 | void *epoxy_conservative_egl_dlsym(const char *name, bool exit_if_fails);
165 | void *epoxy_conservative_glx_dlsym(const char *name, bool exit_if_fails);
166 | 
167 | bool epoxy_extension_in_string(const char *extension_list, const char *ext);
{% endraw %}

```
### src/dispatch_common.c

```c

{% raw %}
315 | }
316 | 
317 | static void *
318 | do_dlsym(void **handle, const char *lib_name, const char *name,
319 |          bool exit_on_fail)
320 | {
327 | #ifdef _WIN32
328 |     result = GetProcAddress(*handle, name);
329 | #else
330 |     result = dlsym(*handle, name);
331 |     if (!result)
332 |         error = dlerror();
511 |      */
512 |     void *sym;
513 | 
514 |     sym = dlsym(NULL, "glXGetCurrentContext");
515 |     if (sym) {
516 |         if (glXGetCurrentContext())
520 |     }
521 | 
522 | #if PLATFORM_HAS_EGL
523 |     sym = dlsym(NULL, "eglGetCurrentContext");
524 |     if (sym) {
525 |         if (epoxy_egl_get_current_gl_context_api() != EGL_NONE)
533 |      * Presumably they dlopened with RTLD_LOCAL, which hides it
534 |      * from us.  Just go dlopen()ing likely libraries and try them.
535 |      */
536 |     sym = do_dlsym(&api.glx_handle, GLX_LIB, "glXGetCurrentContext", false);
537 |     if (sym && glXGetCurrentContext())
538 |         return true;
539 | 
540 | #if PLATFORM_HAS_EGL
541 |     sym = do_dlsym(&api.egl_handle, EGL_LIB, "eglGetCurrentContext",
542 |                    false);
543 |     if (sym && epoxy_egl_get_current_gl_context_api() != EGL_NONE)
575 | }
576 | 
577 | void *
578 | epoxy_conservative_egl_dlsym(const char *name, bool exit_if_fails)
579 | {
580 |     return do_dlsym(&api.egl_handle, EGL_LIB, name, exit_if_fails);
581 | }
582 | 
583 | void *
584 | epoxy_egl_dlsym(const char *name)
585 | {
586 |     return epoxy_conservative_egl_dlsym(name, true);
587 | }
588 | 
589 | void *
590 | epoxy_conservative_glx_dlsym(const char *name, bool exit_if_fails)
591 | {
592 |     return do_dlsym(&api.glx_handle, GLX_LIB, name, exit_if_fails);
593 | }
594 | 
595 | void *
596 | epoxy_glx_dlsym(const char *name)
597 | {
598 |     return epoxy_conservative_glx_dlsym(name, true);
599 | }
600 | 
601 | void *
602 | epoxy_gl_dlsym(const char *name)
603 | {
604 | #ifdef _WIN32
605 |     return do_dlsym(&api.gl_handle, "OPENGL32", name, true);
606 | #elif defined(__APPLE__)
607 |     return do_dlsym(&api.gl_handle,
608 |                     "/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL",
609 |                     name, true);
610 | #else
611 |     /* There's no library for desktop GL support independent of GLX. */
612 |     return epoxy_glx_dlsym(name);
613 | #endif
614 | }
615 | 
616 | void *
617 | epoxy_gles1_dlsym(const char *name)
618 | {
619 |     if (epoxy_current_context_is_glx()) {
620 |         return epoxy_get_proc_address(name);
621 |     } else {
622 |         return do_dlsym(&api.gles1_handle, GLES1_LIB, name, true);
623 |     }
624 | }
625 | 
626 | void *
627 | epoxy_gles2_dlsym(const char *name)
628 | {
629 |     if (epoxy_current_context_is_glx()) {
630 |         return epoxy_get_proc_address(name);
631 |     } else {
632 |         return do_dlsym(&api.gles2_handle, GLES2_LIB, name, true);
633 |     }
634 | }
644 |  * eglGetProcAddress().  Thanks, Khronos.
645 |  */
646 | void *
647 | epoxy_gles3_dlsym(const char *name)
648 | {
649 |     if (epoxy_current_context_is_glx()) {
650 |         return epoxy_get_proc_address(name);
651 |     } else {
652 |         void *func = do_dlsym(&api.gles2_handle, GLES2_LIB, name, false);
653 | 
654 |         if (func)
678 | #endif
679 | 
680 |     if (core_version <= core_symbol_support) {
681 |         return epoxy_gl_dlsym(name);
682 |     } else {
683 |         return epoxy_get_proc_address(name);
718 |      */
719 | #if PLATFORM_HAS_GLX
720 |     if (api.glx_handle && glXGetCurrentContext())
721 |         return epoxy_gl_dlsym(name);
722 | #endif
723 | 
731 |     if (api.egl_handle) {
732 |         switch (epoxy_egl_get_current_gl_context_api()) {
733 |         case EGL_OPENGL_API:
734 |             return epoxy_gl_dlsym(name);
735 |         case EGL_OPENGL_ES_API:
736 |             /* We can't resolve the GL version, because
740 |              */
741 |             get_dlopen_handle(&api.gles2_handle, GLES2_LIB, false);
742 |             if (api.gles2_handle)
743 |                 return epoxy_gles2_dlsym(name);
744 |             else
745 |                 return epoxy_gles1_dlsym(name);
746 |         }
747 |     }
748 | #endif /* PLATFORM_HAS_EGL */
749 | 
750 |     /* Fall back to GLX */
751 |     return epoxy_gl_dlsym(name);
752 | }
753 | 
772 | #if defined(_WIN32)
773 |     return wglGetProcAddress(name);
774 | #elif defined(__APPLE__)
775 |     return epoxy_gl_dlsym(name);
776 | #elif PLATFORM_HAS_GLX
777 |     if (epoxy_current_context_is_glx())
{% endraw %}

```
### src/glx_generated_dispatch.c

```c

{% raw %}
3175 |         switch (providers[i]) {
3176 |         case GLX_10:
3177 |             if (true)
3178 |                 return epoxy_glx_dlsym(entrypoint_strings + entrypoints[i]);
3179 |             break;
3180 |         case GLX_11:
3181 |             if (true)
3182 |                 return epoxy_glx_dlsym(entrypoint_strings + entrypoints[i]);
3183 |             break;
3184 |         case GLX_12:
3185 |             if (true)
3186 |                 return epoxy_glx_dlsym(entrypoint_strings + entrypoints[i]);
3187 |             break;
3188 |         case GLX_13:
3189 |             if (true)
3190 |                 return epoxy_glx_dlsym(entrypoint_strings + entrypoints[i]);
3191 |             break;
3192 |         case GLX_extension_GLX_AMD_gpu_association:
3319 |             break;
3320 |         case always_present:
3321 |             if (true)
3322 |                 return epoxy_glx_dlsym(entrypoint_strings + entrypoints[i]);
3323 |             break;
3324 |         case glx_provider_terminator:
{% endraw %}

```
### src/dispatch_egl.c

```c

{% raw %}
110 | #else
111 |     EGLDisplay* (* pf_eglGetCurrentDisplay) (void);
112 | 
113 |     pf_eglGetCurrentDisplay = epoxy_conservative_egl_dlsym("eglGetCurrentDisplay", false);
114 |     if (pf_eglGetCurrentDisplay)
115 |         return true;
{% endraw %}

```
### src/gl_generated_dispatch.c

```c

{% raw %}
72479 |             break;
72480 |         case OpenGL_ES_1_0:
72481 |             if (!epoxy_is_desktop_gl() && epoxy_gl_version() >= 10 && epoxy_gl_version() < 20)
72482 |                 return epoxy_gles1_dlsym(entrypoint_strings + entrypoints[i]);
72483 |             break;
72484 |         case OpenGL_ES_2_0:
72485 |             if (!epoxy_is_desktop_gl() && epoxy_gl_version() >= 20)
72486 |                 return epoxy_gles2_dlsym(entrypoint_strings + entrypoints[i]);
72487 |             break;
72488 |         case OpenGL_ES_3_0:
72489 |             if (!epoxy_is_desktop_gl() && epoxy_gl_version() >= 30)
72490 |                 return epoxy_gles3_dlsym(entrypoint_strings + entrypoints[i]);
72491 |             break;
72492 |         case OpenGL_ES_3_1:
72493 |             if (!epoxy_is_desktop_gl() && epoxy_gl_version() >= 31)
72494 |                 return epoxy_gles3_dlsym(entrypoint_strings + entrypoints[i]);
72495 |             break;
72496 |         case OpenGL_ES_3_2:
72497 |             if (!epoxy_is_desktop_gl() && epoxy_gl_version() >= 32)
72498 |                 return epoxy_gles3_dlsym(entrypoint_strings + entrypoints[i]);
72499 |             break;
72500 |         case always_present:
{% endraw %}

```
### src/wgl_generated_dispatch.c

```c

{% raw %}
3527 |         switch (providers[i]) {
3528 |         case WGL_10:
3529 |             if (true)
3530 |                 return epoxy_gl_dlsym(entrypoint_strings + entrypoints[i]);
3531 |             break;
3532 |         case WGL_extension_WGL_3DL_stereo_control:
{% endraw %}

```
### src/gen_dispatch.py

```python

{% raw %}
342 |                 condition = '!epoxy_is_desktop_gl() && epoxy_gl_version() >= {0}'.format(version)
343 | 
344 |                 if version <= 20:
345 |                     loader = 'epoxy_gles2_dlsym({0})'
346 |                 else:
347 |                     loader = 'epoxy_gles3_dlsym({0})'
348 |             elif api == 'gles1':
349 |                 human_name = 'OpenGL ES 1.0'
350 |                 condition = '!epoxy_is_desktop_gl() && epoxy_gl_version() >= 10 && epoxy_gl_version() < 20'
351 |                 loader = 'epoxy_gles1_dlsym({0})'
352 |             elif api == 'glx':
353 |                 human_name = 'GLX {0}'.format(version)
359 |                     loader = 'glXGetProcAddress((const GLubyte *){0})'
360 |                 else:
361 |                     condition = 'true'
362 |                     loader = 'epoxy_glx_dlsym({0})'
363 |             elif api == 'egl':
364 |                 human_name = 'EGL {0}'.format(version)
368 |                     condition = 'true'
369 |                 # All EGL core entrypoints must be dlsym()ed out --
370 |                 # eglGetProcAdddress() will return NULL.
371 |                 loader = 'epoxy_egl_dlsym({0})'
372 |             elif api == 'wgl':
373 |                 human_name = 'WGL {0}'.format(version)
374 |                 condition = 'true'
375 |                 loader = 'epoxy_gl_dlsym({0})'
376 |             elif api == 'glsc2':
377 |                 continue
890 |     # required to be present as a public symbol by the Linux OpenGL
891 |     # ABI.
892 |     generator.fixup_bootstrap_function('glXGetProcAddress',
893 |                                        'epoxy_glx_dlsym({0})')
894 | 
895 |     generator.prepare_provider_enum()
{% endraw %}

```
### test/glx_static.c

```c

{% raw %}
48 |     int val;
49 | 
50 | #if NEEDS_TO_BE_STATIC
51 |     if (dlsym(NULL, "epoxy_glCompileShader")) {
52 |         fprintf(stderr, "glx_static requires epoxy built with --enable-static\n");
53 |         return 77;
{% endraw %}

```
### test/dlwrap.h

```c

{% raw %}
50 |  * thing to call is dlwrap_real_dlsym.
51 |  */
52 | void *
53 | dlwrap_real_dlsym(void *handle, const char *symbol);
54 | 
55 | #define DEFER_TO_GL(library, func, name, args)                          \
56 | ({                                                                      \
57 |     void *lib = dlwrap_real_dlopen(library, RTLD_LAZY | RTLD_LOCAL);    \
58 |     typeof(&func) real_func = dlwrap_real_dlsym(lib, name);             \
59 |     /* gcc extension -- func's return value is the return value of      \
60 |      * the statement.                                                   \
{% endraw %}

```
### test/egl_without_glx.c

```c

{% raw %}
63 |         return NULL;
64 | #endif
65 | 
66 |     dlopen_unwrapped = dlsym(RTLD_NEXT, "dlopen");
67 |     assert(dlopen_unwrapped);
68 | 
81 | override_eglBindAPI(EGLenum api)
82 | {
83 |     void *egl = dlopen("libEGL.so.1", RTLD_LAZY | RTLD_LOCAL);
84 |     EGLBoolean (*real_eglBindAPI)(EGLenum api) = dlsym(egl, "eglBindAPI");
85 | 
86 |     last_api = api;
102 | override_eglGetError(void)
103 | {
104 |     void *egl = dlopen("libEGL.so.1", RTLD_LAZY | RTLD_LOCAL);
105 |     EGLint (*real_eglGetError)(void) = dlsym(egl, "eglGetError");
106 | 
107 |     if (extra_error != EGL_SUCCESS) {
{% endraw %}

```
### test/dlwrap.c

```c

{% raw %}
51 | void *libfips_handle;
52 | 
53 | typedef void *(*fips_dlopen_t)(const char *filename, int flag);
54 | typedef void *(*fips_dlsym_t)(void *handle, const char *symbol);
55 | 
56 | void *override_EGL_eglGetProcAddress(const char *name);
130 | 
131 |     if (wrap < wrapped_libs ||
132 |         wrap >= wrapped_libs + ARRAY_SIZE(wrapped_libs)) {
133 |         void (*real_dlclose)(void *handle) = dlwrap_real_dlsym(RTLD_NEXT, "__dlclose");
134 |         real_dlclose(handle);
135 |     }
141 |     static fips_dlopen_t real_dlopen = NULL;
142 | 
143 |     if (!real_dlopen) {
144 |         real_dlopen = (fips_dlopen_t) dlwrap_real_dlsym(RTLD_NEXT, "dlopen");
145 |         if (!real_dlopen) {
146 |             fprintf(stderr, "Error: Failed to find symbol for dlopen.\n");
156 |  * "override_<prefix>_<name>"
157 |  */
158 | static void *
159 | wrapped_dlsym(const char *prefix, const char *name)
160 | {
161 |     char *wrap_name;
162 |     void *symbol;
163 | 
164 |     asprintf(&wrap_name, "override_%s_%s", prefix, name);
165 |     symbol = dlwrap_real_dlsym(RTLD_DEFAULT, wrap_name);
166 |     free(wrap_name);
167 |     return symbol;
175 |  * pass things through with RTLD_next if libfips does not have the
176 |  * function desired.  */
177 | void *
178 | dlsym(void *handle, const char *name)
179 | {
180 |     struct libwrap *wrap = handle;
190 |      * library. */
191 | 
192 |     if (wrap) {
193 |         void *symbol = wrapped_dlsym(wrap->symbol_prefix, name);
194 |         if (symbol)
195 |             return symbol;
196 |         else
197 |             return dlwrap_real_dlsym(wrap->handle, name);
198 |     }
199 | 
201 |      * through.  (This also covers the cases of lookups with
202 |      * special handles such as RTLD_DEFAULT or RTLD_NEXT.)
203 |      */
204 |     return dlwrap_real_dlsym(handle, name);
205 | }
206 | 
207 | void *
208 | dlwrap_real_dlsym(void *handle, const char *name)
209 | {
210 |     static fips_dlsym_t real_dlsym = NULL;
211 | 
212 |     if (!real_dlsym) {
213 |         /* FIXME: This brute-force, hard-coded searching for a versioned
214 |          * symbol is really ugly. The only reason I'm doing this is because
241 |         int num_versions = sizeof(version) / sizeof(version[0]);
242 |         int i;
243 |         for (i = 0; i < num_versions; i++) {
244 |             real_dlsym = (fips_dlsym_t) dlvsym(RTLD_NEXT, "dlsym", version[i]);
245 |             if (real_dlsym)
246 |                 break;
247 |         }
248 |         if (i == num_versions) {
249 |             fprintf(stderr, "Internal error: Failed to find real dlsym\n");
250 |             fprintf(stderr,
251 |                     "This may be a simple matter of fips not knowing about the version of GLIBC that\n"
257 |                     "\n"
258 |                     "\tldd <your-program> | grep libdl.so\n"
259 |                     "\n"
260 |                     "And then inspecting the version attached to the dlsym symbol:\n"
261 |                     "\n"
262 |                     "\treadelf -s /path/to/libdl.so.2 | grep dlsym\n"
263 |                     "\n"
264 |                     "And finally, adding the version to dlwrap.c:dlwrap_real_dlsym.\n");
265 | 
266 |             exit(1);
267 |         }
268 |     }
269 | 
270 |     return real_dlsym(handle, name);
271 | }
272 | 
275 | {
276 |     void *symbol;
277 | 
278 |     symbol = wrapped_dlsym("GL", name);
279 |     if (symbol)
280 |         return symbol;
288 | {
289 |     void *symbol;
290 | 
291 |     symbol = wrapped_dlsym("GL", name);
292 |     if (symbol)
293 |         return symbol;
302 |     void *symbol;
303 | 
304 |     if (!STRNCMP_LITERAL(name, "gl")) {
305 |         symbol = wrapped_dlsym("GLES2", name);
306 |         if (symbol)
307 |             return symbol;
308 |     }
309 | 
310 |     if (!STRNCMP_LITERAL(name, "egl")) {
311 |         symbol = wrapped_dlsym("EGL", name);
312 |         if (symbol)
313 |             return symbol;
{% endraw %}

```