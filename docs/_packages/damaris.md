---
name: "damaris"
layout: package
next_package: fplll
previous_package: at-spi2-core
languages: []
---
## master
1 / 246 files match

 - [src/action/DynamicAction.cpp](#srcactiondynamicactioncpp)

### src/action/DynamicAction.cpp

```

{% raw %}
39 | 		handle_ = dlopen(NULL,RTLD_NOW | RTLD_GLOBAL);
41 | 		handle_ = dlopen(GetModel().library().c_str(), 
{% endraw %}

```