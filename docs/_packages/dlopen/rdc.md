---
name: "rdc"
layout: package
next_package: sandbox
previous_package: keyutils
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 4.0.0
1 / 444 files match, 1 filtered matches.

 - [rdc_libs/bootstrap/src/RdcLibraryLoader.cc](#rdc_libsbootstrapsrcrdclibraryloadercc)

### rdc_libs/bootstrap/src/RdcLibraryLoader.cc

```cpp

{% raw %}
36 |     }
37 | 
38 |     std::lock_guard<std::mutex> guard(library_mutex_);
39 |     libHandler_ = dlopen(filename, RTLD_LAZY);
40 |     if (!libHandler_) {
41 |         char* error = dlerror();
{% endraw %}

```