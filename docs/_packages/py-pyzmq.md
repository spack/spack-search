---
name: "py-pyzmq"
layout: package
next_package: py-rpy2
previous_package: py-pyside2
languages: ['python']
---
## 16.0.2
1 / 271 files match, 1 filtered matches.

 - [zmq/__init__.py](#zmq__init__py)

### zmq/__init__.py

```python

{% raw %}
6 | def _load_libzmq():
7 |     """load bundled libzmq if there is one"""
8 |     import sys, ctypes, platform
9 |     dlopen = hasattr(sys, 'getdlopenflags') # unix-only
10 |     if dlopen:
11 |         dlflags = sys.getdlopenflags()
12 |         sys.setdlopenflags(ctypes.RTLD_GLOBAL | dlflags)
13 |     try:
14 |         from . import libzmq
22 |             # otherwise symbols won't be globally available
23 |             ctypes.CDLL(libzmq.__file__, ctypes.RTLD_GLOBAL)
24 |     finally:
25 |         if dlopen:
26 |             sys.setdlopenflags(dlflags)
27 | 
28 | _load_libzmq()
{% endraw %}

```