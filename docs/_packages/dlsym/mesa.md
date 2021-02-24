---
name: "mesa"
layout: package
next_package: plumed
previous_package: foam-extend
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 20.2.1
20 / 7568 files match, 11 filtered matches.

 - [src/loader/loader.c](#srcloaderloaderc)
 - [src/drm-shim/drm_shim.c](#srcdrm-shimdrm_shimc)
 - [src/gallium/auxiliary/util/u_dl.c](#srcgalliumauxiliaryutilu_dlc)
 - [src/gallium/frontends/dri/dri_helpers.c](#srcgalliumfrontendsdridri_helpersc)
 - [src/mesa/drivers/dri/common/megadriver_stub.c](#srcmesadriversdricommonmegadriver_stubc)
 - [src/intel/tools/intel_dump_gpu.c](#srcinteltoolsintel_dump_gpuc)
 - [src/intel/tools/intel_sanitize_gpu.c](#srcinteltoolsintel_sanitize_gpuc)
 - [src/glx/applegl_glx.c](#srcglxapplegl_glxc)
 - [src/glx/dri_glx.c](#srcglxdri_glxc)
 - [src/glx/windows/windowsgl.c](#srcglxwindowswindowsglc)
 - [src/glx/apple/apple_cgl.c](#srcglxappleapple_cglc)

### src/loader/loader.c

```c

{% raw %}
580 | 
581 |    get_extensions_name = loader_get_extensions_name(driver_name);
582 |    if (get_extensions_name) {
583 |       get_extensions = dlsym(driver, get_extensions_name);
584 |       if (get_extensions) {
585 |          extensions = get_extensions();
591 |    }
592 | 
593 |    if (!extensions)
594 |       extensions = dlsym(driver, __DRI_DRIVER_EXTENSIONS);
595 |    if (extensions == NULL) {
596 |       log_(_LOADER_WARNING,
{% endraw %}

```
### src/drm-shim/drm_shim.c

```c

{% raw %}
135 | 
136 | static void *get_function_pointer(const char *name)
137 | {
138 |    void *func = dlsym(RTLD_NEXT, name);
139 |    if (!func) {
140 |       fprintf(stderr, "Failed to resolve %s\n", name);
{% endraw %}

```
### src/gallium/auxiliary/util/u_dl.c

```c

{% raw %}
58 |                          const char *procname)
59 | {
60 | #if defined(PIPE_OS_UNIX)
61 |    return (util_dl_proc) pointer_to_func(dlsym((void *)library, procname));
62 | #elif defined(PIPE_OS_WINDOWS)
63 |    return (util_dl_proc)GetProcAddress((HMODULE)library, procname);
{% endraw %}

```
### src/gallium/frontends/dri/dri_helpers.c

```c

{% raw %}
53 |    }
54 | 
55 |    screen->opencl_dri_event_add_ref =
56 |       dlsym(RTLD_DEFAULT, "opencl_dri_event_add_ref");
57 |    screen->opencl_dri_event_release =
58 |       dlsym(RTLD_DEFAULT, "opencl_dri_event_release");
59 |    screen->opencl_dri_event_wait =
60 |       dlsym(RTLD_DEFAULT, "opencl_dri_event_wait");
61 |    screen->opencl_dri_event_get_fence =
62 |       dlsym(RTLD_DEFAULT, "opencl_dri_event_get_fence");
63 | 
64 |    success = dri2_is_opencl_interop_loaded_locked(screen);
{% endraw %}

```
### src/mesa/drivers/dri/common/megadriver_stub.c

```c

{% raw %}
115 |     * RTLD_DEFAULT. It seems unlikely that the symbol will
116 |     * be found in another library, but this isn't optimal.
117 |     */
118 |    get_extensions = dlsym(RTLD_DEFAULT, get_extensions_name);
119 |    free(get_extensions_name);
120 |    if (!get_extensions)
{% endraw %}

```
### src/intel/tools/intel_dump_gpu.c

```c

{% raw %}
646 | static void
647 | init(void)
648 | {
649 |    libc_close = dlsym(RTLD_NEXT, "close");
650 |    libc_ioctl = dlsym(RTLD_NEXT, "ioctl");
651 |    fail_if(libc_close == NULL || libc_ioctl == NULL,
652 |            "failed to get libc ioctl or close\n");
{% endraw %}

```
### src/intel/tools/intel_sanitize_gpu.c

```c

{% raw %}
425 | init(void)
426 | {
427 |    fds_to_bo_sizes = _mesa_pointer_hash_table_create(NULL);
428 |    libc_open = dlsym(RTLD_NEXT, "open");
429 |    libc_close = dlsym(RTLD_NEXT, "close");
430 |    libc_fcntl = dlsym(RTLD_NEXT, "fcntl");
431 |    libc_ioctl = dlsym(RTLD_NEXT, "ioctl");
432 | }
433 | 
{% endraw %}

```
### src/glx/applegl_glx.c

```c

{% raw %}
104 | static void *
105 | applegl_get_proc_address(const char *symbol)
106 | {
107 |    return dlsym(apple_cgl_get_dl_handle(), symbol);
108 | }
109 | 
{% endraw %}

```
### src/glx/dri_glx.c

```c

{% raw %}
220 | 
221 |    if (!config) {
222 |       /* Fall back to the old method */
223 |       config = dlsym(handle, "__driConfigOptions");
224 |       if (config)
225 |          config = strdup(config);
{% endraw %}

```
### src/glx/windows/windowsgl.c

```c

{% raw %}
337 |    int *result = (int *)args;
338 | 
339 |    /* Rather than play linkage games using stdcall to ensure we get
340 |       glGetString from opengl32.dll here, use dlsym */
341 |    void *dlhandle = windows_get_dl_handle();
342 |    const char *(*proc)(int) = dlsym(dlhandle, "glGetString");
343 |    const char *gl_renderer = (const char *)proc(GL_RENDERER);
344 | 
367 |    windows_extensions_result *r = (windows_extensions_result *)args;
368 | 
369 |    void *dlhandle = windows_get_dl_handle();
370 |    const char *(*proc)(int) = dlsym(dlhandle, "glGetString");
371 | 
372 |    r->gl_extensions = strdup(proc(GL_EXTENSIONS));
{% endraw %}

```
### src/glx/apple/apple_cgl.c

```c

{% raw %}
49 | {
50 |    void *s;
51 | 
52 |    s = dlsym(h, name);
53 | 
54 |    if (NULL == s) {
{% endraw %}

```