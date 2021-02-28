---
name: "postgresql"
layout: package
next_package: sst-macro
previous_package: mpc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 10.3
22 / 6508 files match, 15 filtered matches.

 - [src/include/utils/dynamic_loader.h](#srcincludeutilsdynamic_loaderh)
 - [src/backend/port/dynloader/win32.h](#srcbackendportdynloaderwin32h)
 - [src/backend/port/dynloader/freebsd.h](#srcbackendportdynloaderfreebsdh)
 - [src/backend/port/dynloader/darwin.h](#srcbackendportdynloaderdarwinh)
 - [src/backend/port/dynloader/win32.c](#srcbackendportdynloaderwin32c)
 - [src/backend/port/dynloader/hpux.h](#srcbackendportdynloaderhpuxh)
 - [src/backend/port/dynloader/netbsd.c](#srcbackendportdynloadernetbsdc)
 - [src/backend/port/dynloader/netbsd.h](#srcbackendportdynloadernetbsdh)
 - [src/backend/port/dynloader/openbsd.h](#srcbackendportdynloaderopenbsdh)
 - [src/backend/port/dynloader/linux.c](#srcbackendportdynloaderlinuxc)
 - [src/backend/port/dynloader/freebsd.c](#srcbackendportdynloaderfreebsdc)
 - [src/backend/port/dynloader/openbsd.c](#srcbackendportdynloaderopenbsdc)
 - [src/backend/port/dynloader/darwin.c](#srcbackendportdynloaderdarwinc)
 - [src/backend/port/dynloader/hpux.c](#srcbackendportdynloaderhpuxc)
 - [src/backend/utils/fmgr/dfmgr.c](#srcbackendutilsfmgrdfmgrc)

### src/include/utils/dynamic_loader.h

```c

{% raw %}
17 | 
18 | 
19 | extern void *pg_dlopen(char *filename);
20 | extern PGFunction pg_dlsym(void *handle, char *funcname);
21 | extern void pg_dlclose(void *handle);
22 | extern char *pg_dlerror(void);
{% endraw %}

```
### src/backend/port/dynloader/win32.h

```c

{% raw %}
12 | 
13 | char	   *dlerror(void);
14 | int			dlclose(void *handle);
15 | void	   *dlsym(void *handle, const char *symbol);
16 | void	   *dlopen(const char *path, int mode);
17 | 
{% endraw %}

```
### src/backend/port/dynloader/freebsd.h

```c

{% raw %}
51 | 
52 | char	   *BSD44_derived_dlerror(void);
53 | void	   *BSD44_derived_dlopen(const char *filename, int num);
54 | void	   *BSD44_derived_dlsym(void *handle, const char *name);
55 | void		BSD44_derived_dlclose(void *handle);
56 | 
{% endraw %}

```
### src/backend/port/dynloader/darwin.h

```c

{% raw %}
2 | #include "fmgr.h"
3 | 
4 | void	   *pg_dlopen(char *filename);
5 | PGFunction	pg_dlsym(void *handle, char *funcname);
6 | void		pg_dlclose(void *handle);
7 | char	   *pg_dlerror(void);
{% endraw %}

```
### src/backend/port/dynloader/win32.c

```c

{% raw %}
3 | 
4 | char	   *dlerror(void);
5 | int			dlclose(void *handle);
6 | void	   *dlsym(void *handle, const char *symbol);
7 | void	   *dlopen(const char *path, int mode);
8 | 
49 | }
50 | 
51 | void *
52 | dlsym(void *handle, const char *symbol)
53 | {
54 | 	void	   *ptr;
{% endraw %}

```
### src/backend/port/dynloader/hpux.h

```c

{% raw %}
19 | #include "fmgr.h"
20 | 
21 | extern void *pg_dlopen(char *filename);
22 | extern PGFunction pg_dlsym(void *handle, char *funcname);
23 | extern void pg_dlclose(void *handle);
24 | extern char *pg_dlerror(void);
{% endraw %}

```
### src/backend/port/dynloader/netbsd.c

```c

{% raw %}
71 | }
72 | 
73 | void *
74 | BSD44_derived_dlsym(void *handle, const char *name)
75 | {
76 | #if !defined(HAVE_DLOPEN)
77 | 	snprintf(error_message, sizeof(error_message),
78 | 			 "dlsym (%s) failed", name);
79 | 	return NULL;
80 | #else
89 | 		name = buf;
90 | 	}
91 | #endif							/* !__ELF__ */
92 | 	if ((vp = dlsym(handle, (char *) name)) == NULL)
93 | 		snprintf(error_message, sizeof(error_message),
94 | 				 "dlsym (%s) failed", name);
95 | 	return vp;
96 | #endif
{% endraw %}

```
### src/backend/port/dynloader/netbsd.h

```c

{% raw %}
52 | 
53 | char	   *BSD44_derived_dlerror(void);
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
55 | void	   *BSD44_derived_dlsym(void *handle, const char *name);
56 | void		BSD44_derived_dlclose(void *handle);
57 | 
{% endraw %}

```
### src/backend/port/dynloader/openbsd.h

```c

{% raw %}
51 | 
52 | char	   *BSD44_derived_dlerror(void);
53 | void	   *BSD44_derived_dlopen(const char *filename, int num);
54 | void	   *BSD44_derived_dlsym(void *handle, const char *name);
55 | void		BSD44_derived_dlclose(void *handle);
56 | 
{% endraw %}

```
### src/backend/port/dynloader/linux.c

```c

{% raw %}
100 | }
101 | 
102 | PGFunction
103 | pg_dlsym(void *handle, char *funcname)
104 | {
105 | #ifndef HAVE_DLD_H
{% endraw %}

```
### src/backend/port/dynloader/freebsd.c

```c

{% raw %}
71 | }
72 | 
73 | void *
74 | BSD44_derived_dlsym(void *handle, const char *name)
75 | {
76 | #if !defined(HAVE_DLOPEN)
77 | 	snprintf(error_message, sizeof(error_message),
78 | 			 "dlsym (%s) failed", name);
79 | 	return NULL;
80 | #else
89 | 		name = buf;
90 | 	}
91 | #endif							/* !__ELF__ */
92 | 	if ((vp = dlsym(handle, (char *) name)) == NULL)
93 | 		snprintf(error_message, sizeof(error_message),
94 | 				 "dlsym (%s) failed", name);
95 | 	return vp;
96 | #endif
{% endraw %}

```
### src/backend/port/dynloader/openbsd.c

```c

{% raw %}
71 | }
72 | 
73 | void *
74 | BSD44_derived_dlsym(void *handle, const char *name)
75 | {
76 | #if !defined(HAVE_DLOPEN)
77 | 	snprintf(error_message, sizeof(error_message),
78 | 			 "dlsym (%s) failed", name);
79 | 	return NULL;
80 | #else
89 | 		name = buf;
90 | 	}
91 | #endif							/* !__ELF__ */
92 | 	if ((vp = dlsym(handle, (char *) name)) == NULL)
93 | 		snprintf(error_message, sizeof(error_message),
94 | 				 "dlsym (%s) failed", name);
95 | 	return vp;
96 | #endif
{% endraw %}

```
### src/backend/port/dynloader/darwin.c

```c

{% raw %}
31 | }
32 | 
33 | PGFunction
34 | pg_dlsym(void *handle, char *funcname)
35 | {
36 | 	/* Do not prepend an underscore: see dlopen(3) */
37 | 	return dlsym(handle, funcname);
38 | }
39 | 
72 | }
73 | 
74 | PGFunction
75 | pg_dlsym(void *handle, char *funcname)
76 | {
77 | 	NSSymbol symbol;
{% endraw %}

```
### src/backend/port/dynloader/hpux.c

```c

{% raw %}
40 | }
41 | 
42 | PGFunction
43 | pg_dlsym(void *handle, char *funcname)
44 | {
45 | 	PGFunction	f;
{% endraw %}

```
### src/backend/utils/fmgr/dfmgr.c

```c

{% raw %}
112 | 	 * should declare its second argument as "const char *", but older
113 | 	 * platforms might not, so for the time being we just cast away const.
114 | 	 */
115 | 	retval = (PGFunction) pg_dlsym(lib_handle, (char *) funcname);
116 | 
117 | 	if (retval == NULL && signalNotFound)
161 | lookup_external_function(void *filehandle, const char *funcname)
162 | {
163 | 	/* as above, cast away const for the time being */
164 | 	return (PGFunction) pg_dlsym(filehandle, (char *) funcname);
165 | }
166 | 
241 | 
242 | 		/* Check the magic function to determine compatibility */
243 | 		magic_func = (PGModuleMagicFunction)
244 | 			pg_dlsym(file_scanner->handle, PG_MAGIC_FUNCTION_NAME_STRING);
245 | 		if (magic_func)
246 | 		{
275 | 		/*
276 | 		 * If the library has a _PG_init() function, call it.
277 | 		 */
278 | 		PG_init = (PG_init_t) pg_dlsym(file_scanner->handle, "_PG_init");
279 | 		if (PG_init)
280 | 			(*PG_init) ();
435 | 			/*
436 | 			 * If the library has a _PG_fini() function, call it.
437 | 			 */
438 | 			PG_fini = (PG_fini_t) pg_dlsym(file_scanner->handle, "_PG_fini");
439 | 			if (PG_fini)
440 | 				(*PG_fini) ();
{% endraw %}

```