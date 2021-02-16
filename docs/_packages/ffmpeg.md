---
name: "ffmpeg"
layout: package
next_package: fio
previous_package: ferret
languages: ['c']
---
## 4.1
9 / 3987 files match, 6 filtered matches.

 - [compat/w32dlfcn.h](#compatw32dlfcnh)
 - [libavformat/avisynth.c](#libavformatavisynthc)
 - [libavfilter/af_ladspa.c](#libavfilteraf_ladspac)
 - [libavcodec/omx.c](#libavcodecomxc)
 - [libavcodec/amfenc.c](#libavcodecamfencc)
 - [libavutil/hwcontext_dxva2.c](#libavutilhwcontext_dxva2c)

### compat/w32dlfcn.h

```c

{% raw %}
34 | static inline HMODULE win32_dlopen(const char *name)
{% endraw %}

```
### libavformat/avisynth.c

```c

{% raw %}
120 |     avs_library.library = dlopen(AVISYNTH_LIB, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### libavfilter/af_ladspa.c

```c

{% raw %}
354 |         ret = dlopen(path, RTLD_LOCAL|RTLD_NOW);
413 |         s->dl_handle = dlopen(s->dl_name, RTLD_LOCAL|RTLD_NOW);
{% endraw %}

```
### libavcodec/omx.c

```c

{% raw %}
100 |         s->lib2 = dlopen(libname2, RTLD_NOW | RTLD_GLOBAL);
113 |     s->lib = dlopen(libname, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### libavcodec/amfenc.c

```c

{% raw %}
126 |     ctx->library = dlopen(AMF_DLL_NAMEA, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### libavutil/hwcontext_dxva2.c

```c

{% raw %}
529 |     priv->d3dlib = dlopen("d3d9.dll", 0);
534 |     priv->dxva2lib = dlopen("dxva2.dll", 0);
{% endraw %}

```