---
name: "berkeley-db"
layout: package
next_package: bind9
previous_package: bedtools2
languages: ['c']
---
## 6.1.29
25 / 9619 files match, 6 filtered matches.

 - [lang/sql/sqlite/src/os_unix.c](#langsqlsqlitesrcos_unixc)
 - [lang/sql/odbc/sqlite4odbc.c](#langsqlodbcsqlite4odbcc)
 - [lang/sql/odbc/sqlite3odbc.c](#langsqlodbcsqlite3odbcc)
 - [lang/sql/odbc/zipfile.c](#langsqlodbczipfilec)
 - [lang/sql/odbc/sqliteodbc.c](#langsqlodbcsqliteodbcc)
 - [lang/sql/generated/sqlite3.c](#langsqlgeneratedsqlite3c)

### lang/sql/sqlite/src/os_unix.c

```c

{% raw %}
5983 | #include <dlfcn.h>
5984 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
5985 |   UNUSED_PARAMETER(NotUsed);
5986 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
5987 | }
5988 | 
{% endraw %}

```
### lang/sql/odbc/sqlite4odbc.c

```c

{% raw %}
1246 |     void *lib;
1247 |     int (*gpps)();
1248 | 
1249 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
1250 |     if (!lib) {
1251 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
1252 |     }
1253 |     if (!lib) {
1254 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
1255 |     }
1256 |     if (!lib) {
1257 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
1258 |     }
1259 |     if (lib) {
19784 | {
19785 |     int i;
19786 | 
19787 |     libsqlite4_so = dlopen("libsqlite4.so.0", RTLD_NOW | RTLD_GLOBAL);
19788 |     i = 0;
19789 |     while (dls_nametab[i].name) {
{% endraw %}

```
### lang/sql/odbc/sqlite3odbc.c

```c

{% raw %}
1263 |     void *lib;
1264 |     int (*gpps)();
1265 | 
1266 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
1267 |     if (!lib) {
1268 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
1269 |     }
1270 |     if (!lib) {
1271 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
1272 |     }
1273 |     if (!lib) {
1274 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
1275 |     }
1276 |     if (lib) {
20501 | {
20502 |     int i;
20503 | 
20504 |     libsqlite3_so = dlopen("libsqlite3.so.0", RTLD_NOW | RTLD_GLOBAL);
20505 |     i = 0;
20506 |     while (dls_nametab[i].name) {
{% endraw %}

```
### lang/sql/odbc/zipfile.c

```c

{% raw %}
1918 |  */
1919 | 
1920 | static void *
1921 | mem_dlopen(sqlite3_vfs *vfs, const char *name)
1922 | {
1923 |     return 0;
2025 |     mem_delete,		/* xDelete */
2026 |     mem_access,		/* xAccess */
2027 |     mem_fullpathname,	/* xFullPathname */
2028 |     mem_dlopen,		/* xDlOpen */
2029 |     mem_dlerror,	/* xDlError */
2030 |     mem_dlsym,		/* xDlSym */
{% endraw %}

```
### lang/sql/odbc/sqliteodbc.c

```c

{% raw %}
748 |     void *lib;
749 |     int (*gpps)();
750 | 
751 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
752 |     if (!lib) {
753 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
754 |     }
755 |     if (!lib) {
756 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
757 |     }
758 |     if (!lib) {
759 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
760 |     }
761 |     if (lib) {
{% endraw %}

```
### lang/sql/generated/sqlite3.c

```c

{% raw %}
29303 | #include <dlfcn.h>
29304 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
29305 |   UNUSED_PARAMETER(NotUsed);
29306 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
29307 | }
29308 | 
{% endraw %}

```