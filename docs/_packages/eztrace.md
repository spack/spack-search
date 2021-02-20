---
name: "eztrace"
layout: package
next_package: fakechroot
previous_package: extrae
languages: ['c']
---
## 1.1-10
36 / 1095 files match, 2 filtered matches.

 - [src/core/eztrace_convert_core.c](#srccoreeztrace_convert_corec)
 - [test/pptrace/perf/tests/libpreload.c](#testpptraceperftestslibpreloadc)

### src/core/eztrace_convert_core.c

```c

{% raw %}
851 |       /* Open the lib. The constructor of this lib is called and should register
852 |        * the module by calling eztrace_convert_register_module()
853 |        */
854 |       void* dlret = dlopen(libname, RTLD_NOW);
855 |       if (!dlret) {
856 | 	fprintf(stderr, "%s\n", dlerror());
{% endraw %}

```
### test/pptrace/perf/tests/libpreload.c

```c

{% raw %}
32 | void __hijack_init(void) __attribute__ ((constructor));
33 | /* Initialize the current library */
34 | void __hijack_init(void) {
35 |   void* handle = dlopen("libalacon.so", RTLD_NOW);
36 |   if (handle) {
37 |     orig_foo = dlsym(handle, "foo");
{% endraw %}

```