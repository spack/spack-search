---
name: "r-igraph"
layout: package
next_package: r-lpsolve
previous_package: r-httpuv
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
33 | 
34 | #include <ltdl.h>
35 | 
36 | void *xdlopen(const char *module)
37 | {     void *h = NULL;
38 |       if (lt_dlinit() != 0)
39 |       {  lib_err_msg(lt_dlerror());
40 |          goto done;
41 |       }
42 |       h = lt_dlopen(module);
43 |       if (h == NULL)
44 |       {  lib_err_msg(lt_dlerror());
45 |          if (lt_dlexit() != 0)
46 |             xerror("xdlopen: %s\n", lt_dlerror());
47 |       }
48 | done: return h;
72 | 
73 | #include <dlfcn.h>
74 | 
75 | void *xdlopen(const char *module)
76 | {     void *h;
77 |       h = dlopen(module, RTLD_NOW);
78 |       if (h == NULL)
79 |          lib_err_msg(dlerror());
102 | 
103 | #include <windows.h>
104 | 
105 | void *xdlopen(const char *module)
106 | {     void *h;
107 |       h = LoadLibrary(module);
133 | 
134 | #else
135 | 
136 | void *xdlopen(const char *module)
137 | {     xassert(module == module);
138 |       lib_err_msg("Shared libraries not supported");
{% endraw %}

```
### src/glpk/glpsql.c

```c

{% raw %}
705 | 
706 |    if (h_odbc == NULL)
707 |    {
708 |       h_odbc = xdlopen(libodbc);
709 |       if (h_odbc == NULL)
710 |       {  xprintf("unable to open library %s\n", libodbc);
1317 | 
1318 |    if (h_mysql == NULL)
1319 |    {
1320 |       h_mysql = xdlopen(libmysql);
1321 |       if (h_mysql == NULL)
1322 |       {  xprintf("unable to open library %s\n", libmysql);
{% endraw %}

```
### src/glpk/glpenv.h

```c

{% raw %}
214 | int xfprintf(XFILE *file, const char *fmt, ...);
215 | 
216 | #define xdlopen _glp_xdlopen
217 | void *xdlopen(const char *module);
218 | 
219 | #define xdlsym _glp_xdlsym
{% endraw %}

```