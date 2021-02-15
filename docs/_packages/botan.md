---
name: "botan"
layout: package
next_package: zookeeper
previous_package: exmcutils
languages: []
---
## 2.14.0
2 / 2721 files match

 - [src/lib/utils/dyn_load/dyn_load.cpp](#srclibutilsdyn_loaddyn_loadcpp)
 - [doc/old_news.rst](#docold_newsrst)

### src/lib/utils/dyn_load/dyn_load.cpp

```

{% raw %}
39 |    m_lib = ::dlopen(m_lib_name.c_str(), RTLD_LAZY);
{% endraw %}

```
### doc/old_news.rst

```

{% raw %}
2533 |   added. Currently only system that use ``dlopen``-style dynamic
{% endraw %}

```