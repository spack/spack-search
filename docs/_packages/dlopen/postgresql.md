---
name: "postgresql"
layout: package
next_package: procps
previous_package: poppler
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 10.3
31 / 6508 files match, 15 filtered matches.

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
16 | #include "fmgr.h"
17 | 
18 | 
19 | extern void *pg_dlopen(char *filename);
20 | extern PGFunction pg_dlsym(void *handle, char *funcname);
21 | extern void pg_dlclose(void *handle);
{% endraw %}

```
### src/backend/port/dynloader/win32.h

```c

{% raw %}
13 | char	   *dlerror(void);
14 | int			dlclose(void *handle);
15 | void	   *dlsym(void *handle, const char *symbol);
16 | void	   *dlopen(const char *path, int mode);
17 | 
18 | #endif							/* PORT_PROTOS_H */
{% endraw %}

```
### src/backend/port/dynloader/freebsd.h

```c

{% raw %}
50 | #define		   pg_dlerror	   BSD44_derived_dlerror
51 | 
52 | char	   *BSD44_derived_dlerror(void);
53 | void	   *BSD44_derived_dlopen(const char *filename, int num);
54 | void	   *BSD44_derived_dlsym(void *handle, const char *name);
55 | void		BSD44_derived_dlclose(void *handle);
{% endraw %}

```
### src/backend/port/dynloader/darwin.h

```c

{% raw %}
1 | 
2 | #include "fmgr.h"
3 | 
4 | void	   *pg_dlopen(char *filename);
5 | PGFunction	pg_dlsym(void *handle, char *funcname);
6 | void		pg_dlclose(void *handle);
{% endraw %}

```
### src/backend/port/dynloader/win32.c

```c

{% raw %}
4 | char	   *dlerror(void);
5 | int			dlclose(void *handle);
6 | void	   *dlsym(void *handle, const char *symbol);
7 | void	   *dlopen(const char *path, int mode);
8 | 
9 | static char last_dyn_error[512];
64 | }
65 | 
66 | void *
67 | dlopen(const char *path, int mode)
68 | {
69 | 	HMODULE		h;
{% endraw %}

```
### src/backend/port/dynloader/hpux.h

```c

{% raw %}
18 | /* System includes */
19 | #include "fmgr.h"
20 | 
21 | extern void *pg_dlopen(char *filename);
22 | extern PGFunction pg_dlsym(void *handle, char *funcname);
23 | extern void pg_dlclose(void *handle);
{% endraw %}

```
### src/backend/port/dynloader/netbsd.c

```c

{% raw %}
54 | }
55 | 
56 | void *
57 | BSD44_derived_dlopen(const char *file, int num)
58 | {
59 | #if !defined(HAVE_DLOPEN)
60 | 	snprintf(error_message, sizeof(error_message),
61 | 			 "dlopen (%s) not supported", file);
62 | 	return NULL;
63 | #else
64 | 	void	   *vp;
65 | 
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
67 | 		snprintf(error_message, sizeof(error_message),
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
69 | 	return vp;
70 | #endif
{% endraw %}

```
### src/backend/port/dynloader/netbsd.h

```c

{% raw %}
51 | #define		   pg_dlerror	   BSD44_derived_dlerror
52 | 
53 | char	   *BSD44_derived_dlerror(void);
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
55 | void	   *BSD44_derived_dlsym(void *handle, const char *name);
56 | void		BSD44_derived_dlclose(void *handle);
{% endraw %}

```
### src/backend/port/dynloader/openbsd.h

```c

{% raw %}
50 | #define		   pg_dlerror	   BSD44_derived_dlerror
51 | 
52 | char	   *BSD44_derived_dlerror(void);
53 | void	   *BSD44_derived_dlopen(const char *filename, int num);
54 | void	   *BSD44_derived_dlsym(void *handle, const char *name);
55 | void		BSD44_derived_dlclose(void *handle);
{% endraw %}

```
### src/backend/port/dynloader/linux.c

```c

{% raw %}
28 | #ifndef HAVE_DLOPEN
29 | 
30 | void *
31 | pg_dlopen(char *filename)
32 | {
33 | #ifndef HAVE_DLD_H
{% endraw %}

```
### src/backend/port/dynloader/freebsd.c

```c

{% raw %}
54 | }
55 | 
56 | void *
57 | BSD44_derived_dlopen(const char *file, int num)
58 | {
59 | #if !defined(HAVE_DLOPEN)
60 | 	snprintf(error_message, sizeof(error_message),
61 | 			 "dlopen (%s) not supported", file);
62 | 	return NULL;
63 | #else
64 | 	void	   *vp;
65 | 
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
67 | 		snprintf(error_message, sizeof(error_message),
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
69 | 	return vp;
70 | #endif
{% endraw %}

```
### src/backend/port/dynloader/openbsd.c

```c

{% raw %}
54 | }
55 | 
56 | void *
57 | BSD44_derived_dlopen(const char *file, int num)
58 | {
59 | #if !defined(HAVE_DLOPEN)
60 | 	snprintf(error_message, sizeof(error_message),
61 | 			 "dlopen (%s) not supported", file);
62 | 	return NULL;
63 | #else
64 | 	void	   *vp;
65 | 
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
67 | 		snprintf(error_message, sizeof(error_message),
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
69 | 	return vp;
70 | #endif
{% endraw %}

```
### src/backend/port/dynloader/darwin.c

```c

{% raw %}
19 | #ifdef HAVE_DLOPEN
20 | 
21 | void *
22 | pg_dlopen(char *filename)
23 | {
24 | 	return dlopen(filename, RTLD_NOW | RTLD_GLOBAL);
25 | }
26 | 
53 | static NSObjectFileImageReturnCode cofiff_result = NSObjectFileImageFailure;
54 | 
55 | void *
56 | pg_dlopen(char *filename)
57 | {
58 | 	NSObjectFileImage image;
{% endraw %}

```
### src/backend/port/dynloader/hpux.c

```c

{% raw %}
25 | #include "utils/dynamic_loader.h"
26 | 
27 | void *
28 | pg_dlopen(char *filename)
29 | {
30 | 	/*
{% endraw %}

```
### src/backend/utils/fmgr/dfmgr.c

```c

{% raw %}
227 | #endif
228 | 		file_scanner->next = NULL;
229 | 
230 | 		file_scanner->handle = pg_dlopen(file_scanner->filename);
231 | 		if (file_scanner->handle == NULL)
232 | 		{
{% endraw %}

```