---
name: "kitty"
layout: package
next_package: dpdk
previous_package: libmicrohttpd
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'python']
---
## 0.11.2
17 / 263 files match, 10 filtered matches.

 - [kitty/desktop.c](#kittydesktopc)
 - [kitty/glfw-wrapper.c](#kittyglfw-wrapperc)
 - [kitty/gl-wrapper.c](#kittygl-wrapperc)
 - [glfw/egl_context.c](#glfwegl_contextc)
 - [glfw/vulkan.c](#glfwvulkanc)
 - [glfw/glfw.py](#glfwglfwpy)
 - [glfw/glx_context.c](#glfwglx_contextc)
 - [glfw/x11_init.c](#glfwx11_initc)
 - [glfw/osmesa_context.c](#glfwosmesa_contextc)
 - [glfw/wl_init.c](#glfwwl_initc)

### kitty/desktop.c

```c

{% raw %}
33 |     if (!done) {
34 |         done = true;
35 | 
36 |         libsn_handle = dlopen(libname, RTLD_LAZY);
37 |         if (libsn_handle == NULL) {
38 |             PyErr_Format(PyExc_OSError, "Failed to load %s with error: %s", libname, dlerror());
{% endraw %}

```
### kitty/glfw-wrapper.c

```c

{% raw %}
9 | const char*
10 | load_glfw(const char* path) {
11 |     static char buf[2048];
12 |     handle = dlopen(path, RTLD_LAZY);
13 |     if (handle == NULL) fail("Failed to dlopen %s with error: %s", path, dlerror());
14 |     dlerror();
15 | 
{% endraw %}

```
### kitty/gl-wrapper.c

```c

{% raw %}
105 | #endif
106 |     unsigned int index = 0;
107 |     for(index = 0; index < (sizeof(NAMES) / sizeof(NAMES[0])); index++) {
108 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
109 |         if(libGL != NULL) {
110 | #ifdef __APPLE__
{% endraw %}

```
### glfw/egl_context.c

```c

{% raw %}
321 | 
322 |     for (i = 0;  sonames[i];  i++)
323 |     {
324 |         _glfw.egl.handle = _glfw_dlopen(sonames[i]);
325 |         if (_glfw.egl.handle)
326 |             break;
676 |             if (_glfw.egl.prefix != (strncmp(sonames[i], "lib", 3) == 0))
677 |                 continue;
678 | 
679 |             window->context.egl.client = _glfw_dlopen(sonames[i]);
680 |             if (window->context.egl.client)
681 |                 break;
{% endraw %}

```
### glfw/vulkan.c

```c

{% raw %}
49 | 
50 | #if !defined(_GLFW_VULKAN_STATIC)
51 | #if defined(_GLFW_VULKAN_LIBRARY)
52 |     _glfw.vk.handle = _glfw_dlopen(_GLFW_VULKAN_LIBRARY);
53 | #elif defined(_GLFW_WIN32)
54 |     _glfw.vk.handle = _glfw_dlopen("vulkan-1.dll");
55 | #elif defined(_GLFW_COCOA)
56 |     _glfw.vk.handle = _glfw_dlopen("libvulkan.1.dylib");
57 | #else
58 |     _glfw.vk.handle = _glfw_dlopen("libvulkan.so.1");
59 | #endif
60 |     if (!_glfw.vk.handle)
{% endraw %}

```
### glfw/glfw.py

```python

{% raw %}
244 | const char*
245 | load_glfw(const char* path) {
246 |     static char buf[2048];
247 |     handle = dlopen(path, RTLD_LAZY);
248 |     if (handle == NULL) fail("Failed to dlopen %s with error: %s", path, dlerror());
249 |     dlerror();
250 | 
{% endraw %}

```
### glfw/glx_context.c

```c

{% raw %}
270 | 
271 |     for (i = 0;  sonames[i];  i++)
272 |     {
273 |         _glfw.glx.handle = _glfw_dlopen(sonames[i]);
274 |         if (_glfw.glx.handle)
275 |             break;
{% endraw %}

```
### glfw/x11_init.c

```c

{% raw %}
150 | //
151 | static GLFWbool initExtensions(void)
152 | {
153 |     _glfw.x11.vidmode.handle = _glfw_dlopen("libXxf86vm.so.1");
154 |     if (_glfw.x11.vidmode.handle)
155 |     {
169 |     }
170 | 
171 | #if defined(__CYGWIN__)
172 |     _glfw.x11.xi.handle = _glfw_dlopen("libXi-6.so");
173 | #else
174 |     _glfw.x11.xi.handle = _glfw_dlopen("libXi.so.6");
175 | #endif
176 |     if (_glfw.x11.xi.handle)
199 |     }
200 | 
201 | #if defined(__CYGWIN__)
202 |     _glfw.x11.randr.handle = _glfw_dlopen("libXrandr-2.so");
203 | #else
204 |     _glfw.x11.randr.handle = _glfw_dlopen("libXrandr.so.2");
205 | #endif
206 |     if (_glfw.x11.randr.handle)
291 |     }
292 | 
293 | #if defined(__CYGWIN__)
294 |     _glfw.x11.xcursor.handle = _glfw_dlopen("libXcursor-1.so");
295 | #else
296 |     _glfw.x11.xcursor.handle = _glfw_dlopen("libXcursor.so.1");
297 | #endif
298 |     if (_glfw.x11.xcursor.handle)
306 |     }
307 | 
308 | #if defined(__CYGWIN__)
309 |     _glfw.x11.xinerama.handle = _glfw_dlopen("libXinerama-1.so");
310 | #else
311 |     _glfw.x11.xinerama.handle = _glfw_dlopen("libXinerama.so.1");
312 | #endif
313 |     if (_glfw.x11.xinerama.handle)
329 |     }
330 | 
331 | #if defined(__CYGWIN__)
332 |     _glfw.x11.xrender.handle = _glfw_dlopen("libXrender-1.so");
333 | #else
334 |     _glfw.x11.xrender.handle = _glfw_dlopen("libXrender.so.1");
335 | #endif
336 |     if (_glfw.x11.xrender.handle)
{% endraw %}

```
### glfw/osmesa_context.c

```c

{% raw %}
133 | 
134 |     for (i = 0;  sonames[i];  i++)
135 |     {
136 |         _glfw.osmesa.handle = _glfw_dlopen(sonames[i]);
137 |         if (_glfw.osmesa.handle)
138 |             break;
{% endraw %}

```
### glfw/wl_init.c

```c

{% raw %}
624 |         return GLFW_FALSE;
625 |     }
626 | 
627 |     _glfw.wl.cursor.handle = _glfw_dlopen("libwayland-cursor.so.0");
628 |     if (!_glfw.wl.cursor.handle)
629 |     {
641 |     _glfw.wl.cursor.image_get_buffer = (PFN_wl_cursor_image_get_buffer)
642 |         _glfw_dlsym(_glfw.wl.cursor.handle, "wl_cursor_image_get_buffer");
643 | 
644 |     _glfw.wl.egl.handle = _glfw_dlopen("libwayland-egl.so.1");
645 |     if (!_glfw.wl.egl.handle)
646 |     {
{% endraw %}

```