---
name: "onednn"
layout: package
next_package: py-pybind11
previous_package: dcap
languages: ['cpp']
---
## 1.6.5
3 / 1404 files match

 - [src/cpu/x64/jit_utils/jitprofiling/jitprofiling.c](#srccpux64jit_utilsjitprofilingjitprofilingc)
 - [src/cpu/x64/jit_utils/jitprofiling/ittnotify_config.h](#srccpux64jit_utilsjitprofilingittnotify_configh)
 - [src/cpu/x64/xbyak/xbyak_util.h](#srccpux64xbyakxbyak_utilh)

### src/cpu/x64/jit_utils/jitprofiling/jitprofiling.c

```cpp

{% raw %}
232 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
241 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### src/cpu/x64/jit_utils/jitprofiling/ittnotify_config.h

```cpp

{% raw %}
302 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
353 | void* dlopen(const char*, int) __attribute__((weak));
357 | void* dlopen(const char*, int);
361 | #define DL_SYMBOLS (dlopen && dlsym && dlclose)
{% endraw %}

```
### src/cpu/x64/xbyak/xbyak_util.h

```cpp

{% raw %}
854 | 			dlopen("dummy", RTLD_LAZY); // force to load dlopen to enable jit profiling
{% endraw %}

```