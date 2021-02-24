---
name: "wt"
layout: package
next_package: shc
previous_package: gdb
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.3.7
2 / 2020 files match, 2 filtered matches.

 - [src/Wt/Dbo/backend/amalgamation/sqlite3.c](#srcwtdbobackendamalgamationsqlite3c)
 - [src/3rdparty/glew-1.10.0/src/glew.c](#src3rdpartyglew-1100srcglewc)

### src/Wt/Dbo/backend/amalgamation/sqlite3.c

```c

{% raw %}
35934 |   */
35935 |   void (*(*x)(void*,const char*))(void);
35936 |   UNUSED_PARAMETER(NotUsed);
35937 |   x = (void(*(*)(void*,const char*))(void))dlsym;
35938 |   return (*x)(p, zSym);
35939 | }
{% endraw %}

```
### src/3rdparty/glew-1.10.0/src/glew.c

```c

{% raw %}
78 |   if (h == NULL)
79 |   {
80 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
81 |     gpa = dlsym(h, "glXGetProcAddress");
82 |   }
83 | 
84 |   if (gpa != NULL)
85 |     return ((void*(*)(const GLubyte*))gpa)(name);
86 |   else
87 |     return dlsym(h, (const char*)name);
88 | }
89 | #endif /* __sgi || __sun || GLEW_APPLE_GLX */
110 | #endif
111 |   }
112 |   if( !image ) return NULL;
113 |   addr = dlsym(image, (const char*)name);
114 |   if( addr ) return addr;
115 | #ifdef GLEW_APPLE_GLX
{% endraw %}

```