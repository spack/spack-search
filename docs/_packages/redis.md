---
name: "redis"
layout: package
next_package: rhash
previous_package: rdma-core
languages: ['c']
---
## 5.0.2
5 / 701 files match, 2 filtered matches.

 - [src/module.c](#srcmodulec)
 - [deps/lua/src/loadlib.c](#depsluasrcloadlibc)

### src/module.c

```c

{% raw %}
41 | 
42 | /* This structure represents a module inside the system. */
43 | struct RedisModule {
44 |     void *handle;   /* Module dlopen() handle. */
45 |     char *name;     /* Module name. */
46 |     int ver;        /* Module version. We use just progressive integers. */
4741 |     void *handle;
4742 |     RedisModuleCtx ctx = REDISMODULE_CTX_INIT;
4743 | 
4744 |     handle = dlopen(path,RTLD_NOW|RTLD_LOCAL);
4745 |     if (handle == NULL) {
4746 |         serverLog(LL_WARNING, "Module %s failed to load: %s", path, dlerror());
{% endraw %}

```
### deps/lua/src/loadlib.c

```c

{% raw %}
65 | 
66 | 
67 | static void *ll_load (lua_State *L, const char *path) {
68 |   void *lib = dlopen(path, RTLD_NOW);
69 |   if (lib == NULL) lua_pushstring(L, dlerror());
70 |   return lib;
{% endraw %}

```