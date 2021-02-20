---
name: "xhmm"
layout: package
next_package: xorg-server
previous_package: xedit
languages: ['c']
---
## 20160104
1 / 158 files match, 1 filtered matches.

 - [sources/hmm++/sources/lib/sqlite3.c](#sourceshmm++sourceslibsqlite3c)

### sources/hmm++/sources/lib/sqlite3.c

```c

{% raw %}
29724 | #include <dlfcn.h>
29725 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
29726 |   UNUSED_PARAMETER(NotUsed);
29727 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
29728 | }
29729 | 
{% endraw %}

```