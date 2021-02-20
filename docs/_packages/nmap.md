---
name: "nmap"
layout: package
next_package: nnvm
previous_package: nix
languages: ['c']
---
## 7.70
11 / 2242 files match, 1 filtered matches.

 - [liblua/loadlib.c](#liblualoadlibc)

### liblua/loadlib.c

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