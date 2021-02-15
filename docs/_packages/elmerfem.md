---
name: "elmerfem"
layout: package
next_package: ferret
previous_package: glog
languages: ['cmake', 'cpp']
---
## devel
5 / 9371 files match

 - [fem/config.h.cmake](#femconfighcmake)
 - [fem/src/Load.c](#femsrcloadc)
 - [post/config.h.cmake](#postconfighcmake)
 - [contrib/lua-5.1.5/src/luaconf.h](#contriblua-515srcluaconfh)
 - [contrib/lua-5.1.5/src/loadlib.c](#contriblua-515srcloadlibc)

### fem/config.h.cmake

```cmake

{% raw %}
32 | /* Define to 1 if you have the `dlopen' function. */
33 | #define HAVE_DLOPEN
35 | /* Define if your system has dlopen, dlsym, dlerror, and dlclose for dynamic */
37 | #cmakedefine HAVE_DLOPEN_API
{% endraw %}

```
### fem/src/Load.c

```cpp

{% raw %}
268 |   INTERNAL: Tries to open library with dlopen, first without
274 | static void STDCALLBULL try_dlopen(char *LibName, void **Handle, char *errorBuf)
286 | #ifdef HAVE_DLOPEN_API
287 |         if ((*Handle = dlopen(dl_names[i], RTLD_NOW)) == NULL) {
319 |     try_dlopen(Library, Handle, errorBuf);
329 |             try_dlopen(CurrentLib, Handle, errorBuf);
386 | 	/* Should not get here unless WIN32 implements DLOPEN_API */
415 | #ifdef HAVE_DLOPEN_API
{% endraw %}

```
### post/config.h.cmake

```cmake

{% raw %}
67 | /* Define to 1 if you have the `dlopen' function. */
68 | #undef HAVE_DLOPEN
70 | /* Define if your system has dlopen, dlsym, dlerror, and dlclose for dynamic
72 | #undef HAVE_DLOPEN_API
{% endraw %}

```
### contrib/lua-5.1.5/src/luaconf.h

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
### contrib/lua-5.1.5/src/loadlib.c

```cpp

{% raw %}
50 | #if defined(LUA_DL_DLOPEN)
68 |   void *lib = dlopen(path, RTLD_NOW);
{% endraw %}

```