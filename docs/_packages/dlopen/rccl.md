---
name: "rccl"
layout: package
next_package: rdc
previous_package: r
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
69 | }
70 | 
71 | ncclResult_t initNetPlugin(ncclNet_t** net, ncclCollNet_t** collnet) {
72 |   void* netPluginLib = dlopen("libnccl-net.so", RTLD_NOW | RTLD_LOCAL);
73 |   if (netPluginLib == NULL) {
74 |     // dlopen does not guarantee to set errno, but dlerror only gives us a
{% endraw %}

```
### src/misc/ibvwrap.cc

```cpp

{% raw %}
55 |   void* tmp;
56 |   void** cast;
57 | 
58 |   ibvhandle=dlopen("libibverbs.so", RTLD_NOW);
59 |   if (!ibvhandle) {
60 |     ibvhandle=dlopen("libibverbs.so.1", RTLD_NOW);
61 |     if (!ibvhandle) {
62 |       WARN("Failed to open libibverbs.so[.1]");
{% endraw %}

```
### src/misc/nvmlwrap.cc

```cpp

{% raw %}
44 |   void* tmp;
45 |   void** cast;
46 | 
47 |   nvmlhandle=dlopen("libnvidia-ml.so.1", RTLD_NOW);
48 |   if (!nvmlhandle) {
49 |     WARN("Failed to open libnvidia-ml.so.1");
{% endraw %}

```