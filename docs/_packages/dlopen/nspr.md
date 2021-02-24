---
name: "nspr"
layout: package
next_package: cntk
previous_package: podio
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.13.1
7 / 635 files match, 6 filtered matches.

 - [nspr/pr/src/linking/prlink.c](#nsprprsrclinkingprlinkc)
 - [nspr/pr/src/malloc/prmem.c](#nsprprsrcmallocprmemc)
 - [nspr/pr/src/pthreads/ptio.c](#nsprprsrcpthreadsptioc)
 - [nspr/pr/src/md/unix/aix.c](#nsprprsrcmdunixaixc)
 - [nspr/pr/src/md/unix/irix.c](#nsprprsrcmdunixirixc)
 - [nspr/pr/src/md/unix/uxproces.c](#nsprprsrcmdunixuxprocesc)

### nspr/pr/src/linking/prlink.c

```c

{% raw %}
165 | #elif defined(XP_UNIX)
166 | #ifdef HAVE_DLL
167 | #if defined(USE_DLFCN) && !defined(NO_DLOPEN_NULL)
168 |     h = dlopen(0, RTLD_LAZY);
169 |     if (!h) {
170 |         char *error;
796 |     /* plain filename in DYLD_LIBRARY_PATH */
797 |     if (strchr(name, PR_DIRECTORY_SEPARATOR) == NULL ||
798 |         PR_Access(name, PR_ACCESS_EXISTS) == PR_SUCCESS) {
799 |             h = dlopen(name, dl_flags);
800 |         }
801 | #else
802 |     h = dlopen(name, dl_flags);
803 | #endif
804 | #elif defined(USE_HPSHL)
{% endraw %}

```
### nspr/pr/src/malloc/prmem.c

```c

{% raw %}
94 |     void *h;
95 |     void *sym;
96 | 
97 |     h = dlopen(0, RTLD_LAZY);
98 |     if (h == NULL)
99 |         return NULL;
{% endraw %}

```
### nspr/pr/src/pthreads/ptio.c

```c

{% raw %}
2103 | 
2104 | static void pt_aix_sendfile_init_routine(void)
2105 | {
2106 |     void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
2107 |     pt_aix_sendfile_fptr = (ssize_t (*)()) dlsym(handle, "send_file");
2108 |     dlclose(handle);
2493 |      * We do not want to unload libsendfile.so.  This handle is leaked
2494 |      * intentionally.
2495 |      */
2496 |     handle = dlopen("libsendfile.so", RTLD_LAZY | RTLD_GLOBAL);
2497 |     PR_LOG(_pr_io_lm, PR_LOG_DEBUG,
2498 |         ("dlopen(libsendfile.so) returns %p", handle));
2499 | 
2500 |     if (NULL == handle) {
2503 |          * sendfilev() may become part of a standard system library in a
2504 |          * future Solaris release.
2505 |          */
2506 |         handle = dlopen(0, RTLD_LAZY | RTLD_GLOBAL);
2507 |         PR_LOG(_pr_io_lm, PR_LOG_DEBUG,
2508 |             ("dlopen(0) returns %p", handle));
2509 |         close_it = PR_TRUE;
2510 |     }
{% endraw %}

```
### nspr/pr/src/md/unix/aix.c

```c

{% raw %}
74 |     void *main_app_handle;
75 | 	char *evp;
76 | 
77 |     main_app_handle = dlopen(NULL, RTLD_NOW);
78 |     PR_ASSERT(NULL != main_app_handle);
79 | 
192 |     if (!aix_select_fcn) {
193 |         void *aix_handle;
194 | 
195 | 	aix_handle = dlopen("/unix", RTLD_NOW);
196 | 	if (!aix_handle) {
197 | 	    PR_SetError(PR_UNKNOWN_ERROR, 0);
215 |     if (!aix_poll_fcn) {
216 |         void *aix_handle;
217 | 
218 | 	aix_handle = dlopen("/unix", RTLD_NOW);
219 | 	if (!aix_handle) {
220 | 	    PR_SetError(PR_UNKNOWN_ERROR, 0);
{% endraw %}

```
### nspr/pr/src/md/unix/irix.c

```c

{% raw %}
994 | 		if (!libc_exit) {
995 | 
996 | 			if (!libc_handle)
997 | 				libc_handle = dlopen("libc.so",RTLD_NOW);
998 | 			if (libc_handle)
999 | 				libc_exit = (void (*)(int)) dlsym(libc_handle, "exit");
1503 |     FD_SET(_pr_irix_primoridal_cpu_fd[0], &_PR_FD_READ_SET(me->cpu));
1504 | #endif
1505 | 
1506 | 	libc_handle = dlopen("libc.so",RTLD_NOW);
1507 | 	PR_ASSERT(libc_handle != NULL);
1508 | 	libc_exit = (void (*)(int)) dlsym(libc_handle, "exit");
{% endraw %}

```
### nspr/pr/src/md/unix/uxproces.c

```c

{% raw %}
713 | 
714 | #ifdef AIX
715 |     {
716 |         void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
717 |         pr_wp.forkptr = (pid_t (*)(void)) dlsym(handle, "f_fork");
718 |         if (!pr_wp.forkptr) {
{% endraw %}

```