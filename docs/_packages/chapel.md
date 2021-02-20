---
name: "chapel"
layout: package
next_package: charmpp
previous_package: cdo
languages: ['c']
---
## 1.18.0
28 / 7639 files match, 3 filtered matches.

 - [third-party/massivethreads/massivethreads-src/src/myth_real.c](#third-partymassivethreadsmassivethreads-srcsrcmyth_realc)
 - [third-party/hwloc/hwloc-src/src/components.c](#third-partyhwlochwloc-srcsrccomponentsc)
 - [third-party/hwloc/hwloc-src/include/hwloc/plugins.h](#third-partyhwlochwloc-srcincludehwlocpluginsh)

### third-party/massivethreads/massivethreads-src/src/myth_real.c

```c

{% raw %}
514 |     if (!strstr(filename, s->file_pat)) continue;
515 |     if (!handle) {
516 |       dlerror();
517 |       handle = dlopen(filename, RTLD_LAZY | RTLD_NOLOAD);
518 |       /* could not open the file; quit */
519 |       if (!handle) return 0;
{% endraw %}

```
### third-party/hwloc/hwloc-src/src/components.c

```c

{% raw %}
97 |   }
98 | 
99 |   /* dlopen and get the component structure */
100 |   handle = lt_dlopenext(filename);
101 |   if (!handle) {
102 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### third-party/hwloc/hwloc-src/include/hwloc/plugins.h

```c

{% raw %}
367 | #ifdef HWLOC_INSIDE_PLUGIN
368 |   lt_dlhandle handle;
369 |   void *sym;
370 |   handle = lt_dlopen(NULL);
371 |   if (!handle)
372 |     /* cannot check, assume things will work */
{% endraw %}

```