---
name: "breseq"
layout: package
next_package: ncbi-magicblast
previous_package: opendx
languages: ['cpp']
---
## 0.33.2
3 / 866 files match

 - [extern/samtools-1.3.1/htslib-1.3.1/configure.ac](#externsamtools-131htslib-131configureac)
 - [extern/samtools-1.3.1/htslib-1.3.1/plugin.c](#externsamtools-131htslib-131pluginc)
 - [extern/samtools-1.3.1/htslib-1.3.1/hfile_internal.h](#externsamtools-131htslib-131hfile_internalh)

### extern/samtools-1.3.1/htslib-1.3.1/configure.ac

```

{% raw %}
89 |   AC_SEARCH_LIBS([dlopen], [dl], [],
90 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### extern/samtools-1.3.1/htslib-1.3.1/plugin.c

```cpp

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### extern/samtools-1.3.1/htslib-1.3.1/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```