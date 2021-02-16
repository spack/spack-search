---
name: "py-grpcio"
layout: package
next_package: vim
previous_package: cntk
languages: ['cpp']
---
## 1.30.0
3 / 2788 files match

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
55 |   if (void* handle = dlopen("libc.so", flag)) {
{% endraw %}

```