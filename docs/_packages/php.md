---
name: "php"
layout: package
next_package: ocaml
previous_package: jchronoss
languages: ['cpp', 'bash']
---
## 7.3.13
9 / 19786 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [build/libtool.m4](#buildlibtoolm4)
 - [ext/sqlite3/libsqlite/sqlite3.c](#extsqlite3libsqlitesqlite3c)
 - [ext/interbase/interbase.c](#extinterbaseinterbasec)
 - [Zend/Zend.m4](#zendzendm4)
 - [Zend/zend_portability.h](#zendzend_portabilityh)
 - [sapi/litespeed/lsapilib.c](#sapilitespeedlsapilibc)
 - [sapi/litespeed/lscriu.c](#sapilitespeedlscriuc)

### configure.ac

```

{% raw %}
407 | PHP_CHECK_FUNC(dlopen, dl)
408 | if test "$ac_cv_func_dlopen" = "yes"; then
{% endraw %}

```
### ltmain.sh

```bash

{% raw %}
557 |   -dlopen)
558 |     prevopt="-dlopen"
642 |   # Only execute mode is allowed to have -dlopen flags.
644 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1186 | 	    dlopen_self=$dlopen_self_static
1192 | 	    dlopen_self=$dlopen_self_static
1198 | 	    dlopen_self=$dlopen_self_static
1255 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1347 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1504 |       -dlopen)
1897 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1970 | 	  # This library was specified with -dlopen.
2111 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2123 | 	passes="conv scan dlopen dlpreopen link"
2136 | 	dlopen) libs="$dlfiles" ;;
2141 |       if test "$pass" = dlopen; then
2325 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2326 | 	      # If there is no dlopen support or we're linking statically,
2359 | 	dlopen=
2380 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2423 | 	# This library was specified with -dlopen.
2424 | 	if test "$pass" = dlopen; then
2426 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2430 | 	     test "$dlopen_support" != yes ||
2432 | 	    # If there is no dlname, no dlopen support or we're linking
2441 | 	fi # $pass = dlopen
2494 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2871 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2872 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
3029 |       if test "$pass" != dlopen; then
3131 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3198 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3838 | 	    $echo "*** a static module, that should work as long as the dlopening"
3839 | 	    $echo "*** application is linked with the -dlopen flag."
3857 | 	    $echo "*** or is declared to -dlopen it."
4271 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4405 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4406 | 	   test "$dlopen_self_static" = unknown; then
4407 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5759 | # The name that we can dlopen(3).
5782 | # Files to dlopen/dlpreopen
5783 | dlopen='$dlfiles'
6398 |     # Handle -dlopen flags immediately.
6427 | 	# Skip this library if it cannot be dlopened.
6454 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6814 |   -dlopen FILE      add the directory containing FILE to the library path
6816 | This mode sets the library path environment variable according to \`-dlopen'
6865 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6874 |   -module           build a library that can dlopened
{% endraw %}

```
### build/libtool.m4

```

{% raw %}
190 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
928 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
931 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
987 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1016 | ])# _LT_AC_TRY_DLOPEN_SELF
1019 | # AC_LIBTOOL_DLOPEN_SELF
1021 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1023 | if test "x$enable_dlopen" != xyes; then
1024 |   enable_dlopen=unknown
1025 |   enable_dlopen_self=unknown
1026 |   enable_dlopen_self_static=unknown
1028 |   lt_cv_dlopen=no
1029 |   lt_cv_dlopen_libs=
1033 |     lt_cv_dlopen="load_add_on"
1034 |     lt_cv_dlopen_libs=
1035 |     lt_cv_dlopen_self=yes
1039 |     lt_cv_dlopen="LoadLibrary"
1040 |     lt_cv_dlopen_libs=
1044 |     lt_cv_dlopen="dlopen"
1045 |     lt_cv_dlopen_libs=
1050 |     AC_CHECK_LIB([dl], [dlopen],
1051 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1052 |     lt_cv_dlopen="dyld"
1053 |     lt_cv_dlopen_libs=
1054 |     lt_cv_dlopen_self=yes
1060 | 	  [lt_cv_dlopen="shl_load"],
1062 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1063 | 	[AC_CHECK_FUNC([dlopen],
1064 | 	      [lt_cv_dlopen="dlopen"],
1065 | 	  [AC_CHECK_LIB([dl], [dlopen],
1066 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1067 | 	    [AC_CHECK_LIB([svld], [dlopen],
1068 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1070 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1079 |   if test "x$lt_cv_dlopen" != xno; then
1080 |     enable_dlopen=yes
1082 |     enable_dlopen=no
1085 |   case $lt_cv_dlopen in
1086 |   dlopen)
1094 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1096 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1097 | 	  lt_cv_dlopen_self, [dnl
1098 | 	  _LT_AC_TRY_DLOPEN_SELF(
1099 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1100 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1103 |     if test "x$lt_cv_dlopen_self" = xyes; then
1105 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1106 |     	  lt_cv_dlopen_self_static, [dnl
1107 | 	  _LT_AC_TRY_DLOPEN_SELF(
1108 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1109 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1119 |   case $lt_cv_dlopen_self in
1120 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1121 |   *) enable_dlopen_self=unknown ;;
1124 |   case $lt_cv_dlopen_self_static in
1125 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1126 |   *) enable_dlopen_self_static=unknown ;;
1129 | ])# AC_LIBTOOL_DLOPEN_SELF
2003 | # AC_LIBTOOL_DLOPEN
2005 | # enable checks for dlopen support
2006 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2008 | ])# AC_LIBTOOL_DLOPEN
2766 | AC_LIBTOOL_DLOPEN_SELF
4280 | # Whether dlopen is supported.
4281 | dlopen_support=$enable_dlopen
4283 | # Whether dlopen of programs is supported.
4284 | dlopen_self=$enable_dlopen_self
4286 | # Whether dlopen of statically linked programs is supported.
4287 | dlopen_self_static=$enable_dlopen_self_static
4295 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### ext/sqlite3/libsqlite/sqlite3.c

```cpp

{% raw %}
2391 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
15986 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
22415 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
22416 |   return pVfs->xDlOpen(pVfs, zPath);
38875 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
38877 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
38882 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
38925 |   #define unixDlOpen  0
40308 |     unixDlOpen,           /* xDlOpen */                     \
46300 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
46307 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46312 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46322 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
46337 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
46359 |   #define winDlOpen  0
46577 |     winDlOpen,             /* xDlOpen */
46602 |     winDlOpen,             /* xDlOpen */
46627 |     winDlOpen,             /* xDlOpen */
46652 |     winDlOpen,             /* xDlOpen */
46787 | static void *memdbDlOpen(sqlite3_vfs*, const char *zFilename);
46808 |   memdbDlOpen,                 /* xDlOpen */
47111 | static void *memdbDlOpen(sqlite3_vfs *pVfs, const char *zPath){
47112 |   return ORIGVFS(pVfs)->xDlOpen(ORIGVFS(pVfs), zPath);
120211 |   handle = sqlite3OsDlOpen(pVfs, zFile);
120216 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
193698 | static void *rbuVfsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
193700 |   return pRealVfs->xDlOpen(pRealVfs, zPath);
193801 |     rbuVfsDlOpen,                 /* xDlOpen */
{% endraw %}

```
### ext/interbase/interbase.c

```cpp

{% raw %}
773 | 	 * By NULLing the dlopen() handle in the module entry, Zend omits the call to dlclose(),
776 | 	 * When reloaded, dlopen() will return the handle of the already loaded module. The module will
{% endraw %}

```
### Zend/Zend.m4

```

{% raw %}
66 | AC_CHECK_LIB(dl, dlopen, [LIBS="-ldl $LIBS"])
67 | AC_CHECK_FUNC(dlopen,[AC_DEFINE(HAVE_LIBDL, 1,[ ])])
75 | _LT_AC_TRY_DLOPEN_SELF([
{% endraw %}

```
### Zend/zend_portability.h

```cpp

{% raw %}
144 | #  define DL_LOAD(libname)			dlopen(libname, RTLD_LAZY | RTLD_GLOBAL | RTLD_GROUP | RTLD_WORLD | RTLD_PARENT)
146 | #  define DL_LOAD(libname)			dlopen(libname, RTLD_LAZY | RTLD_GLOBAL | RTLD_DEEPBIND)
148 | #  define DL_LOAD(libname)			dlopen(libname, RTLD_LAZY | RTLD_GLOBAL)
{% endraw %}

```
### sapi/litespeed/lsapilib.c

```cpp

{% raw %}
781 |     s_liblve = dlopen("liblve.so.0", RTLD_LAZY);
1464 |         void *pthread_lib = dlopen("libpthread.so", RTLD_LAZY);
{% endraw %}

```
### sapi/litespeed/lscriu.c

```cpp

{% raw %}
267 |     if (!(lib_handle = dlopen(last = "liblscapi.so", RTLD_LAZY)) /*||
268 |         !(pthread_lib_handle = dlopen(last = "libpthread.so", RTLD_LAZY))*/)
269 |         fprintf(stderr, "LSCRIU (%d): failed to dlopen %s: %s - ignore CRIU\n",
{% endraw %}

```