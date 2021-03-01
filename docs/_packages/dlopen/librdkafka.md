---
name: "librdkafka"
layout: package
next_package: libtool
previous_package: libpng
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.5.0
8 / 511 files match, 4 filtered matches.

 - [src/rddl.c](#srcrddlc)
 - [src/rdkafka_conf.c](#srcrdkafka_confc)
 - [src/rdkafka_plugin.c](#srcrdkafka_pluginc)
 - [packaging/cmake/try_compile/dlopen_test.c](#packagingcmaketry_compiledlopen_testc)

### src/rddl.c

```c

{% raw %}
75 |         void *handle;
76 |         const char *loadfunc;
77 | #if WITH_LIBDL
78 |         loadfunc = "dlopen()";
79 |         handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
80 | #elif defined(_WIN32)
81 |         loadfunc = "LoadLibrary()";
{% endraw %}

```
### src/rdkafka_conf.c

```c

{% raw %}
876 |         { _RK_GLOBAL, "plugin.library.paths", _RK_C_STR,
877 |           _RK(plugin_paths),
878 |           "List of plugin libraries to load (; separated). "
879 |           "The library search path is platform dependent (see dlopen(3) for Unix and LoadLibrary() for Windows). If no filename extension is specified the "
880 |           "platform-specific extension (such as .dll or .so) will be appended automatically.",
881 |           .set = rd_kafka_plugins_conf_set },
{% endraw %}

```
### src/rdkafka_plugin.c

```c

{% raw %}
33 | typedef struct rd_kafka_plugin_s {
34 |         char *rkplug_path;         /* Library path */
35 |         rd_kafka_t *rkplug_rk;     /* Backpointer to the rk handle */
36 |         void *rkplug_handle;       /* dlopen (or similar) handle */
37 |         void *rkplug_opaque;       /* Plugin's opaque */
38 | 
{% endraw %}

```
### packaging/cmake/try_compile/dlopen_test.c

```c

{% raw %}
3 | int main() {
4 |         void *h;
5 |         /* Try loading anything, we don't care if it works */
6 |         h = dlopen("__nothing_rdkafka.so", RTLD_NOW|RTLD_LOCAL);
7 |         if (h)
8 |                 dlclose(h);
{% endraw %}

```