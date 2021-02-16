---
name: "mvapich2"
layout: package
next_package: mysql
previous_package: musl
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
86 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
327 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### src/mpid/ch3/channels/common/src/memory/mem_hooks.c

```c

{% raw %}
70 |     void* handle = dlopen("libmpich.so", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### src/pmi/pmi2/poe/poe2pmi.c

```c

{% raw %}
98 |     poeptr = dlopen(poelibname, poeflags);
{% endraw %}

```
### test/mpid/dluse.c

```c

{% raw %}
21 |     handle = dlopen( "./libconftest."## #SHLIBEXT, RTLD_LAZY );
{% endraw %}

```
### contrib/hwloc/src/components.c

```c

{% raw %}
92 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### contrib/hwloc/include/hwloc/plugins.h

```c

{% raw %}
370 |   handle = lt_dlopen(NULL);
{% endraw %}

```