---
name: "wt"
layout: package
next_package: shc
previous_package: gdb
library_name: dlopen
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
35894 | #include <dlfcn.h>
35895 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
35896 |   UNUSED_PARAMETER(NotUsed);
35897 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
35898 | }
35899 | 
{% endraw %}

```
### src/3rdparty/glew-1.10.0/src/glew.c

```c

{% raw %}
77 | 
78 |   if (h == NULL)
79 |   {
80 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
81 |     gpa = dlsym(h, "glXGetProcAddress");
82 |   }
104 |   if (NULL == image) 
105 |   {
106 | #ifdef GLEW_REGAL
107 |     image = dlopen("libRegal.dylib", RTLD_LAZY);
108 | #else
109 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
110 | #endif
111 |   }
{% endraw %}

```