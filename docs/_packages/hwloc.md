---
name: "hwloc"
layout: package
next_package: hydra
previous_package: hunspell
languages: ['c']
---
## 1.11.6
11 / 1080 files match, 2 filtered matches.

 - [src/components.c](#srccomponentsc)
 - [include/hwloc/plugins.h](#includehwlocpluginsh)

### src/components.c

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
### include/hwloc/plugins.h

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