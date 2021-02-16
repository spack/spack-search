---
name: "sysbench"
layout: package
next_package: systemtap
previous_package: swipl
languages: ['c']
---
## 1.0.18
3 / 714 files match, 2 filtered matches.

 - [third_party/luajit/luajit/src/lib_package.c](#third_partyluajitluajitsrclib_packagec)
 - [third_party/luajit/luajit/src/lj_clib.c](#third_partyluajitluajitsrclj_clibc)

### third_party/luajit/luajit/src/lib_package.c

```c

{% raw %}
45 |   void *lib = dlopen(path, RTLD_NOW | (gl ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### third_party/luajit/luajit/src/lj_clib.c

```c

{% raw %}
117 |   void *h = dlopen(clib_extname(L, name),
123 |       h = dlopen(name, RTLD_LAZY | (global?RTLD_GLOBAL:RTLD_LOCAL));
{% endraw %}

```