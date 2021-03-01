---
name: "vtk"
layout: package
next_package: weechat
previous_package: vtable-dumper
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 9.0.0
8 / 19019 files match, 3 filtered matches.

 - [ThirdParty/mpi4py/vtkmpi4py/src/dynload.h](#thirdpartympi4pyvtkmpi4pysrcdynloadh)
 - [ThirdParty/glew/vtkglew/src/glew.c](#thirdpartyglewvtkglewsrcglewc)
 - [ThirdParty/sqlite/vtksqlite/sqlite3.c](#thirdpartysqlitevtksqlitesqlite3c)

### ThirdParty/mpi4py/vtkmpi4py/src/dynload.h

```c

{% raw %}
41 |   extern "C" {
42 |   #endif
43 |   extern void *dlopen(const char *, int);
44 |   extern void *dlsym(void *, const char *);
45 |   extern int   dlclose(void *);
46 |   extern char *dlerror(void);
{% endraw %}

```
### ThirdParty/glew/vtkglew/src/glew.c

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
### ThirdParty/sqlite/vtksqlite/sqlite3.c

```c

{% raw %}
39122 |   */
39123 |   void (*(*x)(void*,const char*))(void);
39124 |   UNUSED_PARAMETER(NotUsed);
39125 |   x = (void(*(*)(void*,const char*))(void))dlsym;
39126 |   return (*x)(p, zSym);
39127 | }
{% endraw %}

```