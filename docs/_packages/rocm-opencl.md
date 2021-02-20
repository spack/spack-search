---
name: "rocm-opencl"
layout: package
next_package: rocm-openmp-extras
previous_package: rocm-gdb
languages: ['c']
---
## 3.10.0
3 / 491 files match, 1 filtered matches.

 - [khronos/icd/loader/linux/icd_linux.c](#khronosicdloaderlinuxicd_linuxc)

### khronos/icd/loader/linux/icd_linux.c

```c

{% raw %}
157 | // dynamically load a library.  returns NULL on failure
158 | void *khrIcdOsLibraryLoad(const char *libraryName)
159 | {
160 |     void *retVal = dlopen (libraryName, RTLD_NOW);
161 | 
162 |     if (NULL == retVal) {
{% endraw %}

```