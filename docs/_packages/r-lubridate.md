---
name: "r-lubridate"
layout: package
next_package: r-rcppcctz
previous_package: r-lpsolve
languages: ['cpp']
---
## 1.7.9.2
1 / 198 files match, 1 filtered matches.

 - [src/cctz/src/time_zone_lookup.cc](#srccctzsrctime_zone_lookupcc)

### src/cctz/src/time_zone_lookup.cc

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