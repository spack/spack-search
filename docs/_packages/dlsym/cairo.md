---
name: "cairo"
layout: package
next_package: casacore
previous_package: brltty
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.14.12
16 / 4232 files match, 9 filtered matches.

 - [src/cairo-gl-dispatch.c](#srccairo-gl-dispatchc)
 - [src/cairo-quartz-surface.c](#srccairo-quartz-surfacec)
 - [src/cairo-quartz-font.c](#srccairo-quartz-fontc)
 - [src/drm/cairo-drm-gallium-surface.c](#srcdrmcairo-drm-gallium-surfacec)
 - [boilerplate/cairo-boilerplate.c](#boilerplatecairo-boilerplatec)
 - [util/backtrace-symbols.c](#utilbacktrace-symbolsc)
 - [util/cairo-fdr/fdr.c](#utilcairo-fdrfdrc)
 - [util/cairo-sphinx/fdr.c](#utilcairo-sphinxfdrc)
 - [util/cairo-trace/trace.c](#utilcairo-tracetracec)

### src/cairo-gl-dispatch.c

```c

{% raw %}
51 | static cairo_gl_generic_func_t
52 | _cairo_gl_dispatch_get_proc_addr (void *handle, const char *name)
53 | {
54 |     return (cairo_gl_generic_func_t) dlsym (handle, name);
55 | }
56 | #else
{% endraw %}

```
### src/cairo-quartz-surface.c

```c

{% raw %}
145 |     if (likely (_cairo_quartz_symbol_lookup_done))
146 | 	return;
147 | 
148 |     CGContextDrawTiledImagePtr = dlsym (RTLD_DEFAULT, "CGContextDrawTiledImage");
149 |     CGContextGetTypePtr = dlsym (RTLD_DEFAULT, "CGContextGetType");
150 |     CGContextCopyPathPtr = dlsym (RTLD_DEFAULT, "CGContextCopyPath");
151 |     CGContextGetAllowsFontSmoothingPtr = dlsym (RTLD_DEFAULT, "CGContextGetAllowsFontSmoothing");
152 |     CGContextSetAllowsFontSmoothingPtr = dlsym (RTLD_DEFAULT, "CGContextSetAllowsFontSmoothing");
153 | 
154 |     _cairo_quartz_symbol_lookup_done = TRUE;
{% endraw %}

```
### src/cairo-quartz-font.c

```c

{% raw %}
103 |     if (_cairo_quartz_font_symbol_lookup_done)
104 | 	return;
105 | 
106 |     CGFontCopyTableForTagPtr = dlsym(RTLD_DEFAULT, "CGFontCopyTableForTag");
107 | 
108 |     /* Look for the 10.5 versions first */
109 |     CGFontGetGlyphBBoxesPtr = dlsym(RTLD_DEFAULT, "CGFontGetGlyphBBoxes");
110 |     if (!CGFontGetGlyphBBoxesPtr)
111 | 	CGFontGetGlyphBBoxesPtr = dlsym(RTLD_DEFAULT, "CGFontGetGlyphBoundingBoxes");
112 | 
113 |     CGFontGetGlyphsForUnicharsPtr = dlsym(RTLD_DEFAULT, "CGFontGetGlyphsForUnichars");
114 |     if (!CGFontGetGlyphsForUnicharsPtr)
115 | 	CGFontGetGlyphsForUnicharsPtr = dlsym(RTLD_DEFAULT, "CGFontGetGlyphsForUnicodes");
116 | 
117 |     CGFontGetFontBBoxPtr = dlsym(RTLD_DEFAULT, "CGFontGetFontBBox");
118 | 
119 |     /* We just need one of these two */
120 |     CGFontCreateWithFontNamePtr = dlsym(RTLD_DEFAULT, "CGFontCreateWithFontName");
121 |     CGFontCreateWithNamePtr = dlsym(RTLD_DEFAULT, "CGFontCreateWithName");
122 | 
123 |     /* These have the same name in 10.4 and 10.5 */
124 |     CGFontGetUnitsPerEmPtr = dlsym(RTLD_DEFAULT, "CGFontGetUnitsPerEm");
125 |     CGFontGetGlyphAdvancesPtr = dlsym(RTLD_DEFAULT, "CGFontGetGlyphAdvances");
126 | 
127 |     CGFontGetHMetricsPtr = dlsym(RTLD_DEFAULT, "CGFontGetHMetrics");
128 |     CGFontGetAscentPtr = dlsym(RTLD_DEFAULT, "CGFontGetAscent");
129 |     CGFontGetDescentPtr = dlsym(RTLD_DEFAULT, "CGFontGetDescent");
130 |     CGFontGetLeadingPtr = dlsym(RTLD_DEFAULT, "CGFontGetLeading");
131 | 
132 |     CGContextGetAllowsFontSmoothingPtr = dlsym(RTLD_DEFAULT, "CGContextGetAllowsFontSmoothing");
133 |     CGContextSetAllowsFontSmoothingPtr = dlsym(RTLD_DEFAULT, "CGContextSetAllowsFontSmoothing");
134 | 
135 |     FMGetATSFontRefFromFontPtr = dlsym(RTLD_DEFAULT, "FMGetATSFontRefFromFont");
136 | 
137 |     if ((CGFontCreateWithFontNamePtr || CGFontCreateWithNamePtr) &&
{% endraw %}

```
### src/drm/cairo-drm-gallium-surface.c

```c

{% raw %}
761 |     if (handle == NULL)
762 | 	return NULL;
763 | 
764 |     ctor = dlsym (handle, "drm_api_create");
765 |     if (ctor == NULL) {
766 | 	dlclose (handle);
{% endraw %}

```
### boilerplate/cairo-boilerplate.c

```c

{% raw %}
495 | 	return TRUE;
496 | 
497 | #if HAVE_DLSYM
498 |     return dlsym (NULL, target->probe) != NULL;
499 | #else
500 |     return TRUE;
{% endraw %}

```
### util/backtrace-symbols.c

```c

{% raw %}
67 | static void load_funcs(void)
68 | {
69 | 	void * handle = dlopen("libbfd.so", RTLD_NOW);
70 | 	dbfd_init = dlsym(handle, "bfd_init");
71 | 	dbfd_scan_vma = dlsym(handle, "bfd_scan_vma");
72 | 	dbfd_openr = dlsym(handle, "bfd_openr");
73 | 	dbfd_check_format = dlsym(handle, "bfd_check_format");
74 | 	dbfd_check_format_matches = dlsym(handle, "bfd_check_format_matches");
75 | 	dbfd_close = dlsym(handle, "bfd_close");
76 | 	dbfd_map_over_sections = dlsym(handle, "bfd_map_over_sections");
77 | }
78 | 
{% endraw %}

```
### util/cairo-fdr/fdr.c

```c

{% raw %}
34 | #define DLCALL(name, args...) ({ \
35 |     static typeof (&name) name##_real; \
36 |     if (name##_real == NULL) { \
37 | 	name##_real = dlsym (_dlhandle, #name); \
38 | 	if (name##_real == NULL && _dlhandle == RTLD_NEXT) { \
39 | 	    _dlhandle = dlopen ("libcairo.so", RTLD_LAZY); \
40 | 	    name##_real = dlsym (_dlhandle, #name); \
41 | 	    assert (name##_real != NULL); \
42 | 	} \
{% endraw %}

```
### util/cairo-sphinx/fdr.c

```c

{% raw %}
36 | #define DLCALL(name, args...) ({ \
37 |     static typeof (&name) name##_real; \
38 |     if (name##_real == NULL) { \
39 | 	name##_real = dlsym (_dlhandle, #name); \
40 | 	if (name##_real == NULL && _dlhandle == RTLD_NEXT) { \
41 | 	    _dlhandle = dlopen ("libcairo.so", RTLD_LAZY); \
42 | 	    name##_real = dlsym (_dlhandle, #name); \
43 | 	    assert (name##_real != NULL); \
44 | 	} \
{% endraw %}

```
### util/cairo-trace/trace.c

```c

{% raw %}
116 | #define DLCALL(name, args...) ({ \
117 |     static typeof (&name) name##_real; \
118 |     if (name##_real == NULL) { \
119 | 	name##_real = (typeof (&name))(dlsym (_dlhandle, #name));	\
120 | 	if (name##_real == NULL && _dlhandle == RTLD_NEXT) { \
121 | 	    _dlhandle = dlopen ("libcairo." SHARED_LIB_EXT, RTLD_LAZY); \
122 | 	    name##_real = (typeof (&name))(dlsym (_dlhandle, #name));	\
123 | 	    assert (name##_real != NULL); \
124 | 	} \
{% endraw %}

```