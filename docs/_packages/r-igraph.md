---
name: "r-igraph"
layout: package
next_package: gosam-contrib
previous_package: matio
languages: ['c']
---
## 1.0.1
3 / 1366 files match, 3 filtered matches.

 - [src/glpk/glpenv08.c](#srcglpkglpenv08c)
 - [src/glpk/glpsql.c](#srcglpkglpsqlc)
 - [src/glpk/glpenv.h](#srcglpkglpenvh)

### src/glpk/glpenv08.c

```c

{% raw %}
36 | void *xdlopen(const char *module)
42 |       h = lt_dlopen(module);
46 |             xerror("xdlopen: %s\n", lt_dlerror());
75 | void *xdlopen(const char *module)
77 |       h = dlopen(module, RTLD_NOW);
105 | void *xdlopen(const char *module)
136 | void *xdlopen(const char *module)
{% endraw %}

```
### src/glpk/glpsql.c

```c

{% raw %}
708 |       h_odbc = xdlopen(libodbc);
1320 |       h_mysql = xdlopen(libmysql);
{% endraw %}

```
### src/glpk/glpenv.h

```c

{% raw %}
217 | void *xdlopen(const char *module);
{% endraw %}

```