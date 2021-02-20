---
name: "dimemas"
layout: package
next_package: dmd
previous_package: dcap
languages: ['c']
---
## 5.4.1
3 / 244 files match, 1 filtered matches.

 - [Simulator/model/communic.c](#simulatormodelcommunicc)

### Simulator/model/communic.c

```c

{% raw %}
319 |     /* Initialization of the possible external library */
320 |     if ((external_comm_library_name = getenv("DIMEMAS_EXTERNAL_COMM_LIBRARY")) != NULL)
321 |     {
322 |         external_comm_library = dlopen(external_comm_library_name, RTLD_LAZY);
323 | 
324 |         if (!external_comm_library)
{% endraw %}

```