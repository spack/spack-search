---
name: "r-rhtslib"
layout: package
next_package: r-rmpi
previous_package: r-rgraphviz
languages: ['c']
---
## 1.12.1
3 / 232 files match, 1 filtered matches.

 - [src/htslib-1.7/plugin.c](#srchtslib-17pluginc)

### src/htslib-1.7/plugin.c

```c

{% raw %}
133 | 
134 | void *load_plugin(void **pluginp, const char *filename, const char *symbol)
135 | {
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
137 |     if (lib == NULL) goto error;
138 | 
139 |     void *sym = dlsym(lib, symbol);
140 |     if (sym == NULL) {
141 |         // Reopen the plugin with RTLD_GLOBAL and check for uniquified symbol
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
143 |         if (libg == NULL) goto error;
144 |         dlclose(lib);
{% endraw %}

```