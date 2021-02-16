---
name: "seacas"
layout: package
next_package: libapplewm
previous_package: lua-luajit
languages: ['c']
---
## master
1 / 5313 files match, 1 filtered matches.

 - [packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C](#packagesseacaslibrariesiosssrcvisualizationiovs_databaseioc)

### packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C

```c

{% raw %}
239 |     globalCatalystIossDlHandle = dlopen(plugin_library_path.c_str(), RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```