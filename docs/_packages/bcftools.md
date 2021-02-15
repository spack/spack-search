---
name: "bcftools"
layout: package
next_package: libunwind
previous_package: pangolin
languages: ['cpp']
---
## 1.9
5 / 1127 files match

 - [configure.ac](#configureac)
 - [vcfplugin.c](#vcfpluginc)
 - [htslib-1.9/configure.ac](#htslib-19configureac)
 - [htslib-1.9/plugin.c](#htslib-19pluginc)
 - [htslib-1.9/hfile_internal.h](#htslib-19hfile_internalh)

### configure.ac

```

{% raw %}
141 |   AC_SEARCH_LIBS([dlopen], [dl], [],
142 |     [AC_MSG_ERROR([dlopen() not found
{% endraw %}

```
### vcfplugin.c

```cpp

{% raw %}
203 | static void *dlopen_plugin(args_t *args, const char *fname)
215 |             handle = dlopen(tmp, RTLD_NOW); // valgrind complains about unfreed memory, not our problem though
218 |                 if ( !handle ) fprintf(stderr,"%s:\n\tdlopen   .. %s\n", tmp,dlerror());
219 |                 else fprintf(stderr,"%s:\n\tdlopen   .. ok\n", tmp);
226 |     handle = dlopen(fname, RTLD_NOW);
229 |         if ( !handle ) fprintf(stderr,"%s:\n\tdlopen   .. %s\n", fname,dlerror());
230 |         else fprintf(stderr,"%s:\n\tdlopen   .. ok\n", fname);
255 |     plugin->handle = dlopen_plugin(args, fname);
{% endraw %}

```
### htslib-1.9/configure.ac

```

{% raw %}
177 |   AC_SEARCH_LIBS([dlopen], [dl], [],
178 |     [MSG_ERROR([dlopen() not found
185 |   case "$ac_cv_search_dlopen" in
186 |     -l*) static_LIBS="$static_LIBS $ac_cv_search_dlopen" ;;
{% endraw %}

```
### htslib-1.9/plugin.c

```cpp

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### htslib-1.9/hfile_internal.h

```cpp

{% raw %}
145 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```