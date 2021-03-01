---
name: "swipl"
layout: package
next_package: tau
previous_package: stat
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 8.0.3
5 / 3902 files match, 5 filtered matches.

 - [src/SWI-Prolog.h](#srcswi-prologh)
 - [src/pl-nt.c](#srcpl-ntc)
 - [src/pl-load.c](#srcpl-loadc)
 - [src/pl-beos.c](#srcpl-beosc)
 - [packages/xpce/src/x11/x11-compat.c](#packagesxpcesrcx11x11-compatc)

### src/SWI-Prolog.h

```c

{% raw %}
941 | 
942 | PL_EXPORT(void *)	PL_dlopen(const char *file, int flags);
943 | PL_EXPORT(const char *) PL_dlerror(void);
944 | PL_EXPORT(void *)	PL_dlsym(void *handle, char *symbol);
945 | PL_EXPORT(int)		PL_dlclose(void *handle);
946 | 
{% endraw %}

```
### src/pl-nt.c

```c

{% raw %}
767 | 
768 | 
769 | void *
770 | PL_dlsym(void *handle, char *symbol)
771 | { void *addr = GetProcAddress(handle, symbol);
772 | 
{% endraw %}

```
### src/pl-load.c

```c

{% raw %}
87 | #define dlerror()	    OsError()
88 | 
89 | void *
90 | dlsym(void *handle, const char *name)
91 | { void *value;
92 |   shl_t h = handle;
148 | }
149 | 
150 | void *
151 | PL_dlsym(void *handle, char *symbol)
152 | { return dlsym(handle, symbol);
153 | }
154 | 
279 | 
280 | /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
281 | Some systems (notably MacOS X) prefixes symbols with _. In some version
282 | of this OS, dlsym() adds an _, in others not.  We'll try to work around
283 | this junk with a runtime test ...
284 | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
295 |     fail;
296 | 
297 | #ifdef LD_SYMBOL_PREFIX			/* first try plain anyway */
298 |   if ( !(ef = (dl_funcptr) PL_dlsym(e->dlhandle, fname)) )
299 |   { char symname[MAXSYMBOLLEN+1];
300 | 
306 | 
307 |     strcpy(symname, LD_SYMBOL_PREFIX);
308 |     strcat(symname, fname);
309 |     ef = (dl_funcptr) dlsym(e->dlhandle, symname);
310 |   }
311 | #else
312 |   ef = (dl_funcptr) PL_dlsym(e->dlhandle, fname);
313 | #endif
314 |   if ( ef )
{% endraw %}

```
### src/pl-beos.c

```c

{% raw %}
73 | 
74 | 
75 | void *
76 | PL_dlsym(void *handle, char *symbol)
77 | { void *address;
78 | 
{% endraw %}

```
### packages/xpce/src/x11/x11-compat.c

```c

{% raw %}
57 | 
58 | 
59 | void *
60 | dlsym(void *handle, char *symbol)
61 | { Cprintf("dlsym(%p, %s)\n", handle, symbol);
62 | 
63 |   return NULL;
{% endraw %}

```