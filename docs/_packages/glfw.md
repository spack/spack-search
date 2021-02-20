---
name: "glfw"
layout: package
next_package: glib
previous_package: glew
languages: ['c']
---
## 3.1.2
6 / 132 files match, 2 filtered matches.

 - [src/egl_context.c](#srcegl_contextc)
 - [src/glx_context.c](#srcglx_contextc)

### src/egl_context.c

```c

{% raw %}
197 | 
198 |     for (i = 0;  sonames[i];  i++)
199 |     {
200 |         _glfw.egl.handle = _glfw_dlopen(sonames[i]);
201 |         if (_glfw.egl.handle)
202 |             break;
505 | 
506 |         for (i = 0;  sonames[i];  i++)
507 |         {
508 |             window->egl.client = _glfw_dlopen(sonames[i]);
509 |             if (window->egl.client)
510 |                 break;
{% endraw %}

```
### src/glx_context.c

```c

{% raw %}
164 |     if (!_glfwCreateContextTLS())
165 |         return GL_FALSE;
166 | 
167 |     _glfw.glx.handle = dlopen(soname, RTLD_LAZY | RTLD_GLOBAL);
168 |     if (!_glfw.glx.handle)
169 |     {
{% endraw %}

```