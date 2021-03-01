---
name: "lua"
layout: package
next_package: lvm2
previous_package: llvm
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.3.2
1 / 152 files match, 1 filtered matches.

 - [src/loadlib.c](#srcloadlibc)

### src/loadlib.c

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