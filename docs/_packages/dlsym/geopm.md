---
name: "geopm"
layout: package
next_package: ocaml
previous_package: spot
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.3.0
3 / 366 files match, 1 filtered matches.

 - [src/geopm_plugin.c](#srcgeopm_pluginc)

### src/geopm_plugin.c

```c

{% raw %}
89 |                      strstr(file->fts_name, ".dylib"))) {
90 |                     plugin = dlopen(file->fts_path, RTLD_LAZY);
91 |                     if (plugin != NULL) {
92 |                         register_func = (int (*)(int, struct geopm_factory_c *, void *)) dlsym(plugin, "geopm_plugin_register");
93 |                         if (register_func != NULL) {
94 |                             register_func(plugin_type, factory, plugin);
{% endraw %}

```