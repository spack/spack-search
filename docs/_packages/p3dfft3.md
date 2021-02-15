---
name: "p3dfft3"
layout: package
next_package: jellyfish
previous_package: dakota
languages: []
---
## develop
2 / 98 files match

 - [autom4te.cache/traces.5](#autom4tecachetraces5)
 - [autom4te.cache/traces.2](#autom4tecachetraces2)

### autom4te.cache/traces.5

```

{% raw %}
474 | m4trace:/usr/share/aclocal/libtool.m4:1844: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
475 | if test "x$enable_dlopen" != xyes; then
476 |   enable_dlopen=unknown
477 |   enable_dlopen_self=unknown
478 |   enable_dlopen_self_static=unknown
480 |   lt_cv_dlopen=no
481 |   lt_cv_dlopen_libs=
485 |     lt_cv_dlopen="load_add_on"
486 |     lt_cv_dlopen_libs=
487 |     lt_cv_dlopen_self=yes
491 |     lt_cv_dlopen="LoadLibrary"
492 |     lt_cv_dlopen_libs=
496 |     lt_cv_dlopen="dlopen"
497 |     lt_cv_dlopen_libs=
502 |     AC_CHECK_LIB([dl], [dlopen],
503 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
504 |     lt_cv_dlopen="dyld"
505 |     lt_cv_dlopen_libs=
506 |     lt_cv_dlopen_self=yes
512 | 	  [lt_cv_dlopen="shl_load"],
514 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
515 | 	[AC_CHECK_FUNC([dlopen],
516 | 	      [lt_cv_dlopen="dlopen"],
517 | 	  [AC_CHECK_LIB([dl], [dlopen],
518 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
519 | 	    [AC_CHECK_LIB([svld], [dlopen],
520 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
522 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
531 |   if test "x$lt_cv_dlopen" != xno; then
532 |     enable_dlopen=yes
534 |     enable_dlopen=no
537 |   case $lt_cv_dlopen in
538 |   dlopen)
546 |     LIBS="$lt_cv_dlopen_libs $LIBS"
548 |     AC_CACHE_CHECK([whether a program can dlopen itself],
549 | 	  lt_cv_dlopen_self, [dnl
550 | 	  _LT_TRY_DLOPEN_SELF(
551 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
552 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
555 |     if test "x$lt_cv_dlopen_self" = xyes; then
557 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
558 | 	  lt_cv_dlopen_self_static, [dnl
559 | 	  _LT_TRY_DLOPEN_SELF(
560 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
561 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
571 |   case $lt_cv_dlopen_self in
572 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
573 |   *) enable_dlopen_self=unknown ;;
576 |   case $lt_cv_dlopen_self_static in
577 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
578 |   *) enable_dlopen_self_static=unknown ;;
581 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
582 | 	 [Whether dlopen is supported])
583 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
584 | 	 [Whether dlopen of programs is supported])
585 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
586 | 	 [Whether dlopen of statically linked programs is supported])
588 | m4trace:/usr/share/aclocal/libtool.m4:1961: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
589 | m4trace:/usr/share/aclocal/libtool.m4:1961: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
591 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1065 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1109 | eval "LTDLOPEN=\"$libname_spec\""
1110 | AC_SUBST([LTDLOPEN])
1112 | m4trace:/usr/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1113 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1114 |   [lt_cv_sys_dlopen_deplibs],
1115 |   [# PORTME does your system automatically load deplibs for dlopen?
1119 |   lt_cv_sys_dlopen_deplibs=unknown
1124 |     lt_cv_sys_dlopen_deplibs=unknown
1127 |     lt_cv_sys_dlopen_deplibs=yes
1132 |       lt_cv_sys_dlopen_deplibs=no
1139 |     lt_cv_sys_dlopen_deplibs=yes
1142 |     lt_cv_sys_dlopen_deplibs=yes
1146 |     lt_cv_sys_dlopen_deplibs=yes
1149 |     lt_cv_sys_dlopen_deplibs=yes
1152 |     lt_cv_sys_dlopen_deplibs=yes
1157 |     lt_cv_sys_dlopen_deplibs=unknown
1161 |     # at 6.2 and later dlopen does load deplibs.
1162 |     lt_cv_sys_dlopen_deplibs=yes
1165 |     lt_cv_sys_dlopen_deplibs=yes
1168 |     lt_cv_sys_dlopen_deplibs=yes
1171 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1174 |     lt_cv_sys_dlopen_deplibs=no
1177 |     # dlopen *does* load deplibs and with the right loader patch applied
1183 |     lt_cv_sys_dlopen_deplibs=unknown
1190 |     lt_cv_sys_dlopen_deplibs=yes
1193 |     lt_cv_sys_dlopen_deplibs=yes
1196 |     lt_cv_sys_dlopen_deplibs=yes
1199 |     libltdl_cv_sys_dlopen_deplibs=yes
1203 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
1204 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1205 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1208 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1209 | m4trace:/usr/share/aclocal/ltdl.m4:542: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1211 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1277 | LIBADD_DLOPEN=
1278 | AC_SEARCH_LIBS([dlopen], [dl],
1281 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
1282 | 	  LIBADD_DLOPEN="-ldl"
1284 | 	libltdl_cv_lib_dl_dlopen="yes"
1285 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1289 |     ]], [[dlopen(0, 0);]])],
1292 | 	    libltdl_cv_func_dlopen="yes"
1293 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1294 | 	[AC_CHECK_LIB([svld], [dlopen],
1297 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
1298 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1299 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
1302 |   LIBS="$LIBS $LIBADD_DLOPEN"
1306 | AC_SUBST([LIBADD_DLOPEN])
1312 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1316 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1326 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1329 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1333 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1340 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1356 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1405 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
1406 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
1411 |           LIBS="$LIBS $LIBADD_DLOPEN"
1412 | 	  _LT_TRY_DLOPEN_SELF(
1430 | m4trace:/usr/share/aclocal/ltoptions.m4:111: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1433 | put the `dlopen' option into LT_INIT's first parameter.])
1435 | m4trace:/usr/share/aclocal/ltoptions.m4:111: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1437 | _LT_SET_OPTION([LT_INIT], [dlopen])
1440 | put the `dlopen' option into LT_INIT's first parameter.])
1532 | m4trace:/usr/share/aclocal/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
{% endraw %}

```
### autom4te.cache/traces.2

