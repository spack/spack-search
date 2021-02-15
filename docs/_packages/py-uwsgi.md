---
name: "py-uwsgi"
layout: package
next_package: xrootd
previous_package: sqlite
languages: ['cpp', 'python']
---
## 2.0.18
7 / 648 files match

 - [plugins/rrdtool/rrdtool.c](#pluginsrrdtoolrrdtoolc)
 - [plugins/gccgo/gccgo_plugin.c](#pluginsgccgogccgo_pluginc)
 - [plugins/pypy/pypy_setup.py](#pluginspypypypy_setuppy)
 - [plugins/pypy/pypy_plugin.c](#pluginspypypypy_pluginc)
 - [plugins/cgi/cgi_plugin.c](#pluginscgicgi_pluginc)
 - [core/uwsgi.c](#coreuwsgic)
 - [core/plugins.c](#corepluginsc)

### plugins/rrdtool/rrdtool.c

```cpp

{% raw %}
34 | 	u_rrd.lib = dlopen(u_rrd.lib_name, RTLD_LAZY);
{% endraw %}

```
### plugins/gccgo/gccgo_plugin.c

```cpp

{% raw %}
160 | 		void *handle = dlopen(usl->value, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### plugins/pypy/pypy_setup.py

```python

{% raw %}
266 | libc = ffi.dlopen(None)
{% endraw %}

```
### plugins/pypy/pypy_plugin.c

```cpp

{% raw %}
64 | 		upypy.handler = dlopen(upypy.lib, RTLD_NOW | RTLD_GLOBAL);
77 |                                 upypy.handler = dlopen(libpath, RTLD_NOW | RTLD_GLOBAL);
92 | 					upypy.handler = dlopen(libpath, RTLD_NOW | RTLD_GLOBAL);
100 | 			upypy.handler = dlopen("libpypy-c.dll", RTLD_NOW | RTLD_GLOBAL);
102 | 			upypy.handler = dlopen("libpypy-c.dylib", RTLD_NOW | RTLD_GLOBAL);
104 | 			upypy.handler = dlopen("libpypy-c.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### plugins/cgi/cgi_plugin.c

```cpp

{% raw %}
153 | 		void *cgi_lib = dlopen(ll->value, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### core/uwsgi.c

```cpp

{% raw %}
1004 | 	{"dlopen", required_argument, 0, "blindly load a shared library", uwsgi_opt_load_dl, NULL, UWSGI_OPT_IMMEDIATE},
4402 | 	if (!dlopen(value, RTLD_NOW | RTLD_GLOBAL)) {
{% endraw %}

```
### core/plugins.c

```cpp

{% raw %}
120 | 		plugin_handle = dlopen(plugin_name, RTLD_NOW | RTLD_GLOBAL);
139 | 		plugin_handle = dlopen(plugin_filename, RTLD_NOW | RTLD_GLOBAL);
156 | 		plugin_handle = dlopen(plugin_filename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```