---
name: "rtags"
layout: package
next_package: py-osqp
previous_package: util-linux
languages: ['c']
---
## 2.17
3 / 467 files match, 2 filtered matches.

 - [src/lua/src/loadlib_rel.c](#srcluasrcloadlib_relc)
 - [src/lua/src/loadlib.c](#srcluasrcloadlibc)

### src/lua/src/loadlib_rel.c

```c

{% raw %}
248 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```
### src/lua/src/loadlib.c

```c

{% raw %}
156 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```