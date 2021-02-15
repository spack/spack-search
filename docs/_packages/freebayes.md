---
name: "freebayes"
layout: package
next_package: libidn2
previous_package: openloops
languages: ['cpp']
---
## 1.1.0
6 / 1663 files match

 - [SeqLib/htslib/configure.ac](#seqlibhtslibconfigureac)
 - [SeqLib/htslib/plugin.c](#seqlibhtslibpluginc)
 - [SeqLib/htslib/hfile_internal.h](#seqlibhtslibhfile_internalh)
 - [vcflib/tabixpp/htslib/configure.ac](#vcflibtabixpphtslibconfigureac)
 - [vcflib/tabixpp/htslib/plugin.c](#vcflibtabixpphtslibpluginc)
 - [vcflib/tabixpp/htslib/hfile_internal.h](#vcflibtabixpphtslibhfile_internalh)

### SeqLib/htslib/configure.ac

```

{% raw %}
89 |   AC_SEARCH_LIBS([dlopen], [dl], [],
90 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### SeqLib/htslib/plugin.c

```cpp

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### SeqLib/htslib/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```
### vcflib/tabixpp/htslib/configure.ac

```

{% raw %}
89 |   AC_SEARCH_LIBS([dlopen], [dl], [],
90 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### vcflib/tabixpp/htslib/plugin.c

```cpp

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### vcflib/tabixpp/htslib/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```