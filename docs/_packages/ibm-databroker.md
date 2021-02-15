---
name: "ibm-databroker"
layout: package
next_package: henson
previous_package: buddy
languages: ['cpp', 'python']
---
## master
3 / 245 files match

 - [src/lib/backend.c](#srclibbackendc)
 - [src/util/dbrUtils.c](#srcutildbrutilsc)
 - [bindings/python/dbr_module/dbr.py](#bindingspythondbr_moduledbrpy)

### src/lib/backend.c

```cpp

{% raw %}
49 |     if( (be->_library = dlopen( to_str, RTLD_LAZY )) == NULL )
{% endraw %}

```
### src/util/dbrUtils.c

```cpp

{% raw %}
92 |       // dlopen and load adapter symbol
93 |       if( (gMain_context->_da_library = dlopen( to_str, RTLD_LAZY )) == NULL )
{% endraw %}

```
### bindings/python/dbr_module/dbr.py

```python

{% raw %}
16 | libtransport = ffi.dlopen("libdbbe_transport.so", ffi.RTLD_GLOBAL|ffi.RTLD_NOW)
17 | libbackend = ffi.dlopen("libdbbe_redis.so", ffi.RTLD_GLOBAL|ffi.RTLD_NOW)
18 | libdatabroker = ffi.dlopen("libdatabroker.so")
{% endraw %}

```