---
name: "libtool"
layout: package
next_package: caliper
previous_package: osi
languages: ['cpp', 'bash']
---
## 2.4.6
49 / 327 files match

 - [configure.ac](#configureac)
 - [libtoolize.in](#libtoolizein)
 - [config-h.in](#config-hin)
 - [Makefile.am](#makefileam)
 - [Makefile.in](#makefilein)
 - [tests/stresstest.at](#testsstresstestat)
 - [tests/resident.at](#testsresidentat)
 - [tests/configure-iface.at](#testsconfigure-ifaceat)
 - [tests/lalib-syntax.at](#testslalib-syntaxat)
 - [tests/execute-mode.at](#testsexecute-modeat)
 - [tests/old-ltdl-iface.at](#testsold-ltdl-ifaceat)
 - [tests/lt_dlopen.at](#testslt_dlopenat)
 - [tests/dlloader-api.at](#testsdlloader-apiat)
 - [tests/darwin.at](#testsdarwinat)
 - [tests/ltdl-libdir.at](#testsltdl-libdirat)
 - [tests/mdemo.at](#testsmdemoat)
 - [tests/lt_dladvise.at](#testslt_dladviseat)
 - [tests/static.at](#testsstaticat)
 - [tests/libtoolize.at](#testslibtoolizeat)
 - [tests/loadlibrary.at](#testsloadlibraryat)
 - [tests/no-executables.at](#testsno-executablesat)
 - [tests/lt_dlopenext.at](#testslt_dlopenextat)
 - [tests/need_lib_prefix.at](#testsneed_lib_prefixat)
 - [tests/lt_dlexit.at](#testslt_dlexitat)
 - [tests/exceptions.at](#testsexceptionsat)
 - [tests/lt_dlopen_a.at](#testslt_dlopen_aat)
 - [tests/old-m4-iface.at](#testsold-m4-ifaceat)
 - [tests/testsuite.at](#teststestsuiteat)
 - [tests/demo.at](#testsdemoat)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/ltdl.m4](#m4ltdlm4)
 - [libltdl/configure.ac](#libltdlconfigureac)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/config-h.in](#libltdlconfig-hin)
 - [libltdl/ltdl.mk](#libltdlltdlmk)
 - [libltdl/Makefile.am](#libltdlmakefileam)
 - [libltdl/Makefile.in](#libltdlmakefilein)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)
 - [build-aux/ltmain.in](#build-auxltmainin)
 - [build-aux/ltmain.sh](#build-auxltmainsh)
 - [doc/libtool.info](#doclibtoolinfo)
 - [doc/libtool.info-2](#doclibtoolinfo-2)
 - [doc/libtool.texi](#doclibtooltexi)
 - [doc/libtool.info-1](#doclibtoolinfo-1)

### configure.ac

```

{% raw %}
151 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### libtoolize.in

```

{% raw %}
1893 |   all_pkgltdl_files="COPYING.LIB Makefile Makefile.in Makefile.inc Makefile.am README acinclude.m4 aclocal.m4 argz_.h argz.c config.h.in config-h.in configure configure.ac configure.in libltdl/lt__alloc.h libltdl/lt__argz.h libltdl/lt__dirent.h libltdl/lt__glibc.h libltdl/lt__private.h libltdl/lt__strl.h libltdl/lt_dlloader.h libltdl/lt_error.h libltdl/lt_system.h libltdl/slist.h loaders/dld_link.c loaders/dlopen.c loaders/dyld.c loaders/load_add_on.c loaders/loadlibrary.c loaders/preopen.c loaders/shl_load.c lt__alloc.c lt__argz.c lt__dirent.c lt__strl.c lt_dlloader.c lt_error.c ltdl.c ltdl.h ltdl.mk slist.c"
{% endraw %}

```
### config-h.in

```

{% raw %}
117 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
118 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### Makefile.am

```

{% raw %}
464 | 		  loaders/dlopen.c \
696 | 		  tests/lt_dlopen.at \
697 | 		  tests/lt_dlopen_a.at \
698 | 		  tests/lt_dlopenext.at \
{% endraw %}

```
### Makefile.in

```

{% raw %}
164 | libltdl_dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
165 | am_libltdl_dlopen_la_OBJECTS = libltdl/loaders/dlopen.lo
166 | libltdl_dlopen_la_OBJECTS = $(am_libltdl_dlopen_la_OBJECTS)
167 | libltdl_dlopen_la_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC \
169 | 	$(AM_CFLAGS) $(CFLAGS) $(libltdl_dlopen_la_LDFLAGS) $(LDFLAGS) \
261 | SOURCES = $(libltdl_dld_link_la_SOURCES) $(libltdl_dlopen_la_SOURCES) \
268 | 	$(libltdl_dlopen_la_SOURCES) $(libltdl_dyld_la_SOURCES) \
482 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
489 | LTDLOPEN = @LTDLOPEN@
620 | EXTRA_LTLIBRARIES = libltdl/dlopen.la libltdl/dld_link.la \
733 | libltdl_libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
738 | libltdl_libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
742 | libltdl_dlopen_la_SOURCES = libltdl/loaders/dlopen.c
743 | libltdl_dlopen_la_LDFLAGS = -module -avoid-version
744 | libltdl_dlopen_la_LIBADD = $(LIBADD_DLOPEN)
829 | 		  loaders/dlopen.c \
923 | 		  tests/lt_dlopen.at \
924 | 		  tests/lt_dlopen_a.at \
925 | 		  tests/lt_dlopenext.at \
1107 | libltdl/loaders/dlopen.lo: libltdl/loaders/$(am__dirstamp) \
1110 | libltdl/dlopen.la: $(libltdl_dlopen_la_OBJECTS) $(libltdl_dlopen_la_DEPENDENCIES) $(EXTRA_libltdl_dlopen_la_DEPENDENCIES) libltdl/$(am__dirstamp)
1111 | 	$(AM_V_CCLD)$(libltdl_dlopen_la_LINK)  $(libltdl_dlopen_la_OBJECTS) $(libltdl_dlopen_la_LIBADD) $(LIBS)
1227 | @AMDEP_TRUE@@am__include@ @am__quote@libltdl/loaders/$(DEPDIR)/dlopen.Plo@am__quote@
{% endraw %}

```
### tests/stresstest.at

```

{% raw %}
279 | 	    LT_AT_CHECK([$LIBTOOL --mode=link $CC $CFLAGS $LDFLAGS $st -o "$rel"sub3/dlself$EXEEXT "$rel"sub3/dlself$mst.lo "$rel"sub2/liba.la sub/b.lo -dlopen self $l10],
{% endraw %}

```
### tests/resident.at

```

{% raw %}
58 |       plugin_handle = lt_dlopenadvise (argv[1], advise);
142 | 	 [-dlopen plugin.la $LIBLTDL],
{% endraw %}

```
### tests/configure-iface.at

```

{% raw %}
50 |   handle = lt_dlopenext ("libmodule");
115 | LT_INIT([dlopen])
135 | main_LDFLAGS		= -dlopen libmodule.la
189 | LT_INIT([dlopen])
207 | main_LDFLAGS		= -dlopen libmodule.la
233 | LT_AT_NOINST_EXEC_CHECK([./main], [-dlopen libmodule.la], [], [expout], [])
256 | LT_INIT([dlopen])
276 | main_LDFLAGS		= -dlopen libmodule.la
290 | LT_AT_NOINST_EXEC_CHECK([./main], [-dlopen libmodule.la], [], [expout], [])
309 | AC_LIBTOOL_DLOPEN
{% endraw %}

```
### tests/lalib-syntax.at

```

{% raw %}
47 |   plugin_handle = lt_dlopenext (argv[1]);
{% endraw %}

```
### tests/execute-mode.at

```

{% raw %}
82 | dlopen=''
146 | # check that stdin works even with -dlopen.
147 | AT_CHECK([echo bar | $LIBTOOL --mode=execute -dlopen libfakelib.la ./lt-wrapper foo],
{% endraw %}

```
### tests/old-ltdl-iface.at

```

{% raw %}
105 | libtoolize: linking file 'ltdl/loaders/dlopen.c'
{% endraw %}

```
### tests/lt_dlopen.at

```

{% raw %}
0 | # lt_dlopen.at -- test libltdl functionality                -*- Autotest -*-
22 | AT_SETUP([lt_dlopen error messages])
49 |   plugin_handle = lt_dlopenext (argv[1]);
95 | 	 [-dlopen good-plugin.la -dlopen missing-symbol-plugin.la $LIBLTDL],
{% endraw %}

```
### tests/dlloader-api.at

```

{% raw %}
283 |   module = lt_dlopen ("/libltdl_dlloader_api_test_first");
287 |       printf ("lt_dlopen failed: %s\n", lt_dlerror ());
304 |   module = lt_dlopen ("./module.la");
308 |       printf ("lt_dlopen failed: %s\n", lt_dlerror ());
330 |   module = lt_dlopen ("/libltdl_dlloader_api_test_last");
334 |       printf ("lt_dlopen failed: %s\n", lt_dlerror ());
350 |   if (lt_dlopen ("no-module"))
352 |       printf ("lt_dlopen unexpectedly opened \"no-module\"\n");
435 | 	 [main.$OBJEXT -dlopen module.la $LIBLTDL],
{% endraw %}

```
### tests/darwin.at

```

{% raw %}
231 | AT_SETUP([darwin can lt_dlopen .dylib and .so files])
336 |     module = lt_dlopenext (argv[1]);
426 | 	 [ltdl-loader.$OBJEXT -dlopen self $LIBLTDL],
{% endraw %}

```
### tests/ltdl-libdir.at

```

{% raw %}
67 |   module = lt_dlopen("./a.la");
70 |     fprintf(stderr, "lt_dlopen failed '%s'\n", lt_dlerror());
{% endraw %}

```
### tests/mdemo.at

```

{% raw %}
45 | LT_INIT([dlopen win32-dll])
94 | libmlib_la_LIBADD = \$(LIBLTDL) "-dlopen" foo1.la "-dlopen" libfoo2.la
102 | # Create a version of mdemo that does dlopen.
105 | ## The quotes around -dlopen below fool automake into accepting it
106 | mdemo_LDADD = \$(LIBLTDL) libsub.la "-dlopen" self \
107 | 		"-dlopen" foo1.la "-dlopen" libfoo2.la
236 |   handle = lt_dlopen(filename);
368 |     handle = lt_dlopenext (filename);
370 |     handle = lt_dlopen (filename);
462 |   handle = lt_dlopen(0);
464 |     fprintf (stderr, "can't dlopen the program!\n");
783 | # Create a version of mdemo2 that links a library that does dlopen.
784 | mdemo2_LDFLAGS = -export-dynamic "-dlopen" force
{% endraw %}

```
### tests/lt_dladvise.at

```

{% raw %}
27 | AT_SETUP([lt_dlopenadvise library loading])
55 |   handle = lt_dlopenadvise (filename, advise);
229 |      global module and the local one, we can't lt_dlopen the local module
320 | dlopenable='resident local global'
327 | # are reporting not able to accept the global hint to lt_dlopenadvise().    #
340 |   dlopenable="$dlopen depend"
375 | for module in $dlopenable; do
376 |   modules="${modules+$modules }-dlopen lib$module.la"
{% endraw %}

```
### tests/static.at

```

{% raw %}
61 | # - TODO: test exposure for dlopened and dlpreopened modules,
{% endraw %}

```
### tests/libtoolize.at

```

{% raw %}
407 | libtoolize: copying file 'ltdl/loaders/dlopen.c'
486 | libtoolize: linking file 'ltdl/loaders/dlopen.c'
585 | libtoolize: copying file 'ltdl/loaders/dlopen.c'
906 | libtoolize: copying file 'ltdl/loaders/dlopen.c'
986 | libtoolize: copying file 'ltdl/loaders/dlopen.c'
1062 | libtoolize: linking file 'ltdl/loaders/dlopen.c'
{% endraw %}

```
### tests/loadlibrary.at

```

{% raw %}
105 |   module = lt_dlopen (argv[1]);
110 |       printf ("lt_dlopen: success!\n");
123 |       printf ("lt_dlopen: failure: %s\n", error);
130 |       printf ("lt_dlopen: standard error (bad): %s\n", error);
136 |       printf ("lt_dlopen: custom error (good): %s\n", error);
{% endraw %}

```
### tests/no-executables.at

```

{% raw %}
56 | # Deal with AC_LIBTOOL_DLOPEN in one of two possible ways:
60 | if ${test_ac_libtool_dlopen-false}; then
63 |     ac_cv_func_dlopen=no
64 |     ac_cv_lib_dl_dlopen=no
65 |     ac_cv_lib_svld_dlopen=no
67 |   AC_LIBTOOL_DLOPEN
76 | LT_AT_CONFIGURE([test_ac_libtool_dlopen=:])
{% endraw %}

```
### tests/lt_dlopenext.at

```

{% raw %}
0 | # lt_dlopenext.at -- test libltdl functionality             -*- Autotest -*-
22 | AT_SETUP([lt_dlopenext error messages])
109 |     module = lt_dlopenext (argv[1]);
202 | 	 [ltdl-loader.$OBJEXT -dlopen self $LIBLTDL],
{% endraw %}

```
### tests/need_lib_prefix.at

```

{% raw %}
57 |   handle = lt_dlopen (filename);
181 | LT_AT_NOINST_EXEC_CHECK([./main], [-dlopen foo1.la -dlopen libfoo2.la],
{% endraw %}

```
### tests/lt_dlexit.at

```

{% raw %}
44 | /* lt_dlopen wrapper */
46 | xdlopen (const char *filename)
48 |   lt_dlhandle handle = lt_dlopen (filename);
91 |   if (!(b1 = xdlopen ("modb1.la"))) return 1;
157 | for dlopen in -dlopen; do
159 |            $dlopen modb1.la $LIBLTDL], [], [ignore], [ignore])
160 |   LT_AT_NOINST_EXEC_CHECK([./main], [-dlopen modb1.la])
{% endraw %}

```
### tests/exceptions.at

```

{% raw %}
295 |   lt_dlhandle handle = lt_dlopenadvise ("module.la", advise);
298 |       std::cerr << "dlopen failed: " << lt_dlerror () << '\n';
381 | 	 [main.$OBJEXT l/liba.la l/libcommon.la -dlopen m/module.la $LIBLTDL -export-dynamic],
384 | LT_AT_NOINST_EXEC_CHECK([./main], [-dlopen m/module.la], [], [ignore], [ignore])
{% endraw %}

```
### tests/lt_dlopen_a.at

```

{% raw %}
0 | # lt_dlopen_a.at -- test libltdl functionality                -*- Autotest -*-
22 | AT_SETUP([lt_dlopen archive])
23 | AT_KEYWORDS([libltdl lt_dlopen_a])
29 | /* This dlopen() in the main executable should override any dlopen()s in
32 |    If that is not the case (or the platform does not use dlopen()) then this
37 | void * dlopen(const char *path, int mode) {
58 |   plugin_handle = lt_dlopenext (argv[1]);
85 | 	 [main.$OBJEXT -dlopen plugin.la $LIBLTDL || exit 77],
{% endraw %}

```
### tests/old-m4-iface.at

```

{% raw %}
120 | AC_LIBTOOL_DLOPEN
146 | 	$(LTLINK) main.@OBJEXT@ -dlopen module.la @LIBLTDL@ @LIBS@
{% endraw %}

```
### tests/testsuite.at

```

{% raw %}
334 | # with '-dlopen' arguments in NOINST_MODULES.  STATUS, STDOUT, and
446 |   module = lt_dlopen("./module.la");
448 |     fprintf (stderr, "error dlopening ./module.la: %s\n", lt_dlerror());
500 | 	$(LTLINK) -o ltdldemo$(EXEEXT) main.lo -dlopen module.la ./]_ARG_DIR[/libltdlc.la
{% endraw %}

```
### tests/demo.at

```

{% raw %}
65 | LT_INIT([dlopen win32-dll])
114 | # Create a version of hell that does a preloaded dlopen.
121 | # Create a script that says that -dlopen is not supported.
126 | 	echo 'echo sorry, -dlopen is unsupported' >> $@
844 | # Create a version of hell that does a preloaded dlopen.
851 | # Create a script that says that -dlopen is not supported.
856 | 	echo 'echo sorry, -dlopen is unsupported' >> $@
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### m4/ltdl.m4

```

{% raw %}
199 | 			  _LT_SHELL_INIT([lt_dlopen_dir=$lt_ltdl_dir])],
200 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir=$lt_ltdl_dir; lt_libobj_prefix=$lt_ltdl_dir/])],
374 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
418 | eval "LTDLOPEN=\"$libname_spec\""
419 | AC_SUBST([LTDLOPEN])
440 | # LT_SYS_DLOPEN_DEPLIBS
442 | AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
444 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
445 |   [lt_cv_sys_dlopen_deplibs],
446 |   [# PORTME does your system automatically load deplibs for dlopen?
450 |   lt_cv_sys_dlopen_deplibs=unknown
455 |     lt_cv_sys_dlopen_deplibs=unknown
458 |     lt_cv_sys_dlopen_deplibs=yes
463 |       lt_cv_sys_dlopen_deplibs=no
468 |     lt_cv_sys_dlopen_deplibs=yes
473 |     lt_cv_sys_dlopen_deplibs=yes
476 |     lt_cv_sys_dlopen_deplibs=yes
480 |     lt_cv_sys_dlopen_deplibs=yes
483 |     lt_cv_sys_dlopen_deplibs=yes
486 |     lt_cv_sys_dlopen_deplibs=yes
491 |     lt_cv_sys_dlopen_deplibs=unknown
495 |     # at 6.2 and later dlopen does load deplibs.
496 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     lt_cv_sys_dlopen_deplibs=yes
505 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
508 |     lt_cv_sys_dlopen_deplibs=no
511 |     # dlopen *does* load deplibs and with the right loader patch applied
517 |     lt_cv_sys_dlopen_deplibs=unknown
524 |     lt_cv_sys_dlopen_deplibs=yes
527 |     lt_cv_sys_dlopen_deplibs=yes
530 |     lt_cv_sys_dlopen_deplibs=yes
533 |     libltdl_cv_sys_dlopen_deplibs=yes
537 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
538 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
539 |     [Define if the OS needs help to load dependent libraries for dlopen().])
541 | ])# LT_SYS_DLOPEN_DEPLIBS
544 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
546 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
635 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
660 | LIBADD_DLOPEN=
661 | AC_SEARCH_LIBS([dlopen], [dl],
664 | 	if test "$ac_cv_search_dlopen" != "none required"; then
665 | 	  LIBADD_DLOPEN=-ldl
667 | 	libltdl_cv_lib_dl_dlopen=yes
668 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
672 |     ]], [[dlopen(0, 0);]])],
675 | 	    libltdl_cv_func_dlopen=yes
676 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
677 | 	[AC_CHECK_LIB([svld], [dlopen],
680 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
681 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
682 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
685 |   LIBS="$LIBS $LIBADD_DLOPEN"
689 | AC_SUBST([LIBADD_DLOPEN])
695 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
699 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
709 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
712 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
716 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
723 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
739 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
804 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
809 |       LIBS="$LIBS $LIBADD_DLOPEN"
867 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
{% endraw %}

```
### libltdl/configure.ac

```

{% raw %}
67 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### libltdl/ltdl.h

```cpp

{% raw %}
0 | /* ltdl.h -- generic dlopen functions
75 | /* Portable libltdl versions of the system dlopen() API. */
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
133 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### libltdl/ltdl.c

```cpp

{% raw %}
0 | /* ltdl.c -- system independent dlopen wrapper
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
175 |    dlopen an application module.  */
214 | #define preloaded_symbols	LT_CONC3(lt_, LTDLOPEN, _LTX_preloaded_symbols)
242 | 	 can use _them_ to lt_dlopen its own modules.  */
251 | 	  errors += lt_dlpreload_open (LT_STR(LTDLOPEN), loader_init_callback);
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
492 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
528 |       error += tryall_dlopen_module (handle, (const char *) 0,
531 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
546 |      we want the preopened version of it, even if a dlopenable
548 |   if (old_name && tryall_dlopen (handle, old_name,
560 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
568 | 	  if (tryall_dlopen_module (handle, dir, objdir,
575 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
791 |   /* Try to dlopen the file, but do not continue searching in any
793 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
815 | #if !defined LTDL_DLOPEN_DEPLIBS
823 | #else /* defined LTDL_DLOPEN_DEPLIBS */
952 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
978 | #endif /* defined LTDL_DLOPEN_DEPLIBS */
1158 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1175 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1182 |   /* dlopen self? */
1194 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1313 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1480 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1623 | lt_dlopen (const char *filename)
1625 |   return lt_dlopenadvise (filename, NULL);
1634 | lt_dlopenext (const char *filename)
1640 |     handle = lt_dlopenadvise (filename, advise);
1648 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1668 |       /* Just incase we missed a code path in try_dlopen() that reports
1670 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1679 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1692 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1703 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1898 |    passing to lt_dlopenext.  The extensions are stripped so that
1901 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### libltdl/config-h.in

```

{% raw %}
117 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
118 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### libltdl/ltdl.mk

```

{% raw %}
77 | libltdl_libltdl_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
83 | libltdl_libltdlc_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
92 | EXTRA_LTLIBRARIES	       += libltdl/dlopen.la \
99 | libltdl_dlopen_la_SOURCES	= libltdl/loaders/dlopen.c
100 | libltdl_dlopen_la_LDFLAGS	= -module -avoid-version
101 | libltdl_dlopen_la_LIBADD	= $(LIBADD_DLOPEN)
{% endraw %}

```
### libltdl/Makefile.am

```

{% raw %}
87 | libltdl_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
93 | libltdlc_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
102 | EXTRA_LTLIBRARIES	       += dlopen.la \
109 | dlopen_la_SOURCES	= loaders/dlopen.c
110 | dlopen_la_LDFLAGS	= -module -avoid-version
111 | dlopen_la_LIBADD	= $(LIBADD_DLOPEN)
{% endraw %}

```
### libltdl/Makefile.in

```

{% raw %}
157 | dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
158 | am_dlopen_la_OBJECTS = loaders/dlopen.lo
159 | dlopen_la_OBJECTS = $(am_dlopen_la_OBJECTS)
160 | dlopen_la_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
162 | 	$(dlopen_la_LDFLAGS) $(LDFLAGS) -o $@
241 | SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
245 | DIST_SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
346 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
353 | LTDLOPEN = @LTDLOPEN@
448 | EXTRA_LTLIBRARIES = dlopen.la dld_link.la dyld.la load_add_on.la \
478 | libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
483 | libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
487 | dlopen_la_SOURCES = loaders/dlopen.c
488 | dlopen_la_LDFLAGS = -module -avoid-version
489 | dlopen_la_LIBADD = $(LIBADD_DLOPEN)
612 | loaders/dlopen.lo: loaders/$(am__dirstamp) \
615 | dlopen.la: $(dlopen_la_OBJECTS) $(dlopen_la_DEPENDENCIES) $(EXTRA_dlopen_la_DEPENDENCIES) 
616 | 	$(AM_V_CCLD)$(dlopen_la_LINK)  $(dlopen_la_OBJECTS) $(dlopen_la_LIBADD) $(LIBS)
670 | @AMDEP_TRUE@@am__include@ @am__quote@loaders/$(DEPDIR)/dlopen.Plo@am__quote@
{% endraw %}

```
### libltdl/loaders/preopen.c

```cpp

{% raw %}
365 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### libltdl/loaders/dlopen.c

```cpp

{% raw %}
0 | /* loader-dlopen.c --  dynamic linking with dlopen/dlsym
38 | #define get_vtable	dlopen_LTX_get_vtable
69 |       vtable->name		= "lt_dlopen";
210 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### libltdl/libltdl/lt__private.h

```cpp

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### libltdl/libltdl/lt_error.h

```cpp

{% raw %}
46 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```
### build-aux/ltmain.in

```

{% raw %}
350 |     opt_dlopen=
411 |         --dlopen|-dlopen)
412 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
528 |       # Only execute mode is allowed to have -dlopen flags.
529 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
530 |         func_error "unrecognized option '-dlopen'"
1756 |   -dlopen FILE      add the directory containing FILE to the library path
1758 | This mode sets the library path environment variable according to '-dlopen'
1813 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
1822 |   -module           build a library that can dlopened
1930 |     # Handle -dlopen flags immediately.
1931 |     for file in $opt_dlopen; do
1950 | 	# Skip this library if it cannot be dlopened.
1977 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
4670 | 	    dlopen_self=$dlopen_self_static
4676 | 	    dlopen_self=$dlopen_self_static
4682 | 	    dlopen_self=$dlopen_self_static
4740 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
4830 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
4997 |       -dlopen)
5431 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
5499 | 	  # This library was specified with -dlopen.
5619 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
5630 | 	passes="conv scan dlopen dlpreopen link"
5656 | 	dlopen) libs=$dlfiles ;;
5684 |       if test dlopen = "$pass"; then
5904 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
5905 | 	      # If there is no dlopen support or we're linking statically,
5933 | 	dlopen=
5963 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6009 | 	# This library was specified with -dlopen.
6010 | 	if test dlopen = "$pass"; then
6012 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
6014 | 	     test yes != "$dlopen_support" ||
6017 | 	    # If there is no dlname, no dlopen support or we're linking
6026 | 	fi # $pass = dlopen
6082 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6084 | 	      # We recover the dlopen module name by 'saving' the la file
6108 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6237 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6238 | 	  dlopenmodule=
6241 | 	      dlopenmodule=$dlpremoduletest
6245 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
6342 | 		    # if the lib is a (non-dlopened) module then we cannot
6346 | 		      if test "X$dlopenmodule" != "X$lib"; then
6498 | 	      echo "*** a static module, that should work as long as the dlopening application"
6499 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6643 |       if test dlopen != "$pass"; then
6773 | 	func_warning "'-dlopen' is ignored for archives"
6840 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
7534 | 	    echo "*** a static module, that should work as long as the dlopening"
7535 | 	    echo "*** application is linked with the -dlopen flag."
7553 | 	    echo "*** or is declared to -dlopen it."
8165 | 	func_warning "'-dlopen' is ignored for objects"
8285 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
8286 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
8967 | # The name that we can dlopen(3).
8996 | # Files to dlopen/dlpreopen
8997 | dlopen='$dlfiles'
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### doc/libtool.info

```

{% raw %}
85 | Node: Dlopened modules129852
88 | Node: Linking with dlopened modules138569
91 | Node: Dlopen issues144868
{% endraw %}

```
### doc/libtool.info-2

```

{% raw %}
35 | * '-weak' option:                        Linking with dlopened modules.
53 | * AC_LIBTOOL_DLOPEN:                     LT_INIT.             (line 204)
67 | * application-level dynamic linking:     Dlopened modules.    (line   6)
201 | * dlclose:                               Dlopened modules.    (line   6)
205 | * dlopen:                                Dlopened modules.    (line   6)
206 | * dlopen <1>:                            Using libltdl.       (line   6)
207 | * dlopening modules:                     Dlopened modules.    (line   6)
208 | * dlopening modules <1>:                 Using libltdl.       (line   6)
209 | * dlopening, pitfalls:                   Dlopen issues.       (line   6)
210 | * dlopen_self:                           libtool script contents.
212 | * dlopen_self_static:                    libtool script contents.
214 | * dlopen_support:                        libtool script contents.
216 | * dlsym:                                 Dlopened modules.    (line   6)
221 | * dynamic linking, applications:         Dlopened modules.    (line   6)
378 | * linking, dlopen:                       Linking with dlopened modules.
380 | * linking, dlpreopen:                    Linking with dlopened modules.
475 | * lt_dlopen:                             Libltdl interface.   (line  71)
476 | * lt_dlopenadvise:                       Libltdl interface.   (line 123)
477 | * lt_dlopenext:                          Libltdl interface.   (line 108)
508 | * LT_SYS_DLOPEN_DEPLIBS:                 Autoconf macros.     (line  68)
509 | * LT_SYS_DLOPEN_SELF:                    Autoconf macros.     (line  62)
557 | * modules, dynamic:                      Dlopened modules.    (line   6)
629 | * pitfalls with dlopen:                  Dlopen issues.       (line   6)
671 | * shl_load:                              Dlopened modules.    (line   6)
720 | * trouble with dlopen:                   Dlopen issues.       (line   6)
{% endraw %}

```
### doc/libtool.texi

```

{% raw %}
80 | * Dlopened modules::            @code{dlopen}ing libtool-created libraries.
81 | * Using libltdl::               Libtool's portable @code{dlopen} wrapper library.
158 | Dlopened modules
160 | * Building modules::            Creating dlopenable objects and libraries.
161 | * Dlpreopening::                Dlopening that works on static platforms.
162 | * Linking with dlopened modules::  Using dlopenable modules in libraries.
163 | * Finding the dlname::          Choosing the right file to @code{dlopen}.
164 | * Dlopen issues::               Unresolved problems that need your attention.
169 | * Modules for libltdl::         Creating modules that can be @code{dlopen}ed.
1017 | (@pxref{Linking executables}) and to help programs with dlopening
1018 | (@pxref{Dlopened modules}).
1461 | @item -dlopen @var{file}
1462 | Same as @option{-dlpreopen @var{file}}, if native dlopening is not
1463 | supported on the host platform (@pxref{Dlopened modules}) or if
1467 | program can @code{dlopen} itself, either by enabling
1480 | (@pxref{Dlopened modules}).
1503 | Creates a library that can be dlopened (@pxref{Dlopened modules}).
1610 | supplies the same interface (@pxref{Linking with dlopened modules}).
1657 | @item -dlopen @var{file}
1662 | @option{-dlopen} flags.
1884 | @samp{LIBADD_DLOPEN} if additional system libraries are required by
1885 | the @samp{dlopen} loader, and @samp{LIBADD_SHL_LOAD} if additional
1913 | @defmac LT_SYS_DLOPEN_SELF
1914 | Tests whether a program can dlopen itself, and then also whether the
1915 | same program can still dlopen itself when statically linked.  Results
1916 | are stored in the shell variables @samp{$enable_dlopen_self} and
1917 | @samp{enable_dlopen_self_static} respectively.
1920 | @defmac LT_SYS_DLOPEN_DEPLIBS
1921 | Define the preprocessor symbol @samp{LTDL_DLOPEN_DEPLIBS} if the
1922 | OS needs help to load dependent libraries for @samp{dlopen} (or
1991 | Since GNU Automake 1.5, the flags @option{-dlopen}
1999 | program_LDADD = "-dlopen" libfoo.la
2172 | @item dlopen
2173 | Enable checking for dlopen support.  This option should be used if
2174 | the package makes use of the @option{-dlopen} and @option{-dlpreopen}
2176 | support dlopening.
2293 | @defmac AC_LIBTOOL_DLOPEN
2294 | This macro is deprecated, the @samp{dlopen} option to @code{LT_INIT} should be
3399 | @node Dlopened modules
3400 | @chapter Dlopened modules
3401 | @findex dlopen
3406 | @cindex dlopening modules
3420 | The application calling functions such as @code{dlopen} that load
3426 | linking as @dfn{dlopening} a module.
3428 | The main benefit to dlopening object modules is the ability to access
3430 | interpreted language.  In fact, dlopen calls are frequently used in
3434 | Libtool provides support for dlopened modules.  However, you should
3436 | @code{LT_INIT} option @samp{dlopen} in @file{configure.ac}.  If this
3437 | option is not given, libtool will assume no dlopening mechanism is
3440 | This chapter discusses how you as a dlopen application developer might
3441 | use libtool to generate dlopen-accessible modules.
3444 | * Building modules::            Creating dlopenable objects and libraries.
3445 | * Dlpreopening::                Dlopening that works on static platforms.
3446 | * Linking with dlopened modules::  Using dlopenable modules in libraries.
3447 | * Finding the dlname::          Choosing the right file to @code{dlopen}.
3448 | * Dlopen issues::               Unresolved problems that need your attention.
3452 | @section Building modules to dlopen
3459 | application program that dlopens other modules or a libtool library
3460 | that will also be dlopened.
3463 | that would later be dlopened by an application, we would add
3473 | references in a library you want to dlopen you will have to use the flag
3475 | linking the executable that calls dlopen:
3485 | Libtool provides special support for dlopening libtool object and
3487 | @emph{even on platforms without any @code{dlopen} and @code{dlsym}
3512 | Dlopening a module, so that the application can resolve its own,
3518 | Libtool emulates @option{-dlopen} on static platforms by linking objects
3521 | you must declare the objects you want your application to dlopen by
3522 | using the @option{-dlopen} or @option{-dlpreopen} flags when you link your
3631 | @node Linking with dlopened modules
3632 | @section Linking with dlopened modules
3633 | @cindex linking, dlopen
3636 | When, say, an interpreter application uses dlopened modules to extend
3640 | dlopen.  For one thing, the dlopening functionality will be tested
3652 | dlpreopened modules, and third-party modules loaded by dlopen.  In
3668 | `-------------'    |     Loader       |    |Dlopened Modules |
3683 | this problem.  Recall that the code that dlopens method-provider
3685 | the modules and the dlopener library itself should be linked against
3688 | modules to work at all in this scenario, the dlopener library must
3738 | @section Finding the correct name to dlopen
3742 | After a library has been linked with @option{-module}, it can be dlopened.
3744 | your package needs to determine the correct file to dlopen.
3751 | # The name that we can @code{dlopen}.
3755 | If @var{dlname} is empty, then the library cannot be dlopened.
3759 | dlopened.
3766 | its dlopened modules, even before installation, provided you have linked
3769 | @node Dlopen issues
3770 | @section Unresolved dlopen issues
3771 | @cindex pitfalls with dlopen
3772 | @cindex dlopening, pitfalls
3773 | @cindex trouble with dlopen
3775 | The following problems are not solved by using libtool's dlopen support:
3779 | Dlopen functions are generally only available on shared library
3782 | own alternatives to dlopening dynamic code.
3784 | @code{dlopen} family, which do package-specific tricks when dlopening
3788 | There are major differences in implementations of the @code{dlopen}
3794 | to discover the correct module filename to supply to @code{dlopen}.
3800 | @findex dlopen
3806 | @cindex dlopening modules
3811 | hiding the various difficulties of dlopening libraries from programmers.
3813 | distributed with applications that need dlopening functionality.  On
3823 | @code{dlopen} (POSIX compliant systems, GNU/Linux, etc.)
3851 | * Modules for libltdl::         Creating modules that can be @code{dlopen}ed.
3862 | The libltdl API is similar to the POSIX dlopen interface,
3886 | reported that GNU/Linux's glibc 2.0's @code{dlopen} with
3914 | Every lt_dlopened module has a handle associated with it.
3946 | @deftypefun lt_dlhandle lt_dlopen (const char *@var{filename})
3948 | handle for it.  @code{lt_dlopen} is able to open libtool dynamic
3952 | @code{lt_dlopen} and a dynamic module that can.  For maximum
3954 | @code{lt_dlopen} objects that have been compiled with libtool's
3958 | libraries and previously dlopened modules.  If the executable using
3964 | @option{-export-dynamic} or @option{-dlopen self}, @code{lt_dlopen} will
3992 | If @code{lt_dlopen} fails for any reason, it returns @code{NULL}.
3995 | @deftypefun lt_dlhandle lt_dlopenext (const char *@var{filename})
3996 | The same as @code{lt_dlopen}, except that it tries to append
4008 | to be able to @code{dlopen} such libraries as well as libtool modules
4012 | @deftypefun lt_dlhandle lt_dlopenadvise (const char *@var{filename}, @w{lt_dladvise @var{advise}})
4013 | The same as @code{lt_dlopen}, except that it also requires an additional
4025 | loader when using @code{lt_dlopenadvise} to perform the loading.
4044 | parameter to @code{lt_dlopenadvise} with this hint set causes it to
4045 | try to append different file name extensions like @code{lt_dlopenext}.
4048 | @code{lt_dlopenext (filename)}:
4052 | my_dlopenext (const char *filename)
4058 |     handle = lt_dlopenadvise (filename, advise);
4072 | parameter to @code{lt_dlopenadvise} with this hint set causes it to try
4077 | or if a module is loaded without using the @code{lt_dlopenadvise} call
4090 | parameter to @code{lt_dlopenadvise} with this hint set causes it to try
4095 | or if a module is loaded without using the @code{lt_dlopenadvise} call
4108 | parameter to @code{lt_dlopenadvise} with this hint set causes it to try
4118 | parameter to @code{lt_dlopenadvise} with this hint set causes it to
4120 | not found, @code{lt_dlopenadvise} will return @code{NULL}.
4173 | @code{lt_dlopen} would examine.  This function will continue to make
4189 | If you use @samp{lt_dlopen (NULL)} to get a @var{handle} for the running
4202 | @section Creating modules that can be @code{dlopen}ed
4208 | and you should link any program that is intended to dlopen the module with
4209 | @option{-dlopen @var{modulename.la}} where possible, so that libtool can
4210 | dlpreopen the module on platforms that do not support dlopening.  If
4212 | either when you link the module or when you link programs that dlopen it.
4219 | symbols, so that a program can dlopen them without having to know more
4230 | prefix so that you can also dlopen non-libtool modules.
4308 | be compared to any hints that were passed to @code{lt_dlopenadvise}
4474 | loader, and register it with libltdl so that @code{lt_dlopen} will be
4478 | called by @code{lt_dlopen}, @code{lt_dlsym} and @code{lt_dlclose}.
4492 | @item "dlopen"
4498 | The loader for @code{lt_dlopen}ing of preloaded static modules.
4523 | @code{lt_dlopen} API use it, you need to instantiate one of these
4653 | architecture supports them are @dfn{dlopen}@footnote{This is used for
4659 |    the standard dlopen loader were to fail when lt_dlopening. */
4660 | if (lt_dlloader_add (lt_dlloader_find ("dlopen"), myloader) != 0)
4807 | LT_INIT([dlopen])
4847 | LT_INIT([dlopen])
4890 | LT_INIT([dlopen])
5011 | You should probably also use the @samp{dlopen} option to @code{LT_INIT}
5012 | in your @file{configure.ac}, otherwise libtool will assume no dlopening
5017 | all platforms, because the dlopening functions may not be available
5031 | # Configure libtool with dlopen support if possible
5032 | LT_INIT([dlopen])
5047 | myprog_LDADD = $(LIBLTDL) -dlopen self -dlopen foo1.la
5409 | package that uses libtool and the system independent dlopen wrapper
5411 | dlopen wrapper for various platforms (POSIX)
5438 | directory) that itself does dlopening of libtool modules.
6793 | @defvar dlopen_support
6794 | Whether @code{dlopen} is supported on the platform.
6798 | @defvar dlopen_self
6799 | Whether it is possible to @code{dlopen} the executable itself.
6803 | @defvar dlopen_self_static
6804 | Whether it is possible to @code{dlopen} the executable itself, when it
6814 | Compiler link flag that allows a dlopened shared library to reference
7013 | Whether we can @code{dlopen} modules without a @samp{lib} prefix.
7016 | about it.  @samp{no} means that it is possible to @code{dlopen} a
{% endraw %}

```
### doc/libtool.info-1

```

{% raw %}
48 | * Dlopened modules::            'dlopen'ing libtool-created libraries.
49 | * Using libltdl::               Libtool's portable 'dlopen' wrapper library.
125 | Dlopened modules
127 | * Building modules::            Creating dlopenable objects and libraries.
128 | * Dlpreopening::                Dlopening that works on static platforms.
129 | * Linking with dlopened modules::  Using dlopenable modules in libraries.
130 | * Finding the dlname::          Choosing the right file to 'dlopen'.
131 | * Dlopen issues::               Unresolved problems that need your attention.
136 | * Modules for libltdl::         Creating modules that can be 'dlopen'ed.
903 | (*note Linking executables::) and to help programs with dlopening (*note
904 | Dlopened modules::).
1320 | '-dlopen FILE'
1321 |      Same as '-dlpreopen FILE', if native dlopening is not supported on
1322 |      the host platform (*note Dlopened modules::) or if the program is
1325 |      that the program can 'dlopen' itself, either by enabling
1338 |      Dlopened modules::).
1360 |      Creates a library that can be dlopened (*note Dlopened modules::).
1468 |      the same interface (*note Linking with dlopened modules::).
1513 | '-dlopen FILE'
1517 | '-dlopen' flags.
1726 |      that can be used, and if necessary also sets 'LIBADD_DLOPEN' if
1727 |      additional system libraries are required by the 'dlopen' loader,
1749 |  -- Macro: LT_SYS_DLOPEN_SELF
1750 |      Tests whether a program can dlopen itself, and then also whether
1751 |      the same program can still dlopen itself when statically linked.
1752 |      Results are stored in the shell variables '$enable_dlopen_self' and
1753 |      'enable_dlopen_self_static' respectively.
1755 |  -- Macro: LT_SYS_DLOPEN_DEPLIBS
1756 |      Define the preprocessor symbol 'LTDL_DLOPEN_DEPLIBS' if the OS
1757 |      needs help to load dependent libraries for 'dlopen' (or
1850 |    (1) Since GNU Automake 1.5, the flags '-dlopen' or '-dlpreopen'
1856 |      program_LDADD = "-dlopen" libfoo.la
1979 |      'dlopen'
1980 |           Enable checking for dlopen support.  This option should be
1981 |           used if the package makes use of the '-dlopen' and
1983 |           the system does not support dlopening.
2092 |  -- Macro: AC_LIBTOOL_DLOPEN
2093 |      This macro is deprecated, the 'dlopen' option to 'LT_INIT' should
3075 | File: libtool.info,  Node: Inter-library dependencies,  Next: Dlopened modules,  Prev: Library tips,  Up: Top
3132 | File: libtool.info,  Node: Dlopened modules,  Next: Using libltdl,  Prev: Inter-library dependencies,  Up: Top
3134 | 10 Dlopened modules
3144 |   2. The application calling functions such as 'dlopen' that load
3149 | dynamic linking as "dlopening" a module.
3151 |    The main benefit to dlopening object modules is the ability to access
3153 | interpreted language.  In fact, dlopen calls are frequently used in
3157 |    Libtool provides support for dlopened modules.  However, you should
3159 | 'LT_INIT' option 'dlopen' in 'configure.ac'.  If this option is not
3160 | given, libtool will assume no dlopening mechanism is available, and will
3163 |    This chapter discusses how you as a dlopen application developer
3164 | might use libtool to generate dlopen-accessible modules.
3168 | * Building modules::            Creating dlopenable objects and libraries.
3169 | * Dlpreopening::                Dlopening that works on static platforms.
3170 | * Linking with dlopened modules::  Using dlopenable modules in libraries.
3171 | * Finding the dlname::          Choosing the right file to 'dlopen'.
3172 | * Dlopen issues::               Unresolved problems that need your attention.
3175 | File: libtool.info,  Node: Building modules,  Next: Dlpreopening,  Up: Dlopened modules
3177 | 10.1 Building modules to dlopen
3185 | dlopens other modules or a libtool library that will also be dlopened.
3188 | would later be dlopened by an application, we would add '-module' to the
3196 | references in a library you want to dlopen you will have to use the flag
3198 | executable that calls dlopen:
3204 | File: libtool.info,  Node: Dlpreopening,  Next: Linking with dlopened modules,  Prev: Building modules,  Up: Dlopened modules
3209 | Libtool provides special support for dlopening libtool object and
3211 | platforms without any 'dlopen' and 'dlsym' functions_.
3231 |   4. Dlopening a module, so that the application can resolve its own,
3236 |    Libtool emulates '-dlopen' on static platforms by linking objects
3239 | must declare the objects you want your application to dlopen by using
3240 | the '-dlopen' or '-dlpreopen' flags when you link your program (*note
3334 | File: libtool.info,  Node: Linking with dlopened modules,  Next: Finding the dlname,  Prev: Dlpreopening,  Up: Dlopened modules
3336 | 10.3 Linking with dlopened modules
3339 | When, say, an interpreter application uses dlopened modules to extend
3342 | built in ones supplied with the interpreter) accessed through dlopen.
3343 | For one thing, the dlopening functionality will be tested even during
3355 | modules, and third-party modules loaded by dlopen.  In itself, that is
3370 |      `-------------'    |     Loader       |    |Dlopened Modules |
3384 | this problem.  Recall that the code that dlopens method-provider modules
3386 | and the dlopener library itself should be linked against the common
3389 | work at all in this scenario, the dlopener library must declare that it
3432 | File: libtool.info,  Node: Finding the dlname,  Next: Dlopen issues,  Prev: Linking with dlopened modules,  Up: Dlopened modules
3434 | 10.4 Finding the correct name to dlopen
3437 | After a library has been linked with '-module', it can be dlopened.
3439 | needs to determine the correct file to dlopen.
3445 |      # The name that we can dlopen.
3448 |    If DLNAME is empty, then the library cannot be dlopened.  Otherwise,
3451 | '/usr/local/lib/libhello.so.3' should be dlopened.
3457 | can find its dlopened modules, even before installation, provided you
3465 | File: libtool.info,  Node: Dlopen issues,  Prev: Finding the dlname,  Up: Dlopened modules
3467 | 10.5 Unresolved dlopen issues
3470 | The following problems are not solved by using libtool's dlopen support:
3472 |    * Dlopen functions are generally only available on shared library
3475 |      or develop your own alternatives to dlopening dynamic code.  Most
3477 |      'dlopen' family, which do package-specific tricks when dlopening is
3480 |    * There are major differences in implementations of the 'dlopen'
3485 |      discover the correct module filename to supply to 'dlopen'.
3488 | File: libtool.info,  Node: Using libltdl,  Next: Trace interface,  Prev: Dlopened modules,  Up: Top
3494 | the various difficulties of dlopening libraries from programmers.  It
3496 | distributed with applications that need dlopening functionality.  On
3503 |    * 'dlopen' (POSIX compliant systems, GNU/Linux, etc.)
3522 | * Modules for libltdl::         Creating modules that can be 'dlopen'ed.
3534 | The libltdl API is similar to the POSIX dlopen interface, which is very
3554 | that GNU/Linux's glibc 2.0's 'dlopen' with 'RTLD_LAZY' (that libltdl
3574 |      'lt_dlhandle' is a module "handle".  Every lt_dlopened module has a
3599 |  -- Function: lt_dlhandle lt_dlopen (const char *FILENAME)
3601 |      it.  'lt_dlopen' is able to open libtool dynamic modules, preloaded
3605 |      libraries and previously dlopened modules.  If the executable using
3611 |      '-export-dynamic' or '-dlopen self', 'lt_dlopen' will return a
3634 |      returned.  If 'lt_dlopen' fails for any reason, it returns 'NULL'.
3636 |  -- Function: lt_dlhandle lt_dlopenext (const char *FILENAME)
3637 |      The same as 'lt_dlopen', except that it tries to append different
3648 |      able to 'dlopen' such libraries as well as libtool modules
3651 |  -- Function: lt_dlhandle lt_dlopenadvise (const char *FILENAME,
3653 |      The same as 'lt_dlopen', except that it also requires an additional
3664 |      when using 'lt_dlopenadvise' to perform the loading.  The ADVISE
3681 |      'lt_dlopenadvise' with this hint set causes it to try to append
3682 |      different file name extensions like 'lt_dlopenext'.
3684 |      The following example is equivalent to calling 'lt_dlopenext
3688 |           my_dlopenext (const char *filename)
3694 |               handle = lt_dlopenadvise (filename, advise);
3706 |      'lt_dlopenadvise' with this hint set causes it to try to make the
3711 |      a module is loaded without using the 'lt_dlopenadvise' call in any
3723 |      'lt_dlopenadvise' with this hint set causes it to try to keep the
3728 |      a module is loaded without using the 'lt_dlopenadvise' call in any
3740 |      'lt_dlopenadvise' with this hint set causes it to try to make the
3749 |      'lt_dlopenadvise' with this hint set causes it to load only
3751 |      found, 'lt_dlopenadvise' will return 'NULL'.
3796 |      'NULL', then search all of the standard locations that 'lt_dlopen'
3813 |      If you use 'lt_dlopen (NULL)' to get a HANDLE for the running
3826 | library that cannot be opened by 'lt_dlopen' and a dynamic module that
3828 | pass 'lt_dlopen' objects that have been compiled with libtool's
3834 | 11.2 Creating modules that can be 'dlopen'ed
3841 | should link any program that is intended to dlopen the module with
3842 | '-dlopen MODULENAME.LA' where possible, so that libtool can dlpreopen
3843 | the module on platforms that do not support dlopening.  If the module
3845 | you link the module or when you link programs that dlopen it.  If you
3852 | same symbols, so that a program can dlopen them without having to know
3863 | so that you can also dlopen non-libtool modules.
3938 |      hints that were passed to 'lt_dlopenadvise' to determine whether
4091 | loader, and register it with libltdl so that 'lt_dlopen' will be able to
4095 | be called by 'lt_dlopen', 'lt_dlsym' and 'lt_dlclose'.  Optionally, you
4107 | "dlopen"
4113 |      The loader for 'lt_dlopen'ing of preloaded static modules.
4134 |      the 'lt_dlopen' API use it, you need to instantiate one of these
4247 |      architecture supports them are "dlopen"(1), "dld" and "dlpreload".
4250 |              the standard dlopen loader were to fail when lt_dlopening. */
4251 |           if (lt_dlloader_add (lt_dlloader_find ("dlopen"), myloader) != 0)
4376 |           LT_INIT([dlopen])
4413 |                LT_INIT([dlopen])
4450 |                LT_INIT([dlopen])
4553 |    You should probably also use the 'dlopen' option to 'LT_INIT' in your
4554 | 'configure.ac', otherwise libtool will assume no dlopening mechanism is
4558 | not work on all platforms, because the dlopening functions may not be
4571 |      # Configure libtool with dlopen support if possible
4572 |      LT_INIT([dlopen])
4585 |      myprog_LDADD = $(LIBLTDL) -dlopen self -dlopen foo1.la
4878 |      package that uses libtool and the system independent dlopen wrapper
4879 |      'libltdl' to load modules.  The library 'libltdl' provides a dlopen
4903 |      directory) that itself does dlopening of libtool modules.
6333 |  -- Variable: dlopen_support
6334 |      Whether 'dlopen' is supported on the platform.  Set to 'yes' or
6337 |  -- Variable: dlopen_self
6338 |      Whether it is possible to 'dlopen' the executable itself.  Set to
6341 |  -- Variable: dlopen_self_static
6342 |      Whether it is possible to 'dlopen' the executable itself, when it
6349 |      Compiler link flag that allows a dlopened shared library to
6523 |      Whether we can 'dlopen' modules without a 'lib' prefix.  Set to
6526 |      means that it is possible to 'dlopen' a module without the 'lib'
{% endraw %}

```