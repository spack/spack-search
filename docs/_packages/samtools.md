---
name: "samtools"
layout: package
next_package: sandbox
previous_package: ruby
languages: ['c']
---
## 1.3.1
3 / 530 files match, 1 filtered matches.

 - [htslib-1.3.1/plugin.c](#htslib-131pluginc)

### htslib-1.3.1/plugin.c

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