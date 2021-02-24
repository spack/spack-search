---
name: "glew"
layout: package
next_package: libiberty
previous_package: arrow
library_name: dlsym
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
86 |   if (h == NULL)
87 |   {
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
89 |     gpa = dlsym(h, "glXGetProcAddress");
90 |   }
91 | 
92 |   if (gpa != NULL)
93 |     return ((void*(*)(const GLubyte*))gpa)(name);
94 |   else
95 |     return dlsym(h, (const char*)name);
96 | }
97 | #endif /* __sgi || __sun || GLEW_APPLE_GLX */
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
115 |   }
116 |   if( !image ) return NULL;
117 |   addr = dlsym(image, (const char*)name);
118 |   if( addr ) return addr;
119 | #ifdef GLEW_APPLE_GLX
{% endraw %}

```
### auto/src/glew_head.c

```c

{% raw %}
54 |   if (h == NULL)
55 |   {
56 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
57 |     gpa = dlsym(h, "glXGetProcAddress");
58 |   }
59 | 
60 |   if (gpa != NULL)
61 |     return ((void*(*)(const GLubyte*))gpa)(name);
62 |   else
63 |     return dlsym(h, (const char*)name);
64 | }
65 | #endif /* __sgi || __sun || GLEW_APPLE_GLX */
82 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
83 |   }
84 |   if( !image ) return NULL;
85 |   addr = dlsym(image, (const char*)name);
86 |   if( addr ) return addr;
87 | #ifdef GLEW_APPLE_GLX
{% endraw %}

```