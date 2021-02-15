---
name: "ermod"
layout: package
next_package: emacs
previous_package: libcroco
languages: ['cpp']
---
## 0.3.6
2 / 138 files match

 - [vmdfio.c](#vmdfioc)
 - [vmdplugins/vmdplugin.h](#vmdpluginsvmdpluginh)

### vmdfio.c

```cpp

{% raw %}
156 | 	handle = dlopen(pluginpath, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### vmdplugins/vmdplugin.h

```cpp

{% raw %}
49 |  *  and fini routines via dlopen() or similar operating system interfaces.
178 |  * This API is optional; if found by dlopen, it will be called after first
{% endraw %}

```