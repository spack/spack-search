---
name: "rtags"
layout: package
next_package: py-osqp
previous_package: util-linux
languages: ['cpp']
---
## 2.17
3 / 467 files match

 - [src/rct/rct/Plugin.cpp](#srcrctrctplugincpp)
 - [src/lua/src/loadlib_rel.c](#srcluasrcloadlib_relc)
 - [src/lua/src/loadlib.c](#srcluasrcloadlibc)

### src/rct/rct/Plugin.cpp

```

{% raw %}
13 |     return dlopen(fileName.nullTerminated(), RTLD_LAZY);
{% endraw %}

```
### src/lua/src/loadlib_rel.c

```cpp

{% raw %}
218 | #if defined(LUA_USE_DLOPEN)	/* { */
248 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### src/lua/src/loadlib.c

```cpp

{% raw %}
126 | #if defined(LUA_USE_DLOPEN)	/* { */
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```