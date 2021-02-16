---
name: "thepeg"
layout: package
next_package: libssh
previous_package: care
languages: ['cpp']
---
## 2.2.1
7 / 917 files match, 1 filtered matches.

 - [Utilities/DynamicLoader.cc](#utilitiesdynamicloadercc)

### Utilities/DynamicLoader.cc

```cpp

{% raw %}
76 |   bool ret = dlopen(file.c_str(), RTLD_LAZY|RTLD_GLOBAL) != 0;
{% endraw %}

```