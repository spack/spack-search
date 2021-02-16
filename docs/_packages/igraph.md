---
name: "igraph"
layout: package
next_package: py-pip
previous_package: openexr
languages: ['c']
---
## 0.7.1
5 / 1345 files match, 3 filtered matches.

 - [optional/glpk/glpenv08.c](#optionalglpkglpenv08c)
 - [optional/glpk/glpsql.c](#optionalglpkglpsqlc)
 - [optional/glpk/glpenv.h](#optionalglpkglpenvh)

### optional/glpk/glpenv08.c

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
### optional/glpk/glpsql.c

```c

{% raw %}
708 |       h_odbc = xdlopen(libodbc);
1320 |       h_mysql = xdlopen(libmysql);
{% endraw %}

```
### optional/glpk/glpenv.h

```c

{% raw %}
217 | void *xdlopen(const char *module);
{% endraw %}

```