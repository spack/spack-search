---
name: "lua-luajit"
layout: package
next_package: lvm2
previous_package: lua
languages: ['c']
---
## 2.0.4
2 / 188 files match, 2 filtered matches.

 - [src/lib_package.c](#srclib_packagec)
 - [src/lj_clib.c](#srclj_clibc)

### src/lib_package.c

```c

{% raw %}
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### src/lj_clib.c

```c

{% raw %}
116 |   void *h = dlopen(clib_extname(L, name),
122 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
{% endraw %}

```