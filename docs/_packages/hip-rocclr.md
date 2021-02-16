---
name: "hip-rocclr"
layout: package
next_package: qcachegrind
previous_package: gnutls
languages: ['c']
---
## 3.5.0
7 / 508 files match, 2 filtered matches.

 - [elf/utils/common/elfdefinitions.h](#elfutilscommonelfdefinitionsh)
 - [opencl-on-vdi/khronos/icd/loader/linux/icd_linux.c](#opencl-on-vdikhronosicdloaderlinuxicd_linuxc)

### elf/utils/common/elfdefinitions.h

```c

{% raw %}
306 | 	"default suffix of DSO to be appended by dlopen")		\
{% endraw %}

```
### opencl-on-vdi/khronos/icd/loader/linux/icd_linux.c

```c

{% raw %}
160 |     return dlopen (libraryName, RTLD_NOW);
{% endraw %}

```