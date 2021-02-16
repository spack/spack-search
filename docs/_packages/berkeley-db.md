---
name: "berkeley-db"
layout: package
next_package: qthreads
previous_package: libssh
languages: ['c']
---
## 6.1.29
25 / 9619 files match

 - [lang/sql/sqlite/src/os_unix.c](#langsqlsqlitesrcos_unixc)
 - [lang/sql/odbc/sqlite4odbc.c](#langsqlodbcsqlite4odbcc)
 - [lang/sql/odbc/sqlite3odbc.c](#langsqlodbcsqlite3odbcc)
 - [lang/sql/odbc/zipfile.c](#langsqlodbczipfilec)
 - [lang/sql/odbc/sqliteodbc.c](#langsqlodbcsqliteodbcc)
 - [lang/sql/generated/sqlite3.c](#langsqlgeneratedsqlite3c)

### lang/sql/sqlite/src/os_unix.c

```c

{% raw %}
5986 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### lang/sql/odbc/sqlite4odbc.c

```c

{% raw %}
1249 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
1251 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
1254 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
1257 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
19787 |     libsqlite4_so = dlopen("libsqlite4.so.0", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### lang/sql/odbc/sqlite3odbc.c

```c

{% raw %}
1266 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
1268 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
1271 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
1274 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
20504 |     libsqlite3_so = dlopen("libsqlite3.so.0", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### lang/sql/odbc/zipfile.c

```c

{% raw %}
1921 | mem_dlopen(sqlite3_vfs *vfs, const char *name)
2028 |     mem_dlopen,		/* xDlOpen */
{% endraw %}

```
### lang/sql/odbc/sqliteodbc.c

```c

{% raw %}
751 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
753 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
756 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
759 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
{% endraw %}

```
### lang/sql/generated/sqlite3.c

```c

{% raw %}
29306 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```