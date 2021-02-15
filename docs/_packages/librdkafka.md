---
name: "librdkafka"
layout: package
next_package: cln
previous_package: namd
languages: ['cpp']
---
## 1.5.0
8 / 511 files match

 - [CONFIGURATION.md](#configurationmd)
 - [CMakeLists.txt](#cmakeliststxt)
 - [configure.self](#configureself)
 - [src/rddl.c](#srcrddlc)
 - [src/rdkafka_conf.c](#srcrdkafka_confc)
 - [src/rdkafka_plugin.c](#srcrdkafka_pluginc)
 - [packaging/cmake/try_compile/dlopen_test.c](#packagingcmaketry_compiledlopen_testc)
 - [tests/librdkafka.suppressions](#testslibrdkafkasuppressions)

### CONFIGURATION.md

```

{% raw %}
89 | plugin.library.paths                     |  *  |                 |               | low        | List of plugin libraries to load (; separated). The library search path is platform dependent (see dlopen(3) for Unix and LoadLibrary() for Windows). If no filename extension is specified the platform-specific extension (such as .dll or .so) will be appended automatically. <br>*Type: string*
{% endraw %}

```
### CMakeLists.txt

```

{% raw %}
72 |     "${TRYCOMPILE_SRC_DIR}/dlopen_test.c"
{% endraw %}

```
### configure.self

```

{% raw %}
85 |     # Check if dlopen() is available
91 |    void *h = dlopen(\"__bad_lib\", 0);
{% endraw %}

```
### src/rddl.c

```cpp

{% raw %}
78 |         loadfunc = "dlopen()";
79 |         handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### src/rdkafka_conf.c

```cpp

{% raw %}
879 |           "The library search path is platform dependent (see dlopen(3) for Unix and LoadLibrary() for Windows). If no filename extension is specified the "
{% endraw %}

```
### src/rdkafka_plugin.c

```cpp

{% raw %}
36 |         void *rkplug_handle;       /* dlopen (or similar) handle */
60 |  *         (dlopen() and LoadLibrary() does this for us)
126 |  *         This is true for POSIX dlopen() and Win32 LoadLibrary().
{% endraw %}

```
### packaging/cmake/try_compile/dlopen_test.c

```cpp

{% raw %}
6 |         h = dlopen("__nothing_rdkafka.so", RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### tests/librdkafka.suppressions

```

{% raw %}
336 |    leak_sasl_dlopen
414 |    dlopen1
{% endraw %}

```