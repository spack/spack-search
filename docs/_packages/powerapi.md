---
name: "powerapi"
layout: package
next_package: ncbi-rmblastn
previous_package: gtkmm
languages: ['cpp']
---
## 1.1.1
2 / 246 files match

 - [src/pwr/pluginMeta.h](#srcpwrpluginmetah)
 - [src/pwr/dynamic.cc](#srcpwrdynamiccc)

### src/pwr/pluginMeta.h

```cpp

{% raw %}
28 |     	void* m_lib = dlopen( libName.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/pwr/dynamic.cc

```cpp

{% raw %}
24 |     void* ptr = dlopen( lib.c_str(), RTLD_LAZY);
{% endraw %}

```