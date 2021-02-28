---
name: "scorep"
layout: package
next_package: rccl
previous_package: php
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3
9 / 1990 files match, 2 filtered matches.

 - [src/services/metric/scorep_metric_plugins.c](#srcservicesmetricscorep_metric_pluginsc)
 - [src/measurement/SCOREP_Libwrap.c](#srcmeasurementscorep_libwrapc)

### src/services/metric/scorep_metric_plugins.c

```c

{% raw %}
323 |             /* Now get the address where the
324 |              * info symbol is loaded into memory */
325 |             snprintf( buffer, BUFFER_SIZE, "SCOREP_MetricPlugin_%s_get_info", current_plugin_name );
326 |             get_info.void_ptr = dlsym( handle, buffer );
327 |             dl_lib_error      = dlerror();
328 |             if ( dl_lib_error != NULL )
{% endraw %}

```
### src/measurement/SCOREP_Libwrap.c

```c

{% raw %}
178 | 
179 |         if ( !( *funcPtr ) )
180 |         {
181 |             char* dlsym_error_msg = dlerror();
182 |             if ( dlsym_error_msg != NULL )
183 |             {
184 |                 UTILS_ERROR( SCOREP_ERROR_DLSYM_FAILED, "dlsym( %s ), failed: %s", func, dlsym_error_msg );
185 |             }
186 |             else
187 |             {
188 |                 UTILS_ERROR( SCOREP_ERROR_DLSYM_FAILED, "dlsym( %s ), failed: unknown error", func );
189 |             }
190 |         }
{% endraw %}

```