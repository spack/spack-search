---
name: "cctools"
layout: package
next_package: bazel
previous_package: libx11
languages: ['c']
---
## 7.1.0
2 / 1270 files match, 2 filtered matches.

 - [dttools/src/hdfs_library.c](#dttoolssrchdfs_libraryc)
 - [chirp/src/sqlite3.c](#chirpsrcsqlite3c)

### dttools/src/hdfs_library.c

```c

{% raw %}
126 | 			debug(D_HDFS, "dlopen failed: %s", dlerror());
{% endraw %}

```
### chirp/src/sqlite3.c

```c

{% raw %}
31212 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```