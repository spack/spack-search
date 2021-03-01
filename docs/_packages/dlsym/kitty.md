---
name: "kitty"
layout: package
next_package: kmod
previous_package: keyutils
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['python', 'c']
---
## 0.11.2
15 / 263 files match, 8 filtered matches.

 - [kitty/gl-wrapper.c](#kittygl-wrapperc)
 - [glfw/egl_context.c](#glfwegl_contextc)
 - [glfw/vulkan.c](#glfwvulkanc)
 - [glfw/glfw.py](#glfwglfwpy)
 - [glfw/glx_context.c](#glfwglx_contextc)
 - [glfw/x11_init.c](#glfwx11_initc)
 - [glfw/osmesa_context.c](#glfwosmesa_contextc)
 - [glfw/wl_init.c](#glfwwl_initc)

### kitty/gl-wrapper.c

```c

{% raw %}
110 | #ifdef __APPLE__
111 |             return 1;
112 | #else
113 |             gladGetProcAddressPtr = (PFNGLXGETPROCADDRESSPROC_PRIVATE)dlsym(libGL,
114 |                 "glXGetProcAddressARB");
115 |             return gladGetProcAddressPtr != NULL;
139 | #if defined(_WIN32) || defined(__CYGWIN__)
140 |         result = (void*)GetProcAddress((HMODULE) libGL, namez);
141 | #else
142 |         result = dlsym(libGL, namez);
143 | #endif
144 |     }
{% endraw %}

```
### glfw/egl_context.c

```c

{% raw %}
252 | 
253 |     if (window->context.egl.client)
254 |     {
255 |         GLFWglproc proc = (GLFWglproc) _glfw_dlsym(window->context.egl.client,
256 |                                                    procname);
257 |         if (proc)
335 |     _glfw.egl.prefix = (strncmp(sonames[i], "lib", 3) == 0);
336 | 
337 |     _glfw.egl.GetConfigAttrib = (PFN_eglGetConfigAttrib)
338 |         _glfw_dlsym(_glfw.egl.handle, "eglGetConfigAttrib");
339 |     _glfw.egl.GetConfigs = (PFN_eglGetConfigs)
340 |         _glfw_dlsym(_glfw.egl.handle, "eglGetConfigs");
341 |     _glfw.egl.GetDisplay = (PFN_eglGetDisplay)
342 |         _glfw_dlsym(_glfw.egl.handle, "eglGetDisplay");
343 |     _glfw.egl.GetError = (PFN_eglGetError)
344 |         _glfw_dlsym(_glfw.egl.handle, "eglGetError");
345 |     _glfw.egl.Initialize = (PFN_eglInitialize)
346 |         _glfw_dlsym(_glfw.egl.handle, "eglInitialize");
347 |     _glfw.egl.Terminate = (PFN_eglTerminate)
348 |         _glfw_dlsym(_glfw.egl.handle, "eglTerminate");
349 |     _glfw.egl.BindAPI = (PFN_eglBindAPI)
350 |         _glfw_dlsym(_glfw.egl.handle, "eglBindAPI");
351 |     _glfw.egl.CreateContext = (PFN_eglCreateContext)
352 |         _glfw_dlsym(_glfw.egl.handle, "eglCreateContext");
353 |     _glfw.egl.DestroySurface = (PFN_eglDestroySurface)
354 |         _glfw_dlsym(_glfw.egl.handle, "eglDestroySurface");
355 |     _glfw.egl.DestroyContext = (PFN_eglDestroyContext)
356 |         _glfw_dlsym(_glfw.egl.handle, "eglDestroyContext");
357 |     _glfw.egl.CreateWindowSurface = (PFN_eglCreateWindowSurface)
358 |         _glfw_dlsym(_glfw.egl.handle, "eglCreateWindowSurface");
359 |     _glfw.egl.MakeCurrent = (PFN_eglMakeCurrent)
360 |         _glfw_dlsym(_glfw.egl.handle, "eglMakeCurrent");
361 |     _glfw.egl.SwapBuffers = (PFN_eglSwapBuffers)
362 |         _glfw_dlsym(_glfw.egl.handle, "eglSwapBuffers");
363 |     _glfw.egl.SwapInterval = (PFN_eglSwapInterval)
364 |         _glfw_dlsym(_glfw.egl.handle, "eglSwapInterval");
365 |     _glfw.egl.QueryString = (PFN_eglQueryString)
366 |         _glfw_dlsym(_glfw.egl.handle, "eglQueryString");
367 |     _glfw.egl.GetProcAddress = (PFN_eglGetProcAddress)
368 |         _glfw_dlsym(_glfw.egl.handle, "eglGetProcAddress");
369 | 
370 |     if (!_glfw.egl.GetConfigAttrib ||
{% endraw %}

```
### glfw/vulkan.c

```c

{% raw %}
66 |     }
67 | 
68 |     _glfw.vk.GetInstanceProcAddr = (PFN_vkGetInstanceProcAddr)
69 |         _glfw_dlsym(_glfw.vk.handle, "vkGetInstanceProcAddr");
70 |     if (!_glfw.vk.GetInstanceProcAddr)
71 |     {
262 |     }
263 | #else
264 |     if (!proc)
265 |         proc = (GLFWvkproc) _glfw_dlsym(_glfw.vk.handle, procname);
266 | #endif
267 | 
{% endraw %}

```
### glfw/glfw.py

```python

{% raw %}
176 |         )
177 | 
178 |     def load(self):
179 |         ans = '*(void **) (&{name}_impl) = dlsym(handle, "{name}");'.format(
180 |             name=self.name
181 |         )
{% endraw %}

```
### glfw/glx_context.c

```c

{% raw %}
222 |     else if (_glfw.glx.GetProcAddressARB)
223 |         return _glfw.glx.GetProcAddressARB((const GLubyte*) procname);
224 |     else
225 |         return _glfw_dlsym(_glfw.glx.handle, procname);
226 | }
227 | 
282 |     }
283 | 
284 |     _glfw.glx.GetFBConfigs =
285 |         _glfw_dlsym(_glfw.glx.handle, "glXGetFBConfigs");
286 |     _glfw.glx.GetFBConfigAttrib =
287 |         _glfw_dlsym(_glfw.glx.handle, "glXGetFBConfigAttrib");
288 |     _glfw.glx.GetClientString =
289 |         _glfw_dlsym(_glfw.glx.handle, "glXGetClientString");
290 |     _glfw.glx.QueryExtension =
291 |         _glfw_dlsym(_glfw.glx.handle, "glXQueryExtension");
292 |     _glfw.glx.QueryVersion =
293 |         _glfw_dlsym(_glfw.glx.handle, "glXQueryVersion");
294 |     _glfw.glx.DestroyContext =
295 |         _glfw_dlsym(_glfw.glx.handle, "glXDestroyContext");
296 |     _glfw.glx.MakeCurrent =
297 |         _glfw_dlsym(_glfw.glx.handle, "glXMakeCurrent");
298 |     _glfw.glx.SwapBuffers =
299 |         _glfw_dlsym(_glfw.glx.handle, "glXSwapBuffers");
300 |     _glfw.glx.QueryExtensionsString =
301 |         _glfw_dlsym(_glfw.glx.handle, "glXQueryExtensionsString");
302 |     _glfw.glx.CreateNewContext =
303 |         _glfw_dlsym(_glfw.glx.handle, "glXCreateNewContext");
304 |     _glfw.glx.CreateWindow =
305 |         _glfw_dlsym(_glfw.glx.handle, "glXCreateWindow");
306 |     _glfw.glx.DestroyWindow =
307 |         _glfw_dlsym(_glfw.glx.handle, "glXDestroyWindow");
308 |     _glfw.glx.GetProcAddress =
309 |         _glfw_dlsym(_glfw.glx.handle, "glXGetProcAddress");
310 |     _glfw.glx.GetProcAddressARB =
311 |         _glfw_dlsym(_glfw.glx.handle, "glXGetProcAddressARB");
312 |     _glfw.glx.GetVisualFromFBConfig =
313 |         _glfw_dlsym(_glfw.glx.handle, "glXGetVisualFromFBConfig");
314 | 
315 |     if (!_glfw.glx.GetFBConfigs ||
{% endraw %}

```
### glfw/x11_init.c

```c

{% raw %}
154 |     if (_glfw.x11.vidmode.handle)
155 |     {
156 |         _glfw.x11.vidmode.QueryExtension = (PFN_XF86VidModeQueryExtension)
157 |             _glfw_dlsym(_glfw.x11.vidmode.handle, "XF86VidModeQueryExtension");
158 |         _glfw.x11.vidmode.GetGammaRamp = (PFN_XF86VidModeGetGammaRamp)
159 |             _glfw_dlsym(_glfw.x11.vidmode.handle, "XF86VidModeGetGammaRamp");
160 |         _glfw.x11.vidmode.SetGammaRamp = (PFN_XF86VidModeSetGammaRamp)
161 |             _glfw_dlsym(_glfw.x11.vidmode.handle, "XF86VidModeSetGammaRamp");
162 |         _glfw.x11.vidmode.GetGammaRampSize = (PFN_XF86VidModeGetGammaRampSize)
163 |             _glfw_dlsym(_glfw.x11.vidmode.handle, "XF86VidModeGetGammaRampSize");
164 | 
165 |         _glfw.x11.vidmode.available =
176 |     if (_glfw.x11.xi.handle)
177 |     {
178 |         _glfw.x11.xi.QueryVersion = (PFN_XIQueryVersion)
179 |             _glfw_dlsym(_glfw.x11.xi.handle, "XIQueryVersion");
180 |         _glfw.x11.xi.SelectEvents = (PFN_XISelectEvents)
181 |             _glfw_dlsym(_glfw.x11.xi.handle, "XISelectEvents");
182 | 
183 |         if (XQueryExtension(_glfw.x11.display,
206 |     if (_glfw.x11.randr.handle)
207 |     {
208 |         _glfw.x11.randr.AllocGamma = (PFN_XRRAllocGamma)
209 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRAllocGamma");
210 |         _glfw.x11.randr.FreeGamma = (PFN_XRRFreeGamma)
211 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRFreeGamma");
212 |         _glfw.x11.randr.FreeCrtcInfo = (PFN_XRRFreeCrtcInfo)
213 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRFreeCrtcInfo");
214 |         _glfw.x11.randr.FreeGamma = (PFN_XRRFreeGamma)
215 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRFreeGamma");
216 |         _glfw.x11.randr.FreeOutputInfo = (PFN_XRRFreeOutputInfo)
217 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRFreeOutputInfo");
218 |         _glfw.x11.randr.FreeScreenResources = (PFN_XRRFreeScreenResources)
219 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRFreeScreenResources");
220 |         _glfw.x11.randr.GetCrtcGamma = (PFN_XRRGetCrtcGamma)
221 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRGetCrtcGamma");
222 |         _glfw.x11.randr.GetCrtcGammaSize = (PFN_XRRGetCrtcGammaSize)
223 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRGetCrtcGammaSize");
224 |         _glfw.x11.randr.GetCrtcInfo = (PFN_XRRGetCrtcInfo)
225 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRGetCrtcInfo");
226 |         _glfw.x11.randr.GetOutputInfo = (PFN_XRRGetOutputInfo)
227 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRGetOutputInfo");
228 |         _glfw.x11.randr.GetOutputPrimary = (PFN_XRRGetOutputPrimary)
229 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRGetOutputPrimary");
230 |         _glfw.x11.randr.GetScreenResourcesCurrent = (PFN_XRRGetScreenResourcesCurrent)
231 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRGetScreenResourcesCurrent");
232 |         _glfw.x11.randr.QueryExtension = (PFN_XRRQueryExtension)
233 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRQueryExtension");
234 |         _glfw.x11.randr.QueryVersion = (PFN_XRRQueryVersion)
235 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRQueryVersion");
236 |         _glfw.x11.randr.SelectInput = (PFN_XRRSelectInput)
237 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRSelectInput");
238 |         _glfw.x11.randr.SetCrtcConfig = (PFN_XRRSetCrtcConfig)
239 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRSetCrtcConfig");
240 |         _glfw.x11.randr.SetCrtcGamma = (PFN_XRRSetCrtcGamma)
241 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRSetCrtcGamma");
242 |         _glfw.x11.randr.UpdateConfiguration = (PFN_XRRUpdateConfiguration)
243 |             _glfw_dlsym(_glfw.x11.randr.handle, "XRRUpdateConfiguration");
244 | 
245 |         if (XRRQueryExtension(_glfw.x11.display,
298 |     if (_glfw.x11.xcursor.handle)
299 |     {
300 |         _glfw.x11.xcursor.ImageCreate = (PFN_XcursorImageCreate)
301 |             _glfw_dlsym(_glfw.x11.xcursor.handle, "XcursorImageCreate");
302 |         _glfw.x11.xcursor.ImageDestroy = (PFN_XcursorImageDestroy)
303 |             _glfw_dlsym(_glfw.x11.xcursor.handle, "XcursorImageDestroy");
304 |         _glfw.x11.xcursor.ImageLoadCursor = (PFN_XcursorImageLoadCursor)
305 |             _glfw_dlsym(_glfw.x11.xcursor.handle, "XcursorImageLoadCursor");
306 |     }
307 | 
313 |     if (_glfw.x11.xinerama.handle)
314 |     {
315 |         _glfw.x11.xinerama.IsActive = (PFN_XineramaIsActive)
316 |             _glfw_dlsym(_glfw.x11.xinerama.handle, "XineramaIsActive");
317 |         _glfw.x11.xinerama.QueryExtension = (PFN_XineramaQueryExtension)
318 |             _glfw_dlsym(_glfw.x11.xinerama.handle, "XineramaQueryExtension");
319 |         _glfw.x11.xinerama.QueryScreens = (PFN_XineramaQueryScreens)
320 |             _glfw_dlsym(_glfw.x11.xinerama.handle, "XineramaQueryScreens");
321 | 
322 |         if (XineramaQueryExtension(_glfw.x11.display,
336 |     if (_glfw.x11.xrender.handle)
337 |     {
338 |         _glfw.x11.xrender.QueryExtension = (PFN_XRenderQueryExtension)
339 |             _glfw_dlsym(_glfw.x11.xrender.handle, "XRenderQueryExtension");
340 |         _glfw.x11.xrender.QueryVersion = (PFN_XRenderQueryVersion)
341 |             _glfw_dlsym(_glfw.x11.xrender.handle, "XRenderQueryVersion");
342 |         _glfw.x11.xrender.FindVisualFormat = (PFN_XRenderFindVisualFormat)
343 |             _glfw_dlsym(_glfw.x11.xrender.handle, "XRenderFindVisualFormat");
344 | 
345 |         if (XRenderQueryExtension(_glfw.x11.display,
{% endraw %}

```
### glfw/osmesa_context.c

```c

{% raw %}
145 |     }
146 | 
147 |     _glfw.osmesa.CreateContextExt = (PFN_OSMesaCreateContextExt)
148 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaCreateContextExt");
149 |     _glfw.osmesa.CreateContextAttribs = (PFN_OSMesaCreateContextAttribs)
150 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaCreateContextAttribs");
151 |     _glfw.osmesa.DestroyContext = (PFN_OSMesaDestroyContext)
152 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaDestroyContext");
153 |     _glfw.osmesa.MakeCurrent = (PFN_OSMesaMakeCurrent)
154 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaMakeCurrent");
155 |     _glfw.osmesa.GetColorBuffer = (PFN_OSMesaGetColorBuffer)
156 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaGetColorBuffer");
157 |     _glfw.osmesa.GetDepthBuffer = (PFN_OSMesaGetDepthBuffer)
158 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaGetDepthBuffer");
159 |     _glfw.osmesa.GetProcAddress = (PFN_OSMesaGetProcAddress)
160 |         _glfw_dlsym(_glfw.osmesa.handle, "OSMesaGetProcAddress");
161 | 
162 |     if (!_glfw.osmesa.CreateContextExt ||
{% endraw %}

```
### glfw/wl_init.c

```c

{% raw %}
633 |     }
634 | 
635 |     _glfw.wl.cursor.theme_load = (PFN_wl_cursor_theme_load)
636 |         _glfw_dlsym(_glfw.wl.cursor.handle, "wl_cursor_theme_load");
637 |     _glfw.wl.cursor.theme_destroy = (PFN_wl_cursor_theme_destroy)
638 |         _glfw_dlsym(_glfw.wl.cursor.handle, "wl_cursor_theme_destroy");
639 |     _glfw.wl.cursor.theme_get_cursor = (PFN_wl_cursor_theme_get_cursor)
640 |         _glfw_dlsym(_glfw.wl.cursor.handle, "wl_cursor_theme_get_cursor");
641 |     _glfw.wl.cursor.image_get_buffer = (PFN_wl_cursor_image_get_buffer)
642 |         _glfw_dlsym(_glfw.wl.cursor.handle, "wl_cursor_image_get_buffer");
643 | 
644 |     _glfw.wl.egl.handle = _glfw_dlopen("libwayland-egl.so.1");
650 |     }
651 | 
652 |     _glfw.wl.egl.window_create = (PFN_wl_egl_window_create)
653 |         _glfw_dlsym(_glfw.wl.egl.handle, "wl_egl_window_create");
654 |     _glfw.wl.egl.window_destroy = (PFN_wl_egl_window_destroy)
655 |         _glfw_dlsym(_glfw.wl.egl.handle, "wl_egl_window_destroy");
656 |     _glfw.wl.egl.window_resize = (PFN_wl_egl_window_resize)
657 |         _glfw_dlsym(_glfw.wl.egl.handle, "wl_egl_window_resize");
658 | 
659 |     _glfw.wl.display = wl_display_connect(NULL);
{% endraw %}

```