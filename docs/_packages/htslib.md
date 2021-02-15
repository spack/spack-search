---
name: "htslib"
layout: package
next_package: glusterfs
previous_package: cityhash
languages: ['cpp']
---
## 1.4
3 / 199 files match

 - [configure.ac](#configureac)
 - [plugin.c](#pluginc)
 - [hfile_internal.h](#hfile_internalh)

### configure.ac

```

{% raw %}
144 |   AC_SEARCH_LIBS([dlopen], [dl], [],
145 |     [AC_MSG_ERROR([dlopen() not found
152 |   case "$ac_cv_search_dlopen" in
153 |     -l*) static_LIBS="$static_LIBS $ac_cv_search_dlopen" ;;
{% endraw %}

```
### plugin.c

```cpp

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### hfile_internal.h

```cpp

{% raw %}
122 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```