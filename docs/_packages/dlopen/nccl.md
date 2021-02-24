---
name: "nccl"
layout: package
next_package: tfel
previous_package: root
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 2.8.3-1
4 / 121 files match, 3 filtered matches.

 - [src/init.cc](#srcinitcc)
 - [src/misc/ibvwrap.cc](#srcmiscibvwrapcc)
 - [src/misc/nvmlwrap.cc](#srcmiscnvmlwrapcc)

### src/init.cc

```cpp

{% raw %}
65 | }
66 | 
67 | ncclResult_t initNetPlugin(ncclNet_t** net, ncclCollNet_t** collnet) {
68 |   void* netPluginLib = dlopen("libnccl-net.so", RTLD_NOW | RTLD_LOCAL);
69 |   if (netPluginLib == NULL) {
70 |     // dlopen does not guarantee to set errno, but dlerror only gives us a
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
41 |   void* tmp;
42 |   void** cast;
43 | 
44 |   nvmlhandle=dlopen("libnvidia-ml.so.1", RTLD_NOW);
45 |   if (!nvmlhandle) {
46 |     WARN("Failed to open libnvidia-ml.so.1");
{% endraw %}

```