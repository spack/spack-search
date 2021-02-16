---
name: "glfw"
layout: package
next_package: povray
previous_package: biobambam2
languages: ['c']
---
## 3.1.2
6 / 132 files match, 2 filtered matches.

 - [src/egl_context.c](#srcegl_contextc)
 - [src/glx_context.c](#srcglx_contextc)

### src/egl_context.c

```c

{% raw %}
200 |         _glfw.egl.handle = _glfw_dlopen(sonames[i]);
508 |             window->egl.client = _glfw_dlopen(sonames[i]);
{% endraw %}

```
### src/glx_context.c

```c

{% raw %}
167 |     _glfw.glx.handle = dlopen(soname, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```