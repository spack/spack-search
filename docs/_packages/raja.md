---
name: "raja"
layout: package
next_package: macsio
previous_package: haproxy
languages: []
---
## 0.12.1
3 / 2038 files match

 - [src/RuntimePluginLoader.cpp](#srcruntimepluginloadercpp)
 - [src/KokkosPluginLoader.cpp](#srckokkospluginloadercpp)
 - [blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in](#bltthirdparty_builtingoogletest-master-2020-01-07googletestcmakelibgtestlain)

### src/RuntimePluginLoader.cpp

```

{% raw %}
88 |   void *plugin = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
91 |     printf("[RuntimePluginLoader]: dlopen failed: %s\n", dlerror());
{% endraw %}

```
### src/KokkosPluginLoader.cpp

```

{% raw %}
91 |   void *plugin = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
94 |     printf("[KokkosPluginLoader]: dlopen failed: %s\n", dlerror());
{% endraw %}

```
### blt/thirdparty_builtin/googletest-master-2020-01-07/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```