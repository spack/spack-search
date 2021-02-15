---
name: "samtools"
layout: package
next_package: cc65
previous_package: py-4suite-xml
languages: ['cpp']
---
## 1.3.1
3 / 530 files match

 - [htslib-1.3.1/configure.ac](#htslib-131configureac)
 - [htslib-1.3.1/plugin.c](#htslib-131pluginc)
 - [htslib-1.3.1/hfile_internal.h](#htslib-131hfile_internalh)

### htslib-1.3.1/configure.ac

```

{% raw %}
89 |   AC_SEARCH_LIBS([dlopen], [dl], [],
90 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### htslib-1.3.1/plugin.c

```cpp

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### htslib-1.3.1/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```