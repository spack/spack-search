---
name: "dmtcp"
layout: package
next_package: dotconf
previous_package: dimemas
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.5.2
37 / 648 files match, 10 filtered matches.

 - [src/syscallsreal.c](#srcsyscallsrealc)
 - [src/syscallwrappers.h](#srcsyscallwrappersh)
 - [src/plugin/pid/pidwrappers.h](#srcpluginpidpidwrappersh)
 - [src/plugin/pid/pid_syscallsreal.c](#srcpluginpidpid_syscallsrealc)
 - [include/dmtcp.h](#includedmtcph)
 - [include/trampolines.h](#includetrampolinesh)
 - [include/dmtcp_dlsym.h](#includedmtcp_dlsymh)
 - [include/shareddata.h](#includeshareddatah)
 - [test/plugin/sleep2/sleep2.c](#testpluginsleep2sleep2c)
 - [contrib/infiniband/infinibandtrace.c](#contribinfinibandinfinibandtracec)

### src/syscallsreal.c

```c

{% raw %}
226 | static int dmtcp_wrappers_initialized = 0;
227 | 
228 | #define GET_FUNC_ADDR(name) \
229 |   _real_func_addr[ENUM(name)] = dmtcp_dlsym(RTLD_NEXT, #name);
230 | 
231 | static void initialize_libc_wrappers()
321 |   REAL_FUNC_PASSTHROUGH_WORK(name)                           \
322 |   (*fn)
323 | 
324 | typedef void* (*dlsym_fnptr_t) (void *handle, const char *symbol);
325 | void *dmtcp_get_libc_dlsym_addr(void);
326 | 
327 | LIB_PRIVATE
328 | void *_real_dlsym (void *handle, const char *symbol) {
329 |   static dlsym_fnptr_t _libc_dlsym_fnptr = NULL;
330 |   if (_libc_dlsym_fnptr == NULL) {
331 |     _libc_dlsym_fnptr = dmtcp_dlsym;
332 |   }
333 | 
338 |   // called and so we do not need to disable locking for calloc.
339 |   dmtcp_setThreadPerformingDlopenDlsym();
340 | #endif
341 |   void *res = (*_libc_dlsym_fnptr) (handle, symbol);
342 | #if TRACK_DLOPEN_DLSYM_FOR_LOCKS
343 |   dmtcp_unsetThreadPerformingDlopenDlsym();
{% endraw %}

```
### src/syscallwrappers.h

```c

{% raw %}
104 | 
105 | extern int dmtcp_wrappers_initializing;
106 | 
107 | LIB_PRIVATE extern __thread int thread_performing_dlopen_dlsym;
108 | 
109 | #define FOREACH_GLIBC_MALLOC_FAMILY_WRAPPERS(MACRO)\
406 |   int _real_lxstat(int vers, const char *path, struct stat *buf);
407 |   int _real_lxstat64(int vers, const char *path, struct stat64 *buf);
408 |   ssize_t _real_readlink(const char *path, char *buf, size_t bufsiz);
409 |   void * _real_dlsym (void *handle, const char *symbol);
410 | 
411 |   void *_real_dlopen(const char *filename, int flag);
{% endraw %}

```
### src/plugin/pid/pidwrappers.h

```c

{% raw %}
101 |   void dmtcpResetPidPpid();
102 |   void dmtcpResetTid(pid_t tid);
103 | 
104 |   LIB_PRIVATE void *_real_dlsym(void *handle, const char *symbol);
105 | 
106 | /* The following function are defined in pidwrappers.cpp */
{% endraw %}

```
### src/plugin/pid/pid_syscallsreal.c

```c

{% raw %}
37 | typedef int ( *funcptr_t ) ();
38 | typedef pid_t ( *funcptr_pid_t ) ();
39 | typedef funcptr_t ( *signal_funcptr_t ) ();
40 | typedef void* (*dlsym_fnptr_t) (void *handle, const char *symbol);
41 | 
42 | static void *pid_real_func_addr[numPidVirtWrappers];
43 | static int pid_wrappers_initialized = 0;
44 | 
45 | #define GET_FUNC_ADDR(name) \
46 |   pid_real_func_addr[PIDVIRT_ENUM(name)] = _real_dlsym(RTLD_NEXT, #name);
47 | 
48 | #define GET_FUNC_ADDR_V(name, v) \
113 |   REAL_FUNC_PASSTHROUGH_WORK(name)                           \
114 |   (*fn)
115 | 
116 | void *dmtcp_get_libc_dlsym_addr();
117 | 
118 | LIB_PRIVATE
119 | void *_real_dlsym ( void *handle, const char *symbol ) {
120 |   static dlsym_fnptr_t _libc_dlsym_fnptr = NULL;
121 |   if (_libc_dlsym_fnptr == NULL) {
122 |     _libc_dlsym_fnptr = (dlsym_fnptr_t) dmtcp_dlsym;
123 |   }
124 | 
125 |   return (void*) (*_libc_dlsym_fnptr) ( handle, symbol );
126 | }
127 | 
{% endraw %}

```
### include/dmtcp.h

```c

{% raw %}
315 | EXTERNC void dmtcp_unblock_ckpt_signal(void);
316 | 
317 | // FOR EXPERTS ONLY:
318 | EXTERNC void *dmtcp_get_libc_dlsym_addr(void);
319 | EXTERNC void dmtcp_close_protected_fd(int fd);
320 | EXTERNC int dmtcp_protected_environ_fd(void);
370 |      static __typeof__(&func) _real_##func = (__typeof__(&func)) -1;        \
371 |      if (_real_##func == (__typeof__(&func)) -1) {                          \
372 |        if (dmtcp_initialize) dmtcp_initialize();                            \
373 |        __typeof__(&dlsym) dlsym_fnptr;                                      \
374 |        dlsym_fnptr = (__typeof__(&dlsym)) dmtcp_get_libc_dlsym_addr();      \
375 |        _real_##func = (__typeof__(&func)) (*dlsym_fnptr) (RTLD_NEXT, #func);\
376 |      }                                                                      \
377 |    _real_##func;})
422 |      DECLARE_TYPEOF_FNC(func,_real_##func);                                 \
423 |      if (_real_##func == (__typeof__(&func)) -1) {                          \
424 |        if (dmtcp_prepare_wrappers) dmtcp_prepare_wrappers();                \
425 |        __typeof__(&dlsym) dlsym_fnptr;                                      \
426 |        dlsym_fnptr = (__typeof__(&dlsym)) dmtcp_get_libc_dlsym_addr();      \
427 |        _real_##func = (__typeof__(&func)) (*dlsym_fnptr) (RTLD_NEXT, #func);\
428 |      }                                                                      \
429 |    _real_##func;})
{% endraw %}

```
### include/trampolines.h

```c

{% raw %}
115 |             __FILE__, __LINE__);
116 |     abort();
117 |   }
118 |   void *addr = dlsym(handle, func_name);
119 |   if (addr == NULL) {
120 |     fprintf(stderr, "*** %s:%d DMTCP Internal Error: dlsym() failed.\n",
121 |             __FILE__, __LINE__);
122 |     abort();
{% endraw %}

```
### include/dmtcp_dlsym.h

```c

{% raw %}
34 | # undef __USE_GNU
35 | #endif
36 | 
37 | EXTERNC void *dmtcp_dlsym(void *handle, const char *symbol);
38 | EXTERNC void *dmtcp_dlvsym(void *handle, char *symbol, const char *version);
39 | EXTERNC void *dmtcp_dlsym_lib(const char *libname, const char *symbol);
40 | /*
41 |  * Returns the offset of the given function within the given shared library
42 |  * or -1 if the function does not exist in the library
43 |  */
44 | EXTERNC ptrdiff_t dmtcp_dlsym_lib_fnc_offset(const char *libname,
45 |                                              const char *symbol);
46 | 
52 |      static __typeof__(&func) _real_##func = (__typeof__(&func)) -1;        \
53 |      if (_real_##func == (__typeof__(&func)) -1) {                          \
54 |        if (dmtcp_initialize) dmtcp_initialize();                            \
55 |        _real_##func = (__typeof__(&func)) dmtcp_dlsym(RTLD_NEXT, #func);    \
56 |      }                                                                      \
57 |    _real_##func;})
65 |      static __typeof__(&func) _real_##func = (__typeof__(&func)) -1;           \
66 |      if (_real_##func == (__typeof__(&func)) -1) {                             \
67 |        if (dmtcp_initialize) dmtcp_initialize();                               \
68 |        _real_##func = (__typeof__(&func)) dmtcp_dlsym(RTLD_NEXT, #func, ver);  \
69 |      }                                                                         \
70 |    _real_##func;})
83 |       if (dmtcp_initialize) {                                                  \
84 |         dmtcp_initialize();                                                    \
85 |       }                                                                        \
86 |       _real_##func = (__typeof__(&func)) dmtcp_dlsym_lib(lib,  #func);         \
87 |     }                                                                          \
88 |     _real_##func;                                                              \
98 |   printf("pthread_cond_broadcast (via normal linker): %p\n",
99 |          pthread_cond_broadcast);
100 | 
101 |   printf("================ dlsym ================\n");
102 |   fnc = dlsym(RTLD_DEFAULT, "pthread_cond_broadcast");
103 |   printf("pthread_cond_broadcast (via RTLD_DEFAULT): %p\n", fnc);
104 |   fnc = dlsym(RTLD_NEXT, "pthread_cond_broadcast");
105 |   printf("pthread_cond_broadcast (via RTLD_NEXT): %p\n", fnc);
106 | 
107 |   printf("================ dmtcp_dlsym ================\n");
108 |   // NOTE: RTLD_DEFAULT would try to use this a.out, and fail to find a library
109 |   // fnc = dmtcp_dlsym(RTLD_DEFAULT, "pthread_cond_broadcast");
110 |   // printf("pthread_cond_broadcast (via RTLD_DEFAULT): %p\n", fnc);
111 |   fnc = dmtcp_dlsym(RTLD_NEXT, "pthread_cond_broadcast");
112 |   printf("pthread_cond_broadcast (via RTLD_NEXT): %p\n", fnc);
113 | 
{% endraw %}

```
### include/shareddata.h

```c

{% raw %}
98 |       uint32_t             initialized;
99 |       struct in_addr       localIPAddr;
100 | 
101 |       int32_t              dlsymOffset;
102 |       int32_t              dlsymOffset_m32;
103 | 
104 |       uint32_t             numPidMaps;
168 | 
169 |     void getLocalIPAddr(struct in_addr *in);
170 | 
171 |     void updateDlsymOffset(int32_t dlsymOffset, int32_t dlsymOffset_m32 = 0);
172 |     int32_t getDlsymOffset(void);
173 |     int32_t getDlsymOffset_m32(void);
{% endraw %}

```
### test/plugin/sleep2/sleep2.c

```c

{% raw %}
23 |   if (! handle)
24 |     handle = dlopen("libc.so.6", RTLD_NOW);
25 |   if (! real_fnc)
26 |     real_fnc = (__typeof__(real_fnc)) dlsym(handle, "sleep");
27 |   return (*real_fnc)(seconds);
28 | }
{% endraw %}

```
### contrib/infiniband/infinibandtrace.c

```c

{% raw %}
17 | 
18 | /* This macro requires a static local declaration of "next_fnc". */
19 | #define NEXT_FNC(symbol) \
20 |     (next_fnc ? *next_fnc : *(next_fnc = dlsym(RTLD_NEXT, #symbol)))
21 | 
22 | 
{% endraw %}

```