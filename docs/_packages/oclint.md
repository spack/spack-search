---
name: "oclint"
layout: package
next_package: scalasca
previous_package: oclgrind
languages: []
---
## 0.13
2 / 320 files match

 - [oclint-driver/rules_dlfcn_port.cpp](#oclint-driverrules_dlfcn_portcpp)
 - [oclint-driver/reporters_dlfcn_port.cpp](#oclint-driverreporters_dlfcn_portcpp)

### oclint-driver/rules_dlfcn_port.cpp

```

{% raw %}
21 |             if (dlopen(rulePath.c_str(), RTLD_LAZY) == nullptr)
{% endraw %}

```
### oclint-driver/reporters_dlfcn_port.cpp

```

{% raw %}
26 |             void *reporterHandle = dlopen(reporterPath.c_str(), RTLD_LAZY);
{% endraw %}

```