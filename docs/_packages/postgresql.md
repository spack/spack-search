---
name: "postgresql"
layout: package
next_package: wcs
previous_package: cpio
languages: ['html', 'cpp']
---
## 10.3
31 / 6508 files match

 - [configure.in](#configurein)
 - [src/include/pg_config.h.win32](#srcincludepg_confighwin32)
 - [src/include/pg_config.h.in](#srcincludepg_confighin)
 - [src/include/utils/dynamic_loader.h](#srcincludeutilsdynamic_loaderh)
 - [src/backend/port/dynloader/win32.h](#srcbackendportdynloaderwin32h)
 - [src/backend/port/dynloader/cygwin.h](#srcbackendportdynloadercygwinh)
 - [src/backend/port/dynloader/freebsd.h](#srcbackendportdynloaderfreebsdh)
 - [src/backend/port/dynloader/darwin.h](#srcbackendportdynloaderdarwinh)
 - [src/backend/port/dynloader/win32.c](#srcbackendportdynloaderwin32c)
 - [src/backend/port/dynloader/hpux.h](#srcbackendportdynloaderhpuxh)
 - [src/backend/port/dynloader/solaris.h](#srcbackendportdynloadersolarish)
 - [src/backend/port/dynloader/netbsd.c](#srcbackendportdynloadernetbsdc)
 - [src/backend/port/dynloader/aix.h](#srcbackendportdynloaderaixh)
 - [src/backend/port/dynloader/netbsd.h](#srcbackendportdynloadernetbsdh)
 - [src/backend/port/dynloader/openbsd.h](#srcbackendportdynloaderopenbsdh)
 - [src/backend/port/dynloader/linux.c](#srcbackendportdynloaderlinuxc)
 - [src/backend/port/dynloader/freebsd.c](#srcbackendportdynloaderfreebsdc)
 - [src/backend/port/dynloader/openbsd.c](#srcbackendportdynloaderopenbsdc)
 - [src/backend/port/dynloader/darwin.c](#srcbackendportdynloaderdarwinc)
 - [src/backend/port/dynloader/hpux.c](#srcbackendportdynloaderhpuxc)
 - [src/backend/port/dynloader/linux.h](#srcbackendportdynloaderlinuxh)
 - [src/backend/utils/fmgr/dfmgr.c](#srcbackendutilsfmgrdfmgrc)
 - [src/port/gettimeofday.c](#srcportgettimeofdayc)
 - [doc/src/sgml/release-9.0.sgml](#docsrcsgmlrelease-90sgml)
 - [doc/src/sgml/release-8.4.sgml](#docsrcsgmlrelease-84sgml)
 - [doc/src/sgml/release-8.2.sgml](#docsrcsgmlrelease-82sgml)
 - [doc/src/sgml/release-8.3.sgml](#docsrcsgmlrelease-83sgml)
 - [doc/src/sgml/html/release-8-4-8.html](#docsrcsgmlhtmlrelease-8-4-8html)
 - [doc/src/sgml/html/release-9-0-4.html](#docsrcsgmlhtmlrelease-9-0-4html)
 - [doc/src/sgml/html/release-8-2-21.html](#docsrcsgmlhtmlrelease-8-2-21html)
 - [doc/src/sgml/html/release-8-3-15.html](#docsrcsgmlhtmlrelease-8-3-15html)

### configure.in

```

{% raw %}
1023 | AC_SEARCH_LIBS(dlopen, dl)
1438 | AC_CHECK_FUNCS([cbrt clock_gettime dlopen fdatasync getifaddrs getpeerucred getrlimit mbstowcs_l memmove poll posix_fallocate pstat pthread_is_threaded_np readlink setproctitle setsid shm_open symlink sync_file_range towlower utime utimes wcstombs wcstombs_l])
{% endraw %}

```
### src/include/pg_config.h.win32

```

{% raw %}
111 | /* Define to 1 if you have the `dlopen' function. */
112 | /* #undef HAVE_DLOPEN */
{% endraw %}

```
### src/include/pg_config.h.in

```

{% raw %}
163 | /* Define to 1 if you have the `dlopen' function. */
164 | #undef HAVE_DLOPEN
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
25 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
36 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
47 | #define		   pg_dlopen(f)    BSD44_derived_dlopen((f), RTLD_NOW | RTLD_GLOBAL)
53 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/darwin.h

```cpp

{% raw %}
4 | void	   *pg_dlopen(char *filename);
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
26 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
37 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
48 | #define		   pg_dlopen(f)    BSD44_derived_dlopen((f), RTLD_NOW | RTLD_GLOBAL)
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/openbsd.h

```cpp

{% raw %}
25 |  * libraries (ie. dlopen/dlsym/dlclose). The user must specify a shared
36 |  * argument to dlopen must always be 1.  The RTLD_GLOBAL flag is wanted
47 | #define		   pg_dlopen(f)    BSD44_derived_dlopen((f), RTLD_NOW | RTLD_GLOBAL)
53 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/linux.c

```cpp

{% raw %}
28 | #ifndef HAVE_DLOPEN
31 | pg_dlopen(char *filename)
41 | 	 * needs to do this the first time pg_dlopen is called.)
132 | #endif							/* !HAVE_DLOPEN */
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
137 | #endif							/* HAVE_DLOPEN */
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
41 | #endif							/* HAVE_DLOPEN */
{% endraw %}

```
### src/backend/utils/fmgr/dfmgr.c

```cpp

{% raw %}
230 | 		file_scanner->handle = pg_dlopen(file_scanner->filename);
{% endraw %}

```
### src/port/gettimeofday.c

```cpp

{% raw %}
66 | 	 * closing it afterwards, so we're not using Pg's dlopen/dlsym() wrapper.
{% endraw %}

```
### doc/src/sgml/release-9.0.sgml

```

{% raw %}
6869 |       Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/release-8.4.sgml

```

{% raw %}
4069 |       Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/release-8.2.sgml

```

{% raw %}
633 |       Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/release-8.3.sgml

```

{% raw %}
2064 |       Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/html/release-8-4-8.html

```html

{% raw %}
68 |      </p></li><li class="listitem"><p>      Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/html/release-9-0-4.html

```html

{% raw %}
98 |      </p></li><li class="listitem"><p>      Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/html/release-8-2-21.html

```html

{% raw %}
31 |      </p></li><li class="listitem"><p>      Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```
### doc/src/sgml/html/release-8-3-15.html

```html

{% raw %}
36 |      </p></li><li class="listitem"><p>      Support use of dlopen() in FreeBSD and OpenBSD on MIPS (Tom Lane)
{% endraw %}

```