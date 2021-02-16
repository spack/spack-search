---
name: "imagemagick"
layout: package
next_package: grib-api
previous_package: babeltrace
languages: ['c']
---
## 7.0.8-7
8 / 2378 files match

 - [MagickCore/opencl.c](#magickcoreopenclc)
 - [MagickCore/nt-base.c](#magickcorent-basec)
 - [MagickCore/module.c](#magickcoremodulec)

### MagickCore/opencl.c

```c

{% raw %}
2462 |   openCL_library->library=(void *)dlopen("libOpenCL.so", RTLD_NOW);
{% endraw %}

```
### MagickCore/nt-base.c

```c

{% raw %}
1543 |   ghost_handle=lt_dlopen(path);
{% endraw %}

```
### MagickCore/module.c

```c

{% raw %}
990 |   handle=(ModuleHandle) lt_dlopen(path);
1271 |   handle=(ModuleHandle) lt_dlopen(path);
{% endraw %}

```