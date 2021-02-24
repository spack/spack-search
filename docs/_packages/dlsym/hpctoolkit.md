---
name: "hpctoolkit"
layout: package
next_package: hwloc
previous_package: grpc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2020.08.03
20 / 1254 files match, 13 filtered matches.

 - [src/tool/hpcrun/custom-init-dynamic.c](#srctoolhpcruncustom-init-dynamicc)
 - [src/tool/hpcrun/main.c](#srctoolhpcrunmainc)
 - [src/tool/hpcrun/monitor-exts/monitor_ext.h](#srctoolhpcrunmonitor-extsmonitor_exth)
 - [src/tool/hpcrun/lush/lush.c](#srctoolhpcrunlushlushc)
 - [src/tool/hpcrun/sample-sources/papi-c-cupti.c](#srctoolhpcrunsample-sourcespapi-c-cuptic)
 - [src/tool/hpcrun/sample-sources/gpu_blame.c](#srctoolhpcrunsample-sourcesgpu_blamec)
 - [src/tool/hpcrun/sample-sources/pthread-blame-overrides.c](#srctoolhpcrunsample-sourcespthread-blame-overridesc)
 - [src/tool/hpcrun/sample-sources/libdl.h](#srctoolhpcrunsample-sourceslibdlh)
 - [src/tool/hpcrun/sample-sources/gpu_blame-overrides.c](#srctoolhpcrunsample-sourcesgpu_blame-overridesc)
 - [src/tool/hpcrun/syscalls/ppoll.c](#srctoolhpcrunsyscallsppollc)
 - [src/tool/hpcrun/syscalls/select.c](#srctoolhpcrunsyscallsselectc)
 - [src/tool/hpcrun/syscalls/poll.c](#srctoolhpcrunsyscallspollc)
 - [src/tool/hpcrun-flat/dlpapi.c](#srctoolhpcrun-flatdlpapic)

### src/tool/hpcrun/custom-init-dynamic.c

```c

{% raw %}
83 |   if (ENABLED(CUSTOM_INIT)) {
84 |     void* custom_fns = monitor_real_dlopen("./hpcrun-custom.so", RTLD_LAZY);
85 |     if (custom_fns) {
86 |       void (*hpcrun_custom_init)(void) = (void (*)(void)) dlsym(custom_fns, "hpcrun_custom_init");
87 |       if (hpcrun_custom_init) {
88 | 	TMSG(CUSTOM_INIT, "Before call to custom_init");
{% endraw %}

```
### src/tool/hpcrun/main.c

```c

{% raw %}
311 |   // passed into libc_start_main as real_main. this might be a
312 |   // trampoline in the PLT.
313 |   dlerror();
314 |   main_addr_dl = dlsym(RTLD_NEXT,"main");
315 |   if (main_addr_dl) {
316 |     fnbounds_enclosing_addr(main_addr_dl, &main_lower_dl, &main_upper_dl, &lm);
{% endraw %}

```
### src/tool/hpcrun/monitor-exts/monitor_ext.h

```c

{% raw %}
79 |     if (var == NULL) {					\
80 | 	const char *err_str;				\
81 | 	dlerror();					\
82 | 	var = dlsym(RTLD_NEXT, #name );			\
83 | 	err_str = dlerror();				\
84 | 	if (var == NULL) {				\
85 | 	    hpcrun_abort("dlsym(%s) failed: %s", #name , err_str); \
86 | 	}						\
87 | 	TMSG(MONITOR_EXTS, "%s() = %p", #name , var);	\
{% endraw %}

```
### src/tool/hpcrun/lush/lush.c

```c

{% raw %}
106 |   handle_any_dlerror();
107 | 
108 | #define CALL_DLSYM(BASE, X, ID, HANDLE)	       \
109 |   BASE->X[ID] = (X ## _fn_t)dlsym(HANDLE, #X); \
110 |   handle_any_dlerror()
111 |   
{% endraw %}

```
### src/tool/hpcrun/sample-sources/papi-c-cupti.c

```c

{% raw %}
67 | 
68 | #define Chk_dlsym(h, fn) {                                \
69 |   dlerror();                                              \
70 |   d ## fn = dlsym(h, #fn);                                \
71 |   char* e = dlerror();                                    \
72 |   if (e) {                                                \
73 |     fprintf(stderr, "dlsym(%s) fails w '%s'\n", #fn, e);  \
74 |     return;                                               \
75 |   }                                                       \
127 |   // only use dlfunctions in NON static case
128 | #ifndef HPCRUN_STATIC_LINK
129 |   Chk_dlopen(cudart, "libcudart.so", RTLD_NOW | RTLD_GLOBAL);
130 |   Chk_dlsym(cudart, cudaThreadSynchronize);
131 | 
132 |   Chk_dlopen(cupti, "libcupti.so", RTLD_NOW | RTLD_GLOBAL);
133 |   Chk_dlsym(cupti, cuptiGetResultString);
134 |   Chk_dlsym(cupti, cuptiSubscribe);
135 |   Chk_dlsym(cupti, cuptiEnableCallback);
136 |   Chk_dlsym(cupti, cuptiUnsubscribe);
137 | #endif // ! HPCRUN_STATIC_LINK
138 | }
{% endraw %}

```
### src/tool/hpcrun/sample-sources/gpu_blame.c

```c

{% raw %}
231 | 
232 |     hpcrun_close_kind(blame_kind);
233 |     
234 |     bs_entry.fn = dlsym(RTLD_DEFAULT, "gpu_blame_shifter");
235 |     bs_entry.next = 0;
236 |     blame_shift_register(&bs_entry);
{% endraw %}

```
### src/tool/hpcrun/sample-sources/pthread-blame-overrides.c

```c

{% raw %}
297 | override_lookup(char* fname)
298 | {
299 |   dlerror(); // clear dlerror
300 |   void* rv = dlsym(RTLD_NEXT, fname);
301 |   char* e = dlerror();
302 |   if (e) {
303 |     hpcrun_abort("dlsym(RTLD_NEXT, %s) failed: %s", fname, e);
304 |   }
305 |   return rv;
316 |   void* rv = dlvsym(RTLD_NEXT, fname, "GLIBC_2.3.2");
317 |   char* e = dlerror();
318 |   if (e) {
319 |     hpcrun_abort("dlsym(RTLD_NEXT, %s) failed: %s", fname, e);
320 |   }
321 |   return rv;
{% endraw %}

```
### src/tool/hpcrun/sample-sources/libdl.h

```c

{% raw %}
89 |   
90 | #define CHK_DLSYM(h, fn) {						\
91 |     dlerror();								\
92 |     DYN_FN_NAME(fn) = dlsym(h, #fn);					\
93 |     if (DYN_FN_NAME(fn) == 0) {						\
94 |       return -1;							\
{% endraw %}

```
### src/tool/hpcrun/sample-sources/gpu_blame-overrides.c

```c

{% raw %}
367 |   char *error;                                                                     \
368 |                                                                                    \
369 |   dlerror(); 									   \
370 |   void* dlsym_arg = RTLD_NEXT;                                                     \
371 |   void* try = dlsym(dlsym_arg, basename ## FunctionPointer[0].functionName);	   \
372 |   if ((error=dlerror()) || (! try)) {						   \
373 |     if (getenv("DEBUG_HPCRUN_GPU_CONS"))					   \
374 |       fprintf(stderr, "RTLD_NEXT argument fails for " #basename " (%s)\n",         \
375 | 	      (! try) ? "trial function pointer = NULL" : "dlerror != NULL");	   \
376 |     dlerror();									   \
377 |     dlsym_arg = monitor_real_dlopen(#library, RTLD_LAZY);			   \
378 |     if (! dlsym_arg) {                                                             \
379 |       fprintf(stderr, "fallback dlopen of " #library " failed,"			   \
380 | 	      " dlerror message = '%s'\n", dlerror());				   \
389 |   for (int i = 0; i < sizeof(basename ## FunctionPointer)/sizeof(basename ## FunctionPointer[0]); i++) { \
390 |     dlerror();                                                                     \
391 |     basename ## FunctionPointer[i].generic =					   \
392 |       dlsym(dlsym_arg, basename ## FunctionPointer[i].functionName);		   \
393 |     if (getenv("DEBUG_HPCRUN_GPU_CONS"))					   \
394 |       fprintf(stderr, #basename "Fnptr[%d] @ %p for %s = %p\n",                    \
396 | 	      basename ## FunctionPointer[i].functionName,			   \
397 | 	      basename ## FunctionPointer[i].generic);				   \
398 |     if ((error = dlerror()) != NULL) {                                             \
399 |       EEMSG("%s: during dlsym \n", error);					   \
400 |       monitor_real_abort();							   \
401 |     }										   \
{% endraw %}

```
### src/tool/hpcrun/syscalls/ppoll.c

```c

{% raw %}
103 | #ifdef HPCRUN_STATIC_LINK
104 |   real_ppoll = __real_ppoll;
105 | #else
106 |   real_ppoll = (ppoll_fn *) dlsym(RTLD_NEXT, "ppoll");
107 | #endif
108 | 
115 | #ifdef HPCRUN_STATIC_LINK
116 |   real_pselect = __real_pselect;
117 | #else
118 |   real_pselect = (pselect_fn *) dlsym(RTLD_NEXT, "pselect");
119 | #endif
120 | 
{% endraw %}

```
### src/tool/hpcrun/syscalls/select.c

```c

{% raw %}
114 | #ifdef HPCRUN_STATIC_LINK
115 |   real_select = __real_select;
116 | #else
117 |   real_select = (select_fn *) dlsym(RTLD_NEXT, "select");
118 | #endif
119 | 
{% endraw %}

```
### src/tool/hpcrun/syscalls/poll.c

```c

{% raw %}
105 | #ifdef HPCRUN_STATIC_LINK
106 |   real_poll = __real_poll;
107 | #else
108 |   real_poll = (poll_fn *) dlsym(RTLD_NEXT, "poll");
109 | #endif
110 | 
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.c

```c

{% raw %}
93 | 
94 | /* X is the routine name as called from C (i.e. not a string) */
95 | #define CALL_DLSYM(X) \
96 |     dl_ ## X = (dl_ ## X ## _t)dlsym(libpapi, #X)
97 | 
98 | int
{% endraw %}

```