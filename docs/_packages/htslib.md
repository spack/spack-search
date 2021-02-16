---
name: "htslib"
layout: package
next_package: glusterfs
previous_package: cityhash
languages: ['c']
---
## 1.4
3 / 199 files match

 - [plugin.c](#pluginc)

### plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```