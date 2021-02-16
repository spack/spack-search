---
name: "powerapi"
layout: package
next_package: premake-core
previous_package: postgresql
languages: ['cpp', 'c']
---
## 1.1.1
2 / 246 files match, 2 filtered matches.

 - [src/pwr/pluginMeta.h](#srcpwrpluginmetah)
 - [src/pwr/dynamic.cc](#srcpwrdynamiccc)

### src/pwr/pluginMeta.h

```c

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