---
name: "py-rpy2"
layout: package
next_package: py-scipy
previous_package: py-quast
languages: ['python']
---
## 3.0.4
1 / 55 files match, 1 filtered matches.

 - [rpy/rinterface_lib/openrlib.py](#rpyrinterface_libopenrlibpy)

### rpy/rinterface_lib/openrlib.py

```python

{% raw %}
10 | def _dlopen_rlib(r_home: str):
16 |     rlib = ffi.dlopen(lib_path)
20 | rlib = _dlopen_rlib(R_HOME)
{% endraw %}

```