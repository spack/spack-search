---
name: "sysbench"
layout: package
next_package: p4est
previous_package: libcerf
languages: ['cpp']
---
## 1.0.18
3 / 714 files match

 - [third_party/luajit/luajit/src/lib_package.c](#third_partyluajitluajitsrclib_packagec)
 - [third_party/luajit/luajit/src/lj_clib.c](#third_partyluajitluajitsrclj_clibc)
 - [m4/lib-link.m4](#m4lib-linkm4)

### third_party/luajit/luajit/src/lib_package.c

```cpp

{% raw %}
34 | #if LJ_TARGET_DLOPEN
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### third_party/luajit/luajit/src/lj_clib.c

```cpp

{% raw %}
22 | #if LJ_TARGET_DLOPEN
117 |   void *h = dlopen(clib_extname(L, name),
123 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
459 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```