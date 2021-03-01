---
name: "yorick"
layout: package
next_package: zabbix
previous_package: yasm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.04
10 / 571 files match, 7 filtered matches.

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
16 |   return 0;
17 | }
18 | 
19 | void *dlsym()
20 | {
21 |   return 0;
{% endraw %}

```
### yorick/task.c

```c

{% raw %}
1451 |   }
1452 |   if (plug) {
1453 |     char *tmp = p_strncat("yk_", pname, 0);
1454 |     int failed = p_dlsym(plug, tmp, 0, &init);
1455 |     p_free(tmp);
1456 |     if (failed || !init)
{% endraw %}

```
### play/pstdlib.h

```c

{% raw %}
69 |  * paddr is &addr where addr is void* or void(*)(),
70 |  * p_dlsym return value is 0 on success, 1 on failure */
71 | PLUG_API void *p_dlopen(const char *dlname);
72 | PLUG_API int p_dlsym(void *handle, const char *symbol, int type, void *paddr);
73 | 
74 | /* interface for synchronous subprocess
{% endraw %}

```
### play/win/wdl.c

```c

{% raw %}
36 | }
37 | 
38 | int
39 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
40 | {
41 |   void **addr = paddr;
56 | 
57 | /* ARGSUSED */
58 | int
59 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
60 | {
61 |   void **addr = paddr;
{% endraw %}

```
### play/unix/config.c

```c

{% raw %}
99 |   void *h = test_dlopen();
100 |   if (!h) {
101 |     return 1;
102 |   } else if (!(test_dlsym(h, 1, &addr) & 1)) {
103 |     return 2;
104 |   } else {
105 |     int *pdat = addr.data;
106 |     if (!pdat || pdat[0]!=-1 || pdat[1]!=-2) {
107 |       return 3;
108 |     } else if (!(test_dlsym(h, 0, &addr) & 2)) {
109 |       return 4;
110 |     } else {
{% endraw %}

```
### play/unix/udltest.c

```c

{% raw %}
44 | #endif
45 | 
46 | extern void *test_dlopen(void);
47 | extern int test_dlsym(void *handle, int dat, void *paddr);
48 | 
49 | void *
53 | }
54 | 
55 | int
56 | test_dlsym(void *handle, int dat, void *paddr)
57 | {
58 |   void **addr = paddr;
59 |   addr[0] = dlsym(handle, (dat? "dat" : "fun"));
60 |   return addr[0]? 3 : 0;
61 | }
75 | #endif
76 | 
77 | extern void *test_dlopen(void);
78 | extern int test_dlsym(void *handle, int dat, void *paddr);
79 | 
80 | void *
84 | }
85 | 
86 | int
87 | test_dlsym(void *handle, int dat, void *paddr)
88 | {
89 |   void **addr = paddr;
117 | }
118 | 
119 | int
120 | test_dlsym(void *handle, int dat, void *paddr)
121 | {
122 |   void **addr = paddr;
141 | #endif
142 | 
143 | extern void *test_dlopen(void);
144 | extern int test_dlsym(void *handle, int dat, void *paddr);
145 | 
146 | void *
151 | }
152 | 
153 | int
154 | test_dlsym(void *handle, int dat, void *paddr)
155 | {
156 |   void **addr = paddr;
{% endraw %}

```
### play/unix/udl.c

```c

{% raw %}
44 | }
45 | 
46 | int
47 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
48 | {
49 |   void **addr = paddr;
50 |   addr[0] = dlsym(handle, symbol);
51 |   /* correct way to detect failure if a==0 were legal:
52 |    *   const char *msg = dlerror();
83 | }
84 | 
85 | int
86 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
87 | {
88 |   void **addr = paddr;
124 | }
125 | 
126 | int
127 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
128 | {
129 |   void **addr = paddr;
174 | }
175 | 
176 | int
177 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
178 | {
179 |   void **addr = paddr;
204 | 
205 | /* ARGSUSED */
206 | int
207 | p_dlsym(void *handle, const char *symbol, int type, void *paddr)
208 | {
209 |   void **addr = paddr;
{% endraw %}

```