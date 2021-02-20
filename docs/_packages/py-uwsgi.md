---
name: "py-uwsgi"
layout: package
next_package: py-vermin
previous_package: py-uvloop
languages: ['python', 'c']
---
## 2.0.18
7 / 648 files match, 7 filtered matches.

 - [plugins/rrdtool/rrdtool.c](#pluginsrrdtoolrrdtoolc)
 - [plugins/gccgo/gccgo_plugin.c](#pluginsgccgogccgo_pluginc)
 - [plugins/pypy/pypy_setup.py](#pluginspypypypy_setuppy)
 - [plugins/pypy/pypy_plugin.c](#pluginspypypypy_pluginc)
 - [plugins/cgi/cgi_plugin.c](#pluginscgicgi_pluginc)
 - [core/uwsgi.c](#coreuwsgic)
 - [core/plugins.c](#corepluginsc)

### plugins/rrdtool/rrdtool.c

```c

{% raw %}
31 | 		u_rrd.lib_name = "librrd.so";
32 | 	}
33 | 
34 | 	u_rrd.lib = dlopen(u_rrd.lib_name, RTLD_LAZY);
35 | 	if (!u_rrd.lib) return -1;
36 | 
{% endraw %}

```
### plugins/gccgo/gccgo_plugin.c

```c

{% raw %}
157 | #endif
158 | 	struct uwsgi_string_list *usl = ugccgo.libs;
159 | 	while(usl) {
160 | 		void *handle = dlopen(usl->value, RTLD_NOW | RTLD_GLOBAL);
161 | 		if (!handle) {
162 | 			uwsgi_log("unable to open go shared library: %s\n", dlerror());
{% endraw %}

```
### plugins/pypy/pypy_setup.py

```python

{% raw %}
263 | 
264 | ffi.cdef(cdefines)
265 | lib = ffi.verify(cverify)
266 | libc = ffi.dlopen(None)
267 | 
268 | 
{% endraw %}

```
### plugins/pypy/pypy_plugin.c

```c

{% raw %}
61 | 		goto ready;
62 | 	}
63 | 	else if (upypy.lib) {
64 | 		upypy.handler = dlopen(upypy.lib, RTLD_NOW | RTLD_GLOBAL);
65 | 	}
66 | 	else {
74 |                         char *libpath = uwsgi_concat2(upypy.home, "/bin/libpypy-c.so");
75 | #endif
76 | 			if (uwsgi_file_exists(libpath)) {
77 |                                 upypy.handler = dlopen(libpath, RTLD_NOW | RTLD_GLOBAL);
78 |                         }
79 |                         free(libpath);
89 |                         	char *libpath = uwsgi_concat2(upypy.home, "/libpypy-c.so");
90 | #endif
91 | 				if (uwsgi_file_exists(libpath)) {
92 | 					upypy.handler = dlopen(libpath, RTLD_NOW | RTLD_GLOBAL);
93 | 				}
94 | 				free(libpath);
97 | 		// fallback to standard library search path
98 | 		if (!upypy.handler) {
99 | #ifdef __CYGWIN__
100 | 			upypy.handler = dlopen("libpypy-c.dll", RTLD_NOW | RTLD_GLOBAL);
101 | #elif defined(__APPLE__)
102 | 			upypy.handler = dlopen("libpypy-c.dylib", RTLD_NOW | RTLD_GLOBAL);
103 | #else
104 | 			upypy.handler = dlopen("libpypy-c.so", RTLD_NOW | RTLD_GLOBAL);
105 | #endif
106 | 		}
{% endraw %}

```
### plugins/cgi/cgi_plugin.c

```c

{% raw %}
150 | 			exit(1);
151 | 		}
152 | 		*colon = 0;
153 | 		void *cgi_lib = dlopen(ll->value, RTLD_NOW | RTLD_GLOBAL);
154 | 		if (!cgi_lib) {
155 | 			uwsgi_log( "cgi-loadlib: %s\n", dlerror());
{% endraw %}

```
### core/uwsgi.c

```c

{% raw %}
1001 | 	{"plugins-list", no_argument, 0, "list enabled plugins", uwsgi_opt_true, &uwsgi.plugins_list, 0},
1002 | 	{"plugin-list", no_argument, 0, "list enabled plugins", uwsgi_opt_true, &uwsgi.plugins_list, 0},
1003 | 	{"autoload", no_argument, 0, "try to automatically load plugins when unknown options are found", uwsgi_opt_true, &uwsgi.autoload, UWSGI_OPT_IMMEDIATE},
1004 | 	{"dlopen", required_argument, 0, "blindly load a shared library", uwsgi_opt_load_dl, NULL, UWSGI_OPT_IMMEDIATE},
1005 | 	{"allowed-modifiers", required_argument, 0, "comma separated list of allowed modifiers", uwsgi_opt_set_str, &uwsgi.allowed_modifiers, 0},
1006 | 	{"remap-modifier", required_argument, 0, "remap request modifier from one id to another", uwsgi_opt_set_str, &uwsgi.remap_modifier, 0},
4399 | }
4400 | 
4401 | void uwsgi_opt_load_dl(char *opt, char *value, void *none) {
4402 | 	if (!dlopen(value, RTLD_NOW | RTLD_GLOBAL)) {
4403 | 		uwsgi_log("%s\n", dlerror());
4404 | 	}
{% endraw %}

```
### core/plugins.c

```c

{% raw %}
117 | #ifdef UWSGI_ELF
118 | 		uwsgi_plugin_parse_section(plugin_name);
119 | #endif
120 | 		plugin_handle = dlopen(plugin_name, RTLD_NOW | RTLD_GLOBAL);
121 | 		if (!plugin_handle) {
122 | 			if (!has_option)
136 | #ifdef UWSGI_ELF
137 | 		uwsgi_plugin_parse_section(plugin_filename);
138 | #endif
139 | 		plugin_handle = dlopen(plugin_filename, RTLD_NOW | RTLD_GLOBAL);
140 | 		if (plugin_handle) {
141 | 			plugin_abs_path = plugin_filename;
153 | #ifdef UWSGI_ELF
154 | 		uwsgi_plugin_parse_section(plugin_filename);
155 | #endif
156 | 		plugin_handle = dlopen(plugin_filename, RTLD_NOW | RTLD_GLOBAL);
157 | 		plugin_abs_path = plugin_filename;
158 | 		//free(plugin_filename);
{% endraw %}

```