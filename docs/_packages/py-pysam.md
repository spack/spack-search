---
name: "py-pysam"
layout: package
next_package: libxdamage
previous_package: charmpp
languages: ['cpp']
---
## 0.15.3
5 / 767 files match

 - [bcftools/vcfplugin.c](#bcftoolsvcfpluginc)
 - [bcftools/vcfplugin.c.pysam.c](#bcftoolsvcfplugincpysamc)
 - [htslib/configure.ac](#htslibconfigureac)
 - [htslib/plugin.c](#htslibpluginc)
 - [htslib/hfile_internal.h](#htslibhfile_internalh)

### bcftools/vcfplugin.c

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
### bcftools/vcfplugin.c.pysam.c

```cpp

{% raw %}
205 | static void *dlopen_plugin(args_t *args, const char *fname)
217 |             handle = dlopen(tmp, RTLD_NOW); // valgrind complains about unfreed memory, not our problem though
220 |                 if ( !handle ) fprintf(bcftools_stderr,"%s:\n\tdlopen   .. %s\n", tmp,dlerror());
221 |                 else fprintf(bcftools_stderr,"%s:\n\tdlopen   .. ok\n", tmp);
228 |     handle = dlopen(fname, RTLD_NOW);
231 |         if ( !handle ) fprintf(bcftools_stderr,"%s:\n\tdlopen   .. %s\n", fname,dlerror());
232 |         else fprintf(bcftools_stderr,"%s:\n\tdlopen   .. ok\n", fname);
257 |     plugin->handle = dlopen_plugin(args, fname);
{% endraw %}

```
### htslib/configure.ac

```

{% raw %}
177 |   AC_SEARCH_LIBS([dlopen], [dl], [],
178 |     [MSG_ERROR([dlopen() not found
185 |   case "$ac_cv_search_dlopen" in
186 |     -l*) static_LIBS="$static_LIBS $ac_cv_search_dlopen" ;;
{% endraw %}

```
### htslib/plugin.c

```cpp

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### htslib/hfile_internal.h

```cpp

{% raw %}
145 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```