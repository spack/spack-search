---
name: "redis"
layout: package
next_package: laszip
previous_package: bird
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.0.2
6 / 701 files match, 4 filtered matches.

 - [src/module.c](#srcmodulec)
 - [deps/lua/src/loadlib.c](#depsluasrcloadlibc)
 - [deps/jemalloc/src/background_thread.c](#depsjemallocsrcbackground_threadc)
 - [deps/jemalloc/src/ctl.c](#depsjemallocsrcctlc)

### src/module.c

```c

{% raw %}
4746 |         serverLog(LL_WARNING, "Module %s failed to load: %s", path, dlerror());
4747 |         return C_ERR;
4748 |     }
4749 |     onload = (int (*)(void *, void **, int))(unsigned long) dlsym(handle,"RedisModule_OnLoad");
4750 |     if (onload == NULL) {
4751 |         dlclose(handle);
{% endraw %}

```
### deps/lua/src/loadlib.c

```c

{% raw %}
72 | 
73 | 
74 | static lua_CFunction ll_sym (lua_State *L, void *lib, const char *sym) {
75 |   lua_CFunction f = (lua_CFunction)dlsym(lib, sym);
76 |   if (f == NULL) lua_pushstring(L, dlerror());
77 |   return f;
{% endraw %}

```
### deps/jemalloc/src/background_thread.c

```c

{% raw %}
811 | 	if (pthread_create_fptr != NULL) {
812 | 		return false;
813 | 	}
814 | 	pthread_create_fptr = dlsym(RTLD_NEXT, "pthread_create");
815 | 	if (pthread_create_fptr == NULL) {
816 | 		can_enable_background_thread = false;
817 | 		if (config_lazy_lock || opt_background_thread) {
818 | 			malloc_write("<jemalloc>: Error in dlsym(RTLD_NEXT, "
819 | 			    "\"pthread_create\")\n");
820 | 			abort();
{% endraw %}

```
### deps/jemalloc/src/ctl.c

```c

{% raw %}
1544 | 		background_thread_enabled_set(tsd_tsdn(tsd), newval);
1545 | 		if (newval) {
1546 | 			if (!can_enable_background_thread) {
1547 | 				malloc_printf("<jemalloc>: Error in dlsym("
1548 | 			            "RTLD_NEXT, \"pthread_create\"). Cannot "
1549 | 				    "enable background_thread\n");
1605 | 
1606 | 		if (background_thread_enabled()) {
1607 | 			if (!can_enable_background_thread) {
1608 | 				malloc_printf("<jemalloc>: Error in dlsym("
1609 | 			            "RTLD_NEXT, \"pthread_create\"). Cannot "
1610 | 				    "enable background_thread\n");
{% endraw %}

```