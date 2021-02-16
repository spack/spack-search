---
name: "php"
layout: package
next_package: ocaml
previous_package: jchronoss
languages: ['c']
---
## 7.3.13
9 / 19786 files match, 3 filtered matches.

 - [ext/sqlite3/libsqlite/sqlite3.c](#extsqlite3libsqlitesqlite3c)
 - [sapi/litespeed/lsapilib.c](#sapilitespeedlsapilibc)
 - [sapi/litespeed/lscriu.c](#sapilitespeedlscriuc)

### ext/sqlite3/libsqlite/sqlite3.c

```c

{% raw %}
38877 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### sapi/litespeed/lsapilib.c

```c

{% raw %}
781 |     s_liblve = dlopen("liblve.so.0", RTLD_LAZY);
1464 |         void *pthread_lib = dlopen("libpthread.so", RTLD_LAZY);
{% endraw %}

```
### sapi/litespeed/lscriu.c

```c

{% raw %}
267 |     if (!(lib_handle = dlopen(last = "liblscapi.so", RTLD_LAZY)) /*||
268 |         !(pthread_lib_handle = dlopen(last = "libpthread.so", RTLD_LAZY))*/)
269 |         fprintf(stderr, "LSCRIU (%d): failed to dlopen %s: %s - ignore CRIU\n",
{% endraw %}

```