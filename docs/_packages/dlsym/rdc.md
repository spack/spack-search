---
name: "rdc"
layout: package
next_package: recorder
previous_package: rccl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.0.0
1 / 444 files match, 1 filtered matches.

 - [include/rdc_lib/RdcLibraryLoader.h](#includerdc_librdclibraryloaderh)

### include/rdc_lib/RdcLibraryLoader.h

```c

{% raw %}
66 |     std::lock_guard<std::mutex> guard(library_mutex_);
67 | 
68 |     *reinterpret_cast<void**>(func_handler) =
69 |             dlsym(libHandler_, func_name);
70 |     if (*func_handler == nullptr) {
71 |         char* error = dlerror();
{% endraw %}

```