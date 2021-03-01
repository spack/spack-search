---
name: "glfw"
layout: package
next_package: global
previous_package: glew
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.1.2
3 / 132 files match, 2 filtered matches.

 - [src/egl_context.c](#srcegl_contextc)
 - [src/glx_context.c](#srcglx_contextc)

### src/egl_context.c

```c

{% raw %}
209 |     }
210 | 
211 |     _glfw.egl.GetConfigAttrib =
212 |         _glfw_dlsym(_glfw.egl.handle, "eglGetConfigAttrib");
213 |     _glfw.egl.GetConfigs =
214 |         _glfw_dlsym(_glfw.egl.handle, "eglGetConfigs");
215 |     _glfw.egl.GetDisplay =
216 |         _glfw_dlsym(_glfw.egl.handle, "eglGetDisplay");
217 |     _glfw.egl.GetError =
218 |         _glfw_dlsym(_glfw.egl.handle, "eglGetError");
219 |     _glfw.egl.Initialize =
220 |         _glfw_dlsym(_glfw.egl.handle, "eglInitialize");
221 |     _glfw.egl.Terminate =
222 |         _glfw_dlsym(_glfw.egl.handle, "eglTerminate");
223 |     _glfw.egl.BindAPI =
224 |         _glfw_dlsym(_glfw.egl.handle, "eglBindAPI");
225 |     _glfw.egl.CreateContext =
226 |         _glfw_dlsym(_glfw.egl.handle, "eglCreateContext");
227 |     _glfw.egl.DestroySurface =
228 |         _glfw_dlsym(_glfw.egl.handle, "eglDestroySurface");
229 |     _glfw.egl.DestroyContext =
230 |         _glfw_dlsym(_glfw.egl.handle, "eglDestroyContext");
231 |     _glfw.egl.CreateWindowSurface =
232 |         _glfw_dlsym(_glfw.egl.handle, "eglCreateWindowSurface");
233 |     _glfw.egl.MakeCurrent =
234 |         _glfw_dlsym(_glfw.egl.handle, "eglMakeCurrent");
235 |     _glfw.egl.SwapBuffers =
236 |         _glfw_dlsym(_glfw.egl.handle, "eglSwapBuffers");
237 |     _glfw.egl.SwapInterval =
238 |         _glfw_dlsym(_glfw.egl.handle, "eglSwapInterval");
239 |     _glfw.egl.QueryString =
240 |         _glfw_dlsym(_glfw.egl.handle, "eglQueryString");
241 |     _glfw.egl.GetProcAddress =
242 |         _glfw_dlsym(_glfw.egl.handle, "eglGetProcAddress");
243 | 
244 |     _glfw.egl.display =
643 | 
644 |     if (window->egl.client)
645 |     {
646 |         GLFWglproc proc = (GLFWglproc) _glfw_dlsym(window->egl.client, procname);
647 |         if (proc)
648 |             return proc;
{% endraw %}

```
### src/glx_context.c

```c

{% raw %}
172 |     }
173 | 
174 |     _glfw.glx.GetFBConfigs =
175 |         dlsym(_glfw.glx.handle, "glXGetFBConfigs");
176 |     _glfw.glx.GetFBConfigAttrib =
177 |         dlsym(_glfw.glx.handle, "glXGetFBConfigAttrib");
178 |     _glfw.glx.GetClientString =
179 |         dlsym(_glfw.glx.handle, "glXGetClientString");
180 |     _glfw.glx.QueryExtension =
181 |         dlsym(_glfw.glx.handle, "glXQueryExtension");
182 |     _glfw.glx.QueryVersion =
183 |         dlsym(_glfw.glx.handle, "glXQueryVersion");
184 |     _glfw.glx.DestroyContext =
185 |         dlsym(_glfw.glx.handle, "glXDestroyContext");
186 |     _glfw.glx.MakeCurrent =
187 |         dlsym(_glfw.glx.handle, "glXMakeCurrent");
188 |     _glfw.glx.SwapBuffers =
189 |         dlsym(_glfw.glx.handle, "glXSwapBuffers");
190 |     _glfw.glx.QueryExtensionsString =
191 |         dlsym(_glfw.glx.handle, "glXQueryExtensionsString");
192 |     _glfw.glx.CreateNewContext =
193 |         dlsym(_glfw.glx.handle, "glXCreateNewContext");
194 |     _glfw.glx.GetVisualFromFBConfig =
195 |         dlsym(_glfw.glx.handle, "glXGetVisualFromFBConfig");
196 |     _glfw.glx.GetProcAddress =
197 |         dlsym(_glfw.glx.handle, "glXGetProcAddress");
198 |     _glfw.glx.GetProcAddressARB =
199 |         dlsym(_glfw.glx.handle, "glXGetProcAddressARB");
200 | 
201 |     if (!_glfw_glXQueryExtension(_glfw.x11.display,
560 |     else if (_glfw.glx.GetProcAddressARB)
561 |         return _glfw.glx.GetProcAddressARB((const GLubyte*) procname);
562 |     else
563 |         return dlsym(_glfw.glx.handle, procname);
564 | }
565 | 
{% endraw %}

```