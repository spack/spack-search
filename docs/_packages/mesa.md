---
name: "mesa"
layout: package
next_package: giflib
previous_package: xqilla
languages: ['cpp']
---
## 20.2.1
16 / 7568 files match

 - [meson.build](#mesonbuild)
 - [src/loader/loader.c](#srcloaderloaderc)
 - [src/gallium/auxiliary/util/u_dl.c](#srcgalliumauxiliaryutilu_dlc)
 - [src/mesa/drivers/dri/common/megadriver_stub.c](#srcmesadriversdricommonmegadriver_stubc)
 - [src/mesa/drivers/dri/common/dri_util.c](#srcmesadriversdricommondri_utilc)
 - [src/gbm/backends/dri/gbm_dri.c](#srcgbmbackendsdrigbm_dric)
 - [src/glx/dri_common.c](#srcglxdri_commonc)
 - [src/glx/windows/windowsgl.c](#srcglxwindowswindowsglc)
 - [src/glx/apple/apple_cgl.c](#srcglxappleapple_cglc)
 - [docs/libGL.txt](#docslibgltxt)
 - [docs/relnotes/10.0.rst](#docsrelnotes100rst)
 - [docs/relnotes/10.5.9.rst](#docsrelnotes1059rst)
 - [docs/relnotes/11.1.4.rst](#docsrelnotes1114rst)
 - [docs/relnotes/10.6.1.rst](#docsrelnotes1061rst)
 - [docs/relnotes/11.2.2.rst](#docsrelnotes1122rst)
 - [docs/relnotes/9.1.2.rst](#docsrelnotes912rst)

### meson.build

```

{% raw %}
1298 | if not cc.has_function('dlopen')
{% endraw %}

```
### src/loader/loader.c

```cpp

{% raw %}
522 |  * \param out_driver - Address where the dlopen() return value will be stored.
558 |       driver = dlopen(path, RTLD_NOW | RTLD_GLOBAL);
562 |          driver = dlopen(path, RTLD_NOW | RTLD_GLOBAL);
579 |    log_(_LOADER_DEBUG, "MESA-LOADER: dlopen(%s)\n", path);
{% endraw %}

```
### src/gallium/auxiliary/util/u_dl.c

```cpp

{% raw %}
47 |    return (struct util_dl_library *)dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### src/mesa/drivers/dri/common/megadriver_stub.c

```cpp

{% raw %}
52 |  * When the driver is dlopen'ed, this function will run. It will
114 |     * don't have the dlopen handle, so we have to use
{% endraw %}

```
### src/mesa/drivers/dri/common/dri_util.c

```cpp

{% raw %}
108 |  * after dlopen()ing it.
{% endraw %}

```
### src/gbm/backends/dri/gbm_dri.c

```cpp

{% raw %}
315 |    dlopen("libglapi.so.0", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/glx/dri_common.c

```cpp

{% raw %}
80 |  * Try to \c dlopen the named driver.
87 |  * \param out_driver_handle - Address to return the resulting dlopen() handle.
99 |    glhandle = dlopen(GL_LIB_NAME, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/glx/windows/windowsgl.c

```cpp

{% raw %}
42 |       dl_handle = dlopen("cygnativeGLthunk.dll", RTLD_NOW);
{% endraw %}

```
### src/glx/apple/apple_cgl.c

```cpp

{% raw %}
77 |    h = dlopen(opengl_framework_path, RTLD_NOW);
80 |       fprintf(stderr, "error: unable to dlopen %s : %s\n",
{% endraw %}

```
### docs/libGL.txt

```

{% raw %}
122 | display.  Each screen's driver is then opened with dlopen() and asked
{% endraw %}

```
### docs/relnotes/10.0.rst

```

{% raw %}
122 |    dlopen.h:54: undefined reference to \`dlopen'
{% endraw %}

```
### docs/relnotes/10.5.9.rst

```

{% raw %}
84 | -  gbm: dlopen libglapi so gbm_create_device works
{% endraw %}

```
### docs/relnotes/11.1.4.rst

```

{% raw %}
146 | -  android: enable dlopen() on all architectures
{% endraw %}

```
### docs/relnotes/10.6.1.rst

```

{% raw %}
65 | -  gbm: dlopen libglapi so gbm_create_device works
{% endraw %}

```
### docs/relnotes/11.2.2.rst

```

{% raw %}
171 | -  android: enable dlopen() on all architectures
{% endraw %}

```
### docs/relnotes/9.1.2.rst

```

{% raw %}
57 |    [bisected] 3284.073] (EE) AIGLX error: dlopen of
{% endraw %}

```