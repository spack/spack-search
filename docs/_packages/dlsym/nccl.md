---
name: "nccl"
layout: package
next_package: ncl
previous_package: nbdkit
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 2.8.3-1
3 / 121 files match, 2 filtered matches.

 - [src/init.cc](#srcinitcc)
 - [src/misc/nvmlwrap.cc](#srcmiscnvmlwrapcc)

### src/init.cc

```cpp

{% raw %}
77 |     }
78 |     return ncclSuccess;
79 |   }
80 |   ncclNet_t* extNet = (ncclNet_t*) dlsym(netPluginLib, STR(NCCL_PLUGIN_SYMBOL));
81 |   if (extNet == NULL) {
82 |     INFO(NCCL_INIT|NCCL_NET, "NET/Plugin: Failed to find " STR(NCCL_PLUGIN_SYMBOL) " symbol.");
83 |   } else if (initNet(extNet) == ncclSuccess) {
84 |     *net = extNet;
85 |     // Check for CollNet
86 |     ncclCollNet_t* extCollNet = (ncclCollNet_t*) dlsym(netPluginLib, STR(NCCL_COLLNET_PLUGIN_SYMBOL));
87 |     if (extCollNet == NULL) {
88 |       INFO(NCCL_INIT|NCCL_NET, "NET/Plugin: Failed to find " STR(NCCL_COLLNET_PLUGIN_SYMBOL) " symbol.");
{% endraw %}

```
### src/misc/nvmlwrap.cc

```cpp

{% raw %}
49 | 
50 | #define LOAD_SYM(handle, symbol, funcptr) do {         \
51 |     cast = (void**)&funcptr;                             \
52 |     tmp = dlsym(handle, symbol);                         \
53 |     if (tmp == NULL) {                                   \
54 |       WARN("dlsym failed on %s - %s", symbol, dlerror());\
55 |       goto teardown;                                     \
56 |     }                                                    \
59 | 
60 | #define LOAD_SYM_OPTIONAL(handle, symbol, funcptr) do {\
61 |     cast = (void**)&funcptr;                             \
62 |     tmp = dlsym(handle, symbol);                         \
63 |     if (tmp == NULL) {                                   \
64 |       INFO(NCCL_INIT,"dlsym failed on %s, ignoring", symbol); \
65 |     }                                                    \
66 |     *cast = tmp;                                         \
{% endraw %}

```