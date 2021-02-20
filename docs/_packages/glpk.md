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
705 | 
706 |    if (h_odbc == NULL)
707 |    {
708 |       h_odbc = xdlopen(libodbc);
709 |       if (h_odbc == NULL)
710 |       {  xprintf("unable to open library %s\n", libodbc);
1327 | 
1328 |    if (h_mysql == NULL)
1329 |    {
1330 |       h_mysql = xdlopen(libmysql);
1331 |       if (h_mysql == NULL)
1332 |       {  xprintf("unable to open library %s\n", libmysql);
{% endraw %}

```
### src/env/env.h

```c

{% raw %}
245 | /* compute difference between two time values */
246 | 
247 | #define xdlopen _glp_dlopen
248 | void *xdlopen(const char *module);
249 | /* open dynamically linked library */
250 | 
{% endraw %}

```
### src/env/dlsup.c

```c

{% raw %}
32 | 
33 | #include <ltdl.h>
34 | 
35 | void *xdlopen(const char *module)
36 | {     /* open dynamically linked library */
37 |       void *h = NULL;
39 |       {  put_err_msg(lt_dlerror());
40 |          goto done;
41 |       }
42 |       h = lt_dlopen(module);
43 |       if (h == NULL)
44 |       {  put_err_msg(lt_dlerror());
45 |          if (lt_dlexit() != 0)
46 |             xerror("xdlopen: %s\n", lt_dlerror());
47 |       }
48 | done: return h;
74 | 
75 | #include <dlfcn.h>
76 | 
77 | void *xdlopen(const char *module)
78 | {     /* open dynamically linked library */
79 |       void *h;
80 |       h = dlopen(module, RTLD_NOW);
81 |       if (h == NULL)
82 |          put_err_msg(dlerror());
107 | 
108 | #include <windows.h>
109 | 
110 | void *xdlopen(const char *module)
111 | {     /* open dynamically linked library */
112 |       void *h;
141 | 
142 | #else
143 | 
144 | void *xdlopen(const char *module)
145 | {     /* open dynamically linked library */
146 |       xassert(module == module);
{% endraw %}

```