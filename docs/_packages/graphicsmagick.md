---
name: "graphicsmagick"
layout: package
next_package: grass
previous_package: grafana
languages: ['c']
---
## 1.3.31
16 / 1293 files match, 2 filtered matches.

 - [magick/module.c](#magickmodulec)
 - [magick/nt_base.c](#magicknt_basec)

### magick/module.c

```c

{% raw %}
377 |     handle=lt_dlopen(module_path);
1407 |     handle=lt_dlopen(path);
{% endraw %}

```
### magick/nt_base.c

```c

{% raw %}
768 | %   Method NTdlopen loads a dynamic module into memory and returns a handle
771 | %  The format of the NTdlopen method is:
773 | %      void *NTdlopen(const char *filename)
781 | MagickExport void *NTdlopen(const char *filename)
1744 |   gs_dll_handle = lt_dlopen(dll_path);
{% endraw %}

```