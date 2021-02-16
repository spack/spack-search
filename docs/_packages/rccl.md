---
name: "rccl"
layout: package
next_package: rdc
previous_package: r-rsqlite
languages: ['cpp']
---
## 3.7.0
3 / 193 files match, 3 filtered matches.

 - [src/init.cc](#srcinitcc)
 - [src/misc/ibvwrap.cc](#srcmiscibvwrapcc)
 - [src/misc/nvmlwrap.cc](#srcmiscnvmlwrapcc)

### src/init.cc

```cpp

{% raw %}
72 |   void* netPluginLib = dlopen("libnccl-net.so", RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### src/misc/ibvwrap.cc

```cpp

{% raw %}
58 |   ibvhandle=dlopen("libibverbs.so", RTLD_NOW);
60 |     ibvhandle=dlopen("libibverbs.so.1", RTLD_NOW);
{% endraw %}

```
### src/misc/nvmlwrap.cc

```cpp

{% raw %}
47 |   nvmlhandle=dlopen("libnvidia-ml.so.1", RTLD_NOW);
{% endraw %}

```