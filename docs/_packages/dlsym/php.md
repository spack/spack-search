---
name: "php"
layout: package
next_package: scorep
previous_package: go
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.3.13
10 / 19786 files match, 6 filtered matches.

 - [ext/pdo_firebird/firebird_driver.c](#extpdo_firebirdfirebird_driverc)
 - [ext/sqlite3/libsqlite/sqlite3.c](#extsqlite3libsqlitesqlite3c)
 - [ext/readline/readline_cli.c](#extreadlinereadline_clic)
 - [ext/interbase/interbase.c](#extinterbaseinterbasec)
 - [sapi/litespeed/lsapilib.c](#sapilitespeedlsapilibc)
 - [sapi/litespeed/lscriu.c](#sapilitespeedlscriuc)

### ext/pdo_firebird/firebird_driver.c

```c

{% raw %}
531 | #if defined(__GNUC__) || defined(PHP_WIN32)
532 | 			info_func_t info_func = NULL;
533 | #ifdef __GNUC__
534 | 			info_func = (info_func_t)dlsym(RTLD_DEFAULT, "isc_get_client_version");
535 | #else
536 | 			HMODULE l = GetModuleHandle("fbclient");
{% endraw %}

```
### ext/sqlite3/libsqlite/sqlite3.c

```c

{% raw %}
38914 |   */
38915 |   void (*(*x)(void*,const char*))(void);
38916 |   UNUSED_PARAMETER(NotUsed);
38917 |   x = (void(*(*)(void*,const char*))(void))dlsym;
38918 |   return (*x)(p, zSym);
38919 | }
{% endraw %}

```
### ext/readline/readline_cli.c

```c

{% raw %}
727 | #else
728 | /*
729 | #ifdef COMPILE_DL_READLINE
730 | This dlsym() is always used as even the CGI SAPI is linked against "CLI"-only
731 | extensions. If that is being changed dlsym() should only be used when building
732 | this extension sharedto offer compatibility.
733 | */
735 | 	do { \
736 | 		(cb) = NULL; \
737 | 		cli_shell_callbacks_t *(*get_callbacks)(); \
738 | 		get_callbacks = dlsym(RTLD_DEFAULT, "php_cli_get_shell_callbacks"); \
739 | 		if (get_callbacks) { \
740 | 			(cb) = get_callbacks(); \
{% endraw %}

```
### ext/interbase/interbase.c

```c

{% raw %}
819 | 	do {
820 | 		info_func_t info_func = NULL;
821 | #ifdef __GNUC__
822 | 		info_func = (info_func_t)dlsym(RTLD_DEFAULT, "isc_get_client_version");
823 | #else
824 | 		HMODULE l = GetModuleHandle("fbclient");
{% endraw %}

```
### sapi/litespeed/lsapilib.c

```c

{% raw %}
781 |     s_liblve = dlopen("liblve.so.0", RTLD_LAZY);
782 |     if (s_liblve)
783 |     {
784 |         fp_lve_is_available = dlsym(s_liblve, "lve_is_available");
785 |         if (dlerror() == NULL)
786 |         {
810 |     int rc;
811 |     if ( !s_liblve )
812 |         return -1;
813 |     fp_lve_instance_init = dlsym(s_liblve, "lve_instance_init");
814 |     fp_lve_destroy = dlsym(s_liblve, "lve_destroy");
815 |     fp_lve_enter = dlsym(s_liblve, "lve_enter");
816 |     fp_lve_leave = dlsym(s_liblve, "lve_leave");
817 |     if ( s_enable_lve >= LSAPI_CAGEFS_ENABLED )
818 |         fp_lve_jail = dlsym(s_liblve, "jail" );
819 | 
820 |     if ( s_lve == NULL )
1463 |         s_ppid = getppid();
1464 |         void *pthread_lib = dlopen("libpthread.so", RTLD_LAZY);
1465 |         if (pthread_lib)
1466 |             pthread_atfork_func = dlsym(pthread_lib, "pthread_atfork");
1467 | 
1468 |     }
{% endraw %}

```
### sapi/litespeed/lscriu.c

```c

{% raw %}
268 |         !(pthread_lib_handle = dlopen(last = "libpthread.so", RTLD_LAZY))*/)
269 |         fprintf(stderr, "LSCRIU (%d): failed to dlopen %s: %s - ignore CRIU\n",
270 |                 s_pid, last, dlerror());
271 |     else if (!(s_lscapi_dump_me = dlsym(lib_handle, last = "lscapi_dump_me")) ||
272 |                 !(s_lscapi_prepare_me = dlsym(lib_handle, last = "lscapi_prepare_me")) ||
273 |                 !(psem_open = dlsym(pthread_lib_handle, last = "sem_open")) ||
274 |                 !(psem_post = dlsym(pthread_lib_handle, last = "sem_post")) ||
275 |                 !(psem_close = dlsym(pthread_lib_handle, last = "sem_close")))
276 |         fprintf(stderr, "LSCRIU (%d): failed to dlsym %s: %s - ignore CRIU\n",
277 |                 s_pid, last, dlerror());
278 |     else
{% endraw %}

```