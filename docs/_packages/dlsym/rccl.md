---
name: "rccl"
layout: package
next_package: scr
previous_package: gpgme
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 3.7.0
2 / 193 files match, 2 filtered matches.

 - [src/init.cc](#srcinitcc)
 - [src/misc/nvmlwrap.cc](#srcmiscnvmlwrapcc)

### src/init.cc

```cpp

{% raw %}
81 |     }
82 |     return ncclSuccess;
83 |   }
84 |   ncclNet_t* extNet = (ncclNet_t*) dlsym(netPluginLib, STR(NCCL_PLUGIN_SYMBOL));
85 |   if (extNet == NULL) {
86 |     INFO(NCCL_INIT|NCCL_NET, "NET/Plugin: Failed to find " STR(NCCL_PLUGIN_SYMBOL) " symbol.");
87 |   } else if (initNet(extNet) == ncclSuccess) {
88 |     *net = extNet;
89 |     // Check for CollNet
90 |     ncclCollNet_t* extCollNet = (ncclCollNet_t*) dlsym(netPluginLib, STR(NCCL_COLLNET_PLUGIN_SYMBOL));
91 |     if (extCollNet == NULL) {
92 |       INFO(NCCL_INIT|NCCL_NET, "NET/Plugin: Failed to find " STR(NCCL_COLLNET_PLUGIN_SYMBOL) " symbol.");
{% endraw %}

```
### src/misc/nvmlwrap.cc

```cpp

{% raw %}
52 | 
53 | #define LOAD_SYM(handle, symbol, funcptr) do {         \
54 |     cast = (void**)&funcptr;                             \
55 |     tmp = dlsym(handle, symbol);                         \
56 |     if (tmp == NULL) {                                   \
57 |       WARN("dlsym failed on %s - %s", symbol, dlerror());\
58 |       goto teardown;                                     \
59 |     }                                                    \
62 | 
63 | #define LOAD_SYM_OPTIONAL(handle, symbol, funcptr) do {\
64 |     cast = (void**)&funcptr;                             \
65 |     tmp = dlsym(handle, symbol);                         \
66 |     if (tmp == NULL) {                                   \
67 |       INFO(NCCL_INIT,"dlsym failed on %s, ignoring", symbol); \
68 |     }                                                    \
69 |     *cast = tmp;                                         \
{% endraw %}

```