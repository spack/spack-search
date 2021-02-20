---
name: "ompt-openmp"
layout: package
next_package: onednn
previous_package: octave
languages: ['c']
---
## 0.1
3 / 416 files match, 1 filtered matches.

 - [runtime/src/z_Linux_util.c](#runtimesrcz_linux_utilc)

### runtime/src/z_Linux_util.c

```c

{% raw %}
1612 | 
1613 |     /* This is necessary to make sure no stale data is left around */
1614 |     /* AC: customers complain that we use unsafe routines in the atfork
1615 |        handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
1616 |        in dynamic_link when check the presence of shared tbbmalloc library.
1617 |        Suggestion is to make the library initialization lazier, similar
{% endraw %}

```