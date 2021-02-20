---
name: "ibm-databroker"
layout: package
next_package: icarus
previous_package: hyphy
languages: ['python', 'c']
---
## master
3 / 245 files match, 3 filtered matches.

 - [src/lib/backend.c](#srclibbackendc)
 - [src/util/dbrUtils.c](#srcutildbrutilsc)
 - [bindings/python/dbr_module/dbr.py](#bindingspythondbr_moduledbrpy)

### src/lib/backend.c

```c

{% raw %}
46 |     if( be == NULL )
47 |       return NULL;
48 | 
49 |     if( (be->_library = dlopen( to_str, RTLD_LAZY )) == NULL )
50 |     {
51 |       LOG( DBG_ERR, stderr, "libdatabroker: failed to load Backend Library %s. Looked for in %s\n", to_str, getenv("LD_LIBRARY_PATH") );
{% endraw %}

```
### src/util/dbrUtils.c

```c

{% raw %}
90 |     else
91 |     {
92 |       // dlopen and load adapter symbol
93 |       if( (gMain_context->_da_library = dlopen( to_str, RTLD_LAZY )) == NULL )
94 |       {
95 |         LOG( DBG_ERR, stderr, "libdatabroker: failed to load Data Adapter library %s. Looked for in %s\n", to_str, getenv("LD_LIBRARY_PATH") );
{% endraw %}

```
### bindings/python/dbr_module/dbr.py

```python

{% raw %}
13 |  # limitations under the License.
14 |  #
15 | from _dbr_interface import ffi
16 | libtransport = ffi.dlopen("libdbbe_transport.so", ffi.RTLD_GLOBAL|ffi.RTLD_NOW)
17 | libbackend = ffi.dlopen("libdbbe_redis.so", ffi.RTLD_GLOBAL|ffi.RTLD_NOW)
18 | libdatabroker = ffi.dlopen("libdatabroker.so")
19 | import _cffi_backend
20 | from dbr_module.dbr_errorcodes import Errors
{% endraw %}

```