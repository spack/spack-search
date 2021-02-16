---
name: "xorg-server"
layout: package
next_package: gdal
previous_package: perl
languages: ['c']
---
## 1.18.99.901
9 / 1773 files match

 - [hw/xquartz/GL/indirect.c](#hwxquartzglindirectc)
 - [hw/xfree86/loader/loader.c](#hwxfree86loaderloaderc)
 - [glx/glxdricommon.c](#glxglxdricommonc)

### hw/xquartz/GL/indirect.c

```c

{% raw %}
659 |     opengl_framework_handle = dlopen(opengl_framework_path, RTLD_LOCAL);
662 |         ErrorF("unable to dlopen %s : %s, using RTLD_DEFAULT\n",
{% endraw %}

```
### hw/xfree86/loader/loader.c

```c

{% raw %}
112 |     if (!(ret = dlopen(module, RTLD_LAZY | RTLD_GLOBAL))) {
135 |         global_scope = dlopen(NULL, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### glx/glxdricommon.c

```c

{% raw %}
254 |     driver = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
256 |         LogMessage(X_ERROR, "AIGLX error: dlopen of %s failed (%s)\n",
{% endraw %}

```