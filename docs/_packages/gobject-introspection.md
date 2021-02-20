---
name: "gobject-introspection"
layout: package
next_package: goblin-hmc-sim
previous_package: go-bootstrap
languages: ['c']
---
## 1.49.2
8 / 2382 files match, 1 filtered matches.

 - [girepository/gitypelib.c](#girepositorygitypelibc)

### girepository/gitypelib.c

```c

{% raw %}
2282 | }
2283 | 
2284 | static void
2285 | _g_typelib_do_dlopen (GITypelib *typelib)
2286 | {
2287 |   Header *header;
2346 |   if (typelib->open_attempted)
2347 |     return;
2348 |   typelib->open_attempted = TRUE;
2349 |   _g_typelib_do_dlopen (typelib);
2350 | }
2351 | 
{% endraw %}

```