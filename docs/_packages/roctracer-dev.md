---
name: "roctracer-dev"
layout: package
next_package: lzo
previous_package: py-packaging
languages: ['cpp']
---
## 3.10.0
2 / 71 files match

 - [src/util/hsa_rsrc_factory.cpp](#srcutilhsa_rsrc_factorycpp)
 - [src/core/loader.h](#srccoreloaderh)

### src/util/hsa_rsrc_factory.cpp

```

{% raw %}
257 |   void* handle = dlopen(kAqlProfileLib, RTLD_NOW);
{% endraw %}

```
### src/core/loader.h

```cpp

{% raw %}
55 |     handle_ = dlopen(lib_name_, flags);
{% endraw %}

```