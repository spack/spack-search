---
name: "py-grpcio"
layout: package
next_package: py-jedi
previous_package: py-gevent
languages: ['cpp']
---
## 1.30.0
3 / 2788 files match, 2 filtered matches.

 - [third_party/abseil-cpp/absl/random/internal/randen_detect.cc](#third_partyabseil-cppabslrandominternalranden_detectcc)
 - [third_party/abseil-cpp/absl/time/internal/cctz/src/time_zone_lookup.cc](#third_partyabseil-cppabsltimeinternalcctzsrctime_zone_lookupcc)

### third_party/abseil-cpp/absl/random/internal/randen_detect.cc

```cpp

{% raw %}
75 |   // NOLINTNEXTLINE(runtime/int)
76 |   typedef unsigned long (*getauxval_func_t)(unsigned long);
77 | 
78 |   dlerror();  // Cleaning error state before calling dlopen.
79 |   void* libc_handle = dlopen("libc.so", RTLD_NOW);
80 |   if (!libc_handle) {
81 |     return 0;
{% endraw %}

```
### third_party/abseil-cpp/absl/time/internal/cctz/src/time_zone_lookup.cc

```cpp

{% raw %}
52 | #if defined(RTLD_NOLOAD)
53 |   flag |= RTLD_NOLOAD;  // libc.so should already be resident
54 | #endif
55 |   if (void* handle = dlopen("libc.so", flag)) {
56 |     void* sym = dlsym(handle, "__system_property_get");
57 |     dlclose(handle);
{% endraw %}

```