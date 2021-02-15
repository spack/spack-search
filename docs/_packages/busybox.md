---
name: "busybox"
layout: package
next_package: m4
previous_package: mpip
languages: ['cpp']
---
## 1.30.0
1 / 2335 files match

 - [scripts/kconfig/kconfig_load.c](#scriptskconfigkconfig_loadc)

### scripts/kconfig/kconfig_load.c

```cpp

{% raw %}
15 | 	handle = dlopen("./libkconfig.so", RTLD_LAZY);
17 | 		handle = dlopen("./scripts/kconfig/libkconfig.so", RTLD_LAZY);
{% endraw %}

```