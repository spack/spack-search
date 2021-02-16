---
name: "cairo"
layout: package
next_package: caliper
previous_package: busybox
languages: ['c']
---
## 1.14.12
11 / 4232 files match, 6 filtered matches.

 - [src/cairo-gl-dispatch.c](#srccairo-gl-dispatchc)
 - [src/drm/cairo-drm-gallium-surface.c](#srcdrmcairo-drm-gallium-surfacec)
 - [util/backtrace-symbols.c](#utilbacktrace-symbolsc)
 - [util/cairo-fdr/fdr.c](#utilcairo-fdrfdrc)
 - [util/cairo-sphinx/fdr.c](#utilcairo-sphinxfdrc)
 - [util/cairo-trace/trace.c](#utilcairo-tracetracec)

### src/cairo-gl-dispatch.c

```c

{% raw %}
42 |     return dlopen (NULL, RTLD_LAZY);
{% endraw %}

```
### src/drm/cairo-drm-gallium-surface.c

```c

{% raw %}
760 |     handle = dlopen (buf, RTLD_LAZY);
{% endraw %}

```
### util/backtrace-symbols.c

```c

{% raw %}
69 | 	void * handle = dlopen("libbfd.so", RTLD_NOW);
{% endraw %}

```
### util/cairo-fdr/fdr.c

```c

{% raw %}
39 | 	    _dlhandle = dlopen ("libcairo.so", RTLD_LAZY); \
{% endraw %}

```
### util/cairo-sphinx/fdr.c

```c

{% raw %}
41 | 	    _dlhandle = dlopen ("libcairo.so", RTLD_LAZY); \
{% endraw %}

```
### util/cairo-trace/trace.c

```c

{% raw %}
121 | 	    _dlhandle = dlopen ("libcairo." SHARED_LIB_EXT, RTLD_LAZY); \
{% endraw %}

```