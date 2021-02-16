---
name: "py-cyvcf2"
layout: package
next_package: mono
previous_package: vim
languages: ['c']
---
## 0.11.7
2 / 145 files match, 1 filtered matches.

 - [htslib/plugin.c](#htslibpluginc)

### htslib/plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```