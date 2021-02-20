---
name: "czmq"
layout: package
next_package: dakota
previous_package: cyrus-sasl
languages: ['python']
---
## 4.0.2
2 / 585 files match, 1 filtered matches.

 - [bindings/python_cffi/czmq_cffi.py](#bindingspython_cfficzmq_cffipy)

### bindings/python_cffi/czmq_cffi.py

```python

{% raw %}
19 |             libpath = 'libczmq.so.4'
20 |     elif os.name == 'nt':
21 |         libpath = 'libczmq.dll'
22 |     lib = ffi.dlopen(libpath)
23 | except OSError:
24 |     libpath = find_library("czmq")
25 |     if not libpath:
26 |         raise ImportError("Unable to find libczmq")
27 |     lib = ffi.dlopen(libpath)
28 | 
29 | # Custom setup for czmq
{% endraw %}

```