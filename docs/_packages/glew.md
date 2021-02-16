---
name: "glew"
layout: package
next_package: py-pillow
previous_package: paraview
languages: ['c']
---
## 2.1.0
2 / 165 files match, 2 filtered matches.

 - [src/glew.c](#srcglewc)
 - [auto/src/glew_head.c](#autosrcglew_headc)

### src/glew.c

```c

{% raw %}
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```
### auto/src/glew_head.c

```c

{% raw %}
56 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
82 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```