---
name: "abseil-cpp"
layout: package
next_package: rocprofiler-dev
previous_package: jasper
languages: ['cpp']
---
## 20200923.1
3 / 689 files match, 2 filtered matches.

 - [absl/random/internal/randen_detect.cc](#abslrandominternalranden_detectcc)
 - [absl/time/internal/cctz/src/time_zone_lookup.cc](#absltimeinternalcctzsrctime_zone_lookupcc)

### absl/random/internal/randen_detect.cc

```cpp

{% raw %}
78 |   dlerror();  // Cleaning error state before calling dlopen.
79 |   void* libc_handle = dlopen("libc.so", RTLD_NOW);
{% endraw %}

```
### absl/time/internal/cctz/src/time_zone_lookup.cc

```cpp

{% raw %}
55 |   if (void* handle = dlopen("libc.so", flag)) {
{% endraw %}

```