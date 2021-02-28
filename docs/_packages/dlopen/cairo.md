---
name: "cairo"
layout: package
next_package: nbdkit
previous_package: file
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
39 | static void *
40 | _cairo_gl_dispatch_open_lib (void)
41 | {
42 |     return dlopen (NULL, RTLD_LAZY);
43 | }
44 | 
{% endraw %}

```
### src/drm/cairo-drm-gallium-surface.c

```c

{% raw %}
757 | 	libdir = "/usr/lib/dri";
758 |     buf[snprintf (buf, sizeof (buf)-1, "%s/i915_dri.so", libdir)] = '\0';
759 | 
760 |     handle = dlopen (buf, RTLD_LAZY);
761 |     if (handle == NULL)
762 | 	return NULL;
{% endraw %}

```
### util/backtrace-symbols.c

```c

{% raw %}
66 | 
67 | static void load_funcs(void)
68 | {
69 | 	void * handle = dlopen("libbfd.so", RTLD_NOW);
70 | 	dbfd_init = dlsym(handle, "bfd_init");
71 | 	dbfd_scan_vma = dlsym(handle, "bfd_scan_vma");
{% endraw %}

```
### util/cairo-fdr/fdr.c

```c

{% raw %}
36 |     if (name##_real == NULL) { \
37 | 	name##_real = dlsym (_dlhandle, #name); \
38 | 	if (name##_real == NULL && _dlhandle == RTLD_NEXT) { \
39 | 	    _dlhandle = dlopen ("libcairo.so", RTLD_LAZY); \
40 | 	    name##_real = dlsym (_dlhandle, #name); \
41 | 	    assert (name##_real != NULL); \
{% endraw %}

```
### util/cairo-sphinx/fdr.c

```c

{% raw %}
38 |     if (name##_real == NULL) { \
39 | 	name##_real = dlsym (_dlhandle, #name); \
40 | 	if (name##_real == NULL && _dlhandle == RTLD_NEXT) { \
41 | 	    _dlhandle = dlopen ("libcairo.so", RTLD_LAZY); \
42 | 	    name##_real = dlsym (_dlhandle, #name); \
43 | 	    assert (name##_real != NULL); \
{% endraw %}

```
### util/cairo-trace/trace.c

```c

{% raw %}
118 |     if (name##_real == NULL) { \
119 | 	name##_real = (typeof (&name))(dlsym (_dlhandle, #name));	\
120 | 	if (name##_real == NULL && _dlhandle == RTLD_NEXT) { \
121 | 	    _dlhandle = dlopen ("libcairo." SHARED_LIB_EXT, RTLD_LAZY); \
122 | 	    name##_real = (typeof (&name))(dlsym (_dlhandle, #name));	\
123 | 	    assert (name##_real != NULL); \
{% endraw %}

```