---
name: "scorep"
layout: package
next_package: seacas
previous_package: scalpel
languages: ['c']
---
## 1.3
12 / 1990 files match, 2 filtered matches.

 - [src/services/metric/scorep_metric_plugins.c](#srcservicesmetricscorep_metric_pluginsc)
 - [src/measurement/SCOREP_Libwrap.c](#srcmeasurementscorep_libwrapc)

### src/services/metric/scorep_metric_plugins.c

```c

{% raw %}
311 |             handle = dlopen( buffer, RTLD_NOW );
{% endraw %}

```
### src/measurement/SCOREP_Libwrap.c

```c

{% raw %}
139 |             ( *handle )->shared_lib_handles[ i ] = dlopen( ( *handle )->attributes->shared_libs[ i ], RTLD_LAZY | RTLD_LOCAL );
{% endraw %}

```