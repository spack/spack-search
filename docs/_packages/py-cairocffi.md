---
name: "py-cairocffi"
layout: package
next_package: py-cffi
previous_package: py-billiard
languages: ['python']
---
## 1.0.2
2 / 20 files match, 2 filtered matches.

 - [cairocffi/__init__.py](#cairocffi__init__py)
 - [cairocffi/pixbuf.py](#cairocffipixbufpy)

### cairocffi/__init__.py

```python

{% raw %}
21 | version_info = (1, 16, 0)
22 | 
23 | 
24 | def dlopen(ffi, *names):
25 |     """Try various names for the same library, for different platforms."""
26 |     for name in names:
27 |         for lib_name in (name, 'lib' + name):
28 |             try:
29 |                 path = ctypes.util.find_library(lib_name)
30 |                 lib = ffi.dlopen(path or lib_name)
31 |                 if lib:
32 |                     return lib
33 |             except OSError:
34 |                 pass
35 |     raise OSError("dlopen() failed to load a library: %s" % ' / '.join(names))
36 | 
37 | 
38 | cairo = dlopen(ffi, 'cairo', 'cairo-2', 'cairo-gobject-2', 'cairo.so.2')
39 | 
40 | 
{% endraw %}

```
### cairocffi/pixbuf.py

```python

{% raw %}
13 | from functools import partial
14 | from io import BytesIO
15 | 
16 | from . import Context, ImageSurface, constants, dlopen
17 | from ._generated.ffi_pixbuf import ffi
18 | 
19 | __all__ = ['decode_to_image_surface']
20 | 
21 | gdk_pixbuf = dlopen(ffi, 'gdk_pixbuf-2.0', 'gdk_pixbuf-2.0-0')
22 | gobject = dlopen(ffi, 'gobject-2.0', 'gobject-2.0-0')
23 | glib = dlopen(ffi, 'glib-2.0', 'glib-2.0-0')
24 | try:
25 |     gdk = dlopen(ffi, 'gdk-3', 'gdk-x11-2.0', 'gdk-win32-2.0-0')
26 | except OSError:
27 |     gdk = None
{% endraw %}

```