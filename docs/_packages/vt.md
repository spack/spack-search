---
name: "vt"
layout: package
next_package: libhbaapi
previous_package: libxkbcommon
languages: ['cpp']
---
## 0.577
2 / 605 files match

 - [lib/htslib/configure.ac](#libhtslibconfigureac)
 - [lib/htslib/hfile_internal.h](#libhtslibhfile_internalh)

### lib/htslib/configure.ac

```

{% raw %}
87 |   AC_SEARCH_LIBS([dlopen], [dl], [],
88 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### lib/htslib/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```