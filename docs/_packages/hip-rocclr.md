---
name: "hip-rocclr"
layout: package
next_package: hpctoolkit
previous_package: hepmc3
languages: ['c']
---
## 3.5.0
7 / 508 files match, 2 filtered matches.

 - [elf/utils/common/elfdefinitions.h](#elfutilscommonelfdefinitionsh)
 - [opencl-on-vdi/khronos/icd/loader/linux/icd_linux.c](#opencl-on-vdikhronosicdloaderlinuxicd_linuxc)

### elf/utils/common/elfdefinitions.h

```c

{% raw %}
303 | _ELF_DEFINE_DT(DT_MIPS_RLD_TEXT_RESOLVE_ADDR, 0x7000002DUL,		\
304 | 	"address of _rld_text_resolve in GOT")				\
305 | _ELF_DEFINE_DT(DT_MIPS_PERF_SUFFIX, 0x7000002EUL,			\
306 | 	"default suffix of DSO to be appended by dlopen")		\
307 | _ELF_DEFINE_DT(DT_MIPS_COMPACT_SIZE, 0x7000002FUL,			\
308 | 	"size of a ucode compact relocation record (o32)")		\
{% endraw %}

```
### opencl-on-vdi/khronos/icd/loader/linux/icd_linux.c

```c

{% raw %}
157 | // dynamically load a library.  returns NULL on failure
158 | void *khrIcdOsLibraryLoad(const char *libraryName)
159 | {
160 |     return dlopen (libraryName, RTLD_NOW);
161 | }
162 | 
{% endraw %}

```