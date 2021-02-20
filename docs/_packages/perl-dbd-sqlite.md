---
name: "perl-dbd-sqlite"
layout: package
next_package: petsc
previous_package: perl
languages: ['c']
---
## 1.56
1 / 138 files match, 1 filtered matches.

 - [sqlite3.c](#sqlite3c)

### sqlite3.c

```c

{% raw %}
36976 | #include <dlfcn.h>
36977 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
36978 |   UNUSED_PARAMETER(NotUsed);
36979 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
36980 | }
36981 | 
{% endraw %}

```