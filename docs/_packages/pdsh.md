---
name: "pdsh"
layout: package
next_package: npm
previous_package: mysql
languages: ['cpp', 'bash']
---
## 2.31
9 / 162 files match

 - [config.h.in](#confighin)
 - [aclocal.m4](#aclocalm4)
 - [config/libtool.m4](#configlibtoolm4)
 - [config/ltmain.sh](#configltmainsh)
 - [src/qsnet/qswutil.c](#srcqsnetqswutilc)
 - [src/pdsh/opt.c](#srcpdshoptc)
 - [src/pdsh/ltdl.h](#srcpdshltdlh)
 - [src/pdsh/ltdl.c](#srcpdshltdlc)
 - [src/pdsh/mod.c](#srcpdshmodc)

### config.h.in

```

{% raw %}
302 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
303 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### aclocal.m4

```

{% raw %}
84 | AC_REQUIRE([AC_LTDL_SYS_DLOPEN_DEPLIBS])
111 | # AC_LTDL_SYS_DLOPEN_DEPLIBS
113 | AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS],
115 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
116 |   [libltdl_cv_sys_dlopen_deplibs],
117 |   [# PORTME does your system automatically load deplibs for dlopen?
121 |   libltdl_cv_sys_dlopen_deplibs=unknown
126 |     libltdl_cv_sys_dlopen_deplibs=unknown
129 |     libltdl_cv_sys_dlopen_deplibs=yes
134 |     libltdl_cv_sys_dlopen_deplibs=yes
138 |     libltdl_cv_sys_dlopen_deplibs=yes
141 |     libltdl_cv_sys_dlopen_deplibs=yes
144 |     libltdl_cv_sys_dlopen_deplibs=yes
149 |     libltdl_cv_sys_dlopen_deplibs=unknown
153 |     # at 6.2 and later dlopen does load deplibs.
154 |     libltdl_cv_sys_dlopen_deplibs=yes
157 |     libltdl_cv_sys_dlopen_deplibs=yes
160 |     libltdl_cv_sys_dlopen_deplibs=yes
163 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
166 |     libltdl_cv_sys_dlopen_deplibs=no
169 |     # dlopen *does* load deplibs and with the right loader patch applied
175 |     libltdl_cv_sys_dlopen_deplibs=unknown
182 |     libltdl_cv_sys_dlopen_deplibs=yes
185 |     libltdl_cv_sys_dlopen_deplibs=yes
188 |     libltdl_cv_sys_dlopen_deplibs=yes
192 | if test "$libltdl_cv_sys_dlopen_deplibs" != yes; then
193 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
194 |     [Define if the OS needs help to load dependent libraries for dlopen().])
196 | ])# AC_LTDL_SYS_DLOPEN_DEPLIBS
280 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
309 |     [AC_CHECK_LIB([dl], [dlopen],
312 | 	        LIBADD_DL="-ldl" libltdl_cv_lib_dl_dlopen="yes"],
317 | 	[dlopen(0, 0);],
319 | 		             [Define if you have the libdl library or equivalent.]) libltdl_cv_func_dlopen="yes"],
320 | 	[AC_CHECK_LIB([svld], [dlopen],
323 | 	            LIBADD_DL="-lsvld" libltdl_cv_func_dlopen="yes"],
338 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
392 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
393 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
399 | 	  _LT_AC_TRY_DLOPEN_SELF(
{% endraw %}

```
### config/libtool.m4

```

{% raw %}
199 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
814 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
817 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
873 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
902 | ])# _LT_AC_TRY_DLOPEN_SELF
905 | # AC_LIBTOOL_DLOPEN_SELF
907 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
909 | if test "x$enable_dlopen" != xyes; then
910 |   enable_dlopen=unknown
911 |   enable_dlopen_self=unknown
912 |   enable_dlopen_self_static=unknown
914 |   lt_cv_dlopen=no
915 |   lt_cv_dlopen_libs=
919 |     lt_cv_dlopen="load_add_on"
920 |     lt_cv_dlopen_libs=
921 |     lt_cv_dlopen_self=yes
925 |     lt_cv_dlopen="LoadLibrary"
926 |     lt_cv_dlopen_libs=
930 |     lt_cv_dlopen="dlopen"
931 |     lt_cv_dlopen_libs=
936 |     AC_CHECK_LIB([dl], [dlopen],
937 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
938 |     lt_cv_dlopen="dyld"
939 |     lt_cv_dlopen_libs=
940 |     lt_cv_dlopen_self=yes
946 | 	  [lt_cv_dlopen="shl_load"],
948 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
949 | 	[AC_CHECK_FUNC([dlopen],
950 | 	      [lt_cv_dlopen="dlopen"],
951 | 	  [AC_CHECK_LIB([dl], [dlopen],
952 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
953 | 	    [AC_CHECK_LIB([svld], [dlopen],
954 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
956 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
965 |   if test "x$lt_cv_dlopen" != xno; then
966 |     enable_dlopen=yes
968 |     enable_dlopen=no
971 |   case $lt_cv_dlopen in
972 |   dlopen)
980 |     LIBS="$lt_cv_dlopen_libs $LIBS"
982 |     AC_CACHE_CHECK([whether a program can dlopen itself],
983 | 	  lt_cv_dlopen_self, [dnl
984 | 	  _LT_AC_TRY_DLOPEN_SELF(
985 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
986 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
989 |     if test "x$lt_cv_dlopen_self" = xyes; then
991 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
992 |     	  lt_cv_dlopen_self_static, [dnl
993 | 	  _LT_AC_TRY_DLOPEN_SELF(
994 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
995 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1005 |   case $lt_cv_dlopen_self in
1006 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1007 |   *) enable_dlopen_self=unknown ;;
1010 |   case $lt_cv_dlopen_self_static in
1011 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1012 |   *) enable_dlopen_self_static=unknown ;;
1015 | ])# AC_LIBTOOL_DLOPEN_SELF
1900 | # AC_LIBTOOL_DLOPEN
1902 | # enable checks for dlopen support
1903 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1905 | ])# AC_LIBTOOL_DLOPEN
2697 | AC_LIBTOOL_DLOPEN_SELF
4376 | # Whether dlopen is supported.
4377 | dlopen_support=$enable_dlopen
4379 | # Whether dlopen of programs is supported.
4380 | dlopen_self=$enable_dlopen_self
4382 | # Whether dlopen of statically linked programs is supported.
4383 | dlopen_self_static=$enable_dlopen_self_static
4391 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1146 | 	    dlopen_self=$dlopen_self_static
1151 | 	    dlopen_self=$dlopen_self_static
1207 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1299 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1456 |       -dlopen)
1843 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1916 | 	  # This library was specified with -dlopen.
2057 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2069 | 	passes="conv scan dlopen dlpreopen link"
2082 | 	dlopen) libs="$dlfiles" ;;
2090 |       if test "$pass" = dlopen; then
2269 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2270 | 	      # If there is no dlopen support or we're linking statically,
2303 | 	dlopen=
2324 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2367 | 	# This library was specified with -dlopen.
2368 | 	if test "$pass" = dlopen; then
2370 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2374 | 	     test "$dlopen_support" != yes ||
2376 | 	    # If there is no dlname, no dlopen support or we're linking
2385 | 	fi # $pass = dlopen
2438 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2813 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2814 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2965 |       if test "$pass" != dlopen; then
3066 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3133 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3776 | 	    $echo "*** a static module, that should work as long as the dlopening"
3777 | 	    $echo "*** application is linked with the -dlopen flag."
3795 | 	    $echo "*** or is declared to -dlopen it."
4205 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4337 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4338 | 	   test "$dlopen_self_static" = unknown; then
4339 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5677 | # The name that we can dlopen(3).
5700 | # Files to dlopen/dlpreopen
5701 | dlopen='$dlfiles'
6316 |     # Handle -dlopen flags immediately.
6345 | 	# Skip this library if it cannot be dlopened.
6370 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6730 |   -dlopen FILE      add the directory containing FILE to the library path
6732 | This mode sets the library path environment variable according to \`-dlopen'
6781 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6790 |   -module           build a library that can dlopened
{% endraw %}

```
### src/qsnet/qswutil.c

```cpp

{% raw %}
192 |  * Use dlopen () for libelan3.so (when needed)
268 |     if (!(elan3h = dlopen ("libelan3.so", RTLD_LAZY))) {
{% endraw %}

```
### src/pdsh/opt.c

```cpp

{% raw %}
499 |      *   dlopened modules.
{% endraw %}

```
### src/pdsh/ltdl.h

```cpp

{% raw %}
0 | /* ltdl.h -- generic dlopen functions
169 | /* Portable libltdl versions of the system dlopen() API. */
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
244 |   int	ref_count;		/* number of times lt_dlopened minus
314 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available")	\
{% endraw %}

```
### src/pdsh/ltdl.c

```cpp

{% raw %}
0 | /* ltdl.c -- system independent dlopen wrapper
842 |   lt_dlloader	       *loader;		/* dlopening interface */
1048 | /* --- DLOPEN() INTERFACE LOADER --- */
1053 | /* dynamic linking with dlopen/dlsym */
1109 |   lt_module   module   = dlopen (filename, LT_GLOBAL | LT_LAZY_OR_NOW);
2182 | static	int	try_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2184 | static	int	tryall_dlopen	      LT_PARAMS((lt_dlhandle *handle,
2227 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_dl, "dlopen");
2230 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_shl, "dlopen");
2233 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_wll, "dlopen");
2236 |       errors += lt_dlloader_add (lt_dlloader_next (0), &sys_bedl, "dlopen");
2254 | 	  LT_DLMUTEX_SETERROR (LT_DLSTRERROR (DLOPEN_NOT_SUPPORTED));
2372 | tryall_dlopen (handle, filename, useloader)
2391 |       /* try to dlopen the program itself? */
2475 | tryall_dlopen_module (handle, prefix, dirname, dlname)
2513 |       error += tryall_dlopen_module (handle,
2516 |   else if (tryall_dlopen (handle, filename, NULL) != 0)
2535 |      we want the preopened version of it, even if a dlopenable
2537 |   if (old_name && tryall_dlopen (handle, old_name, "dlpreload") == 0)
2548 | 	  if (tryall_dlopen_module (handle,
2556 | 	  if (tryall_dlopen_module (handle, dir, objdir, dlname) == 0)
2562 | 	  if (dir && (tryall_dlopen_module (handle,
2799 |   /* Try to dlopen the file, but do not continue searching in any
2801 |   if (tryall_dlopen (handle, filename,NULL) != 0)
2830 | #if LTDL_DLOPEN_DEPLIBS
2840 | #if LTDL_DLOPEN_DEPLIBS
2957 | 	  handle->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
3059 | try_dlopen (phandle, filename)
3077 |   /* dlopen self? */
3090 |       if (tryall_dlopen (&newhandle, 0, NULL) != 0)
3396 |           if (tryall_dlopen (&newhandle, filename, NULL) != 0)
3435 | lt_dlopen (filename)
3440 |   /* Just incase we missed a code path in try_dlopen() that reports
3442 |   if (try_dlopen (&handle, filename) != 0)
3467 | lt_dlopenext (filename)
3478 |       return lt_dlopen (filename);
3494 |       return lt_dlopen (filename);
3504 |   errors = try_dlopen (&handle, tmp);
3534 |   errors = try_dlopen (&handle, tmp);
3748 |    passing to lt_dlopenext.  The extensions are stripped so that
3751 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### src/pdsh/mod.c

```cpp

{% raw %}
814 |     if (!(mod->handle = lt_dlopen(fq_path)))
{% endraw %}

```