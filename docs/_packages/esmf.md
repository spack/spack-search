---
name: "esmf"
layout: package
next_package: geopm
previous_package: tcsh
languages: ['c']
---
## 8.0.1
3 / 3654 files match

 - [src/Infrastructure/Trace/src/ESMCI_Trace.C](#srcinfrastructuretracesrcesmci_tracec)
 - [src/Superstructure/Component/src/ESMCI_MethodTable.C](#srcsuperstructurecomponentsrcesmci_methodtablec)
 - [src/Superstructure/Component/src/ESMCI_FTable.C](#srcsuperstructurecomponentsrcesmci_ftablec)

### src/Infrastructure/Trace/src/ESMCI_Trace.C

```c

{% raw %}
404 |     void *preload_lib = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### src/Superstructure/Component/src/ESMCI_MethodTable.C

```c

{% raw %}
309 |       lib = dlopen(shobj.c_str(), RTLD_LAZY);
311 |       lib = dlopen(NULL, RTLD_LAZY);  // search in executable
{% endraw %}

```
### src/Superstructure/Component/src/ESMCI_FTable.C

```c

{% raw %}
246 |       lib = dlopen(sharedObj.c_str(), RTLD_LAZY);
248 |       lib = dlopen(NULL, RTLD_LAZY);  // search in executable
299 |       lib = dlopen(sharedObj.c_str(), RTLD_LAZY);
301 |       lib = dlopen(NULL, RTLD_LAZY);  // search in executable
1906 |             lib = dlopen(envVar, RTLD_LAZY);  // envVar==NULL -> look into exe
1972 |             lib = dlopen(envVar, RTLD_LAZY);  // envVar==NULL -> look into exe
{% endraw %}

```