---
name: "py-awkward1"
layout: package
next_package: musl
previous_package: lvarray
languages: []
---
## 0.3.1
2 / 542 files match

 - [src/libawkward/kernel-dispatch.cpp](#srclibawkwardkernel-dispatchcpp)
 - [src/python/startup.cpp](#srcpythonstartupcpp)

### src/libawkward/kernel-dispatch.cpp

```

{% raw %}
41 |         auto handle = dlopen(i->library_path().c_str(), RTLD_LAZY);
55 |         handle = dlopen(path.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/python/startup.cpp

```

{% raw %}
32 |   // be handled by the dlopen and dlsym in the C++ layer.
{% endraw %}

```