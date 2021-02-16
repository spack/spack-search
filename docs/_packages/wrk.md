---
name: "wrk"
layout: package
next_package: cbtf
previous_package: py-petsc4py
languages: ['c']
---
## 3.1.2
2 / 222 files match, 2 filtered matches.

 - [deps/luajit/src/lib_package.c](#depsluajitsrclib_packagec)
 - [deps/luajit/src/lj_clib.c](#depsluajitsrclj_clibc)

### deps/luajit/src/lib_package.c

```c

{% raw %}
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### deps/luajit/src/lj_clib.c

```c

{% raw %}
116 |   void *h = dlopen(clib_extname(L, name),
122 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
{% endraw %}

```