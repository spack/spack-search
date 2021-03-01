---
name: "ffmpeg"
layout: package
next_package: file
previous_package: fakexrandr
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
31 |  * @param name  The dynamic lib name.
32 |  * @return A handle to the opened lib.
33 |  */
34 | static inline HMODULE win32_dlopen(const char *name)
35 | {
36 | #if _WIN32_WINNT < 0x0602
{% endraw %}

```
### libavformat/avisynth.c

```c

{% raw %}
117 | 
118 | static av_cold int avisynth_load_library(void)
119 | {
120 |     avs_library.library = dlopen(AVISYNTH_LIB, RTLD_NOW | RTLD_LOCAL);
121 |     if (!avs_library.library)
122 |         return AVERROR_UNKNOWN;
{% endraw %}

```
### libavfilter/af_ladspa.c

```c

{% raw %}
351 |     void *ret = NULL;
352 | 
353 |     if (path) {
354 |         ret = dlopen(path, RTLD_LOCAL|RTLD_NOW);
355 |         av_free(path);
356 |     }
410 | 
411 |     if (s->dl_name[0] == '/' || s->dl_name[0] == '.') {
412 |         // argument is a path
413 |         s->dl_handle = dlopen(s->dl_name, RTLD_LOCAL|RTLD_NOW);
414 |     } else {
415 |         // argument is a shared object name
{% endraw %}

```
### libavcodec/omx.c

```c

{% raw %}
97 |                                 const char *libname2)
98 | {
99 |     if (libname2) {
100 |         s->lib2 = dlopen(libname2, RTLD_NOW | RTLD_GLOBAL);
101 |         if (!s->lib2) {
102 |             av_log(logctx, AV_LOG_WARNING, "%s not found\n", libname);
110 |             return AVERROR_ENCODER_NOT_FOUND;
111 |         }
112 |     }
113 |     s->lib = dlopen(libname, RTLD_NOW | RTLD_GLOBAL);
114 |     if (!s->lib) {
115 |         av_log(logctx, AV_LOG_WARNING, "%s not found\n", libname);
{% endraw %}

```
### libavcodec/amfenc.c

```c

{% raw %}
123 |     ctx->dts_delay = 0;
124 | 
125 | 
126 |     ctx->library = dlopen(AMF_DLL_NAMEA, RTLD_NOW | RTLD_LOCAL);
127 |     AMF_RETURN_IF_FALSE(ctx, ctx->library != NULL,
128 |         AVERROR_UNKNOWN, "DLL %s failed to open\n", AMF_DLL_NAMEA);
{% endraw %}

```
### libavutil/hwcontext_dxva2.c

```c

{% raw %}
526 | 
527 |     priv->device_handle = INVALID_HANDLE_VALUE;
528 | 
529 |     priv->d3dlib = dlopen("d3d9.dll", 0);
530 |     if (!priv->d3dlib) {
531 |         av_log(ctx, AV_LOG_ERROR, "Failed to load D3D9 library\n");
532 |         return AVERROR_UNKNOWN;
533 |     }
534 |     priv->dxva2lib = dlopen("dxva2.dll", 0);
535 |     if (!priv->dxva2lib) {
536 |         av_log(ctx, AV_LOG_ERROR, "Failed to load DXVA2 library\n");
{% endraw %}

```