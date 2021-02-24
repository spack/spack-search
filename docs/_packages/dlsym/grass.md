---
name: "grass"
layout: package
next_package: turbine
previous_package: rocfft
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.8.2
2 / 6347 files match, 1 filtered matches.

 - [lib/raster/gdal.c](#librastergdalc)

### lib/raster/gdal.c

```c

{% raw %}
78 |     void *sym;
79 | 
80 | # ifdef __unix__
81 |     sym = dlsym(library_h, name);
82 | # endif
83 | # ifdef _WIN32
{% endraw %}

```