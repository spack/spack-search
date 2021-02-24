---
name: "kaldi"
layout: package
next_package: multiverso
previous_package: emacs
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 2018-07-11
1 / 5620 files match, 1 filtered matches.

 - [src/cudamatrix/cu-device.cc](#srccudamatrixcu-devicecc)

### src/cudamatrix/cu-device.cc

```cpp

{% raw %}
468 |     // pre-fill ``safe'' values that will not cause problems
469 |     mem_free = 1; mem_total = 1;
470 |     // open libcuda.so
471 |     void* libcuda = dlopen("libcuda.so",RTLD_LAZY);
472 |     if (NULL == libcuda) {
473 |       KALDI_WARN << "cannot open libcuda.so";
512 |   cuDeviceGetName(name, len, dev);
513 | #else
514 |   // open libcuda.so
515 |   void* libcuda = dlopen("libcuda.so",RTLD_LAZY);
516 |   if (NULL == libcuda) {
517 |     KALDI_WARN << "cannot open libcuda.so";
{% endraw %}

```