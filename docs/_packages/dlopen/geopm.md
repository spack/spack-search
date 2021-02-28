---
name: "geopm"
layout: package
next_package: rose
previous_package: dimemas
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.5.1
5 / 462 files match, 1 filtered matches.

 - [src/geopm_plugin.c](#srcgeopm_pluginc)

### src/geopm_plugin.c

```c

{% raw %}
124 |                         if ((geopm_name_begins_with(file->fts_name, "libgeopmagent_") ||
125 |                              geopm_name_begins_with(file->fts_name, "libgeopmiogroup_") ||
126 |                              geopm_name_begins_with(file->fts_name, "libgeopmcomm_")) &&
127 |                             dlopen(file->fts_path, RTLD_NOLOAD) == NULL) {
128 |                             if (NULL == dlopen(file->fts_path, RTLD_LAZY)) {
129 | #ifdef GEOPM_DEBUG
130 |                                 fprintf(stderr, "Warning: failed to dlopen plugin %s.\n", file->fts_path);
131 | #endif
132 |                             }
135 |                     else {
136 |                         if ((geopm_name_begins_with(file->fts_name, "libgeopmpi_") ||
137 |                              geopm_name_begins_with(file->fts_name, "libgeopmiogroup_")) &&
138 |                             dlopen(file->fts_path, RTLD_NOLOAD) == NULL) {
139 |                             if (NULL == dlopen(file->fts_path, RTLD_LAZY)) {
140 | #ifdef GEOPM_DEBUG
141 |                                 fprintf(stderr, "Warning: failed to dlopen plugin %s.\n", file->fts_path);
142 | #endif
143 |                             }
{% endraw %}

```