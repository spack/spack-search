---
name: "r"
layout: package
next_package: nspr
previous_package: keepalived
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.3.1
12 / 4124 files match, 3 filtered matches.

 - [src/unix/hpdlfcn.c](#srcunixhpdlfcnc)
 - [src/unix/dynload.c](#srcunixdynloadc)
 - [src/unix/hpdlfcn.h](#srcunixhpdlfcnh)

### src/unix/hpdlfcn.c

```c

{% raw %}
124 |  * Opening and Closing Liraries.
125 |  */
126 | 
127 | void *dlopen(const char *fname, int mode)
128 | {
129 |   shl_t handle;
{% endraw %}

```
### src/unix/dynload.c

```c

{% raw %}
21 | 
22 | 
23 | /* This provides a table of built-in C and Fortran functions.
24 |    We include this table, even when we have dlopen and friends.
25 |    This is so that the functions are actually loaded at link time. */
26 | 
88 |     int openFlag = 0;
89 | 
90 |     openFlag = computeDLOpenFlag(asLocal, now);
91 |     handle = (void *) dlopen(path,openFlag);
92 | 
93 |     return(handle);
123 | 
124 | 
125 |  /*
126 |     Computes the flag to be passed as the second argument to dlopen(),
127 |     controlling whether the local or global symbol integration
128 |     and lazy or eager resolution of the undefined symbols.
162 | 
163 |     int openFlag = 0;		/* Default value so no-ops for undefined
164 | 				   flags should do nothing in the
165 | 				   resulting dlopen(). */
166 | 
167 |     if(asLocal != 0) {
{% endraw %}

```
### src/unix/hpdlfcn.h

```c

{% raw %}
1 | void *dlsym(void *, const char *);
2 | int dlclose(void *);
{% endraw %}

```