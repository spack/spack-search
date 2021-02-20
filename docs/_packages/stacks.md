---
name: "stacks"
layout: package
next_package: stat
previous_package: sst-transports
languages: ['c']
---
## 1.46
2 / 250 files match, 1 filtered matches.

 - [htslib/plugin.c](#htslibpluginc)

### htslib/plugin.c

```c

{% raw %}
136 | 
137 | void *load_plugin(void **pluginp, const char *filename, const char *symbol)
138 | {
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
140 |     if (lib == NULL) goto error;
141 | 
{% endraw %}

```