---
name: "gpdb"
layout: package
next_package: rr
previous_package: geoip-api-c
languages: ['cpp']
---
## 6.1.0
28 / 8154 files match

 - [configure.in](#configurein)
 - [src/include/pg_config.h.win32](#srcincludepg_confighwin32)
 - [src/include/pg_config.h.in](#srcincludepg_confighin)
 - [src/include/utils/dynamic_loader.h](#srcincludeutilsdynamic_loaderh)
 - [src/backend/port/dynloader/win32.h](#srcbackendportdynloaderwin32h)
 - [src/backend/port/dynloader/cygwin.h](#srcbackendportdynloadercygwinh)
 - [src/backend/port/dynloader/freebsd.h](#srcbackendportdynloaderfreebsdh)
 - [src/backend/port/dynloader/darwin.h](#srcbackendportdynloaderdarwinh)
 - [src/backend/port/dynloader/sco.h](#srcbackendportdynloaderscoh)
 - [src/backend/port/dynloader/win32.c](#srcbackendportdynloaderwin32c)
 - [src/backend/port/dynloader/hpux.h](#srcbackendportdynloaderhpuxh)
 - [src/backend/port/dynloader/osf.h](#srcbackendportdynloaderosfh)
 - [src/backend/port/dynloader/solaris.h](#srcbackendportdynloadersolarish)
 - [src/backend/port/dynloader/netbsd.c](#srcbackendportdynloadernetbsdc)
 - [src/backend/port/dynloader/aix.h](#srcbackendportdynloaderaixh)
 - [src/backend/port/dynloader/netbsd.h](#srcbackendportdynloadernetbsdh)
 - [src/backend/port/dynloader/unixware.h](#srcbackendportdynloaderunixwareh)
 - [src/backend/port/dynloader/openbsd.h](#srcbackendportdynloaderopenbsdh)
 - [src/backend/port/dynloader/linux.c](#srcbackendportdynloaderlinuxc)
 - [src/backend/port/dynloader/freebsd.c](#srcbackendportdynloaderfreebsdc)
 - [src/backend/port/dynloader/nextstep.c](#srcbackendportdynloadernextstepc)
 - [src/backend/port/dynloader/openbsd.c](#srcbackendportdynloaderopenbsdc)
 - [src/backend/port/dynloader/darwin.c](#srcbackendportdynloaderdarwinc)
 - [src/backend/port/dynloader/hpux.c](#srcbackendportdynloaderhpuxc)
 - [src/backend/port/dynloader/linux.h](#srcbackendportdynloaderlinuxh)
 - [src/backend/utils/fmgr/dfmgr.c](#srcbackendutilsfmgrdfmgrc)
 - [src/test/regress/pg_regress.c](#srctestregresspg_regressc)
 - [contrib/pg_upgrade/page.c](#contribpg_upgradepagec)

### configure.in

```

{% raw %}
1320 | AC_SEARCH_LIBS(dlopen, dl)
1912 | 	dlopen
{% endraw %}

```
### src/include/pg_config.h.win32

```

{% raw %}
153 | /* Define to 1 if you have the `dlopen' function. */
154 | /* #undef HAVE_DLOPEN */
{% endraw %}

```
### src/include/pg_config.h.in

```

{% raw %}
182 | /* Define to 1 if you have the `dlopen' function. */
183 | #undef HAVE_DLOPEN
{% endraw %}

```
### src/include/utils/dynamic_loader.h

```cpp

{% raw %}
19 | extern void *pg_dlopen(char *filename);
{% endraw %}

```
### src/backend/port/dynloader/win32.h

```cpp

{% raw %}
8 | #define pg_dlopen(f)	dlopen((f), 1)
16 | void	   *dlopen(const char *path, int mode);
{% endraw %}

```
### src/backend/port/dynloader/cygwin.h

```cpp

{% raw %}
19 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
30 | #define pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/backend/port/dynloader/freebsd.h

```cpp

{% raw %}
26 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
37 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
48 | #define		   pg_dlopen(f)    BSD44_derived_dlopen((f), RTLD_NOW | RTLD_GLOBAL)
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/darwin.h

```cpp

{% raw %}
4 | void	   *pg_dlopen(char *filename);
{% endraw %}

```
### src/backend/port/dynloader/sco.h

```cpp

{% raw %}
23 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
29 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
40 | #define pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/backend/port/dynloader/win32.c

```cpp

{% raw %}
7 | void	   *dlopen(const char *path, int mode);
67 | dlopen(const char *path, int mode)
{% endraw %}

```
### src/backend/port/dynloader/hpux.h

```cpp

{% raw %}
21 | extern void *pg_dlopen(char *filename);
{% endraw %}

```
### src/backend/port/dynloader/osf.h

```cpp

{% raw %}
24 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
30 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
41 | #define  pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/backend/port/dynloader/solaris.h

```cpp

{% raw %}
21 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
32 | #define pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/backend/port/dynloader/netbsd.c

```cpp

{% raw %}
57 | BSD44_derived_dlopen(const char *file, int num)
59 | #if !defined(HAVE_DLOPEN)
61 | 			 "dlopen (%s) not supported", file);
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
76 | #if !defined(HAVE_DLOPEN)
102 | #if defined(HAVE_DLOPEN)
{% endraw %}

```
### src/backend/port/dynloader/aix.h

```cpp

{% raw %}
22 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
33 | #define  pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/backend/port/dynloader/netbsd.h

```cpp

{% raw %}
27 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
38 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
49 | #define		   pg_dlopen(f)    BSD44_derived_dlopen((f), RTLD_NOW | RTLD_GLOBAL)
55 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/unixware.h

```cpp

{% raw %}
26 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
32 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
43 | #define pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/backend/port/dynloader/openbsd.h

```cpp

{% raw %}
26 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
37 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
48 | #define		   pg_dlopen(f)    BSD44_derived_dlopen((f), RTLD_NOW | RTLD_GLOBAL)
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/linux.c

```cpp

{% raw %}
28 | #ifndef HAVE_DLOPEN
31 | pg_dlopen(char *filename)
41 | 	 * needs to do this the first time pg_dlopen is called.)
132 | #endif   /* !HAVE_DLOPEN */
{% endraw %}

```
### src/backend/port/dynloader/freebsd.c

```cpp

{% raw %}
57 | BSD44_derived_dlopen(const char *file, int num)
59 | #if !defined(HAVE_DLOPEN)
61 | 			 "dlopen (%s) not supported", file);
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
76 | #if !defined(HAVE_DLOPEN)
102 | #if defined(HAVE_DLOPEN)
{% endraw %}

```
### src/backend/port/dynloader/nextstep.c

```cpp

{% raw %}
41 | next_dlopen(char *name)
{% endraw %}

```
### src/backend/port/dynloader/openbsd.c

```cpp

{% raw %}
57 | BSD44_derived_dlopen(const char *file, int num)
59 | #if !defined(HAVE_DLOPEN)
61 | 			 "dlopen (%s) not supported", file);
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
76 | #if !defined(HAVE_DLOPEN)
102 | #if defined(HAVE_DLOPEN)
{% endraw %}

```
### src/backend/port/dynloader/darwin.c

```cpp

{% raw %}
3 |  * If dlopen() is available (Darwin 10.3 and later), we just use it.
10 | #ifdef HAVE_DLOPEN
19 | #ifdef HAVE_DLOPEN
22 | pg_dlopen(char *filename)
24 | 	return dlopen(filename, RTLD_NOW | RTLD_GLOBAL);
36 | 	/* Do not prepend an underscore: see dlopen(3) */
45 | #else							/* !HAVE_DLOPEN */
56 | pg_dlopen(char *filename)
134 | #endif   /* HAVE_DLOPEN */
{% endraw %}

```
### src/backend/port/dynloader/hpux.c

```cpp

{% raw %}
28 | pg_dlopen(char *filename)
{% endraw %}

```
### src/backend/port/dynloader/linux.h

```cpp

{% raw %}
17 | #ifdef HAVE_DLOPEN
22 | #ifdef HAVE_DLOPEN
26 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
37 | #define pg_dlopen(f)	dlopen((f), RTLD_NOW | RTLD_GLOBAL)
41 | #endif   /* HAVE_DLOPEN */
{% endraw %}

```
### src/backend/utils/fmgr/dfmgr.c

```cpp

{% raw %}
230 | 		file_scanner->handle = pg_dlopen(file_scanner->filename);
{% endraw %}

```
### src/test/regress/pg_regress.c

```cpp

{% raw %}
1300 | 		 * executables, not dlopen'ed ones). Feel free to account for others
{% endraw %}

```
### contrib/pg_upgrade/page.c

```cpp

{% raw %}
137 | 	if ((plugin = pg_dlopen(pluginName)) == NULL)
{% endraw %}

```