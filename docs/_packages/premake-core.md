---
name: "premake-core"
layout: package
next_package: prism
previous_package: powerapi
languages: ['c']
---
## 5.0.0-alpha13
2 / 1665 files match, 1 filtered matches.

 - [contrib/lua/src/loadlib.c](#contribluasrcloadlibc)

### contrib/lua/src/loadlib.c

```c

{% raw %}
123 | 
124 | 
125 | static void *lsys_load (lua_State *L, const char *path, int seeglb) {
126 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
127 |   if (lib == NULL) lua_pushstring(L, dlerror());
128 |   return lib;
{% endraw %}

```