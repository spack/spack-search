---
name: "openresty"
layout: package
next_package: openscenegraph
previous_package: openpmd-api
languages: ['c']
---
## 1.13.6.2
7 / 2240 files match, 3 filtered matches.

 - [bundle/LuaJIT-2.1-20180420/src/lib_package.c](#bundleluajit-21-20180420srclib_packagec)
 - [bundle/LuaJIT-2.1-20180420/src/lj_clib.c](#bundleluajit-21-20180420srclj_clibc)
 - [bundle/nginx-1.13.6/src/core/nginx.c](#bundlenginx-1136srccorenginxc)

### bundle/LuaJIT-2.1-20180420/src/lib_package.c

```c

{% raw %}
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### bundle/LuaJIT-2.1-20180420/src/lj_clib.c

```c

{% raw %}
117 |   void *h = dlopen(clib_extname(L, name),
123 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
{% endraw %}

```
### bundle/nginx-1.13.6/src/core/nginx.c

```c

{% raw %}
1526 |     handle = ngx_dlopen(file.data);
1529 |                            ngx_dlopen_n " \"%s\" failed (%s)",
{% endraw %}

```