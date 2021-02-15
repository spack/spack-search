---
name: "kibana"
layout: package
next_package: fenics
previous_package: py-cairocffi
languages: ['cpp', 'python', 'js']
---
## 6.4.0
6 / 56280 files match

 - [node/lib/node_modules/npm/node_modules/node-gyp/gyp/pylib/gyp/generator/make.py](#nodelibnode_modulesnpmnode_modulesnode-gypgyppylibgypgeneratormakepy)
 - [node/include/node/uv-win.h](#nodeincludenodeuv-winh)
 - [node/include/node/uv.h](#nodeincludenodeuvh)
 - [node/include/node/uv-unix.h](#nodeincludenodeuv-unixh)
 - [node/include/node/openssl/dso.h](#nodeincludenodeopenssldsoh)
 - [node_modules/node-libs-browser/mock/process.js](#node_modulesnode-libs-browsermockprocessjs)

### node/lib/node_modules/npm/node_modules/node-gyp/gyp/pylib/gyp/generator/make.py

```python

{% raw %}
149 | # 2) loadable_module, which is generating a module intended for dlopen().
{% endraw %}

```
### node/include/node/uv-win.h

```cpp

{% raw %}
303 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### node/include/node/uv.h

```cpp

{% raw %}
1460 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### node/include/node/uv-unix.h

```cpp

{% raw %}
186 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### node/include/node/openssl/dso.h

```cpp

{% raw %}
196 |      * Standard dlopen uses a (void *). Win32 uses a HANDLE. VMS doesn't use
324 |  * If DSO_DLFCN is defined, the standard dlfcn.h-style functions (dlopen,
{% endraw %}

```
### node_modules/node-libs-browser/mock/process.js

```js

{% raw %}
26 | exports.umask = exports.dlopen = 
{% endraw %}

```