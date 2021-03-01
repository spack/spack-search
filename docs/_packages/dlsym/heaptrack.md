---
name: "heaptrack"
layout: package
next_package: hpctoolkit
previous_package: hashcat
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.0
3 / 147 files match, 1 filtered matches.

 - [src/track/heaptrack_api.h](#srctrackheaptrack_apih)

### src/track/heaptrack_api.h

```c

{% raw %}
109 | {
110 |     static int initialized = 0;
111 |     if (!initialized) {
112 |         void* sym = dlsym(RTLD_NEXT, "heaptrack_malloc");
113 |         if (sym)
114 |             heaptrack_api.malloc = (void (*)(void*, size_t))sym;
115 | 
116 |         sym = dlsym(RTLD_NEXT, "heaptrack_realloc");
117 |         if (sym)
118 |             heaptrack_api.realloc = (void (*)(void*, size_t, void*))sym;
119 | 
120 |         sym = dlsym(RTLD_NEXT, "heaptrack_free");
121 |         if (sym)
122 |             heaptrack_api.free = (void (*)(void*))sym;
{% endraw %}

```