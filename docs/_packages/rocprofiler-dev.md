---
name: "rocprofiler-dev"
layout: package
next_package: r-fs
previous_package: abseil-cpp
languages: ['cpp']
---
## 3.9.0
5 / 152 files match

 - [src/util/hsa_rsrc_factory.cpp](#srcutilhsa_rsrc_factorycpp)
 - [src/core/rocprofiler.cpp](#srccorerocprofilercpp)
 - [roctracer/src/util/hsa_rsrc_factory.cpp](#roctracersrcutilhsa_rsrc_factorycpp)
 - [roctracer/src/core/loader.h](#roctracersrccoreloaderh)
 - [test/util/hsa_rsrc_factory.cpp](#testutilhsa_rsrc_factorycpp)

### src/util/hsa_rsrc_factory.cpp

```

{% raw %}
273 |   void* handle = dlopen(kAqlProfileLib, RTLD_NOW);
{% endraw %}

```
### src/core/rocprofiler.cpp

```

{% raw %}
179 |     tool_handle = dlopen(tool_lib, RTLD_NOW);
{% endraw %}

```
### roctracer/src/util/hsa_rsrc_factory.cpp

```

{% raw %}
257 |   void* handle = dlopen(kAqlProfileLib, RTLD_NOW);
{% endraw %}

```
### roctracer/src/core/loader.h

```cpp

{% raw %}
55 |     handle_ = dlopen(lib_name_, flags);
{% endraw %}

```
### test/util/hsa_rsrc_factory.cpp

```

{% raw %}
268 |   void* handle = dlopen(kAqlProfileLib, RTLD_NOW);
{% endraw %}

```