---
name: "exodusii"
layout: package
next_package: extrae
previous_package: exmcutils
languages: ['c']
---
## master
1 / 5313 files match, 1 filtered matches.

 - [packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C](#packagesseacaslibrariesiosssrcvisualizationiovs_databaseioc)

### packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C

```c

{% raw %}
236 |     }
237 | 
238 | #ifdef IOSS_DLOPEN_ENABLED
239 |     globalCatalystIossDlHandle = dlopen(plugin_library_path.c_str(), RTLD_NOW | RTLD_GLOBAL);
240 |     if (globalCatalystIossDlHandle == nullptr) {
241 |       throw std::runtime_error(dlerror());
{% endraw %}

```