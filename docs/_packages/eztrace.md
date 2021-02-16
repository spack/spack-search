---
name: "eztrace"
layout: package
next_package: postgis
previous_package: ntirpc
languages: ['c']
---
## 1.1-10
36 / 1095 files match, 2 filtered matches.

 - [src/core/eztrace_convert_core.c](#srccoreeztrace_convert_corec)
 - [test/pptrace/perf/tests/libpreload.c](#testpptraceperftestslibpreloadc)

### src/core/eztrace_convert_core.c

```c

{% raw %}
854 |       void* dlret = dlopen(libname, RTLD_NOW);
{% endraw %}

```
### test/pptrace/perf/tests/libpreload.c

```c

{% raw %}
35 |   void* handle = dlopen("libalacon.so", RTLD_NOW);
{% endraw %}

```