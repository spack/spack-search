---
name: "bloaty"
layout: package
next_package: xcb-util
previous_package: zfp
languages: ['cpp']
---
## 1.1
5 / 1641 files match

 - [third_party/abseil-cpp/absl/random/internal/randen_detect.cc](#third_partyabseil-cppabslrandominternalranden_detectcc)
 - [third_party/abseil-cpp/absl/time/internal/cctz/src/time_zone_lookup.cc](#third_partyabseil-cppabsltimeinternalcctzsrctime_zone_lookupcc)

### third_party/abseil-cpp/absl/random/internal/randen_detect.cc

```cpp

{% raw %}
78 |   dlerror();  // Cleaning error state before calling dlopen.
79 |   void* libc_handle = dlopen("libc.so", RTLD_NOW);
{% endraw %}

```
### third_party/abseil-cpp/absl/time/internal/cctz/src/time_zone_lookup.cc

```cpp

{% raw %}
52 |   if (void* handle = dlopen("libc.so", flag)) {
{% endraw %}

```