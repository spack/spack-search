---
name: "hpx5"
layout: package
next_package: hsakmt-roct
previous_package: hpctoolkit
languages: ['c']
---
## 2.2.0
14 / 2138 files match, 2 filtered matches.

 - [contrib/hwloc-1.11.0/src/components.c](#contribhwloc-1110srccomponentsc)
 - [contrib/hwloc-1.11.0/include/hwloc/plugins.h](#contribhwloc-1110includehwlocpluginsh)

### contrib/hwloc-1.11.0/src/components.c

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
### contrib/hwloc-1.11.0/include/hwloc/plugins.h

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