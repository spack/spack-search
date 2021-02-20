---
name: "sysbench"
layout: package
next_package: systemtap
previous_package: swipl
languages: ['c']
---
## 1.0.18
3 / 714 files match, 2 filtered matches.

 - [third_party/luajit/luajit/src/lib_package.c](#third_partyluajitluajitsrclib_packagec)
 - [third_party/luajit/luajit/src/lj_clib.c](#third_partyluajitluajitsrclj_clibc)

### third_party/luajit/luajit/src/lib_package.c

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
### third_party/luajit/luajit/src/lj_clib.c

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