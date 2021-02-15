---
name: "rsem"
layout: package
next_package: ispc
previous_package: oce
languages: ['cpp']
---
## 1.3.1
3 / 2717 files match

 - [samtools-1.3/htslib-1.3/configure.ac](#samtools-13htslib-13configureac)
 - [samtools-1.3/htslib-1.3/plugin.c](#samtools-13htslib-13pluginc)
 - [samtools-1.3/htslib-1.3/hfile_internal.h](#samtools-13htslib-13hfile_internalh)

### samtools-1.3/htslib-1.3/configure.ac

```

{% raw %}
87 |   AC_SEARCH_LIBS([dlopen], [dl], [],
88 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### samtools-1.3/htslib-1.3/plugin.c

```cpp

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### samtools-1.3/htslib-1.3/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```