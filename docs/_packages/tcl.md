---
name: "tcl"
layout: package
next_package: exciting
previous_package: libxcursor
languages: ['cpp']
---
## 8.6.6
9 / 1481 files match

 - [ChangeLog.2002](#changelog2002)
 - [compat/dlfcn.h](#compatdlfcnh)
 - [pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c](#pkgssqlite3130compatsqlite3sqlite3c)
 - [unix/tclLoadOSF.c](#unixtclloadosfc)
 - [unix/tclLoadDyld.c](#unixtclloaddyldc)
 - [unix/tcl.m4](#unixtclm4)
 - [unix/tclLoadDl.c](#unixtclloaddlc)
 - [unix/tclUnixInit.c](#unixtclunixinitc)
 - [unix/tclLoadAix.c](#unixtclloadaixc)

### ChangeLog.2002

```

{% raw %}
4591 | 	in an actual build; Linux without dlopen appears to be a nonexistent
{% endraw %}

```
### compat/dlfcn.h

```cpp

{% raw %}
33 |  * Mode flags for the dlopen routine.
48 | void *dlopen (const char *path, int mode);
{% endraw %}

```
### pkgs/sqlite3.13.0/compat/sqlite3/sqlite3.c

```cpp

{% raw %}
1461 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
13397 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
19753 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
19754 |   return pVfs->xDlOpen(pVfs, zPath);
35271 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
35273 |   return dlopen(zFilename, RTLD_NOW | RTLD_LOCAL);
35278 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
35321 |   #define unixDlOpen  0
36704 |     unixDlOpen,           /* xDlOpen */                     \
42462 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
42469 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
42474 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
42484 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
42499 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
42521 |   #define winDlOpen  0
42758 |     winDlOpen,           /* xDlOpen */
42783 |     winDlOpen,           /* xDlOpen */
109406 |   handle = sqlite3OsDlOpen(pVfs, zFile);
109410 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
109421 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
168712 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
168714 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
168815 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### unix/tclLoadOSF.c

```cpp

{% raw %}
6 |  *	use ELF, rtld, and dlopen()[/usr/include/ldfcn.h].
24 |  *	supported dlopen().
49 |  * TclpDlopen --
65 | TclpDlopen(
192 | 				 * TclpDlopen(). The loadHandle is a token
{% endraw %}

```
### unix/tclLoadDyld.c

```cpp

{% raw %}
128 |  * TclpDlopen --
144 | TclpDlopen(
174 |     int dlopenflags = 0;
193 |     	dlopenflags |= RTLD_GLOBAL;
195 |     	dlopenflags |= RTLD_LOCAL;
198 |     	dlopenflags |= RTLD_LAZY;
200 |     	dlopenflags |= RTLD_NOW;
202 |     dlHandle = dlopen(nativePath, dlopenflags);
210 | 	dlHandle = dlopen(nativeFileName, dlopenflags);
331 |     Tcl_LoadHandle loadHandle,	/* Handle from TclpDlopen. */
429 |  *	TclpDlopen() above.
437 | 				 * TclpDlopen(). The loadHandle is a token
{% endraw %}

```
### unix/tcl.m4

```

{% raw %}
1075 |     AC_CHECK_LIB(dl, dlopen, have_dl=yes, have_dl=no)
1778 | 	    # dlopen is in -lc on QNX
1784 | 	    # Note, dlopen is available only on SCO 3.2.5 and greater. However,
{% endraw %}

```
### unix/tclLoadDl.c

```cpp

{% raw %}
4 |  *	the "dlopen" and "dlsym" library procedures for dynamic loading.
21 |  * argument to dlopen must always be 1. The RTLD_LOCAL flag doesn't exist on
45 |  * TclpDlopen --
61 | TclpDlopen(
77 |     int dlopenflags = 0;
90 |     	dlopenflags |= RTLD_GLOBAL;
92 |     	dlopenflags |= RTLD_LOCAL;
95 |     	dlopenflags |= RTLD_LAZY;
97 |     	dlopenflags |= RTLD_NOW;
99 |     handle = dlopen(native, dlopenflags);
114 | 	handle = dlopen(native, dlopenflags);
162 |     Tcl_LoadHandle loadHandle,	/* Value from TcpDlopen(). */
228 | 				 * TclpDlopen(). The loadHandle is a token
{% endraw %}

```
### unix/tclUnixInit.c

```cpp

{% raw %}
409 |     (void) dlopen(NULL, RTLD_NOW);			/* INTL: Native. */
{% endraw %}

```
### unix/tclLoadAix.c

```cpp

{% raw %}
3 |  *	This file implements the dlopen and dlsym APIs under the AIX operating
40 |  * We simulate dlopen() et al. through a call to load. Because AIX has no call
61 |  * The void * handle returned from dlopen is actually a ModulePtr.
96 | dlopen(
149 | 	strcpy(errbuf, "dlopen: ");
{% endraw %}

```