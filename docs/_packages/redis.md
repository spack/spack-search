---
name: "redis"
layout: package
next_package: netgauge
previous_package: libctl
languages: ['cpp']
---
## 5.0.2
5 / 701 files match

 - [src/module.c](#srcmodulec)
 - [deps/lua/src/luaconf.h](#depsluasrcluaconfh)
 - [deps/lua/src/loadlib.c](#depsluasrcloadlibc)
 - [deps/jemalloc/INSTALL.md](#depsjemallocinstallmd)
 - [deps/jemalloc/src/jemalloc.c](#depsjemallocsrcjemallocc)

### src/module.c

```cpp

{% raw %}
44 |     void *handle;   /* Module dlopen() handle. */
4744 |     handle = dlopen(path,RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### deps/lua/src/luaconf.h

```cpp

{% raw %}
37 | #define LUA_USE_DLOPEN		/* needs an extra library: -ldl */
689 | ** dyld, or Unix's dlopen). If your system is some kind of Unix, there
690 | ** is a good chance that it has dlopen, so LUA_DL_DLOPEN will work for
691 | ** it.  To use dlopen you also need to adapt the src/Makefile (probably
694 | ** also add -DLUA_USE_DLOPEN.)
699 | #if defined(LUA_USE_DLOPEN)
700 | #define LUA_DL_DLOPEN
{% endraw %}

```
### deps/lua/src/loadlib.c

```cpp

{% raw %}
50 | #if defined(LUA_DL_DLOPEN)
68 |   void *lib = dlopen(path, RTLD_NOW);
{% endraw %}

```
### deps/jemalloc/INSTALL.md

```

{% raw %}
273 |     jemalloc to be dynamically loaded after program startup (e.g. using dlopen).
{% endraw %}

```
### deps/jemalloc/src/jemalloc.c

```cpp

{% raw %}
2486 |  * glibc provides the RTLD_DEEPBIND flag for dlopen which can make it possible
{% endraw %}

```