---
name: "jimtcl"
layout: package
next_package: julia
previous_package: jchronoss
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
10 | #if defined(_WIN32) || defined(WIN32)
11 | 
12 | #define HAVE_DLOPEN
13 | void *dlopen(const char *path, int mode);
14 | int dlclose(void *handle);
15 | void *dlsym(void *handle, const char *symbol);
{% endraw %}

```
### jim-win32compat.c

```c

{% raw %}
8 | #include <windows.h>
9 | 
10 | #if defined(HAVE_DLOPEN_COMPAT)
11 | void *dlopen(const char *path, int mode)
12 | {
13 |     JIM_NOTUSED(mode);
{% endraw %}

```
### jim-load.c

```c

{% raw %}
28 |  */
29 | int Jim_LoadLibrary(Jim_Interp *interp, const char *pathName)
30 | {
31 |     void *handle = dlopen(pathName, RTLD_NOW | RTLD_LOCAL);
32 |     if (handle == NULL) {
33 |         Jim_SetResultFormatted(interp, "error loading extension \"%s\": %s", pathName,
{% endraw %}

```
### sqlite3/sqlite3.c

```c

{% raw %}
35413 | #include <dlfcn.h>
35414 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
35415 |   UNUSED_PARAMETER(NotUsed);
35416 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
35417 | }
35418 | 
{% endraw %}

```
### autosetup/jimsh0.c

```c

{% raw %}
59 | #if defined(_WIN32) || defined(WIN32)
60 | 
61 | #define HAVE_DLOPEN
62 | void *dlopen(const char *path, int mode);
63 | int dlclose(void *handle);
64 | void *dlsym(void *handle, const char *symbol);
21830 | #include <windows.h>
21831 | 
21832 | #if defined(HAVE_DLOPEN_COMPAT)
21833 | void *dlopen(const char *path, int mode)
21834 | {
21835 |     JIM_NOTUSED(mode);
{% endraw %}

```