---
name: "dimemas"
layout: package
next_package: libxslt
previous_package: tcl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.4.1
1 / 244 files match, 1 filtered matches.

 - [Simulator/model/communic.c](#simulatormodelcommunicc)

### Simulator/model/communic.c

```c

{% raw %}
284 | {
285 |     struct t_machine *machine;
286 |     size_t machines_it;
287 |     char *external_comm_library_name, *dlsym_error;
288 | 
289 | 
329 |         }
330 |         else
331 |         { 
332 |             external_get_communication_type = dlsym(
333 |                     external_comm_library, 
334 |                     "external_get_communication_type");
335 |             if ((dlsym_error = dlerror()) != NULL)
336 |             {
337 |                 warning("-> WARN: Unable to load function \"external_get_communication_type\""\
338 |                         " from library \"%s\": %s\n",
339 |                         external_comm_library_name,
340 |                         dlsym_error);
341 |                 return;
342 |             }
343 | 
344 |             get_startup_value = dlsym(external_comm_library, "get_startup_value");
345 |             if ((dlsym_error = dlerror()) != NULL)
346 |             {
347 |                 warning("-> WARN: Unable to load function \"get_startup_value\" from library"\
348 |                         " \"%s\": %s\n",
349 |                         external_comm_library_name,
350 |                         dlsym_error);
351 |                 return;
352 |             }
353 | 
354 |             get_bandwidth_value = dlsym(external_comm_library, "get_bandwidth_value");
355 |             if ((dlsym_error = dlerror()) != NULL)
356 |             {
357 |                 warning("-> WARN: Unable to load function \"get_bandwidth_value\" from library"\
358 |                         " \"%s\": %s\n",
359 |                         external_comm_library_name,
360 |                         dlsym_error);
361 |                 return;
362 |             }
363 | 
364 |             external_get_global_op_type = dlsym(external_comm_library, "external_get_global_op_type");
365 |             if ((dlsym_error = dlerror()) != NULL)
366 |             {
367 |                 warning("-> WARN: Unable to load function \"external_get_global_op_type\" from"\
368 |                         " library \"%s\": %s\n",
369 |                         external_comm_library_name,
370 |                         dlsym_error);
371 |                 return;
372 |             }
373 | 
374 |             external_compute_global_operation_time = dlsym(
375 |                     external_comm_library, 
376 |                     "external_compute_global_operation_time");
377 |             if ((dlsym_error = dlerror()) != NULL)
378 |             {
379 |                 warning("-> WARN: Unable to load function \"external_compute_global_"\
380 |                         "operation_time\" from library \"%s\": %s\n",
381 |                         external_comm_library_name,
382 |                         dlsym_error);
383 |                 return;
384 |             }
{% endraw %}

```