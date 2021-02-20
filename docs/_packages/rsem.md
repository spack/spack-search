---
name: "rsem"
layout: package
next_package: rsync
previous_package: rr
languages: ['c']
---
## 1.3.1
3 / 2717 files match, 1 filtered matches.

 - [samtools-1.3/htslib-1.3/plugin.c](#samtools-13htslib-13pluginc)

### samtools-1.3/htslib-1.3/plugin.c

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