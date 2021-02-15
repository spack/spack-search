---
name: "czmq"
layout: package
next_package: py-tables
previous_package: cistem
languages: ['python']
---
## 4.0.2
2 / 585 files match

 - [src/Makemodule-local.am](#srcmakemodule-localam)
 - [bindings/python_cffi/czmq_cffi.py](#bindingspython_cfficzmq_cffipy)

### src/Makemodule-local.am

```

{% raw %}
8 | 	$(LIBTOOL) --mode=execute -dlopen src/libczmq.la python bindings/python/test.py
{% endraw %}

```
### bindings/python_cffi/czmq_cffi.py

```python

{% raw %}
22 |     lib = ffi.dlopen(libpath)
27 |     lib = ffi.dlopen(libpath)
{% endraw %}

```