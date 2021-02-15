---
name: "kitty"
layout: package
next_package: ncbi-toolkit
previous_package: globalarrays
languages: ['cpp', 'python']
---
## 0.11.2
17 / 263 files match

 - [kitty/desktop.c](#kittydesktopc)
 - [kitty/glfw-wrapper.c](#kittyglfw-wrapperc)
 - [kitty/gl-wrapper.c](#kittygl-wrapperc)
 - [glfw/egl_context.c](#glfwegl_contextc)
 - [glfw/x11_platform.h](#glfwx11_platformh)
 - [glfw/null_platform.h](#glfwnull_platformh)
 - [glfw/vulkan.c](#glfwvulkanc)
 - [glfw/glfw.py](#glfwglfwpy)
 - [glfw/win32_platform.h](#glfwwin32_platformh)
 - [glfw/glx_context.c](#glfwglx_contextc)
 - [glfw/nsgl_context.h](#glfwnsgl_contexth)
 - [glfw/x11_init.c](#glfwx11_initc)
 - [glfw/cocoa_platform.h](#glfwcocoa_platformh)
 - [glfw/glx_context.h](#glfwglx_contexth)
 - [glfw/osmesa_context.c](#glfwosmesa_contextc)
 - [glfw/wl_platform.h](#glfwwl_platformh)
 - [glfw/wl_init.c](#glfwwl_initc)

### kitty/desktop.c

```cpp

{% raw %}
36 |         libsn_handle = dlopen(libname, RTLD_LAZY);
{% endraw %}

```
### kitty/glfw-wrapper.c

```cpp

{% raw %}
12 |     handle = dlopen(path, RTLD_LAZY);
13 |     if (handle == NULL) fail("Failed to dlopen %s with error: %s", path, dlerror());
{% endraw %}

```
### kitty/gl-wrapper.c

```cpp

{% raw %}
108 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### glfw/egl_context.c

```cpp

{% raw %}
324 |         _glfw.egl.handle = _glfw_dlopen(sonames[i]);
679 |             window->context.egl.client = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### glfw/x11_platform.h

```cpp

{% raw %}
165 | #define _glfw_dlopen(name) dlopen(name, RTLD_LAZY | RTLD_LOCAL)
{% endraw %}

```
### glfw/null_platform.h

```cpp

{% raw %}
45 |  #define _glfw_dlopen(name) LoadLibraryA(name)
49 |  #define _glfw_dlopen(name) dlopen(name, RTLD_LAZY | RTLD_LOCAL)
{% endraw %}

```
### glfw/vulkan.c

```cpp

{% raw %}
52 |     _glfw.vk.handle = _glfw_dlopen(_GLFW_VULKAN_LIBRARY);
54 |     _glfw.vk.handle = _glfw_dlopen("vulkan-1.dll");
56 |     _glfw.vk.handle = _glfw_dlopen("libvulkan.1.dylib");
58 |     _glfw.vk.handle = _glfw_dlopen("libvulkan.so.1");
{% endraw %}

```
### glfw/glfw.py

```python

{% raw %}
247 |     handle = dlopen(path, RTLD_LAZY);
248 |     if (handle == NULL) fail("Failed to dlopen %s with error: %s", path, dlerror());
{% endraw %}

```
### glfw/win32_platform.h

```cpp

{% raw %}
248 | #define _glfw_dlopen(name) LoadLibraryA(name)
{% endraw %}

```
### glfw/glx_context.c

```cpp

{% raw %}
273 |         _glfw.glx.handle = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### glfw/nsgl_context.h

```cpp

{% raw %}
43 |     // dlopen handle for OpenGL.framework (for glfwGetProcAddress)
{% endraw %}

```
### glfw/x11_init.c

```cpp

{% raw %}
153 |     _glfw.x11.vidmode.handle = _glfw_dlopen("libXxf86vm.so.1");
172 |     _glfw.x11.xi.handle = _glfw_dlopen("libXi-6.so");
174 |     _glfw.x11.xi.handle = _glfw_dlopen("libXi.so.6");
202 |     _glfw.x11.randr.handle = _glfw_dlopen("libXrandr-2.so");
204 |     _glfw.x11.randr.handle = _glfw_dlopen("libXrandr.so.2");
294 |     _glfw.x11.xcursor.handle = _glfw_dlopen("libXcursor-1.so");
296 |     _glfw.x11.xcursor.handle = _glfw_dlopen("libXcursor.so.1");
309 |     _glfw.x11.xinerama.handle = _glfw_dlopen("libXinerama-1.so");
311 |     _glfw.x11.xinerama.handle = _glfw_dlopen("libXinerama.so.1");
332 |     _glfw.x11.xrender.handle = _glfw_dlopen("libXrender-1.so");
334 |     _glfw.x11.xrender.handle = _glfw_dlopen("libXrender.so.1");
{% endraw %}

```
### glfw/cocoa_platform.h

```cpp

{% raw %}
58 | #define _glfw_dlopen(name) dlopen(name, RTLD_LAZY | RTLD_LOCAL)
{% endraw %}

```
### glfw/glx_context.h

```cpp

{% raw %}
130 |     // dlopen handle for libGL.so.1
{% endraw %}

```
### glfw/osmesa_context.c

```cpp

{% raw %}
136 |         _glfw.osmesa.handle = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### glfw/wl_platform.h

```cpp

{% raw %}
61 | #define _glfw_dlopen(name) dlopen(name, RTLD_LAZY | RTLD_LOCAL)
{% endraw %}

```
### glfw/wl_init.c

```cpp

{% raw %}
627 |     _glfw.wl.cursor.handle = _glfw_dlopen("libwayland-cursor.so.0");
644 |     _glfw.wl.egl.handle = _glfw_dlopen("libwayland-egl.so.1");
{% endraw %}

```