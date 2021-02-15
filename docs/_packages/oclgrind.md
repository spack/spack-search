---
name: "oclgrind"
layout: package
next_package: oclint
previous_package: tixi
languages: []
---
## 19.10
2 / 360 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [src/core/Context.cpp](#srccorecontextcpp)

### CMakeLists.txt

```

{% raw %}
250 |   # Change the SONAME of the library so that it gets recognized by dlopen
{% endraw %}

```
### src/core/Context.cpp

```

{% raw %}
125 |       void *library = dlopen(libpath.c_str(), RTLD_NOW);
128 |         cerr << "Loading Oclgrind plugin failed (dlopen): "
{% endraw %}

```