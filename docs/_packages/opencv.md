---
name: "opencv"
layout: package
next_package: opendx
previous_package: opa-psm2
languages: ['c']
---
## 3.4.4
8 / 5975 files match, 3 filtered matches.

 - [3rdparty/cpufeatures/cpu-features.c](#3rdpartycpufeaturescpu-featuresc)
 - [3rdparty/ittnotify/src/ittnotify/jitprofiling.c](#3rdpartyittnotifysrcittnotifyjitprofilingc)
 - [3rdparty/ittnotify/src/ittnotify/ittnotify_config.h](#3rdpartyittnotifysrcittnotifyittnotify_configh)

### 3rdparty/cpufeatures/cpu-features.c

```c

{% raw %}
538 |     typedef unsigned long getauxval_func_t(unsigned long);
539 | 
540 |     dlerror();
541 |     void* libc_handle = dlopen("libc.so", RTLD_NOW);
542 |     if (!libc_handle) {
543 |         D("Could not dlopen() C library: %s\n", dlerror());
544 |         return 0;
545 |     }
{% endraw %}

```
### 3rdparty/ittnotify/src/ittnotify/jitprofiling.c

```c

{% raw %}
250 |     if (dllName)
251 |     {
252 |         /* Try to load the dll from the PATH... */
253 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
254 |     }
255 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
259 | #if ITT_PLATFORM==ITT_PLATFORM_WIN
260 |         m_libHandle = LoadLibraryA(DEFAULT_DLLNAME);
261 | #else  /* ITT_PLATFORM==ITT_PLATFORM_WIN */
262 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
263 | #endif /* ITT_PLATFORM==ITT_PLATFORM_WIN */
264 |     }
{% endraw %}

```
### 3rdparty/ittnotify/src/ittnotify/ittnotify_config.h

```c

{% raw %}
370 | }
371 | #endif /* ITT_SIMPLE_INIT */
372 | 
373 | void* dlopen(const char*, int) __attribute__((weak));
374 | void* dlsym(void*, const char*) __attribute__((weak));
375 | int dlclose(void*) __attribute__((weak));
{% endraw %}

```