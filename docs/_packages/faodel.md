---
name: "faodel"
layout: package
next_package: aml
previous_package: faust
languages: ['cpp']
---
## 1.1906.1
3 / 1101 files match

 - [tpl/gperftools/src/heap-checker.cc](#tplgperftoolssrcheap-checkercc)
 - [tpl/gperftools/src/thread_cache.h](#tplgperftoolssrcthread_cacheh)
 - [tpl/gperftools/src/base/elf_mem_image.cc](#tplgperftoolssrcbaseelf_mem_imagecc)

### tpl/gperftools/src/heap-checker.cc

```cpp

{% raw %}
444 | // the cost you can't dlopen this library.  But dlopen on heap-checker
{% endraw %}

```
### tpl/gperftools/src/thread_cache.h

```cpp

{% raw %}
274 |   // you cannot dlopen this library.  (To see the difference, look at
276 |   // Since we don't really use dlopen in google code -- and using dlopen
{% endraw %}

```
### tpl/gperftools/src/base/elf_mem_image.cc

```cpp

{% raw %}
262 |       // "fake" dlopen()ed vdso library, the loader relocates some (but
{% endraw %}

```