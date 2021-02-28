---
name: "yorick"
layout: package
next_package: chrony
previous_package: libmicrohttpd
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.04
9 / 571 files match, 7 filtered matches.

 - [yorick/dlsym.c](#yorickdlsymc)
 - [yorick/task.c](#yoricktaskc)
 - [play/pstdlib.h](#playpstdlibh)
 - [play/win/wdl.c](#playwinwdlc)
 - [play/unix/config.c](#playunixconfigc)
 - [play/unix/udltest.c](#playunixudltestc)
 - [play/unix/udl.c](#playunixudlc)

### yorick/dlsym.c

```c

{% raw %}
11 |  * is to include these stub routines when you link.
12 |  */
13 | 
14 | void *dlopen()
15 | {
16 |   return 0;
{% endraw %}

```
### yorick/task.c

```c

{% raw %}
1438 | 
1439 |   if (!yplug_path) Y_plug_dir(0);
1440 | 
1441 |   plug = p_dlopen(pkgname);
1442 |   if (!plug && !YIsAbsolute(pkgname)) {
1443 |     /* check in plug_dir and Y_HOME/lib before giving up */
1444 |     char *tmp;
1445 |     for (i=0 ; yplug_path[i] ; i++) {
1446 |       tmp = p_strncat(yplug_path[i], pkgname, 0L);
1447 |       plug = p_dlopen(tmp);
1448 |       p_free(tmp);
1449 |       if (plug) break;
{% endraw %}

```
### play/pstdlib.h

```c

{% raw %}
68 |  * type is 0 if expecting a function, 1 if expecting data
69 |  * paddr is &addr where addr is void* or void(*)(),
70 |  * p_dlsym return value is 0 on success, 1 on failure */
71 | PLUG_API void *p_dlopen(const char *dlname);
72 | PLUG_API int p_dlsym(void *handle, const char *symbol, int type, void *paddr);
73 | 
{% endraw %}

```
### play/win/wdl.c

```c

{% raw %}
24 | #endif
25 | 
26 | void *
27 | p_dlopen(const char *dlname)
28 | {
29 |   void *handle = 0;
49 | 
50 | /* ARGSUSED */
51 | void *
52 | p_dlopen(const char *dlname)
53 | {
54 |   return 0;
{% endraw %}

```
### play/unix/config.c

```c

{% raw %}
96 |     void *data;
97 |     void (*function)(int);
98 |   } addr;
99 |   void *h = test_dlopen();
100 |   if (!h) {
101 |     return 1;
{% endraw %}

```
### play/unix/udltest.c

```c

{% raw %}
43 | # define PLUG_FLAGS RTLD_LAZY | RTLD_GLOBAL
44 | #endif
45 | 
46 | extern void *test_dlopen(void);
47 | extern int test_dlsym(void *handle, int dat, void *paddr);
48 | 
49 | void *
50 | test_dlopen(void)
51 | {
52 |   return dlopen("./udltest" PLUG_SUFFIX, PLUG_FLAGS);
53 | }
54 | 
74 | # define PLUG_FLAGS BIND_DEFERRED
75 | #endif
76 | 
77 | extern void *test_dlopen(void);
78 | extern int test_dlsym(void *handle, int dat, void *paddr);
79 | 
80 | void *
81 | test_dlopen(void)
82 | {
83 |   return (void *)shl_load("./udltest" PLUG_SUFFIX, PLUG_FLAGS);
102 | #endif
103 | 
104 | void *
105 | test_dlopen(void)
106 | {
107 |   void *handle = 0;
140 | # define PLUG_FLAGS NSLOOKUPSYMBOLINIMAGE_OPTION_BIND
141 | #endif
142 | 
143 | extern void *test_dlopen(void);
144 | extern int test_dlsym(void *handle, int dat, void *paddr);
145 | 
146 | void *
147 | test_dlopen(void)
148 | {
149 |   return (void *)NSAddImage("./udltest" PLUG_SUFFIX,
{% endraw %}

```
### play/unix/udl.c

```c

{% raw %}
32 | #endif
33 | 
34 | void *
35 | p_dlopen(const char *dlname)
36 | {
37 |   void *handle = 0;
38 |   if (dlname && dlname[0]) {
39 |     char *name = p_strncat(u_pathname(dlname), PLUG_SUFFIX, 0);
40 |     handle = dlopen(name, PLUG_FLAGS);
41 |     p_free(name);
42 |   }
71 | #endif
72 | 
73 | void *
74 | p_dlopen(const char *dlname)
75 | {
76 |   void *handle = 0;
105 | #endif
106 | 
107 | void *
108 | p_dlopen(const char *dlname)
109 | {
110 |   void *handle = 0;
162 | #endif
163 | 
164 | void *
165 | p_dlopen(const char *dlname)
166 | {
167 |   void *handle = 0;
197 | 
198 | /* ARGSUSED */
199 | void *
200 | p_dlopen(const char *dlname)
201 | {
202 |   return 0;
{% endraw %}

```