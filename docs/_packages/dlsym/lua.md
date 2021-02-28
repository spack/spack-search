---
name: "lua"
layout: package
next_package: ucx
previous_package: erlang
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.3.2
1 / 152 files match, 1 filtered matches.

 - [src/loadlib.c](#srcloadlibc)

### src/loadlib.c

```c

{% raw %}
160 | 
161 | 
162 | static lua_CFunction lsys_sym (lua_State *L, void *lib, const char *sym) {
163 |   lua_CFunction f = cast_func(dlsym(lib, sym));
164 |   if (f == NULL) lua_pushstring(L, dlerror());
165 |   return f;
{% endraw %}

```