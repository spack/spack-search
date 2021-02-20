---
name: "xorg-server"
layout: package
next_package: xrootd
previous_package: xhmm
languages: ['c']
---
## 1.18.99.901
9 / 1773 files match, 3 filtered matches.

 - [hw/xquartz/GL/indirect.c](#hwxquartzglindirectc)
 - [hw/xfree86/loader/loader.c](#hwxfree86loaderloaderc)
 - [glx/glxdricommon.c](#glxglxdricommonc)

### hw/xquartz/GL/indirect.c

```c

{% raw %}
656 |     }
657 | 
658 |     (void)dlerror();             /*drain dlerror */
659 |     opengl_framework_handle = dlopen(opengl_framework_path, RTLD_LOCAL);
660 | 
661 |     if (!opengl_framework_handle) {
662 |         ErrorF("unable to dlopen %s : %s, using RTLD_DEFAULT\n",
663 |                opengl_framework_path, dlerror());
664 |         opengl_framework_handle = RTLD_DEFAULT;
{% endraw %}

```
### hw/xfree86/loader/loader.c

```c

{% raw %}
109 | 
110 |     xf86Msg(X_INFO, "Loading %s\n", module);
111 | 
112 |     if (!(ret = dlopen(module, RTLD_LAZY | RTLD_GLOBAL))) {
113 |         xf86Msg(X_ERROR, "Failed to load %s: %s\n", module, dlerror());
114 |         if (errmaj)
132 |         return p;
133 | 
134 |     if (!global_scope)
135 |         global_scope = dlopen(NULL, RTLD_LAZY | RTLD_GLOBAL);
136 | 
137 |     if (global_scope)
{% endraw %}

```
### glx/glxdricommon.c

```c

{% raw %}
251 |     snprintf(filename, sizeof filename, "%s/%s_dri.so",
252 |              dri_driver_path, driverName);
253 | 
254 |     driver = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
255 |     if (driver == NULL) {
256 |         LogMessage(X_ERROR, "AIGLX error: dlopen of %s failed (%s)\n",
257 |                    filename, dlerror());
258 |         goto cleanup_failure;
{% endraw %}

```