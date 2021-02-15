---
name: "global"
layout: package
next_package: xz
previous_package: grib-api
languages: ['cpp', 'bash']
---
## 6.5
13 / 391 files match

 - [config-h.in](#config-hin)
 - [ltmain.sh](#ltmainsh)
 - [aclocal.m4](#aclocalm4)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/Makefile.am](#libltdlmakefileam)
 - [libltdl/Makefile.in](#libltdlmakefilein)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [libltdl/libltdl/lt__private.h](#libltdllibltdllt__privateh)
 - [libltdl/libltdl/lt_error.h](#libltdllibltdllt_errorh)
 - [libglibc/sqlite3.c](#libglibcsqlite3c)
 - [libparser/parser.c](#libparserparserc)

### config-h.in

```

{% raw %}
258 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
259 | #undef LTDL_DLOPEN_DEPLIBS
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
### aclocal.m4

```

{% raw %}
1835 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1838 | m4_defun([_LT_TRY_DLOPEN_SELF],
1896 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1929 | ])# _LT_TRY_DLOPEN_SELF
1932 | # LT_SYS_DLOPEN_SELF
1934 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1936 | if test yes != "$enable_dlopen"; then
1937 |   enable_dlopen=unknown
1938 |   enable_dlopen_self=unknown
1939 |   enable_dlopen_self_static=unknown
1941 |   lt_cv_dlopen=no
1942 |   lt_cv_dlopen_libs=
1946 |     lt_cv_dlopen=load_add_on
1947 |     lt_cv_dlopen_libs=
1948 |     lt_cv_dlopen_self=yes
1952 |     lt_cv_dlopen=LoadLibrary
1953 |     lt_cv_dlopen_libs=
1957 |     lt_cv_dlopen=dlopen
1958 |     lt_cv_dlopen_libs=
1963 |     AC_CHECK_LIB([dl], [dlopen],
1964 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1965 |     lt_cv_dlopen=dyld
1966 |     lt_cv_dlopen_libs=
1967 |     lt_cv_dlopen_self=yes
1974 |     lt_cv_dlopen=dlopen
1975 |     lt_cv_dlopen_libs=
1976 |     lt_cv_dlopen_self=no
1981 | 	  [lt_cv_dlopen=shl_load],
1983 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1984 | 	[AC_CHECK_FUNC([dlopen],
1985 | 	      [lt_cv_dlopen=dlopen],
1986 | 	  [AC_CHECK_LIB([dl], [dlopen],
1987 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1988 | 	    [AC_CHECK_LIB([svld], [dlopen],
1989 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1991 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2000 |   if test no = "$lt_cv_dlopen"; then
2001 |     enable_dlopen=no
2003 |     enable_dlopen=yes
2006 |   case $lt_cv_dlopen in
2007 |   dlopen)
2015 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2017 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2018 | 	  lt_cv_dlopen_self, [dnl
2019 | 	  _LT_TRY_DLOPEN_SELF(
2020 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2021 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2024 |     if test yes = "$lt_cv_dlopen_self"; then
2026 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2027 | 	  lt_cv_dlopen_self_static, [dnl
2028 | 	  _LT_TRY_DLOPEN_SELF(
2029 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2030 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2040 |   case $lt_cv_dlopen_self in
2041 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2042 |   *) enable_dlopen_self=unknown ;;
2045 |   case $lt_cv_dlopen_self_static in
2046 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2047 |   *) enable_dlopen_self_static=unknown ;;
2050 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2051 | 	 [Whether dlopen is supported])
2052 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2053 | 	 [Whether dlopen of programs is supported])
2054 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2055 | 	 [Whether dlopen of statically linked programs is supported])
2056 | ])# LT_SYS_DLOPEN_SELF
2059 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2061 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6136 |     [Compiler flag to allow reflexive dlopens])
6245 |   LT_SYS_DLOPEN_SELF
8644 | 			  _LT_SHELL_INIT([lt_dlopen_dir=$lt_ltdl_dir])],
8645 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir=$lt_ltdl_dir; lt_libobj_prefix=$lt_ltdl_dir/])],
8819 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
8863 | eval "LTDLOPEN=\"$libname_spec\""
8864 | AC_SUBST([LTDLOPEN])
8885 | # LT_SYS_DLOPEN_DEPLIBS
8887 | AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
8889 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
8890 |   [lt_cv_sys_dlopen_deplibs],
8891 |   [# PORTME does your system automatically load deplibs for dlopen?
8895 |   lt_cv_sys_dlopen_deplibs=unknown
8900 |     lt_cv_sys_dlopen_deplibs=unknown
8903 |     lt_cv_sys_dlopen_deplibs=yes
8908 |       lt_cv_sys_dlopen_deplibs=no
8913 |     lt_cv_sys_dlopen_deplibs=yes
8918 |     lt_cv_sys_dlopen_deplibs=yes
8921 |     lt_cv_sys_dlopen_deplibs=yes
8925 |     lt_cv_sys_dlopen_deplibs=yes
8928 |     lt_cv_sys_dlopen_deplibs=yes
8931 |     lt_cv_sys_dlopen_deplibs=yes
8936 |     lt_cv_sys_dlopen_deplibs=unknown
8940 |     # at 6.2 and later dlopen does load deplibs.
8941 |     lt_cv_sys_dlopen_deplibs=yes
8944 |     lt_cv_sys_dlopen_deplibs=yes
8947 |     lt_cv_sys_dlopen_deplibs=yes
8950 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
8953 |     lt_cv_sys_dlopen_deplibs=no
8956 |     # dlopen *does* load deplibs and with the right loader patch applied
8962 |     lt_cv_sys_dlopen_deplibs=unknown
8969 |     lt_cv_sys_dlopen_deplibs=yes
8972 |     lt_cv_sys_dlopen_deplibs=yes
8975 |     lt_cv_sys_dlopen_deplibs=yes
8978 |     libltdl_cv_sys_dlopen_deplibs=yes
8982 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
8983 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
8984 |     [Define if the OS needs help to load dependent libraries for dlopen().])
8986 | ])# LT_SYS_DLOPEN_DEPLIBS
8989 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
8991 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
9080 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
9105 | LIBADD_DLOPEN=
9106 | AC_SEARCH_LIBS([dlopen], [dl],
9109 | 	if test "$ac_cv_search_dlopen" != "none required"; then
9110 | 	  LIBADD_DLOPEN=-ldl
9112 | 	libltdl_cv_lib_dl_dlopen=yes
9113 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
9117 |     ]], [[dlopen(0, 0);]])],
9120 | 	    libltdl_cv_func_dlopen=yes
9121 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
9122 | 	[AC_CHECK_LIB([svld], [dlopen],
9125 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
9126 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
9127 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
9130 |   LIBS="$LIBS $LIBADD_DLOPEN"
9134 | AC_SUBST([LIBADD_DLOPEN])
9140 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
9144 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
9154 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
9157 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
9161 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
9168 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
9184 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
9249 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
9254 |       LIBS="$LIBS $LIBADD_DLOPEN"
9312 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
9425 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
9459 | # dlopen
9461 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
9464 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
9465 | [_LT_SET_OPTION([LT_INIT], [dlopen])
9468 | put the 'dlopen' option into LT_INIT's first parameter.])
9472 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
9986 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
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
151 | dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
152 | am_dlopen_la_OBJECTS = loaders/dlopen.lo
153 | dlopen_la_OBJECTS = $(am_dlopen_la_OBJECTS)
154 | dlopen_la_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
156 | 	$(dlopen_la_LDFLAGS) $(LDFLAGS) -o $@
236 | SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
240 | DIST_SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
327 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
337 | LTDLOPEN = @LTDLOPEN@
442 | EXTRA_LTLIBRARIES = dlopen.la dld_link.la dyld.la load_add_on.la \
472 | libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
477 | libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
481 | dlopen_la_SOURCES = loaders/dlopen.c
482 | dlopen_la_LDFLAGS = -module -avoid-version
483 | dlopen_la_LIBADD = $(LIBADD_DLOPEN)
587 | loaders/dlopen.lo: loaders/$(am__dirstamp) \
590 | dlopen.la: $(dlopen_la_OBJECTS) $(dlopen_la_DEPENDENCIES) $(EXTRA_dlopen_la_DEPENDENCIES) 
591 | 	$(AM_V_CCLD)$(dlopen_la_LINK)  $(dlopen_la_OBJECTS) $(dlopen_la_LIBADD) $(LIBS)
642 | @AMDEP_TRUE@@am__include@ @am__quote@loaders/$(DEPDIR)/dlopen.Plo@am__quote@
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
### libglibc/sqlite3.c

```cpp

{% raw %}
1280 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
10313 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
16121 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
16122 |   return pVfs->xDlOpen(pVfs, zPath);
30839 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
30841 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
30846 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
30889 |   #define unixDlOpen  0
32263 |     unixDlOpen,           /* xDlOpen */                     \
37775 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
37782 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
37787 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
37797 |     OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)0));
37812 |   OSTRACE(("DLOPEN name=%s, handle=%p\n", zFilename, (void*)h));
37834 |   #define winDlOpen  0
38017 |     winDlOpen,           /* xDlOpen */
38042 |     winDlOpen,           /* xDlOpen */
100427 |   handle = sqlite3OsDlOpen(pVfs, zFile);
100432 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
{% endraw %}

```
### libparser/parser.c

```cpp

{% raw %}
217 | 		pent->handle = lt_dlopen(lt_dl_name);
{% endraw %}

```