---
name: "gpdb"
layout: package
next_package: rr
previous_package: geoip-api-c
languages: ['c']
---
## 6.1.0
28 / 8154 files match, 17 filtered matches.

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
 - [src/backend/port/dynloader/nextstep.c](#srcbackendportdynloadernextstepc)
 - [src/backend/port/dynloader/openbsd.c](#srcbackendportdynloaderopenbsdc)
 - [src/backend/port/dynloader/darwin.c](#srcbackendportdynloaderdarwinc)
 - [src/backend/port/dynloader/hpux.c](#srcbackendportdynloaderhpuxc)
 - [src/backend/utils/fmgr/dfmgr.c](#srcbackendutilsfmgrdfmgrc)
 - [contrib/pg_upgrade/page.c](#contribpg_upgradepagec)

### src/include/utils/dynamic_loader.h

```c

{% raw %}
19 | extern void *pg_dlopen(char *filename);
{% endraw %}

```
### src/backend/port/dynloader/win32.h

```c

{% raw %}
16 | void	   *dlopen(const char *path, int mode);
{% endraw %}

```
### src/backend/port/dynloader/freebsd.h

```c

{% raw %}
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/darwin.h

```c

{% raw %}
4 | void	   *pg_dlopen(char *filename);
{% endraw %}

```
### src/backend/port/dynloader/win32.c

```c

{% raw %}
7 | void	   *dlopen(const char *path, int mode);
67 | dlopen(const char *path, int mode)
{% endraw %}

```
### src/backend/port/dynloader/hpux.h

```c

{% raw %}
21 | extern void *pg_dlopen(char *filename);
{% endraw %}

```
### src/backend/port/dynloader/netbsd.c

```c

{% raw %}
57 | BSD44_derived_dlopen(const char *file, int num)
61 | 			 "dlopen (%s) not supported", file);
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
{% endraw %}

```
### src/backend/port/dynloader/netbsd.h

```c

{% raw %}
55 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/openbsd.h

```c

{% raw %}
54 | void	   *BSD44_derived_dlopen(const char *filename, int num);
{% endraw %}

```
### src/backend/port/dynloader/linux.c

```c

{% raw %}
31 | pg_dlopen(char *filename)
{% endraw %}

```
### src/backend/port/dynloader/freebsd.c

```c

{% raw %}
57 | BSD44_derived_dlopen(const char *file, int num)
61 | 			 "dlopen (%s) not supported", file);
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
{% endraw %}

```
### src/backend/port/dynloader/nextstep.c

```c

{% raw %}
41 | next_dlopen(char *name)
{% endraw %}

```
### src/backend/port/dynloader/openbsd.c

```c

{% raw %}
57 | BSD44_derived_dlopen(const char *file, int num)
61 | 			 "dlopen (%s) not supported", file);
66 | 	if ((vp = dlopen((char *) file, num)) == NULL)
68 | 				 "dlopen (%s) failed: %s", file, dlerror());
{% endraw %}

```
### src/backend/port/dynloader/darwin.c

```c

{% raw %}
22 | pg_dlopen(char *filename)
24 | 	return dlopen(filename, RTLD_NOW | RTLD_GLOBAL);
56 | pg_dlopen(char *filename)
{% endraw %}

```
### src/backend/port/dynloader/hpux.c

```c

{% raw %}
28 | pg_dlopen(char *filename)
{% endraw %}

```
### src/backend/utils/fmgr/dfmgr.c

```c

{% raw %}
230 | 		file_scanner->handle = pg_dlopen(file_scanner->filename);
{% endraw %}

```
### contrib/pg_upgrade/page.c

```c

{% raw %}
137 | 	if ((plugin = pg_dlopen(pluginName)) == NULL)
{% endraw %}

```