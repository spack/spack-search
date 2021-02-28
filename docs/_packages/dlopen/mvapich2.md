---
name: "mvapich2"
layout: package
next_package: global
previous_package: tk
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2
43 / 8321 files match, 7 filtered matches.

 - [src/pm/hydra/tools/topo/hwloc/hwloc/src/components.c](#srcpmhydratoolstopohwlochwlocsrccomponentsc)
 - [src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h](#srcpmhydratoolstopohwlochwlocincludehwlocpluginsh)
 - [src/mpid/ch3/channels/common/src/memory/mem_hooks.c](#srcmpidch3channelscommonsrcmemorymem_hooksc)
 - [src/pmi/pmi2/poe/poe2pmi.c](#srcpmipmi2poepoe2pmic)
 - [test/mpid/dluse.c](#testmpiddlusec)
 - [contrib/hwloc/src/components.c](#contribhwlocsrccomponentsc)
 - [contrib/hwloc/include/hwloc/plugins.h](#contribhwlocincludehwlocpluginsh)

### src/pm/hydra/tools/topo/hwloc/hwloc/src/components.c

```c

{% raw %}
83 |     basename++;
84 | 
85 |   /* dlopen and get the component structure */
86 |   handle = lt_dlopenext(filename);
87 |   if (!handle) {
88 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
324 | #ifdef HWLOC_INSIDE_PLUGIN
325 |   lt_dlhandle handle;
326 |   void *sym;
327 |   handle = lt_dlopen(NULL);
328 |   if (!handle)
329 |     /* cannot check, assume things will work */
{% endraw %}

```
### src/mpid/ch3/channels/common/src/memory/mem_hooks.c

```c

{% raw %}
67 |      * function from the second library instead of the one from the system.
68 |      */
69 | 
70 |     void* handle = dlopen("libmpich.so", RTLD_LAZY | RTLD_LOCAL);
71 |     dlerror_str = dlerror();
72 |     if(NULL != dlerror_str) {
{% endraw %}

```
### src/pmi/pmi2/poe/poe2pmi.c

```c

{% raw %}
95 |     else
96 |       poelibname = "libpoe_r.a(poe_r.o)";
97 | #endif
98 |     poeptr = dlopen(poelibname, poeflags);
99 |     if (poeptr == NULL) {
100 |         TRACE_ERR("failed to open %s error=%s\n", poelibname, dlerror());
{% endraw %}

```
### test/mpid/dluse.c

```c

{% raw %}
18 | 
19 |     /* We allow different extensions for the shared libraries here, 
20 |      as OSX uses .dylib and Cygwin may use .dll . */
21 |     handle = dlopen( "./libconftest."## #SHLIBEXT, RTLD_LAZY );
22 |     if (!handle) {
23 | 	fprintf( stderr, "Could not open test library: %s\n", dlerror() );
{% endraw %}

```
### contrib/hwloc/src/components.c

```c

{% raw %}
89 |     basename++;
90 | 
91 |   /* dlopen and get the component structure */
92 |   handle = lt_dlopenext(filename);
93 |   if (!handle) {
94 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### contrib/hwloc/include/hwloc/plugins.h

```c

{% raw %}
367 | #ifdef HWLOC_INSIDE_PLUGIN
368 |   lt_dlhandle handle;
369 |   void *sym;
370 |   handle = lt_dlopen(NULL);
371 |   if (!handle)
372 |     /* cannot check, assume things will work */
{% endraw %}

```