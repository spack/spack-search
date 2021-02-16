---
name: "librdkafka"
layout: package
next_package: cln
previous_package: namd
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
78 |         loadfunc = "dlopen()";
79 |         handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### src/rdkafka_conf.c

```c

{% raw %}
879 |           "The library search path is platform dependent (see dlopen(3) for Unix and LoadLibrary() for Windows). If no filename extension is specified the "
{% endraw %}

```
### src/rdkafka_plugin.c

```c

{% raw %}
36 |         void *rkplug_handle;       /* dlopen (or similar) handle */
{% endraw %}

```
### packaging/cmake/try_compile/dlopen_test.c

```c

{% raw %}
6 |         h = dlopen("__nothing_rdkafka.so", RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```