---
name: "geopm"
layout: package
next_package: krb5
previous_package: esmf
languages: ['c']
---
## 0.5.1
5 / 462 files match

 - [src/geopm_plugin.c](#srcgeopm_pluginc)

### src/geopm_plugin.c

```c

{% raw %}
127 |                             dlopen(file->fts_path, RTLD_NOLOAD) == NULL) {
128 |                             if (NULL == dlopen(file->fts_path, RTLD_LAZY)) {
130 |                                 fprintf(stderr, "Warning: failed to dlopen plugin %s.\n", file->fts_path);
138 |                             dlopen(file->fts_path, RTLD_NOLOAD) == NULL) {
139 |                             if (NULL == dlopen(file->fts_path, RTLD_LAZY)) {
141 |                                 fprintf(stderr, "Warning: failed to dlopen plugin %s.\n", file->fts_path);
{% endraw %}

```