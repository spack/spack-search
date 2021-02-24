---
name: "glew"
layout: package
next_package: libiberty
previous_package: arrow
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.1.0
2 / 165 files match, 2 filtered matches.

 - [src/glew.c](#srcglewc)
 - [auto/src/glew_head.c](#autosrcglew_headc)

### src/glew.c

```c

{% raw %}
85 | 
86 |   if (h == NULL)
87 |   {
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
89 |     gpa = dlsym(h, "glXGetProcAddress");
90 |   }
111 |   void* addr;
112 |   if (NULL == image)
113 |   {
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
115 |   }
116 |   if( !image ) return NULL;
{% endraw %}

```
### auto/src/glew_head.c

```c

{% raw %}
53 | 
54 |   if (h == NULL)
55 |   {
56 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
57 |     gpa = dlsym(h, "glXGetProcAddress");
58 |   }
79 |   void* addr;
80 |   if (NULL == image)
81 |   {
82 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
83 |   }
84 |   if( !image ) return NULL;
{% endraw %}

```