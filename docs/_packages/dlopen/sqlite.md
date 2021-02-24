---
name: "sqlite"
layout: package
next_package: poppler
previous_package: rose
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.27.1
4 / 29 files match, 1 filtered matches.

 - [sqlite3.c](#sqlite3c)

### sqlite3.c

```c

{% raw %}
38761 | #include <dlfcn.h>
38762 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38763 |   UNUSED_PARAMETER(NotUsed);
38764 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38765 | }
38766 | 
{% endraw %}

```