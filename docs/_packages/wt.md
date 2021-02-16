---
name: "wt"
layout: package
next_package: wxwidgets
previous_package: wrk
languages: ['c']
---
## 3.3.7
2 / 2020 files match, 2 filtered matches.

 - [src/Wt/Dbo/backend/amalgamation/sqlite3.c](#srcwtdbobackendamalgamationsqlite3c)
 - [src/3rdparty/glew-1.10.0/src/glew.c](#src3rdpartyglew-1100srcglewc)

### src/Wt/Dbo/backend/amalgamation/sqlite3.c

```c

{% raw %}
35897 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/3rdparty/glew-1.10.0/src/glew.c

```c

{% raw %}
80 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
107 |     image = dlopen("libRegal.dylib", RTLD_LAZY);
109 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```