---
name: "rdc"
layout: package
next_package: rdma-core
previous_package: rccl
languages: ['cpp']
---
## 4.0.0
1 / 444 files match, 1 filtered matches.

 - [rdc_libs/bootstrap/src/RdcLibraryLoader.cc](#rdc_libsbootstrapsrcrdclibraryloadercc)

### rdc_libs/bootstrap/src/RdcLibraryLoader.cc

```cpp

{% raw %}
39 |     libHandler_ = dlopen(filename, RTLD_LAZY);
{% endraw %}

```