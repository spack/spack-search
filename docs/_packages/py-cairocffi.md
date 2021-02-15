---
name: "py-cairocffi"
layout: package
next_package: kibana
previous_package: sst-transports
languages: ['python']
---
## 1.0.2
2 / 20 files match

 - [cairocffi/__init__.py](#cairocffi__init__py)
 - [cairocffi/pixbuf.py](#cairocffipixbufpy)

### cairocffi/__init__.py

```python

{% raw %}
24 | def dlopen(ffi, *names):
30 |                 lib = ffi.dlopen(path or lib_name)
35 |     raise OSError("dlopen() failed to load a library: %s" % ' / '.join(names))
38 | cairo = dlopen(ffi, 'cairo', 'cairo-2', 'cairo-gobject-2', 'cairo.so.2')
{% endraw %}

```
### cairocffi/pixbuf.py

```python

{% raw %}
16 | from . import Context, ImageSurface, constants, dlopen
21 | gdk_pixbuf = dlopen(ffi, 'gdk_pixbuf-2.0', 'gdk_pixbuf-2.0-0')
22 | gobject = dlopen(ffi, 'gobject-2.0', 'gobject-2.0-0')
23 | glib = dlopen(ffi, 'glib-2.0', 'glib-2.0-0')
25 |     gdk = dlopen(ffi, 'gdk-3', 'gdk-x11-2.0', 'gdk-win32-2.0-0')
{% endraw %}

```