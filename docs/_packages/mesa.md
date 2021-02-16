---
name: "mesa"
layout: package
next_package: giflib
previous_package: xqilla
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
558 |       driver = dlopen(path, RTLD_NOW | RTLD_GLOBAL);
562 |          driver = dlopen(path, RTLD_NOW | RTLD_GLOBAL);
579 |    log_(_LOADER_DEBUG, "MESA-LOADER: dlopen(%s)\n", path);
{% endraw %}

```
### src/gallium/auxiliary/util/u_dl.c

```c

{% raw %}
47 |    return (struct util_dl_library *)dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### src/gbm/backends/dri/gbm_dri.c

```c

{% raw %}
315 |    dlopen("libglapi.so.0", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/glx/dri_common.c

```c

{% raw %}
99 |    glhandle = dlopen(GL_LIB_NAME, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/glx/windows/windowsgl.c

```c

{% raw %}
42 |       dl_handle = dlopen("cygnativeGLthunk.dll", RTLD_NOW);
{% endraw %}

```
### src/glx/apple/apple_cgl.c

```c

{% raw %}
77 |    h = dlopen(opengl_framework_path, RTLD_NOW);
80 |       fprintf(stderr, "error: unable to dlopen %s : %s\n",
{% endraw %}

```