---
name: "hpctoolkit"
layout: package
next_package: vampirtrace
previous_package: linux-pam
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
81 | void hpcrun_stats_num_samples_blocked_dlopen_inc(void);
82 | long hpcrun_stats_num_samples_blocked_dlopen(void);
{% endraw %}

```
### src/tool/hpcrun/custom-init-dynamic.c

```c

{% raw %}
84 |     void* custom_fns = monitor_real_dlopen("./hpcrun-custom.so", RTLD_LAZY);
{% endraw %}

```
### src/tool/hpcrun/hpcrun_stats.c

```c

{% raw %}
68 | static atomic_long num_samples_blocked_dlopen = ATOMIC_VAR_INIT(0);
97 |   atomic_store_explicit(&num_samples_blocked_dlopen, 0, memory_order_relaxed);
181 | hpcrun_stats_num_samples_blocked_dlopen_inc(void)
183 |   atomic_fetch_add_explicit(&num_samples_blocked_dlopen, 1L, memory_order_relaxed);
188 | hpcrun_stats_num_samples_blocked_dlopen(void)
190 |   return atomic_load_explicit(&num_samples_blocked_dlopen, memory_order_relaxed);
444 |   long cpu_blocked_dlopen = atomic_load_explicit(&num_samples_blocked_dlopen, memory_order_relaxed);
445 |   long cpu_blocked = cpu_blocked_async + cpu_blocked_dlopen;
480 |   AMSG("SAMPLE ANOMALIES: blocks: %ld (async: %ld, dlopen: %ld), "
482 |        cpu_blocked, cpu_blocked_async, cpu_blocked_dlopen, 
{% endraw %}

```
### src/tool/hpcrun/epoch.c

```c

{% raw %}
96 |   dlopen()'s a new shared object, which begins an entirely
{% endraw %}

```
### src/tool/hpcrun/hpcrun_dlfns.h

```c

{% raw %}
49 | void hpcrun_pre_dlopen(const char *path, int flags);
50 | void hpcrun_dlopen(const char *module_name, int flags, void *handle);
54 | long hpcrun_dlopen_pending(void);
{% endraw %}

```
### src/tool/hpcrun/main.h

```c

{% raw %}
62 | extern void hpcrun_force_dlopen(bool forced);
{% endraw %}

```
### src/tool/hpcrun/main.c

```c

{% raw %}
238 | static bool hpcrun_dlopen_forced = false;
340 | hpcrun_force_dlopen(bool forced)
342 |   hpcrun_dlopen_forced = forced;
1669 | monitor_pre_dlopen(const char* path, int flags)
1677 |   hpcrun_pre_dlopen(path, flags);
1683 | monitor_dlopen(const char *path, int flags, void* handle)
1686 |   hpcrun_dlopen(path, flags, handle);
{% endraw %}

```
### src/tool/hpcrun/hpcrun_dlfns.c

```c

{% raw %}
97 | static spinlock_t dlopen_lock = SPINLOCK_UNLOCKED;
98 | static atomic_long dlopen_num_readers = ATOMIC_VAR_INIT(0);
99 | static volatile long dlopen_num_writers = 0;
100 | static int  dlopen_writer_tid = -1;
103 | static atomic_long num_dlopen_pending = ATOMIC_VAR_INIT(0);
108 | hpcrun_dlopen_pending(void)
110 |   return atomic_load_explicit(&num_dlopen_pending, memory_order_relaxed);
114 | hpcrun_pre_dlopen(const char *path, int flags)
121 | hpcrun_dlopen(const char *module_name, int flags, void *handle)
{% endraw %}

```
### src/tool/hpcrun/loadmap.h

```c

{% raw %}
53 |    an loadmap can span across dlopen and dlclose operations. an loadmap
54 |    ends when a dlopen maps a new load module on top of a region of 
{% endraw %}

```
### src/tool/hpcrun/fnbounds/fnbounds_dynamic.c

```c

{% raw %}
522 |   if (!dso && ENABLED(DLOPEN_RISKY) && hpcrun_dlopen_pending() > 0) {
{% endraw %}

```
### src/tool/hpcrun/lush/lush.c

```c

{% raw %}
105 |   x->dlhandle = monitor_real_dlopen(path, RTLD_LAZY);
115 |   CALL_DLSYM(pool, LUSHI_reg_dlopen,   id, x->dlhandle);
181 |   FN_TBL_ALLOC(x, LUSHI_reg_dlopen,      num_agents + 1);
210 |   FN_TBL_FREE(x, LUSHI_reg_dlopen);
{% endraw %}

```
### src/tool/hpcrun/lush/lush.h

```c

{% raw %}
105 |   POOL_DECL(LUSHI_reg_dlopen);
{% endraw %}

```
### src/tool/hpcrun/lush/lushi.h

```c

{% raw %}
113 | LUSHI_DECL(int, LUSHI_reg_dlopen, ());
{% endraw %}

```
### src/tool/hpcrun/gpu/nvidia/cupti-api.c

```c

{% raw %}
504 |   void *h = monitor_real_dlopen("libcudart.so", RTLD_LOCAL | RTLD_LAZY);
554 |   hpcrun_force_dlopen(true);
556 |   hpcrun_force_dlopen(false);
{% endraw %}

```
### src/tool/hpcrun/gpu/amd/roctracer-api.c

```c

{% raw %}
442 |   hpcrun_force_dlopen(true);
444 |   hpcrun_force_dlopen(false);
{% endraw %}

```
### src/tool/hpcrun/sample-sources/papi-c-cupti.c

```c

{% raw %}
62 |   void* v = monitor_real_dlopen(lib, flags);          \
64 |     fprintf(stderr, "gpu dlopen %s failed\n", lib);   \
129 |   Chk_dlopen(cudart, "libcudart.so", RTLD_NOW | RTLD_GLOBAL);
132 |   Chk_dlopen(cupti, "libcupti.so", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/tool/hpcrun/sample-sources/libdl.h

```c

{% raw %}
85 |   void* h = dlopen(lib, flags);          \
{% endraw %}

```
### src/tool/hpcrun/sample-sources/gpu_blame-overrides.c

```c

{% raw %}
377 |     dlsym_arg = monitor_real_dlopen(#library, RTLD_LAZY);			   \
379 |       fprintf(stderr, "fallback dlopen of " #library " failed,"			   \
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-cilk.c

```c

{% raw %}
162 | LUSHI_reg_dlopen()
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-tbb.c

```c

{% raw %}
132 | LUSHI_reg_dlopen()
{% endraw %}

```
### src/tool/hpcrun/lush-agents/agent-pthread.c

```c

{% raw %}
139 | LUSHI_reg_dlopen()
{% endraw %}

```
### src/tool/hpcrun-flat/monitor_preload.c

```c

{% raw %}
164 | monitor_dlopen(char* lib)
167 |     fprintf(stderr, "dlopen(%s) callback from monitor received\n", lib); 
{% endraw %}

```
### src/tool/hpcrun-flat/monitor.c

```c

{% raw %}
454 | handle_dlopen()
457 |     DIE0("dlopen before process initialization!");
498 |   if (opt_debug >= 1) { MSG0(stderr, "*** dlopen handling complete ***"); }
{% endraw %}

```
### src/tool/hpcrun-flat/monitor.h

```c

{% raw %}
227 | typedef void* (*dlopen_fptr_t) (const char *filename, int flag);
276 | extern void handle_dlopen();
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.c

```c

{% raw %}
99 | dlopen_papi()
102 |   libpapi = dlopen(HPC_LIBPAPI_SO, RTLD_LAZY);
{% endraw %}

```
### src/tool/hpcrun-flat/dlpapi.h

```c

{% raw %}
81 | extern int dlopen_papi();
{% endraw %}

```