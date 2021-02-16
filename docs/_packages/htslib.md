---
name: "htslib"
layout: package
next_package: httpd
previous_package: hsakmt-roct
languages: ['c']
---
## 1.4
3 / 199 files match, 1 filtered matches.

 - [plugin.c](#pluginc)

### plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```