---
name: "libquo"
layout: package
next_package: librdkafka
previous_package: libpulsar
languages: ['c']
---
## master
7 / 308 files match, 2 filtered matches.

 - [src/hwloc/include/hwloc/plugins.h](#srchwlocincludehwlocpluginsh)
 - [src/hwloc/hwloc/components.c](#srchwlochwloccomponentsc)

### src/hwloc/include/hwloc/plugins.h

```c

{% raw %}
419 | #ifdef HWLOC_INSIDE_PLUGIN
420 |   lt_dlhandle handle;
421 |   void *sym;
422 |   handle = lt_dlopen(NULL);
423 |   if (!handle)
424 |     /* cannot check, assume things will work */
{% endraw %}

```
### src/hwloc/hwloc/components.c

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