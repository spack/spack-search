---
name: "rtags"
layout: package
next_package: ruby
previous_package: rt-tests
languages: ['c']
---
## 2.17
3 / 467 files match, 2 filtered matches.

 - [src/lua/src/loadlib_rel.c](#srcluasrcloadlib_relc)
 - [src/lua/src/loadlib.c](#srcluasrcloadlibc)

### src/lua/src/loadlib_rel.c

```c

{% raw %}
245 | 
246 | 
247 | static void *lsys_load (lua_State *L, const char *path, int seeglb) {
248 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
249 |   if (lib == NULL) lua_pushstring(L, dlerror());
250 |   return lib;
{% endraw %}

```
### src/lua/src/loadlib.c

```c

{% raw %}
153 | 
154 | 
155 | static void *lsys_load (lua_State *L, const char *path, int seeglb) {
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
157 |   if (lib == NULL) lua_pushstring(L, dlerror());
158 |   return lib;
{% endraw %}

```