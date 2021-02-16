---
name: "rocm-opencl"
layout: package
next_package: rocprofiler-dev
previous_package: rocm-gdb
languages: ['c']
---
## 3.10.0
3 / 491 files match, 1 filtered matches.

 - [khronos/icd/loader/linux/icd_linux.c](#khronosicdloaderlinuxicd_linuxc)

### khronos/icd/loader/linux/icd_linux.c

```c

{% raw %}
160 |     void *retVal = dlopen (libraryName, RTLD_NOW);
{% endraw %}

```