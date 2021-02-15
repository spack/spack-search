---
name: "kaldi"
layout: package
next_package: coin3d
previous_package: libxv
languages: ['cpp']
---
## 2018-07-11
1 / 5620 files match

 - [src/cudamatrix/cu-device.cc](#srccudamatrixcu-devicecc)

### src/cudamatrix/cu-device.cc

```cpp

{% raw %}
471 |     void* libcuda = dlopen("libcuda.so",RTLD_LAZY);
515 |   void* libcuda = dlopen("libcuda.so",RTLD_LAZY);
{% endraw %}

```