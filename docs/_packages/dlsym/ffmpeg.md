---
name: "ffmpeg"
layout: package
next_package: clamav
previous_package: esmf
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.1
9 / 3987 files match, 7 filtered matches.

 - [libavformat/avisynth.c](#libavformatavisynthc)
 - [libavfilter/vf_frei0r.c](#libavfiltervf_frei0rc)
 - [libavfilter/af_ladspa.c](#libavfilteraf_ladspac)
 - [libavcodec/omx.c](#libavcodecomxc)
 - [libavcodec/videotoolboxenc.c](#libavcodecvideotoolboxencc)
 - [libavcodec/amfenc.c](#libavcodecamfencc)
 - [libavutil/hwcontext_dxva2.c](#libavutilhwcontext_dxva2c)

### libavformat/avisynth.c

```c

{% raw %}
122 |         return AVERROR_UNKNOWN;
123 | 
124 | #define LOAD_AVS_FUNC(name, continue_on_fail)                          \
125 |         avs_library.name = dlsym(avs_library.library, #name);          \
126 |         if (!continue_on_fail && !avs_library.name)                    \
127 |             goto fail;
{% endraw %}

```
### libavfilter/vf_frei0r.c

```c

{% raw %}
79 | static void *load_sym(AVFilterContext *ctx, const char *sym_name)
80 | {
81 |     Frei0rContext *s = ctx->priv;
82 |     void *sym = dlsym(s->dl_handle, sym_name);
83 |     if (!sym)
84 |         av_log(ctx, AV_LOG_ERROR, "Could not find symbol '%s' in loaded module.\n", sym_name);
{% endraw %}

```
### libavfilter/af_ladspa.c

```c

{% raw %}
441 |         return AVERROR(EINVAL);
442 |     }
443 | 
444 |     descriptor_fn = dlsym(s->dl_handle, "ladspa_descriptor");
445 |     if (!descriptor_fn) {
446 |         av_log(ctx, AV_LOG_ERROR, "Could not find ladspa_descriptor: %s\n", dlerror());
{% endraw %}

```
### libavcodec/omx.c

```c

{% raw %}
85 |     void (*host_init)(void);
86 | } OMXContext;
87 | 
88 | static av_cold void *dlsym_prefixed(void *handle, const char *symbol, const char *prefix)
89 | {
90 |     char buf[50];
91 |     snprintf(buf, sizeof(buf), "%s%s", prefix ? prefix : "", symbol);
92 |     return dlsym(handle, buf);
93 | }
94 | 
102 |             av_log(logctx, AV_LOG_WARNING, "%s not found\n", libname);
103 |             return AVERROR_ENCODER_NOT_FOUND;
104 |         }
105 |         s->host_init = dlsym(s->lib2, "bcm_host_init");
106 |         if (!s->host_init) {
107 |             av_log(logctx, AV_LOG_WARNING, "bcm_host_init not found\n");
115 |         av_log(logctx, AV_LOG_WARNING, "%s not found\n", libname);
116 |         return AVERROR_ENCODER_NOT_FOUND;
117 |     }
118 |     s->ptr_Init                = dlsym_prefixed(s->lib, "OMX_Init", prefix);
119 |     s->ptr_Deinit              = dlsym_prefixed(s->lib, "OMX_Deinit", prefix);
120 |     s->ptr_ComponentNameEnum   = dlsym_prefixed(s->lib, "OMX_ComponentNameEnum", prefix);
121 |     s->ptr_GetHandle           = dlsym_prefixed(s->lib, "OMX_GetHandle", prefix);
122 |     s->ptr_FreeHandle          = dlsym_prefixed(s->lib, "OMX_FreeHandle", prefix);
123 |     s->ptr_GetComponentsOfRole = dlsym_prefixed(s->lib, "OMX_GetComponentsOfRole", prefix);
124 |     s->ptr_GetRolesOfComponent = dlsym_prefixed(s->lib, "OMX_GetRolesOfComponent", prefix);
125 |     if (!s->ptr_Init || !s->ptr_Deinit || !s->ptr_ComponentNameEnum ||
126 |         !s->ptr_GetHandle || !s->ptr_FreeHandle ||
{% endraw %}

```
### libavcodec/videotoolboxenc.c

```c

{% raw %}
88 | 
89 | #define GET_SYM(symbol, defaultVal)                                     \
90 | do{                                                                     \
91 |     CFStringRef* handle = (CFStringRef*)dlsym(RTLD_DEFAULT, #symbol);   \
92 |     if(!handle)                                                         \
93 |         compat_keys.symbol = CFSTR(defaultVal);                         \
99 | 
100 | static void loadVTEncSymbols(){
101 |     compat_keys.CMVideoFormatDescriptionGetHEVCParameterSetAtIndex =
102 |         (getParameterSetAtIndex)dlsym(
103 |             RTLD_DEFAULT,
104 |             "CMVideoFormatDescriptionGetHEVCParameterSetAtIndex"
{% endraw %}

```
### libavcodec/amfenc.c

```c

{% raw %}
127 |     AMF_RETURN_IF_FALSE(ctx, ctx->library != NULL,
128 |         AVERROR_UNKNOWN, "DLL %s failed to open\n", AMF_DLL_NAMEA);
129 | 
130 |     init_fun = (AMFInit_Fn)dlsym(ctx->library, AMF_INIT_FUNCTION_NAME);
131 |     AMF_RETURN_IF_FALSE(ctx, init_fun != NULL, AVERROR_UNKNOWN, "DLL %s failed to find function %s\n", AMF_DLL_NAMEA, AMF_INIT_FUNCTION_NAME);
132 | 
133 |     version_fun = (AMFQueryVersion_Fn)dlsym(ctx->library, AMF_QUERY_VERSION_FUNCTION_NAME);
134 |     AMF_RETURN_IF_FALSE(ctx, version_fun != NULL, AVERROR_UNKNOWN, "DLL %s failed to find function %s\n", AMF_DLL_NAMEA, AMF_QUERY_VERSION_FUNCTION_NAME);
135 | 
{% endraw %}

```
### libavutil/hwcontext_dxva2.c

```c

{% raw %}
437 |     D3DPRESENT_PARAMETERS d3dpp = dxva2_present_params;
438 |     D3DDISPLAYMODE d3ddm;
439 |     HRESULT hr;
440 |     pDirect3DCreate9 *createD3D = (pDirect3DCreate9 *)dlsym(priv->d3dlib, "Direct3DCreate9");
441 |     if (!createD3D) {
442 |         av_log(ctx, AV_LOG_ERROR, "Failed to locate Direct3DCreate9\n");
472 |     IDirect3D9Ex *d3d9ex = NULL;
473 |     IDirect3DDevice9Ex *exdev = NULL;
474 |     HRESULT hr;
475 |     pDirect3DCreate9Ex *createD3DEx = (pDirect3DCreate9Ex *)dlsym(priv->d3dlib, "Direct3DCreate9Ex");
476 |     if (!createD3DEx)
477 |         return AVERROR(ENOSYS);
537 |         return AVERROR_UNKNOWN;
538 |     }
539 | 
540 |     createDeviceManager = (pCreateDeviceManager9 *)dlsym(priv->dxva2lib,
541 |                                                          "DXVA2CreateDirect3DDeviceManager9");
542 |     if (!createDeviceManager) {
{% endraw %}

```