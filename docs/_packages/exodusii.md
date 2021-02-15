---
name: "exodusii"
layout: package
next_package: viennarna
previous_package: gtkplus
languages: ['cpp']
---
## master
1 / 5313 files match

 - [packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C](#packagesseacaslibrariesiosssrcvisualizationiovs_databaseioc)

### packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C

```cpp

{% raw %}
36 | #ifdef IOSS_DLOPEN_ENABLED
189 | #ifdef IOSS_DLOPEN_ENABLED
238 | #ifdef IOSS_DLOPEN_ENABLED
239 |     globalCatalystIossDlHandle = dlopen(plugin_library_path.c_str(), RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```