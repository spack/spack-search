---
name: "nspr"
layout: package
next_package: numamma
previous_package: nix
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.13.1
7 / 635 files match, 7 filtered matches.

 - [nspr/pr/src/linking/prlink.c](#nsprprsrclinkingprlinkc)
 - [nspr/pr/src/malloc/prmem.c](#nsprprsrcmallocprmemc)
 - [nspr/pr/src/pthreads/ptthread.c](#nsprprsrcpthreadsptthreadc)
 - [nspr/pr/src/pthreads/ptio.c](#nsprprsrcpthreadsptioc)
 - [nspr/pr/src/md/unix/aix.c](#nsprprsrcmdunixaixc)
 - [nspr/pr/src/md/unix/irix.c](#nsprprsrcmdunixirixc)
 - [nspr/pr/src/md/unix/uxproces.c](#nsprprsrcmdunixuxprocesc)

### nspr/pr/src/linking/prlink.c

```c

{% raw %}
1157 | #ifdef XP_UNIX
1158 | #ifdef HAVE_DLL
1159 | #ifdef USE_DLFCN
1160 |     f = dlsym(lm->dlh, name);
1161 | #elif defined(USE_HPSHL)
1162 |     if (shl_findsym(&lm->dlh, name, TYPE_PROCEDURE, &f) == -1) {
{% endraw %}

```
### nspr/pr/src/malloc/prmem.c

```c

{% raw %}
97 |     h = dlopen(0, RTLD_LAZY);
98 |     if (h == NULL)
99 |         return NULL;
100 |     sym = dlsym(h, name);
101 |     (void)dlclose(h);
102 |     return sym;
{% endraw %}

```
### nspr/pr/src/pthreads/ptthread.c

```c

{% raw %}
1770 | #endif
1771 | 
1772 |     *(void**)(&dynamic_pthread_setname_np) =
1773 |         dlsym(RTLD_DEFAULT, "pthread_setname_np");
1774 |     if (!dynamic_pthread_setname_np)
1775 |         return PR_SUCCESS;
{% endraw %}

```
### nspr/pr/src/pthreads/ptio.c

```c

{% raw %}
2104 | static void pt_aix_sendfile_init_routine(void)
2105 | {
2106 |     void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
2107 |     pt_aix_sendfile_fptr = (ssize_t (*)()) dlsym(handle, "send_file");
2108 |     dlclose(handle);
2109 | }
2508 |             ("dlopen(0) returns %p", handle));
2509 |         close_it = PR_TRUE;
2510 |     }
2511 |     pt_solaris_sendfilev_fptr = (ssize_t (*)()) dlsym(handle, "sendfilev");
2512 |     PR_LOG(_pr_io_lm, PR_LOG_DEBUG,
2513 |         ("dlsym(sendfilev) returns %p", pt_solaris_sendfilev_fptr));
2514 |     
2515 |     if (close_it) {
{% endraw %}

```
### nspr/pr/src/md/unix/aix.c

```c

{% raw %}
77 |     main_app_handle = dlopen(NULL, RTLD_NOW);
78 |     PR_ASSERT(NULL != main_app_handle);
79 | 
80 |     _PT_aix_yield_fcn = (int(*)())dlsym(main_app_handle, "sched_yield");
81 |     if (!_PT_aix_yield_fcn) {
82 |         _PT_aix_yield_fcn = (int(*)())dlsym(main_app_handle,"pthread_yield");
83 |         PR_ASSERT(NULL != _PT_aix_yield_fcn);
84 |     }
197 | 	    PR_SetError(PR_UNKNOWN_ERROR, 0);
198 | 	    return -1;
199 | 	}
200 | 	aix_select_fcn = (int(*)())dlsym(aix_handle,"select");
201 |         dlclose(aix_handle);
202 | 	if (!aix_select_fcn) {
220 | 	    PR_SetError(PR_UNKNOWN_ERROR, 0);
221 | 	    return -1;
222 | 	}
223 | 	aix_poll_fcn = (int(*)())dlsym(aix_handle,"poll");
224 |         dlclose(aix_handle);
225 | 	if (!aix_poll_fcn) {
{% endraw %}

```
### nspr/pr/src/md/unix/irix.c

```c

{% raw %}
996 | 			if (!libc_handle)
997 | 				libc_handle = dlopen("libc.so",RTLD_NOW);
998 | 			if (libc_handle)
999 | 				libc_exit = (void (*)(int)) dlsym(libc_handle, "exit");
1000 | 		}
1001 | 		if (libc_exit)
1505 | 
1506 | 	libc_handle = dlopen("libc.so",RTLD_NOW);
1507 | 	PR_ASSERT(libc_handle != NULL);
1508 | 	libc_exit = (void (*)(int)) dlsym(libc_handle, "exit");
1509 | 	PR_ASSERT(libc_exit != NULL);
1510 | 	/* dlclose(libc_handle); */
{% endraw %}

```
### nspr/pr/src/md/unix/uxproces.c

```c

{% raw %}
714 | #ifdef AIX
715 |     {
716 |         void *handle = dlopen(NULL, RTLD_NOW | RTLD_GLOBAL);
717 |         pr_wp.forkptr = (pid_t (*)(void)) dlsym(handle, "f_fork");
718 |         if (!pr_wp.forkptr) {
719 |             pr_wp.forkptr = fork;
{% endraw %}

```