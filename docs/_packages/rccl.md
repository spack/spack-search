---
name: "rccl"
layout: package
next_package: virtualgl
previous_package: rivet
languages: ['cpp']
---
## 3.7.0
3 / 193 files match

 - [src/init.cc](#srcinitcc)
 - [src/misc/ibvwrap.cc](#srcmiscibvwrapcc)
 - [src/misc/nvmlwrap.cc](#srcmiscnvmlwrapcc)

### src/init.cc

```cpp

{% raw %}
72 |   void* netPluginLib = dlopen("libnccl-net.so", RTLD_NOW | RTLD_LOCAL);
74 |     // dlopen does not guarantee to set errno, but dlerror only gives us a
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