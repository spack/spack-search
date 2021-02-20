---
name: "graphviz"
layout: package
next_package: grass
previous_package: graphicsmagick
languages: ['c']
---
## 2.46.0
3 / 3596 files match, 1 filtered matches.

 - [lib/gvc/gvplugin.c](#libgvcgvpluginc)

### lib/gvc/gvplugin.c

```c

{% raw %}
197 |         agerr(AGERR, "failed to init libltdl\n");
198 |         return NULL;
199 |     }
200 |     hndl = lt_dlopen(p);
201 |     if (!hndl) {
202 |         if ((stat(p, &sb)) == 0) {
{% endraw %}

```