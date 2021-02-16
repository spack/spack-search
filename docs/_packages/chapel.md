---
name: "chapel"
layout: package
next_package: charmpp
previous_package: cdo
languages: ['c']
---
## 1.18.0
28 / 7639 files match, 3 filtered matches.

 - [third-party/massivethreads/massivethreads-src/src/myth_real.c](#third-partymassivethreadsmassivethreads-srcsrcmyth_realc)
 - [third-party/hwloc/hwloc-src/src/components.c](#third-partyhwlochwloc-srcsrccomponentsc)
 - [third-party/hwloc/hwloc-src/include/hwloc/plugins.h](#third-partyhwlochwloc-srcincludehwlocpluginsh)

### third-party/massivethreads/massivethreads-src/src/myth_real.c

```c

{% raw %}
517 |       handle = dlopen(filename, RTLD_LAZY | RTLD_NOLOAD);
{% endraw %}

```
### third-party/hwloc/hwloc-src/src/components.c

```c

{% raw %}
100 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### third-party/hwloc/hwloc-src/include/hwloc/plugins.h

```c

{% raw %}
370 |   handle = lt_dlopen(NULL);
{% endraw %}

```