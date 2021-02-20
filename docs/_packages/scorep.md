---
name: "scorep"
layout: package
next_package: sdl2
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
308 |              * RTLD_NOW: all undefined symbols in the library are resolved
309 |              *           before dlopen() returns, if this cannot be done,
310 |              *           an error is returned. */
311 |             handle = dlopen( buffer, RTLD_NOW );
312 | 
313 |             /* If it is not valid */
{% endraw %}

```
### src/measurement/SCOREP_Libwrap.c

```c

{% raw %}
136 | 
137 |         for ( int i = 0; i < ( *handle )->attributes->number_of_shared_libs; i++ )
138 |         {
139 |             ( *handle )->shared_lib_handles[ i ] = dlopen( ( *handle )->attributes->shared_libs[ i ], RTLD_LAZY | RTLD_LOCAL );
140 |             if ( ( *handle )->shared_lib_handles[ i ] == NULL )
141 |             {
{% endraw %}

```