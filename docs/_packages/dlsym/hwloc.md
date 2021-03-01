---
name: "hwloc"
layout: package
next_package: imagemagick
previous_package: hpctoolkit
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.11.6
5 / 1080 files match, 2 filtered matches.

 - [src/components.c](#srccomponentsc)
 - [include/hwloc/plugins.h](#includehwlocpluginsh)

### src/components.c

```c

{% raw %}
105 |   }
106 |   componentsymbolname = malloc(strlen(basename)+10+1);
107 |   sprintf(componentsymbolname, "%s_component", basename);
108 |   component = lt_dlsym(handle, componentsymbolname);
109 |   if (!component) {
110 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### include/hwloc/plugins.h

```c

{% raw %}
371 |   if (!handle)
372 |     /* cannot check, assume things will work */
373 |     return 0;
374 |   sym = lt_dlsym(handle, symbol);
375 |   lt_dlclose(handle);
376 |   if (!sym) {
{% endraw %}

```