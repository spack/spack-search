---
name: "php"
layout: package
next_package: cpuinfo
previous_package: numamma
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.3.13
9 / 19786 files match, 3 filtered matches.

 - [ext/sqlite3/libsqlite/sqlite3.c](#extsqlite3libsqlitesqlite3c)
 - [sapi/litespeed/lsapilib.c](#sapilitespeedlsapilibc)
 - [sapi/litespeed/lscriu.c](#sapilitespeedlscriuc)

### ext/sqlite3/libsqlite/sqlite3.c

```c

{% raw %}
38874 | #include <dlfcn.h>
38875 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38876 |   UNUSED_PARAMETER(NotUsed);
38877 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38878 | }
38879 | 
{% endraw %}

```
### sapi/litespeed/lsapilib.c

```c

{% raw %}
778 | static int (*fp_lve_jail)( struct passwd *, char *) = NULL;
779 | static int lsapi_load_lve_lib(void)
780 | {
781 |     s_liblve = dlopen("liblve.so.0", RTLD_LAZY);
782 |     if (s_liblve)
783 |     {
1461 |             return -1;
1462 |         g_inited = 1;
1463 |         s_ppid = getppid();
1464 |         void *pthread_lib = dlopen("libpthread.so", RTLD_LAZY);
1465 |         if (pthread_lib)
1466 |             pthread_atfork_func = dlsym(pthread_lib, "pthread_atfork");
{% endraw %}

```
### sapi/litespeed/lscriu.c

```c

{% raw %}
264 |     int error = 1;
265 |     char *last;
266 | 
267 |     if (!(lib_handle = dlopen(last = "liblscapi.so", RTLD_LAZY)) /*||
268 |         !(pthread_lib_handle = dlopen(last = "libpthread.so", RTLD_LAZY))*/)
269 |         fprintf(stderr, "LSCRIU (%d): failed to dlopen %s: %s - ignore CRIU\n",
270 |                 s_pid, last, dlerror());
271 |     else if (!(s_lscapi_dump_me = dlsym(lib_handle, last = "lscapi_dump_me")) ||
{% endraw %}

```