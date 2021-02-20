---
name: "openresty"
layout: package
next_package: openscenegraph
previous_package: openpbs
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
42 | 
43 | static void *ll_load(lua_State *L, const char *path, int gl)
44 | {
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
46 |   if (lib == NULL) lua_pushstring(L, dlerror());
47 |   return lib;
{% endraw %}

```
### bundle/LuaJIT-2.1-20180420/src/lj_clib.c

```c

{% raw %}
114 | 
115 | static void *clib_loadlib(lua_State *L, const char *name, int global)
116 | {
117 |   void *h = dlopen(clib_extname(L, name),
118 | 		   RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
119 |   if (!h) {
120 |     const char *e, *err = dlerror();
121 |     if (*err == '/' && (e = strchr(err, ':')) &&
122 | 	(name = clib_resolve_lds(L, strdata(lj_str_new(L, err, e-err))))) {
123 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
124 |       if (h) return h;
125 |       err = dlerror();
{% endraw %}

```
### bundle/nginx-1.13.6/src/core/nginx.c

```c

{% raw %}
1523 |         return NGX_CONF_ERROR;
1524 |     }
1525 | 
1526 |     handle = ngx_dlopen(file.data);
1527 |     if (handle == NULL) {
1528 |         ngx_conf_log_error(NGX_LOG_EMERG, cf, 0,
1529 |                            ngx_dlopen_n " \"%s\" failed (%s)",
1530 |                            file.data, ngx_dlerror());
1531 |         return NGX_CONF_ERROR;
{% endraw %}

```