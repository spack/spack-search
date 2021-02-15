---
name: "bedtools2"
layout: package
next_package: sst-core
previous_package: jags
languages: ['cpp']
---
## 2.29.2
3 / 1042 files match

 - [src/utils/htslib/configure.ac](#srcutilshtslibconfigureac)
 - [src/utils/htslib/plugin.c](#srcutilshtslibpluginc)
 - [src/utils/htslib/hfile_internal.h](#srcutilshtslibhfile_internalh)

### src/utils/htslib/configure.ac

```

{% raw %}
177 |   AC_SEARCH_LIBS([dlopen], [dl], [],
178 |     [MSG_ERROR([dlopen() not found
185 |   case "$ac_cv_search_dlopen" in
186 |     -l*) static_LIBS="$static_LIBS $ac_cv_search_dlopen" ;;
{% endraw %}

```
### src/utils/htslib/plugin.c

```cpp

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/utils/htslib/hfile_internal.h

```cpp

{% raw %}
145 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```