---
name: "glpk"
layout: package
next_package: glusterfs
previous_package: globalarrays
languages: ['c']
---
## 4.57
6 / 429 files match, 3 filtered matches.

 - [src/glpsql.c](#srcglpsqlc)
 - [src/env/env.h](#srcenvenvh)
 - [src/env/dlsup.c](#srcenvdlsupc)

### src/glpsql.c

```c

{% raw %}
708 |       h_odbc = xdlopen(libodbc);
1330 |       h_mysql = xdlopen(libmysql);
{% endraw %}

```
### src/env/env.h

```c

{% raw %}
248 | void *xdlopen(const char *module);
{% endraw %}

```
### src/env/dlsup.c

```c

{% raw %}
35 | void *xdlopen(const char *module)
42 |       h = lt_dlopen(module);
46 |             xerror("xdlopen: %s\n", lt_dlerror());
77 | void *xdlopen(const char *module)
80 |       h = dlopen(module, RTLD_NOW);
110 | void *xdlopen(const char *module)
144 | void *xdlopen(const char *module)
{% endraw %}

```