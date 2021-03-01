---
name: "kaldi"
layout: package
next_package: kbd
previous_package: julia
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 2018-07-11
1 / 5620 files match, 1 filtered matches.

 - [src/cudamatrix/cu-device.cc](#srccudamatrixcu-devicecc)

### src/cudamatrix/cu-device.cc

```cpp

{% raw %}
476 |       // and get the symbol
477 | #if (CUDA_VERSION >= 3020)
478 |       typedef CUresult (*cu_fun_ptr)(size_t*, size_t*);
479 |       cu_fun_ptr dl_cuMemGetInfo = (cu_fun_ptr)dlsym(libcuda,"cuMemGetInfo_v2");
480 | #else
481 |       typedef CUresult (*cu_fun_ptr)(int*, int*);
482 |       cu_fun_ptr dl_cuMemGetInfo = (cu_fun_ptr)dlsym(libcuda,"cuMemGetInfo");
483 | #endif
484 |       if (NULL == dl_cuMemGetInfo) {
519 |     // define the function signature type
520 |     typedef CUresult (*cu_fun_ptr)(char*,int,CUdevice);
521 |     // get the symbol
522 |     cu_fun_ptr cuDeviceGetName_ptr = (cu_fun_ptr)dlsym(libcuda,"cuDeviceGetName");
523 |     if (NULL == cuDeviceGetName_ptr) {
524 |       KALDI_WARN << "cannot load cuDeviceGetName from libcuda.so";
{% endraw %}

```