```

{% raw %}
411 | m4trace:/opt/gnu/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
412 | if test yes != "$enable_dlopen"; then
413 |   enable_dlopen=unknown
414 |   enable_dlopen_self=unknown
415 |   enable_dlopen_self_static=unknown
417 |   lt_cv_dlopen=no
418 |   lt_cv_dlopen_libs=
422 |     lt_cv_dlopen=load_add_on
423 |     lt_cv_dlopen_libs=
424 |     lt_cv_dlopen_self=yes
428 |     lt_cv_dlopen=LoadLibrary
429 |     lt_cv_dlopen_libs=
433 |     lt_cv_dlopen=dlopen
434 |     lt_cv_dlopen_libs=
439 |     AC_CHECK_LIB([dl], [dlopen],
440 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
441 |     lt_cv_dlopen=dyld
442 |     lt_cv_dlopen_libs=
443 |     lt_cv_dlopen_self=yes
450 |     lt_cv_dlopen=dlopen
451 |     lt_cv_dlopen_libs=
452 |     lt_cv_dlopen_self=no
457 | 	  [lt_cv_dlopen=shl_load],
459 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
460 | 	[AC_CHECK_FUNC([dlopen],
461 | 	      [lt_cv_dlopen=dlopen],
462 | 	  [AC_CHECK_LIB([dl], [dlopen],
463 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
464 | 	    [AC_CHECK_LIB([svld], [dlopen],
465 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
467 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
476 |   if test no = "$lt_cv_dlopen"; then
477 |     enable_dlopen=no
479 |     enable_dlopen=yes
482 |   case $lt_cv_dlopen in
483 |   dlopen)
491 |     LIBS="$lt_cv_dlopen_libs $LIBS"
493 |     AC_CACHE_CHECK([whether a program can dlopen itself],
494 | 	  lt_cv_dlopen_self, [dnl
495 | 	  _LT_TRY_DLOPEN_SELF(
496 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
497 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
500 |     if test yes = "$lt_cv_dlopen_self"; then
502 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
503 | 	  lt_cv_dlopen_self_static, [dnl
504 | 	  _LT_TRY_DLOPEN_SELF(
505 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
506 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
516 |   case $lt_cv_dlopen_self in
517 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
518 |   *) enable_dlopen_self=unknown ;;
521 |   case $lt_cv_dlopen_self_static in
522 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
523 |   *) enable_dlopen_self_static=unknown ;;
526 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
527 | 	 [Whether dlopen is supported])
528 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
529 | 	 [Whether dlopen of programs is supported])
530 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
531 | 	 [Whether dlopen of statically linked programs is supported])
533 | m4trace:/opt/gnu/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/opt/gnu/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/opt/gnu/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1134 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1135 |   [lt_cv_sys_dlopen_deplibs],
1136 |   [# PORTME does your system automatically load deplibs for dlopen?
1140 |   lt_cv_sys_dlopen_deplibs=unknown
1145 |     lt_cv_sys_dlopen_deplibs=unknown
1148 |     lt_cv_sys_dlopen_deplibs=yes
1153 |       lt_cv_sys_dlopen_deplibs=no
1158 |     lt_cv_sys_dlopen_deplibs=yes
1163 |     lt_cv_sys_dlopen_deplibs=yes
1166 |     lt_cv_sys_dlopen_deplibs=yes
1170 |     lt_cv_sys_dlopen_deplibs=yes
1173 |     lt_cv_sys_dlopen_deplibs=yes
1176 |     lt_cv_sys_dlopen_deplibs=yes
1181 |     lt_cv_sys_dlopen_deplibs=unknown
1185 |     # at 6.2 and later dlopen does load deplibs.
1186 |     lt_cv_sys_dlopen_deplibs=yes
1189 |     lt_cv_sys_dlopen_deplibs=yes
1192 |     lt_cv_sys_dlopen_deplibs=yes
1195 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1198 |     lt_cv_sys_dlopen_deplibs=no
1201 |     # dlopen *does* load deplibs and with the right loader patch applied
1207 |     lt_cv_sys_dlopen_deplibs=unknown
1214 |     lt_cv_sys_dlopen_deplibs=yes
1217 |     lt_cv_sys_dlopen_deplibs=yes
1220 |     lt_cv_sys_dlopen_deplibs=yes
1223 |     libltdl_cv_sys_dlopen_deplibs=yes
1227 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1228 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1229 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1232 | m4trace:/opt/gnu/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/opt/gnu/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1235 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1307 | LIBADD_DLOPEN=
1308 | AC_SEARCH_LIBS([dlopen], [dl],
1311 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1312 | 	  LIBADD_DLOPEN=-ldl
1314 | 	libltdl_cv_lib_dl_dlopen=yes
1315 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1319 |     ]], [[dlopen(0, 0);]])],
1322 | 	    libltdl_cv_func_dlopen=yes
1323 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1324 | 	[AC_CHECK_LIB([svld], [dlopen],
1327 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1328 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1329 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1332 |   LIBS="$LIBS $LIBADD_DLOPEN"
1336 | AC_SUBST([LIBADD_DLOPEN])
1342 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1346 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1356 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1359 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1363 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1370 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1386 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1438 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
1443 |       LIBS="$LIBS $LIBADD_DLOPEN"
1501 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1543 | m4trace:/opt/gnu/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/opt/gnu/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/opt/gnu/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
{% endraw %}

```