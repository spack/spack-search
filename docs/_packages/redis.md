---
name: "redis"
layout: package
next_package: netgauge
previous_package: libctl
languages: ['c']
---
## 5.0.2
5 / 701 files match, 2 filtered matches.

 - [src/module.c](#srcmodulec)
 - [deps/lua/src/loadlib.c](#depsluasrcloadlibc)

### src/module.c

```c

{% raw %}
44 |     void *handle;   /* Module dlopen() handle. */
4744 |     handle = dlopen(path,RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### deps/lua/src/loadlib.c

```c

{% raw %}
68 |   void *lib = dlopen(path, RTLD_NOW);
{% endraw %}

```