---
name: "zfs"
layout: package
next_package: libpmemobj-cpp
previous_package: keepalived
languages: ['python', 'c']
---
## 0.8.2
6 / 3305 files match, 2 filtered matches.

 - [lib/libzpool/util.c](#liblibzpoolutilc)
 - [contrib/pyzfs/libzfs_core/bindings/__init__.py](#contribpyzfslibzfs_corebindings__init__py)

### lib/libzpool/util.c

```c

{% raw %}
184 | 	zpoolhdl = dlopen("libzpool.so", RTLD_LAZY);
{% endraw %}

```
### contrib/pyzfs/libzfs_core/bindings/__init__.py

```python

{% raw %}
42 |                         self._lib = self._ffi.dlopen(self._libname)
{% endraw %}

```