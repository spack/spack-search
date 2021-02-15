---
name: "jags"
layout: package
next_package: bedtools2
previous_package: hdf
languages: ['cpp', 'bash']
---
## 4.3.0
18 / 1147 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [src/terminal/parser.yy](#srcterminalparseryy)
 - [src/terminal/parser.cc](#srcterminalparsercc)
 - [src/terminal/Makefile.am](#srcterminalmakefileam)
 - [src/terminal/Makefile.in](#srcterminalmakefilein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/ltdl.m4](#m4ltdlm4)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/Makefile.am](#libltdlmakefileam)
 - [libltdl/Makefile.in](#libltdlmakefilein)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)

### config.h.in

```

{% raw %}
181 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
182 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### configure.ac

```

{% raw %}
45 | LT_INIT([dlopen disable-static win32-dll])
{% endraw %}

```
### ltmain.sh

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
### src/terminal/parser.yy

```

{% raw %}
1353 |     lt_dlhandle mod = lt_dlopenext(name.c_str());
{% endraw %}

```
### src/terminal/parser.cc

```cpp

{% raw %}
3427 |     lt_dlhandle mod = lt_dlopenext(name.c_str());
{% endraw %}

```
### src/terminal/Makefile.am

```

{% raw %}
15 | -dlopen ${top_builddir}/src/modules/base/basemod.la \
16 | -dlopen ${top_builddir}/src/modules/bugs/bugs.la \
17 | -dlopen ${top_builddir}/src/modules/dic/dic.la \
18 | -dlopen ${top_builddir}/src/modules/glm/glm.la \
19 | -dlopen ${top_builddir}/src/modules/lecuyer/lecuyer.la \
20 | -dlopen ${top_builddir}/src/modules/mix/mix.la \
21 | -dlopen ${top_builddir}/src/modules/msm/msm.la 
{% endraw %}

```
### src/terminal/Makefile.in

```

{% raw %}
313 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
323 | LTDLOPEN = @LTDLOPEN@
420 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/base/basemod.la \
421 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/bugs/bugs.la \
422 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/dic/dic.la \
423 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/glm/glm.la \
424 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/lecuyer/lecuyer.la \
425 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/mix/mix.la \
426 | @WINDOWS_FALSE@-dlopen ${top_builddir}/src/modules/msm/msm.la 
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
6125 |     [Compiler flag to allow reflexive dlopens])
6238 |   LT_SYS_DLOPEN_SELF
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
154 | dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
155 | am_dlopen_la_OBJECTS = loaders/dlopen.lo
156 | dlopen_la_OBJECTS = $(am_dlopen_la_OBJECTS)
157 | dlopen_la_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
159 | 	$(dlopen_la_LDFLAGS) $(LDFLAGS) -o $@
239 | SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
243 | DIST_SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
331 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
341 | LTDLOPEN = @LTDLOPEN@
446 | EXTRA_LTLIBRARIES = dlopen.la dld_link.la dyld.la load_add_on.la \
476 | libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
481 | libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
485 | dlopen_la_SOURCES = loaders/dlopen.c
486 | dlopen_la_LDFLAGS = -module -avoid-version
487 | dlopen_la_LIBADD = $(LIBADD_DLOPEN)
591 | loaders/dlopen.lo: loaders/$(am__dirstamp) \
594 | dlopen.la: $(dlopen_la_OBJECTS) $(dlopen_la_DEPENDENCIES) $(EXTRA_dlopen_la_DEPENDENCIES) 
595 | 	$(AM_V_CCLD)$(dlopen_la_LINK)  $(dlopen_la_OBJECTS) $(dlopen_la_LIBADD) $(LIBS)
646 | @AMDEP_TRUE@@am__include@ @am__quote@loaders/$(DEPDIR)/dlopen.Plo@am__quote@
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