---
name: "py-rpy2"
layout: package
next_package: py-scipy
previous_package: py-pyzmq
languages: ['python']
---
## 3.0.4
1 / 55 files match, 1 filtered matches.

 - [rpy/rinterface_lib/openrlib.py](#rpyrinterface_libopenrlibpy)

### rpy/rinterface_lib/openrlib.py

```python

{% raw %}
7 | R_HOME = rpy2.situation.get_r_home()
8 | 
9 | 
10 | def _dlopen_rlib(r_home: str):
11 |     """Open R's shared C library."""
12 |     if r_home is None:
13 |         raise ValueError('r_home is None. '
14 |                          'Try python -m rpy2.situation')
15 |     lib_path = rpy2.situation.get_rlib_path(r_home, platform.system())
16 |     rlib = ffi.dlopen(lib_path)
17 |     return rlib
18 | 
19 | 
20 | rlib = _dlopen_rlib(R_HOME)
21 | 
22 | 
{% endraw %}

```