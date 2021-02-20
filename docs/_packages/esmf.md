---
name: "esmf"
layout: package
next_package: etcd
previous_package: ermod
languages: ['c']
---
## 8.0.1
3 / 3654 files match, 3 filtered matches.

 - [src/Infrastructure/Trace/src/ESMCI_Trace.C](#srcinfrastructuretracesrcesmci_tracec)
 - [src/Superstructure/Component/src/ESMCI_MethodTable.C](#srcsuperstructurecomponentsrcesmci_methodtablec)
 - [src/Superstructure/Component/src/ESMCI_FTable.C](#srcsuperstructurecomponentsrcesmci_ftablec)

### src/Infrastructure/Trace/src/ESMCI_Trace.C

```c

{% raw %}
401 |   static void InitializeWrappers() {
402 |     int wrappersPresent = TRACE_WRAP_NONE;
403 | #ifndef ESMF_NO_DLFCN
404 |     void *preload_lib = dlopen(NULL, RTLD_LAZY);
405 |     if (preload_lib == NULL) {
406 |       ESMC_LogDefault.Write("ESMF Tracing/Profiling could not open shared library containing instrumentation.", ESMC_LOGMSG_WARN);
{% endraw %}

```
### src/Superstructure/Component/src/ESMCI_MethodTable.C

```c

{% raw %}
306 | #else
307 |     void *lib;
308 |     if (shobj.length()>0)
309 |       lib = dlopen(shobj.c_str(), RTLD_LAZY);
310 |     else
311 |       lib = dlopen(NULL, RTLD_LAZY);  // search in executable
312 |     if (lib == NULL){
313 |       ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD, 
{% endraw %}

```
### src/Superstructure/Component/src/ESMCI_FTable.C

```c

{% raw %}
243 |     if (llen>0){
244 |       string sharedObj(sharedObjArg, llen);
245 |       sharedObj.resize(sharedObj.find_last_not_of(" ")+1);
246 |       lib = dlopen(sharedObj.c_str(), RTLD_LAZY);
247 |     }else
248 |       lib = dlopen(NULL, RTLD_LAZY);  // search in executable
249 |     if (lib == NULL){
250 |       ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD,
296 |     if (llen>0){
297 |       string sharedObj(sharedObjArg, llen);
298 |       sharedObj.resize(sharedObj.find_last_not_of(" ")+1);
299 |       lib = dlopen(sharedObj.c_str(), RTLD_LAZY);
300 |     }else
301 |       lib = dlopen(NULL, RTLD_LAZY);  // search in executable
302 |     if (lib == NULL){
303 |       ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD,
1903 |             // check and see if an alternate compliance ic object was specified
1904 |             envVar = VM::getenv("ESMF_RUNTIME_COMPLIANCEICOBJECT");
1905 |             void *lib;
1906 |             lib = dlopen(envVar, RTLD_LAZY);  // envVar==NULL -> look into exe
1907 |             if (lib == NULL){
1908 |               ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD,
1969 | 
1970 |             envVar = VM::getenv("ESMF_RUNTIME_COMPLIANCEICOBJECT");
1971 |             void *lib;
1972 |             lib = dlopen(envVar, RTLD_LAZY);  // envVar==NULL -> look into exe
1973 |             if (lib == NULL){
1974 |               ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD,
{% endraw %}

```