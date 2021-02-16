---
name: "charmpp"
layout: package
next_package: py-pysam
previous_package: py-exodus-bundler
languages: ['c']
---
## 6.9.0
15 / 4475 files match, 4 filtered matches.

 - [src/util/ckdll_dlopen.C](#srcutilckdll_dlopenc)
 - [tests/ampi/privatization/test-cxx.C](#testsampiprivatizationtest-cxxc)
 - [contrib/hwloc/src/components.c](#contribhwlocsrccomponentsc)
 - [contrib/hwloc/include/hwloc/plugins.h](#contribhwlocincludehwlocpluginsh)

### src/util/ckdll_dlopen.C

```c

{% raw %}
1 |  dlopen version of CkDll class.  
11 | 	handle=dlopen(name,RTLD_NOW);
{% endraw %}

```
### tests/ampi/privatization/test-cxx.C

```c

{% raw %}
61 |   void * dynamiclib = dlopen("libcxx-" privatization_method_str "-shared-library-dynamic.so", RTLD_NOW);
64 |     fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### contrib/hwloc/src/components.c

```c

{% raw %}
100 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### contrib/hwloc/include/hwloc/plugins.h

```c

{% raw %}
370 |   handle = lt_dlopen(NULL);
{% endraw %}

```