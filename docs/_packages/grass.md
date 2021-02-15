---
name: "grass"
layout: package
next_package: libmad
previous_package: ncl
languages: ['cpp', 'python']
---
## 7.8.2
3 / 6347 files match

 - [lib/python/ctypes/loader.py](#libpythonctypesloaderpy)
 - [lib/python/ctypes/ctypesgencore/libraryloader.py](#libpythonctypesctypesgencorelibraryloaderpy)
 - [lib/raster/gdal.c](#librastergdalc)

### lib/python/ctypes/loader.py

```python

{% raw %}
68 |             # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
{% endraw %}

```
### lib/python/ctypes/ctypesgencore/libraryloader.py

```python

{% raw %}
69 |             # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
{% endraw %}

```
### lib/raster/gdal.c

```cpp

{% raw %}
96 |     library_h = dlopen(name, RTLD_NOW);
{% endraw %}

```