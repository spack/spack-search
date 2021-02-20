---
name: "onednn"
layout: package
next_package: opa-psm2
previous_package: ompt-openmp
languages: ['c']
---
## 1.6.5
3 / 1404 files match, 3 filtered matches.

 - [src/cpu/x64/jit_utils/jitprofiling/jitprofiling.c](#srccpux64jit_utilsjitprofilingjitprofilingc)
 - [src/cpu/x64/jit_utils/jitprofiling/ittnotify_config.h](#srccpux64jit_utilsjitprofilingittnotify_configh)
 - [src/cpu/x64/xbyak/xbyak_util.h](#srccpux64xbyakxbyak_utilh)

### src/cpu/x64/jit_utils/jitprofiling/jitprofiling.c

```c

{% raw %}
229 |     if (dllName)
230 |     {
231 |         /* Try to load the dll from the PATH... */
232 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
233 |     }
234 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
238 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
239 |         m_libHandle = LoadLibraryA(DEFAULT_DLLNAME);
240 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
241 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
242 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
243 |     }
{% endraw %}

```
### src/cpu/x64/jit_utils/jitprofiling/ittnotify_config.h

```c

{% raw %}
350 | #endif /* ITT_SIMPLE_INIT */
351 | 
352 | #if 0
353 | void* dlopen(const char*, int) __attribute__((weak));
354 | void* dlsym(void*, const char*) __attribute__((weak));
355 | int dlclose(void*) __attribute__((weak));
356 | #else
357 | void* dlopen(const char*, int);
358 | void* dlsym(void*, const char*);
359 | int dlclose(void*);
{% endraw %}

```
### src/cpu/x64/xbyak/xbyak_util.h

```c

{% raw %}
851 | 			return;
852 | 		case VTune:
853 | #ifdef XBYAK_USE_VTUNE
854 | 			dlopen("dummy", RTLD_LAZY); // force to load dlopen to enable jit profiling
855 | 			if (iJIT_IsProfilingActive() != iJIT_SAMPLING_ON) {
856 | 				fprintf(stderr, "VTune profiling is not active\n");
{% endraw %}

```