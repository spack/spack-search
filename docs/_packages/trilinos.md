---
name: "trilinos"
layout: package
next_package: tulip
previous_package: treelite
languages: ['c']
---
## xsdk-0.2.0
8 / 46265 files match, 1 filtered matches.

 - [packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C](#packagesseacaslibrariesiosssrcvisualizationiovs_databaseioc)

### packages/seacas/libraries/ioss/src/visualization/Iovs_DatabaseIO.C

```c

{% raw %}
265 |           //for glew in paraview 5
266 |           //
267 | #ifdef SIERRA_DLOPEN_ENABLED
268 |           void *dl = dlopen(plugin_library_path.c_str(), RTLD_NOW | RTLD_GLOBAL);
269 |           if (!dl) {
270 |             throw std::runtime_error(dlerror());
{% endraw %}

```