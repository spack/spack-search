---
name: "py-jpype1"
layout: package
next_package: py-mpi4py
previous_package: py-jedi
languages: ['c']
---
## 0.6.0
2 / 193 files match, 1 filtered matches.

 - [native/common/include/jp_platform_linux.h](#nativecommonincludejp_platform_linuxh)

### native/common/include/jp_platform_linux.h

```c

{% raw %}
34 | #if defined(_HPUX) && !defined(_IA64)
35 | 		jvmLibrary = shl_load(path, BIND_DEFERRED|BIND_VERBOSE, 0L);
36 | #else
37 | 		jvmLibrary = dlopen(path, RTLD_LAZY|RTLD_GLOBAL);
38 | #endif // HPUX
39 | 
{% endraw %}

```