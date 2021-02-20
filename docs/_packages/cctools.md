---
name: "cctools"
layout: package
next_package: cdo
previous_package: cc65
languages: ['c']
---
## 7.1.0
2 / 1270 files match, 2 filtered matches.

 - [dttools/src/hdfs_library.c](#dttoolssrchdfs_libraryc)
 - [chirp/src/sqlite3.c](#chirpsrcsqlite3c)

### dttools/src/hdfs_library.c

```c

{% raw %}
123 | 			rc = 0;
124 | 			goto out;
125 | 		} else {
126 | 			debug(D_HDFS, "dlopen failed: %s", dlerror());
127 | 		}
128 | 	}
{% endraw %}

```
### chirp/src/sqlite3.c

```c

{% raw %}
31209 | #include <dlfcn.h>
31210 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
31211 |   UNUSED_PARAMETER(NotUsed);
31212 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
31213 | }
31214 | 
{% endraw %}

```