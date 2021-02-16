---
name: "kitty"
layout: package
next_package: kmod
previous_package: keepalived
languages: ['python', 'c']
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
36 |         libsn_handle = dlopen(libname, RTLD_LAZY);
{% endraw %}

```
### kitty/glfw-wrapper.c

```c

{% raw %}
12 |     handle = dlopen(path, RTLD_LAZY);
13 |     if (handle == NULL) fail("Failed to dlopen %s with error: %s", path, dlerror());
{% endraw %}

```
### kitty/gl-wrapper.c

```c

{% raw %}
108 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### glfw/egl_context.c

```c

{% raw %}
324 |         _glfw.egl.handle = _glfw_dlopen(sonames[i]);
679 |             window->context.egl.client = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### glfw/vulkan.c

```c

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
### glfw/glx_context.c

```c

{% raw %}
273 |         _glfw.glx.handle = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### glfw/x11_init.c

```c

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
### glfw/osmesa_context.c

```c

{% raw %}
136 |         _glfw.osmesa.handle = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### glfw/wl_init.c

```c

{% raw %}
627 |     _glfw.wl.cursor.handle = _glfw_dlopen("libwayland-cursor.so.0");
644 |     _glfw.wl.egl.handle = _glfw_dlopen("libwayland-egl.so.1");
{% endraw %}

```