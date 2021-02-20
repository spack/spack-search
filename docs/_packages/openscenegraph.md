---
name: "openscenegraph"
layout: package
next_package: openssh
previous_package: openresty
languages: ['c']
---
## 3.4.1
3 / 2864 files match, 1 filtered matches.

 - [src/osgPlugins/lua/lua-5.2.3/src/loadlib.c](#srcosgpluginslualua-523srcloadlibc)

### src/osgPlugins/lua/lua-5.2.3/src/loadlib.c

```c

{% raw %}
131 | 
132 | 
133 | static void *ll_load (lua_State *L, const char *path, int seeglb) {
134 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
135 |   if (lib == NULL) lua_pushstring(L, dlerror());
136 |   return lib;
{% endraw %}

```