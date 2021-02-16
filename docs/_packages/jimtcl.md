---
name: "jimtcl"
layout: package
next_package: julia
previous_package: jemalloc
languages: ['c']
---
## 0.77
6 / 213 files match, 5 filtered matches.

 - [jim-win32compat.h](#jim-win32compath)
 - [jim-win32compat.c](#jim-win32compatc)
 - [jim-load.c](#jim-loadc)
 - [sqlite3/sqlite3.c](#sqlite3sqlite3c)
 - [autosetup/jimsh0.c](#autosetupjimsh0c)

### jim-win32compat.h

```c

{% raw %}
13 | void *dlopen(const char *path, int mode);
{% endraw %}

```
### jim-win32compat.c

```c

{% raw %}
11 | void *dlopen(const char *path, int mode)
{% endraw %}

```
### jim-load.c

```c

{% raw %}
31 |     void *handle = dlopen(pathName, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### sqlite3/sqlite3.c

```c

{% raw %}
35416 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### autosetup/jimsh0.c

```c

{% raw %}
62 | void *dlopen(const char *path, int mode);
21833 | void *dlopen(const char *path, int mode)
{% endraw %}

```