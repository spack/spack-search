---
name: "hydra"
layout: package
next_package: hyphy
previous_package: hwloc
languages: ['c']
---
## 3.2
14 / 770 files match, 2 filtered matches.

 - [tools/topo/hwloc/hwloc/src/components.c](#toolstopohwlochwlocsrccomponentsc)
 - [tools/topo/hwloc/hwloc/include/hwloc/plugins.h](#toolstopohwlochwlocincludehwlocpluginsh)

### tools/topo/hwloc/hwloc/src/components.c

```c

{% raw %}
89 |     basename++;
90 | 
91 |   /* dlopen and get the component structure */
92 |   handle = lt_dlopenext(filename);
93 |   if (!handle) {
94 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### tools/topo/hwloc/hwloc/include/hwloc/plugins.h

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