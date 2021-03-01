---
name: "nest"
layout: package
next_package: netdata
previous_package: ncl
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['python']
---
## 2.14.0
2 / 1388 files match, 1 filtered matches.

 - [pynest/nest/__init__.py](#pynestnest__init__py)

### pynest/nest/__init__.py

```python

{% raw %}
43 | # yet other libraries.
44 | try:
45 |     # Python 3.3 and later has flags in os
46 |     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
47 | except AttributeError:
48 |     # Python 2.6 and 2.7 have flags in ctypes, but RTLD_NOW may only
52 |     # first try dl and DLFCN, then ctypes just for OSX.
53 |     try:
54 |         import dl
55 |         sys.setdlopenflags(dl.RTLD_GLOBAL | dl.RTLD_NOW)
56 |     except (ImportError, AttributeError):
57 |         try:
58 |             import DLFCN
59 |             sys.setdlopenflags(DLFCN.RTLD_GLOBAL | DLFCN.RTLD_NOW)
60 |         except (ImportError, AttributeError):
61 |             import ctypes
62 |             try:
63 |                 sys.setdlopenflags(ctypes.RTLD_GLOBAL | ctypes.RTLD_NOW)
64 |             except AttributeError:
65 |                 # We must test this last, since it is the only case without
66 |                 # RTLD_NOW (OSX)
67 |                 sys.setdlopenflags(ctypes.RTLD_GLOBAL)
68 | 
69 | from . import pynestkernel as _kernel      # noqa
{% endraw %}

```