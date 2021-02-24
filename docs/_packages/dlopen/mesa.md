---
name: "mesa"
layout: package
next_package: plumed
previous_package: foam-extend
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 20.2.1
16 / 7568 files match, 6 filtered matches.

 - [src/loader/loader.c](#srcloaderloaderc)
 - [src/gallium/auxiliary/util/u_dl.c](#srcgalliumauxiliaryutilu_dlc)
 - [src/gbm/backends/dri/gbm_dri.c](#srcgbmbackendsdrigbm_dric)
 - [src/glx/dri_common.c](#srcglxdri_commonc)
 - [src/glx/windows/windowsgl.c](#srcglxwindowswindowsglc)
 - [src/glx/apple/apple_cgl.c](#srcglxappleapple_cglc)

### src/loader/loader.c

```c

{% raw %}
555 |       len = next - p;
556 | #if USE_ELF_TLS
557 |       snprintf(path, sizeof(path), "%.*s/tls/%s_dri.so", len, p, driver_name);
558 |       driver = dlopen(path, RTLD_NOW | RTLD_GLOBAL);
559 | #endif
560 |       if (driver == NULL) {
561 |          snprintf(path, sizeof(path), "%.*s/%s_dri.so", len, p, driver_name);
562 |          driver = dlopen(path, RTLD_NOW | RTLD_GLOBAL);
563 |          if (driver == NULL)
564 |             log_(_LOADER_DEBUG, "MESA-LOADER: failed to open %s: %s\n",
576 |       return NULL;
577 |    }
578 | 
579 |    log_(_LOADER_DEBUG, "MESA-LOADER: dlopen(%s)\n", path);
580 | 
581 |    get_extensions_name = loader_get_extensions_name(driver_name);
{% endraw %}

```
### src/gallium/auxiliary/util/u_dl.c

```c

{% raw %}
44 | util_dl_open(const char *filename)
45 | {
46 | #if defined(PIPE_OS_UNIX)
47 |    return (struct util_dl_library *)dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
48 | #elif defined(PIPE_OS_WINDOWS)
49 |    return (struct util_dl_library *)LoadLibraryA(filename);
{% endraw %}

```
### src/gbm/backends/dri/gbm_dri.c

```c

{% raw %}
312 |    /* XXX: Library name differs on per platforms basis. Update this as
313 |     * osx/cygwin/windows/bsd gets support for GBM..
314 |     */
315 |    dlopen("libglapi.so.0", RTLD_LAZY | RTLD_GLOBAL);
316 | 
317 |    static const char *search_path_vars[] = {
{% endraw %}

```
### src/glx/dri_common.c

```c

{% raw %}
96 |    void *glhandle;
97 | 
98 |    /* Attempt to make sure libGL symbols will be visible to the driver */
99 |    glhandle = dlopen(GL_LIB_NAME, RTLD_NOW | RTLD_GLOBAL);
100 | 
101 |    static const char *search_path_vars[] = {
{% endraw %}

```
### src/glx/windows/windowsgl.c

```c

{% raw %}
39 |    static void *dl_handle = NULL;
40 | 
41 |    if (!dl_handle)
42 |       dl_handle = dlopen("cygnativeGLthunk.dll", RTLD_NOW);
43 | 
44 |    return dl_handle;
{% endraw %}

```
### src/glx/apple/apple_cgl.c

```c

{% raw %}
74 |    }
75 | 
76 |    (void) dlerror();            /*drain dlerror */
77 |    h = dlopen(opengl_framework_path, RTLD_NOW);
78 | 
79 |    if (NULL == h) {
80 |       fprintf(stderr, "error: unable to dlopen %s : %s\n",
81 |               opengl_framework_path, dlerror());
82 |       abort();
{% endraw %}

```