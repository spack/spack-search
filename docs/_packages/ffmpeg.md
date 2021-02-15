---
name: "ffmpeg"
layout: package
next_package: extrae
previous_package: cppcheck
languages: ['cpp']
---
## 4.1
9 / 3987 files match

 - [compat/w32dlfcn.h](#compatw32dlfcnh)
 - [compat/cuda/dynlink_loader.h](#compatcudadynlink_loaderh)
 - [libavformat/avisynth.c](#libavformatavisynthc)
 - [libavfilter/vf_frei0r.c](#libavfiltervf_frei0rc)
 - [libavfilter/af_ladspa.c](#libavfilteraf_ladspac)
 - [libavfilter/vf_telecine.c](#libavfiltervf_telecinec)
 - [libavcodec/omx.c](#libavcodecomxc)
 - [libavcodec/amfenc.c](#libavcodecamfencc)
 - [libavutil/hwcontext_dxva2.c](#libavutilhwcontext_dxva2c)

### compat/w32dlfcn.h

```cpp

{% raw %}
34 | static inline HMODULE win32_dlopen(const char *name)
86 | #define dlopen(name, flags) win32_dlopen(name)
{% endraw %}

```
### compat/cuda/dynlink_loader.h

```cpp

{% raw %}
24 | #define FFNV_LOAD_FUNC(path) dlopen((path), RTLD_LAZY)
{% endraw %}

```
### libavformat/avisynth.c

```cpp

{% raw %}
120 |     avs_library.library = dlopen(AVISYNTH_LIB, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### libavfilter/vf_frei0r.c

```cpp

{% raw %}
178 |     *handle_ptr = dlopen(path, RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### libavfilter/af_ladspa.c

```cpp

{% raw %}
354 |         ret = dlopen(path, RTLD_LOCAL|RTLD_NOW);
413 |         s->dl_handle = dlopen(s->dl_name, RTLD_LOCAL|RTLD_NOW);
{% endraw %}

```
### libavfilter/vf_telecine.c

```cpp

{% raw %}
22 |  * @file telecine filter, heavily based from mpv-player:TOOLS/vf_dlopen/telecine.c by
{% endraw %}

```
### libavcodec/omx.c

```cpp

{% raw %}
100 |         s->lib2 = dlopen(libname2, RTLD_NOW | RTLD_GLOBAL);
113 |     s->lib = dlopen(libname, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### libavcodec/amfenc.c

```cpp

{% raw %}
126 |     ctx->library = dlopen(AMF_DLL_NAMEA, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### libavutil/hwcontext_dxva2.c

```cpp

{% raw %}
529 |     priv->d3dlib = dlopen("d3d9.dll", 0);
534 |     priv->dxva2lib = dlopen("dxva2.dll", 0);
{% endraw %}

```