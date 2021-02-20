---
name: "abseil-cpp"
layout: package
next_package: ace
previous_package: 3proxy
languages: ['cpp']
---
## 20200923.1
3 / 689 files match, 2 filtered matches.

 - [absl/random/internal/randen_detect.cc](#abslrandominternalranden_detectcc)
 - [absl/time/internal/cctz/src/time_zone_lookup.cc](#absltimeinternalcctzsrctime_zone_lookupcc)

### absl/random/internal/randen_detect.cc

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
### absl/time/internal/cctz/src/time_zone_lookup.cc

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