---
name: "embree"
layout: package
next_package: nbdkit
previous_package: py-mysqlclient
languages: []
---
## 3.7.0
1 / 1017 files match

 - [common/sys/library.cpp](#commonsyslibrarycpp)

### common/sys/library.cpp

```

{% raw %}
70 |     void* lib = dlopen(fullName.c_str(), RTLD_NOW);
73 |     lib = dlopen((executable.path() + fullName).c_str(),RTLD_NOW);
{% endraw %}

```