---
name: "glfw"
layout: package
next_package: povray
previous_package: biobambam2
languages: ['cpp']
---
## 3.1.2
6 / 132 files match

 - [README.md](#readmemd)
 - [src/egl_context.c](#srcegl_contextc)
 - [src/glx_context.c](#srcglx_contextc)
 - [src/nsgl_context.h](#srcnsgl_contexth)
 - [src/glx_context.h](#srcglx_contexth)
 - [src/egl_context.h](#srcegl_contexth)

### README.md

```

{% raw %}
115 |  - [GLX] Added dependency on `libdl` on systems where it provides `dlopen`
117 |  - [GLX] Removed `_GLFW_HAS_GLXGETPROCADDRESS*` and `_GLFW_HAS_DLOPEN`
{% endraw %}

```
### src/egl_context.c

```cpp

{% raw %}
200 |         _glfw.egl.handle = _glfw_dlopen(sonames[i]);
508 |             window->egl.client = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### src/glx_context.c

```cpp

{% raw %}
167 |     _glfw.glx.handle = dlopen(soname, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/nsgl_context.h

```cpp

{% raw %}
48 |     // dlopen handle for OpenGL.framework (for glfwGetProcAddress)
{% endraw %}

```
### src/glx_context.h

```cpp

{% raw %}
89 |     // dlopen handle for libGL.so.1
{% endraw %}

```
### src/egl_context.h

```cpp

{% raw %}
31 |  #define _glfw_dlopen(name) LoadLibraryA(name)
36 |  #define _glfw_dlopen(name) dlopen(name, RTLD_LAZY | RTLD_LOCAL)
{% endraw %}

```