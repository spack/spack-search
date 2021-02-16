---
name: "kallisto"
layout: package
next_package: libxrender
previous_package: nanoflann
languages: ['c']
---
## 0.46.2
3 / 270 files match, 1 filtered matches.

 - [ext/htslib/plugin.c](#exthtslibpluginc)

### ext/htslib/plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```