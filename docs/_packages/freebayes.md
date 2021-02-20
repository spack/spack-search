---
name: "freebayes"
layout: package
next_package: frontier-client
previous_package: foundationdb
languages: ['c']
---
## 1.1.0
6 / 1663 files match, 2 filtered matches.

 - [SeqLib/htslib/plugin.c](#seqlibhtslibpluginc)
 - [vcflib/tabixpp/htslib/plugin.c](#vcflibtabixpphtslibpluginc)

### SeqLib/htslib/plugin.c

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
### vcflib/tabixpp/htslib/plugin.c

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