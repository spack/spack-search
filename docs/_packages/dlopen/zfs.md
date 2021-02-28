---
name: "zfs"
layout: package
next_package: pythia8
previous_package: pmix
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'python']
---
## 0.8.2
6 / 3305 files match, 2 filtered matches.

 - [lib/libzpool/util.c](#liblibzpoolutilc)
 - [contrib/pyzfs/libzfs_core/bindings/__init__.py](#contribpyzfslibzfs_corebindings__init__py)

### lib/libzpool/util.c

```c

{% raw %}
181 | 		return (EINVAL);
182 | 	}
183 | 
184 | 	zpoolhdl = dlopen("libzpool.so", RTLD_LAZY);
185 | 	if (zpoolhdl != NULL) {
186 | 		uint32_t *var;
{% endraw %}

```
### contrib/pyzfs/libzfs_core/bindings/__init__.py

```python

{% raw %}
39 |             if self._lib is None:
40 |                 with self._lock:
41 |                     if self._lib is None:
42 |                         self._lib = self._ffi.dlopen(self._libname)
43 | 
44 |             return getattr(self._lib, name)
{% endraw %}

```