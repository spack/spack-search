---
name: "kallisto"
layout: package
next_package: libxrender
previous_package: nanoflann
languages: ['cpp']
---
## 0.46.2
3 / 270 files match

 - [ext/htslib/configure.ac](#exthtslibconfigureac)
 - [ext/htslib/plugin.c](#exthtslibpluginc)
 - [ext/htslib/hfile_internal.h](#exthtslibhfile_internalh)

### ext/htslib/configure.ac

```

{% raw %}
144 |   AC_SEARCH_LIBS([dlopen], [dl], [],
145 |     [AC_MSG_ERROR([dlopen() not found
152 |   case "$ac_cv_search_dlopen" in
153 |     -l*) static_LIBS="$static_LIBS $ac_cv_search_dlopen" ;;
{% endraw %}

```
### ext/htslib/plugin.c

```cpp

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### ext/htslib/hfile_internal.h

```cpp

{% raw %}
122 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```