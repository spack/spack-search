---
name: "ermod"
layout: package
next_package: esmf
previous_package: erlang
languages: ['c']
---
## 0.3.6
2 / 138 files match, 1 filtered matches.

 - [vmdfio.c](#vmdfioc)

### vmdfio.c

```c

{% raw %}
153 |       
154 |       if(is_executable(pluginpath) && pluginpath[strlen(pluginpath)-1] != '.'){
155 | 	void* handle;
156 | 	handle = dlopen(pluginpath, RTLD_NOW | RTLD_GLOBAL);
157 | 	if(!handle){
158 | 	  fprintf(stderr, "Warning: failed to load plugin \"%s\", reason: \"%s\"\n", pluginpath, dlerror());
{% endraw %}

```