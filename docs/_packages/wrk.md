---
name: "wrk"
layout: package
next_package: wt
previous_package: whizard
languages: ['c']
---
## 3.1.2
2 / 222 files match, 2 filtered matches.

 - [deps/luajit/src/lib_package.c](#depsluajitsrclib_packagec)
 - [deps/luajit/src/lj_clib.c](#depsluajitsrclj_clibc)

### deps/luajit/src/lib_package.c

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
### deps/luajit/src/lj_clib.c

```c

{% raw %}
113 | 
114 | static void *clib_loadlib(lua_State *L, const char *name, int global)
115 | {
116 |   void *h = dlopen(clib_extname(L, name),
117 | 		   RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
118 |   if (!h) {
119 |     const char *e, *err = dlerror();
120 |     if (*err == '/' && (e = strchr(err, ':')) &&
121 | 	(name = clib_resolve_lds(L, strdata(lj_str_new(L, err, e-err))))) {
122 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
123 |       if (h) return h;
124 |       err = dlerror();
{% endraw %}

```