---
name: "py-pyzmq"
layout: package
next_package: libwebp
previous_package: py-easybuild-easyconfigs
languages: ['python']
---
## 16.0.2
1 / 271 files match

 - [zmq/__init__.py](#zmq__init__py)

### zmq/__init__.py

```python

{% raw %}
9 |     dlopen = hasattr(sys, 'getdlopenflags') # unix-only
10 |     if dlopen:
11 |         dlflags = sys.getdlopenflags()
12 |         sys.setdlopenflags(ctypes.RTLD_GLOBAL | dlflags)
25 |         if dlopen:
26 |             sys.setdlopenflags(dlflags)
{% endraw %}

```