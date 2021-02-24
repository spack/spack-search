---
name: "grass"
layout: package
next_package: turbine
previous_package: rocfft
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.8.2
3 / 6347 files match, 1 filtered matches.

 - [lib/raster/gdal.c](#librastergdalc)

### lib/raster/gdal.c

```c

{% raw %}
93 | static void try_load_library(const char *name)
94 | {
95 | # ifdef __unix__
96 |     library_h = dlopen(name, RTLD_NOW);
97 | # endif
98 | # ifdef _WIN32
{% endraw %}

```