---
name: "hpctoolkit"
layout: package
next_package: hwloc
previous_package: hdf5
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2020.08.03
39 / 1254 files match, 26 filtered matches.

 - [src/tool/hpcrun/hpcrun_stats.h](#srctoolhpcrunhpcrun_statsh)
 - [src/tool/hpcrun/custom-init-dynamic.c](#srctoolhpcruncustom-init-dynamicc)
 - [src/tool/hpcrun/hpcrun_stats.c](#srctoolhpcrunhpcrun_statsc)
 - [src/tool/hpcrun/epoch.c](#srctoolhpcrunepochc)
 - [src/tool/hpcrun/hpcrun_dlfns.h](#srctoolhpcrunhpcrun_dlfnsh)
 - [src/tool/hpcrun/main.h](#srctoolhpcrunmainh)
 - [src/tool/hpcrun/main.c](#srctoolhpcrunmainc)
 - [src/tool/hpcrun/hpcrun_dlfns.c](#srctoolhpcrunhpcrun_dlfnsc)
 - [src/tool/hpcrun/loadmap.h](#srctoolhpcrunloadmaph)
 - [src/tool/hpcrun/fnbounds/fnbounds_dynamic.c](#srctoolhpcrunfnboundsfnbounds_dynamicc)
 - [src/tool/hpcrun/lush/lush.c](#srctoolhpcrunlushlushc)
 - [src/tool/hpcrun/lush/lush.h](#srctoolhpcrunlushlushh)
 - [src/tool/hpcrun/lush/lushi.h](#srctoolhpcrunlushlushih)
 - [src/tool/hpcrun/gpu/nvidia/cupti-api.c](#srctoolhpcrungpunvidiacupti-apic)
 - [src/tool/hpcrun/gpu/amd/roctracer-api.c](#srctoolhpcrungpuamdroctracer-apic)
 - [src/tool/hpcrun/sample-sources/papi-c-cupti.c](#srctoolhpcrunsample-sourcespapi-c-cuptic)
 - [src/tool/hpcrun/sample-sources/libdl.h](#srctoolhpcrunsample-sourceslibdlh)
 - [src/tool/hpcrun/sample-sources/gpu_blame-overrides.c](#srctoolhpcrunsample-sourcesgpu_blame-overridesc)
 - [src/tool/hpcrun/lush-agents/agent-cilk.c](#srctoolhpcrunlush-agentsagent-cilkc)
 - [src/tool/hpcrun/lush-agents/agent-tbb.c](#srctoolhpcrunlush-agentsagent-tbbc)
 - [src/tool/hpcrun/lush-agents/agent-pthread.c](#srctoolhpcrunlush-agentsagent-pthreadc)
 - [src/tool/hpcrun-flat/monitor_preload.c](#srctoolhpcrun-flatmonitor_preloadc)
 - [src/tool/hpcrun-flat/monitor.c](#srctoolhpcrun-flatmonitorc)
 - [src/tool/hpcrun-flat/monitor.h](#srctoolhpcrun-flatmonitorh)
 - [src/tool/hpcrun-flat/dlpapi.c](#srctoolhpcrun-flatdlpapic)
 - [src/tool/hpcrun-flat/dlpapi.h](#srctoolhpcrun-flatdlpapih)

### src/tool/hpcrun/hpcrun_stats.h

```c

{% raw %}
78 | // samples blocked dlopen 
79 | //-----------------------------
80 | 
81 | void hpcrun_stats_num_samples_blocked_dlopen_inc(void);
82 | long hpcrun_stats_num_samples_blocked_dlopen(void);
83 | 
84 | 
{% endraw %}

```
### src/tool/hpcrun/custom-init-dynamic.c

```c

{% raw %}
81 | hpcrun_do_custom_init(void)
82 | {
83 |   if (ENABLED(CUSTOM_INIT)) {
84 |     void* custom_fns = monitor_real_dlopen("./hpcrun-custom.so", RTLD_LAZY);
85 |     if (custom_fns) {
86 |       void (*hpcrun_custom_init)(void) = (void (*)(void)) dlsym(custom_fns, "hpcrun_custom_init");
{% endraw %}

```
### src/tool/hpcrun/hpcrun_stats.c

```c

{% raw %}
65 | static atomic_long num_samples_total = ATOMIC_VAR_INIT(0);
66 | static atomic_long num_samples_attempted = ATOMIC_VAR_INIT(0);
67 | static atomic_long num_samples_blocked_async = ATOMIC_VAR_INIT(0);
68 | static atomic_long num_samples_blocked_dlopen = ATOMIC_VAR_INIT(0);
69 | static atomic_long num_samples_dropped = ATOMIC_VAR_INIT(0);
70 | static atomic_long num_samples_segv = ATOMIC_VAR_INIT(0);
94 |   atomic_store_explicit(&num_samples_total, 0, memory_order_relaxed);
95 |   atomic_store_explicit(&num_samples_attempted, 0, memory_order_relaxed);
96 |   atomic_store_explicit(&num_samples_blocked_async, 0, memory_order_relaxed);
97 |   atomic_store_explicit(&num_samples_blocked_dlopen, 0, memory_order_relaxed);
98 |   atomic_store_explicit(&num_samples_segv, 0, memory_order_relaxed);
99 | 
178 | //-----------------------------
179 | 
180 | void
181 | hpcrun_stats_num_samples_blocked_dlopen_inc(void)
182 | {
183 |   atomic_fetch_add_explicit(&num_samples_blocked_dlopen, 1L, memory_order_relaxed);
184 | }
185 | 
186 | 
187 | long
188 | hpcrun_stats_num_samples_blocked_dlopen(void)
189 | {
190 |   return atomic_load_explicit(&num_samples_blocked_dlopen, memory_order_relaxed);
191 | }
192 | 
441 | hpcrun_stats_print_summary(void)
442 | {
443 |   long cpu_blocked_async  = atomic_load_explicit(&num_samples_blocked_async, memory_order_relaxed);
444 |   long cpu_blocked_dlopen = atomic_load_explicit(&num_samples_blocked_dlopen, memory_order_relaxed);
445 |   long cpu_blocked = cpu_blocked_async + cpu_blocked_dlopen;
446 | 
447 |   long cpu_dropped = atomic_load_explicit(&num_samples_dropped, memory_order_relaxed);
477 |        acc_samp + acc_samp_dropped, acc_samp, acc_samp_dropped
478 |        );
479 | 
480 |   AMSG("SAMPLE ANOMALIES: blocks: %ld (async: %ld, dlopen: %ld), "
481 |        "errors: %ld (segv: %ld, soft: %ld)",
482 |        cpu_blocked, cpu_blocked_async, cpu_blocked_dlopen, 
483 |        cpu_dropped, cpu_segv, cpu_dropped - cpu_segv);
484 | 
{% endraw %}

```
### src/tool/hpcrun/epoch.c

```c

{% raw %}
93 |   since we don't bother doing anything on dlclose()...;
94 | 
95 |   3. somebody else (thread in step 2 or a different thread)
96 |   dlopen()'s a new shared object, which begins an entirely
97 |   new loadmap--one which does not include the shared object
98 |   which resides in our backtrace;
{% endraw %}

```
### src/tool/hpcrun/hpcrun_dlfns.h

```c

{% raw %}
46 | #ifndef _CSPROF_DLFNS_H_
47 | #define _CSPROF_DLFNS_H_
48 | 
49 | void hpcrun_pre_dlopen(const char *path, int flags);
50 | void hpcrun_dlopen(const char *module_name, int flags, void *handle);
51 | void hpcrun_dlclose(void *handle);
52 | void hpcrun_post_dlclose(void *handle, int ret);
53 | 
54 | long hpcrun_dlopen_pending(void);
55 | 
56 | #endif
{% endraw %}

```
### src/tool/hpcrun/main.h

```c

{% raw %}
59 | extern void hpcrun_set_safe_to_sync(void);
60 | extern void hpcrun_set_real_siglongjmp(void);
61 | 
62 | extern void hpcrun_force_dlopen(bool forced);
63 | 
64 | //
{% endraw %}

```
### src/tool/hpcrun/main.c

```c

{% raw %}
235 | 
236 | static hpcrun_options_t opts;
237 | static bool hpcrun_is_initialized_private = false;
238 | static bool hpcrun_dlopen_forced = false;
239 | static bool safe_to_sync_sample = false;
240 | static void* main_addr = NULL;
337 | //
338 | 
339 | void
340 | hpcrun_force_dlopen(bool forced)
341 | {
342 |   hpcrun_dlopen_forced = forced;
343 | }
344 | 
1666 | #ifndef HPCRUN_STATIC_LINK
1667 | 
1668 | void
1669 | monitor_pre_dlopen(const char* path, int flags)
1670 | {
1671 |   if (!hpcrun_is_initialized()) {
1674 | 
1675 |   hpcrun_dlfunction_begin();
1676 |   hpcrun_safe_enter();
1677 |   hpcrun_pre_dlopen(path, flags);
1678 |   hpcrun_safe_exit();
1679 | }
1680 | 
1681 | 
1682 | void
1683 | monitor_dlopen(const char *path, int flags, void* handle)
1684 | {
1685 |   hpcrun_safe_enter();
1686 |   hpcrun_dlopen(path, flags, handle);
1687 |   hpcrun_safe_exit();
1688 |   hpcrun_dlfunction_end();
{% endraw %}

```
### src/tool/hpcrun/hpcrun_dlfns.c

```c

{% raw %}
94 | //
95 | 
96 | #if 0
97 | static spinlock_t dlopen_lock = SPINLOCK_UNLOCKED;
98 | static atomic_long dlopen_num_readers = ATOMIC_VAR_INIT(0);
99 | static volatile long dlopen_num_writers = 0;
100 | static int  dlopen_writer_tid = -1;
101 | #endif
102 | 
103 | static atomic_long num_dlopen_pending = ATOMIC_VAR_INIT(0);
104 | 
105 | 
106 | // We use this only in the DLOPEN_RISKY case.
107 | long
108 | hpcrun_dlopen_pending(void)
109 | {
110 |   return atomic_load_explicit(&num_dlopen_pending, memory_order_relaxed);
111 | }
112 | 
113 | void 
114 | hpcrun_pre_dlopen(const char *path, int flags)
115 | {
116 |     
118 | 
119 | 
120 | void 
121 | hpcrun_dlopen(const char *module_name, int flags, void *handle)
122 | {
123 |   fnbounds_map_open_dsos();
{% endraw %}

```
### src/tool/hpcrun/loadmap.h

```c

{% raw %}
50 | 
51 | /* an "loadmap" is an interval of time during which no two dynamic 
52 |    libraries are mapped to the same region of the address space. 
53 |    an loadmap can span across dlopen and dlclose operations. an loadmap
54 |    ends when a dlopen maps a new load module on top of a region of 
55 |    the address space that has previously been occupied by another
56 |    module earlier during the loadmap.
{% endraw %}

```
### src/tool/hpcrun/fnbounds/fnbounds_dynamic.c

```c

{% raw %}
519 |   // However, the risk is small, and if we're willing to take the
520 |   // risk, then analyzing the new DSO here allows us to sample inside
521 |   // an init constructor.
522 |   if (!dso && ENABLED(DLOPEN_RISKY) && hpcrun_dlopen_pending() > 0) {
523 |     char module_name[PATH_MAX];
524 |     void *mstart, *mend;
{% endraw %}

```
### src/tool/hpcrun/lush/lush.c

```c

{% raw %}
102 |   strcpy(x->path, path);
103 | 
104 |   //x->dlhandle = dlopen(path, RTLD_LAZY);
105 |   x->dlhandle = monitor_real_dlopen(path, RTLD_LAZY);
106 |   handle_any_dlerror();
107 | 
112 |   CALL_DLSYM(pool, LUSHI_init,         id, x->dlhandle);
113 |   CALL_DLSYM(pool, LUSHI_fini,         id, x->dlhandle);
114 |   CALL_DLSYM(pool, LUSHI_strerror,     id, x->dlhandle);
115 |   CALL_DLSYM(pool, LUSHI_reg_dlopen,   id, x->dlhandle);
116 |   CALL_DLSYM(pool, LUSHI_ismycode,     id, x->dlhandle);
117 |   CALL_DLSYM(pool, LUSHI_step_bichord, id, x->dlhandle);
178 |   FN_TBL_ALLOC(x, LUSHI_init,            num_agents + 1);
179 |   FN_TBL_ALLOC(x, LUSHI_fini,            num_agents + 1);
180 |   FN_TBL_ALLOC(x, LUSHI_strerror,        num_agents + 1);
181 |   FN_TBL_ALLOC(x, LUSHI_reg_dlopen,      num_agents + 1);
182 |   FN_TBL_ALLOC(x, LUSHI_ismycode,        num_agents + 1);
183 |   FN_TBL_ALLOC(x, LUSHI_step_bichord,    num_agents + 1);
207 |   FN_TBL_FREE(x, LUSHI_init);
208 |   FN_TBL_FREE(x, LUSHI_fini);
209 |   FN_TBL_FREE(x, LUSHI_strerror);
210 |   FN_TBL_FREE(x, LUSHI_reg_dlopen);
211 |   FN_TBL_FREE(x, LUSHI_ismycode);
212 |   FN_TBL_FREE(x, LUSHI_step_bichord);
{% endraw %}

```
### src/tool/hpcrun/lush/lush.h

```c

{% raw %}
102 |   POOL_DECL(LUSHI_init);
103 |   POOL_DECL(LUSHI_fini);
104 |   POOL_DECL(LUSHI_strerror);
105 |   POOL_DECL(LUSHI_reg_dlopen);
106 |   POOL_DECL(LUSHI_ismycode);
107 |   POOL_DECL(LUSHI_step_bichord);
{% endraw %}

```
### src/tool/hpcrun/lush/lushi.h

```c

{% raw %}
110 | // Maintaining Responsibility for Code/Frame-space
111 | // --------------------------------------------------------------------------
112 | 
113 | LUSHI_DECL(int, LUSHI_reg_dlopen, ());
114 | 
115 | LUSHI_DECL(bool, LUSHI_ismycode, (void* addr));
{% endraw %}

```
### src/tool/hpcrun/gpu/nvidia/cupti-api.c

```c

{% raw %}
501 |   // note: a version of this file with a more specific name may
502 |   // already be loaded. thus, even if the dlopen fails, we search with
503 |   // dl_iterate_phdr.
504 |   void *h = monitor_real_dlopen("libcudart.so", RTLD_LOCAL | RTLD_LAZY);
505 | 
506 |   if (dl_iterate_phdr(cuda_path, buffer)) {
551 | {
552 | #ifndef HPCRUN_STATIC_LINK
553 |   // dynamic libraries only availabile in non-static case
554 |   hpcrun_force_dlopen(true);
555 |   CHK_DLOPEN(cupti, cupti_path(), RTLD_NOW | RTLD_GLOBAL);
556 |   hpcrun_force_dlopen(false);
557 | 
558 | #define CUPTI_BIND(fn) \
{% endraw %}

```
### src/tool/hpcrun/gpu/amd/roctracer-api.c

```c

{% raw %}
439 |   
440 | #ifndef HPCRUN_STATIC_LINK
441 |   // dynamic libraries only availabile in non-static case
442 |   hpcrun_force_dlopen(true);
443 |   CHK_DLOPEN(roctracer, roctracer_path(), RTLD_NOW | RTLD_GLOBAL);
444 |   hpcrun_force_dlopen(false);
445 | 
446 | #define ROCTRACER_BIND(fn) \
{% endraw %}

```
### src/tool/hpcrun/sample-sources/papi-c-cupti.c

```c

{% raw %}
59 | }
60 | 
61 | #define Chk_dlopen(v, lib, flags)                     \
62 |   void* v = monitor_real_dlopen(lib, flags);          \
63 |   if (! v) {                                          \
64 |     fprintf(stderr, "gpu dlopen %s failed\n", lib);   \
65 |     return;                                           \
66 |   }                                                   \
126 | {
127 |   // only use dlfunctions in NON static case
128 | #ifndef HPCRUN_STATIC_LINK
129 |   Chk_dlopen(cudart, "libcudart.so", RTLD_NOW | RTLD_GLOBAL);
130 |   Chk_dlsym(cudart, cudaThreadSynchronize);
131 | 
132 |   Chk_dlopen(cupti, "libcupti.so", RTLD_NOW | RTLD_GLOBAL);
133 |   Chk_dlsym(cupti, cuptiGetResultString);
134 |   Chk_dlsym(cupti, cuptiSubscribe);
{% endraw %}

```
### src/tool/hpcrun/sample-sources/libdl.h

```c

{% raw %}
82 | #define DYN_FN_NAME(f) f ## _fn
83 | 
84 | #define CHK_DLOPEN(h, lib, flags)		      \
85 |   void* h = dlopen(lib, flags);          \
86 |   if (!h) {					      \
87 |     return -1;					      \
{% endraw %}

```
### src/tool/hpcrun/sample-sources/gpu_blame-overrides.c

```c

{% raw %}
374 |       fprintf(stderr, "RTLD_NEXT argument fails for " #basename " (%s)\n",         \
375 | 	      (! try) ? "trial function pointer = NULL" : "dlerror != NULL");	   \
376 |     dlerror();									   \
377 |     dlsym_arg = monitor_real_dlopen(#library, RTLD_LAZY);			   \
378 |     if (! dlsym_arg) {                                                             \
379 |       fprintf(stderr, "fallback dlopen of " #library " failed,"			   \
380 | 	      " dlerror message = '%s'\n", dlerror());				   \
381 |       monitor_real_abort();							   \
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-cilk.c

```c

{% raw %}
159 | // **************************************************************************
160 | 
161 | extern int 
162 | LUSHI_reg_dlopen()
163 | {
164 |   return 0; // FIXME: coordinate with dylib stuff
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-tbb.c

```c

{% raw %}
129 | // **************************************************************************
130 | 
131 | extern int 
132 | LUSHI_reg_dlopen()
133 | {
134 |   return 0; // FIXME: coordinate with dylib stuff
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-pthread.c

```c

{% raw %}
136 | // **************************************************************************
137 | 
138 | extern int 
139 | LUSHI_reg_dlopen()
140 | {
141 |   return 0; // FIXME: coordinate with dylib stuff
{% endraw %}

```
### src/tool/hpcrun-flat/monitor_preload.c

```c

{% raw %}
161 | 
162 | 
163 | void 
164 | monitor_dlopen(char* lib)
165 | {
166 |   if (opt_debug >= 1) {
167 |     fprintf(stderr, "dlopen(%s) callback from monitor received\n", lib); 
168 |   }
169 |   /* update profile tables */
{% endraw %}

```
### src/tool/hpcrun-flat/monitor.c

```c

{% raw %}
451 |  *
452 |  */
453 | extern void
454 | handle_dlopen()
455 | {
456 |   if (hpc_profdesc == NULL) {
457 |     DIE0("dlopen before process initialization!");
458 |   }
459 | 
495 |   if (HPC_GET_PAPIPROFS(hpc_profdesc)) {
496 |     start_papi_for_thread(HPC_GET_PAPIPROFS(hpc_profdesc));
497 |   }
498 |   if (opt_debug >= 1) { MSG0(stderr, "*** dlopen handling complete ***"); }
499 | }
500 | 
{% endraw %}

```
### src/tool/hpcrun-flat/monitor.h

```c

{% raw %}
224 | typedef int (*execve_fptr_t) PARAMS_EXECVE;
225 | 
226 | typedef pid_t (*fork_fptr_t) (void);
227 | typedef void* (*dlopen_fptr_t) (const char *filename, int flag);
228 | 
229 | typedef void (*_exit_fptr_t) (int);
273 | hpcrun_parse_execl(const char*** argv, const char* const** envp,
274 | 		   const char* arg, va_list arglist);
275 | 
276 | extern void handle_dlopen();
277 | 
278 | 
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.c

```c

{% raw %}
96 |     dl_ ## X = (dl_ ## X ## _t)dlsym(libpapi, #X)
97 | 
98 | int
99 | dlopen_papi()
100 | {
101 |   /* Open PAPI lib */
102 |   libpapi = dlopen(HPC_LIBPAPI_SO, RTLD_LAZY);
103 |   handle_any_dlerror();
104 |   
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.h

```c

{% raw %}
78 |    called multiple times, but the number of closes should equal the
79 |    number of opens. */
80 | 
81 | extern int dlopen_papi();
82 | extern int dlclose_papi();
83 | 
{% endraw %}

```