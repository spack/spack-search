---
name: "r-rcppcctz"
layout: package
next_package: r-rgraphviz
previous_package: r-lubridate
languages: ['cpp']
---
## 0.2.6
1 / 40 files match, 1 filtered matches.

 - [src/time_zone_lookup.cc](#srctime_zone_lookupcc)

### src/time_zone_lookup.cc

```cpp

{% raw %}
47 | #if defined(RTLD_NOLOAD)
48 |   flag |= RTLD_NOLOAD;  // libc.so should already be resident
49 | #endif
50 |   if (void* handle = dlopen("libc.so", flag)) {
51 |     void* sym = dlsym(handle, "__system_property_get");
52 |     dlclose(handle);
{% endraw %}

```