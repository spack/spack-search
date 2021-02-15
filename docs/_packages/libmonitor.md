---
name: "libmonitor"
layout: package
next_package: vpic
previous_package: libfs
languages: ['cpp', 'bash']
---
## 2013.02.18
11 / 63 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [aclocal.m4](#aclocalm4)
 - [config/ltmain.sh](#configltmainsh)
 - [src/monitor.h](#srcmonitorh)
 - [src/callback.c](#srccallbackc)
 - [src/main.c](#srcmainc)
 - [src/Makefile.am](#srcmakefileam)
 - [src/dlopen.c](#srcdlopenc)
 - [src/Makefile.in](#srcmakefilein)
 - [tests/early.c](#testsearlyc)

### config.h.in

```

{% raw %}
51 | /* Include support for dlopen. */
52 | #undef MONITOR_USE_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
315 | # Note: autoconf uses 'enable_dlopen', so we use dlfcn.
319 | 	[include support for dlopen (default=yes)])],
324 |     AC_SEARCH_LIBS([dlopen], [dl], [], [enable_dlfcn=no])
328 |     AC_DEFINE([MONITOR_USE_DLOPEN], [1],
329 | 	[Include support for dlopen.])
330 |     wrap_list="${wrap_list} dlopen dlclose"
333 | AM_CONDITIONAL([MONITOR_TEST_USE_DLOPEN],
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1620 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1623 | m4_defun([_LT_TRY_DLOPEN_SELF],
1681 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1714 | ])# _LT_TRY_DLOPEN_SELF
1717 | # LT_SYS_DLOPEN_SELF
1719 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1721 | if test "x$enable_dlopen" != xyes; then
1722 |   enable_dlopen=unknown
1723 |   enable_dlopen_self=unknown
1724 |   enable_dlopen_self_static=unknown
1726 |   lt_cv_dlopen=no
1727 |   lt_cv_dlopen_libs=
1731 |     lt_cv_dlopen="load_add_on"
1732 |     lt_cv_dlopen_libs=
1733 |     lt_cv_dlopen_self=yes
1737 |     lt_cv_dlopen="LoadLibrary"
1738 |     lt_cv_dlopen_libs=
1742 |     lt_cv_dlopen="dlopen"
1743 |     lt_cv_dlopen_libs=
1748 |     AC_CHECK_LIB([dl], [dlopen],
1749 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1750 |     lt_cv_dlopen="dyld"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1758 | 	  [lt_cv_dlopen="shl_load"],
1760 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1761 | 	[AC_CHECK_FUNC([dlopen],
1762 | 	      [lt_cv_dlopen="dlopen"],
1763 | 	  [AC_CHECK_LIB([dl], [dlopen],
1764 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1765 | 	    [AC_CHECK_LIB([svld], [dlopen],
1766 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1768 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1777 |   if test "x$lt_cv_dlopen" != xno; then
1778 |     enable_dlopen=yes
1780 |     enable_dlopen=no
1783 |   case $lt_cv_dlopen in
1784 |   dlopen)
1792 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1794 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1795 | 	  lt_cv_dlopen_self, [dnl
1796 | 	  _LT_TRY_DLOPEN_SELF(
1797 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1798 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1801 |     if test "x$lt_cv_dlopen_self" = xyes; then
1803 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1804 | 	  lt_cv_dlopen_self_static, [dnl
1805 | 	  _LT_TRY_DLOPEN_SELF(
1806 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1807 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1817 |   case $lt_cv_dlopen_self in
1818 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1819 |   *) enable_dlopen_self=unknown ;;
1822 |   case $lt_cv_dlopen_self_static in
1823 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1824 |   *) enable_dlopen_self_static=unknown ;;
1827 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1828 | 	 [Whether dlopen is supported])
1829 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1830 | 	 [Whether dlopen of programs is supported])
1831 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1832 | 	 [Whether dlopen of statically linked programs is supported])
1833 | ])# LT_SYS_DLOPEN_SELF
1836 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1838 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5276 |     [Compiler flag to allow reflexive dlopens])
5388 |   LT_SYS_DLOPEN_SELF
7513 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7545 | # dlopen
7547 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7550 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7551 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7554 | put the `dlopen' option into LT_INIT's first parameter.])
7558 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8004 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
885 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
946 |       -dlopen=*|--mode=*|--tag=*)
1036 |   # Only execute mode is allowed to have -dlopen flags.
1038 |     func_error "unrecognized option \`-dlopen'"
1672 |   -dlopen FILE      add the directory containing FILE to the library path
1674 | This mode sets the library path environment variable according to \`-dlopen'
1729 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1738 |   -module           build a library that can dlopened
1844 |     # Handle -dlopen flags immediately.
1861 | 	# Skip this library if it cannot be dlopened.
1888 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4436 | 	    dlopen_self=$dlopen_self_static
4442 | 	    dlopen_self=$dlopen_self_static
4448 | 	    dlopen_self=$dlopen_self_static
4506 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4590 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4752 |       -dlopen)
5140 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5207 | 	  # This library was specified with -dlopen.
5322 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5333 | 	passes="conv scan dlopen dlpreopen link"
5359 | 	dlopen) libs="$dlfiles" ;;
5386 |       if test "$pass" = dlopen; then
5598 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5599 | 	      # If there is no dlopen support or we're linking statically,
5629 | 	dlopen=
5659 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5699 | 	# This library was specified with -dlopen.
5700 | 	if test "$pass" = dlopen; then
5702 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5705 | 	     test "$dlopen_support" != yes ||
5707 | 	    # If there is no dlname, no dlopen support or we're linking
5716 | 	fi # $pass = dlopen
5774 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5900 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5901 | 	  dlopenmodule=""
5904 | 	      dlopenmodule="$dlpremoduletest"
5908 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6005 | 		    # if the lib is a (non-dlopened) module then we can not
6009 | 		      if test "X$dlopenmodule" != "X$lib"; then
6161 | 	      echo "*** a static module, that should work as long as the dlopening application"
6162 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6298 |       if test "$pass" != dlopen; then
6397 | 	func_warning "\`-dlopen' is ignored for archives"
6464 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7126 | 	    echo "*** a static module, that should work as long as the dlopening"
7127 | 	    echo "*** application is linked with the -dlopen flag."
7145 | 	    echo "*** or is declared to -dlopen it."
7716 | 	func_warning "\`-dlopen' is ignored for objects"
7831 |         && test "$dlopen_support" = unknown \
7832 | 	&& test "$dlopen_self" = unknown \
7833 | 	&& test "$dlopen_self_static" = unknown && \
7834 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8473 | # The name that we can dlopen(3).
8502 | # Files to dlopen/dlpreopen
8503 | dlopen='$dlfiles'
{% endraw %}

```
### src/monitor.h

```cpp

{% raw %}
66 | extern void monitor_pre_dlopen(const char *path, int flags);
67 | extern void monitor_dlopen(const char *path, int flags, void *handle);
84 | extern void *monitor_real_dlopen(const char *path, int flags);
{% endraw %}

```
### src/callback.c

```cpp

{% raw %}
113 | monitor_pre_dlopen(const char *path, int flags)
119 | monitor_dlopen(const char *path, int flags, void *handle)
{% endraw %}

```
### src/main.c

```cpp

{% raw %}
658 | monitor_real_dlopen(const char *path, int flags)
{% endraw %}

```
### src/Makefile.am

```

{% raw %}
54 | if MONITOR_TEST_USE_DLOPEN
55 |     libmonitor_la_SOURCES += dlopen.c
79 | if MONITOR_TEST_USE_DLOPEN
80 |     libmonitor_wrap_a_SOURCES += dlopen.c
{% endraw %}

```
### src/dlopen.c

```cpp

{% raw %}
1 |  *  Libmonitor dlopen functions.
37 |  *    dlopen
42 |  *    monitor_real_dlopen
61 | typedef void *dlopen_fcn_t(const char *, int);
65 | extern dlopen_fcn_t   __real_dlopen;
69 | static dlopen_fcn_t   *real_dlopen = NULL;
79 | monitor_dlopen_init(void)
86 |     MONITOR_GET_REAL_NAME_WRAP(real_dlopen, dlopen);
98 |  *  Client access to the real dlopen() and dlclose().
101 | monitor_real_dlopen(const char *path, int flags)
103 |     monitor_dlopen_init();
104 |     return (*real_dlopen)(path, flags);
110 |     monitor_dlopen_init();
115 |  *  Override dlopen() and dlclose().
118 | MONITOR_WRAP_NAME(dlopen)(const char *path, int flags)
122 |     monitor_dlopen_init();
124 |     monitor_pre_dlopen(path, flags);
125 |     handle = (*real_dlopen)(path, flags);
126 |     monitor_dlopen(path, flags, handle);
137 |     monitor_dlopen_init();
{% endraw %}

```
### src/Makefile.in

```

{% raw %}
40 | @MONITOR_TEST_LINK_PRELOAD_TRUE@@MONITOR_TEST_USE_DLOPEN_TRUE@am__append_2 = dlopen.c
47 | @MONITOR_TEST_LINK_STATIC_TRUE@@MONITOR_TEST_USE_DLOPEN_TRUE@am__append_9 = dlopen.c
96 | @MONITOR_TEST_LINK_STATIC_TRUE@@MONITOR_TEST_USE_DLOPEN_TRUE@am__objects_2 = libmonitor_wrap_a-dlopen.$(OBJEXT)
130 | @MONITOR_TEST_LINK_PRELOAD_TRUE@@MONITOR_TEST_USE_DLOPEN_TRUE@am__objects_10 = libmonitor_la-dlopen.lo
474 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/libmonitor_la-dlopen.Plo@am__quote@
499 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/libmonitor_wrap_a-dlopen.Po@am__quote@
600 | libmonitor_wrap_a-dlopen.o: dlopen.c
601 | @am__fastdepCC_TRUE@	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(libmonitor_wrap_a_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT libmonitor_wrap_a-dlopen.o -MD -MP -MF $(DEPDIR)/libmonitor_wrap_a-dlopen.Tpo -c -o libmonitor_wrap_a-dlopen.o `test -f 'dlopen.c' || echo '$(srcdir)/'`dlopen.c
602 | @am__fastdepCC_TRUE@	$(am__mv) $(DEPDIR)/libmonitor_wrap_a-dlopen.Tpo $(DEPDIR)/libmonitor_wrap_a-dlopen.Po
603 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	source='dlopen.c' object='libmonitor_wrap_a-dlopen.o' libtool=no @AMDEPBACKSLASH@
605 | @am__fastdepCC_FALSE@	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(libmonitor_wrap_a_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o libmonitor_wrap_a-dlopen.o `test -f 'dlopen.c' || echo '$(srcdir)/'`dlopen.c
607 | libmonitor_wrap_a-dlopen.obj: dlopen.c
608 | @am__fastdepCC_TRUE@	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(libmonitor_wrap_a_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT libmonitor_wrap_a-dlopen.obj -MD -MP -MF $(DEPDIR)/libmonitor_wrap_a-dlopen.Tpo -c -o libmonitor_wrap_a-dlopen.obj `if test -f 'dlopen.c'; then $(CYGPATH_W) 'dlopen.c'; else $(CYGPATH_W) '$(srcdir)/dlopen.c'; fi`
609 | @am__fastdepCC_TRUE@	$(am__mv) $(DEPDIR)/libmonitor_wrap_a-dlopen.Tpo $(DEPDIR)/libmonitor_wrap_a-dlopen.Po
610 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	source='dlopen.c' object='libmonitor_wrap_a-dlopen.obj' libtool=no @AMDEPBACKSLASH@
612 | @am__fastdepCC_FALSE@	$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(libmonitor_wrap_a_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o libmonitor_wrap_a-dlopen.obj `if test -f 'dlopen.c'; then $(CYGPATH_W) 'dlopen.c'; else $(CYGPATH_W) '$(srcdir)/dlopen.c'; fi`
908 | libmonitor_la-dlopen.lo: dlopen.c
909 | @am__fastdepCC_TRUE@	$(LIBTOOL)  --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(libmonitor_la_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT libmonitor_la-dlopen.lo -MD -MP -MF $(DEPDIR)/libmonitor_la-dlopen.Tpo -c -o libmonitor_la-dlopen.lo `test -f 'dlopen.c' || echo '$(srcdir)/'`dlopen.c
910 | @am__fastdepCC_TRUE@	$(am__mv) $(DEPDIR)/libmonitor_la-dlopen.Tpo $(DEPDIR)/libmonitor_la-dlopen.Plo
911 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	source='dlopen.c' object='libmonitor_la-dlopen.lo' libtool=yes @AMDEPBACKSLASH@
913 | @am__fastdepCC_FALSE@	$(LIBTOOL)  --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(libmonitor_la_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o libmonitor_la-dlopen.lo `test -f 'dlopen.c' || echo '$(srcdir)/'`dlopen.c
{% endraw %}

```
### tests/early.c

```cpp

{% raw %}
1 |  * Library that makes calls to dlopen(), dlclose(), pthread_create(),
6 |  * 'e' (_exit), 'f' (fork), 'o' (dlopen) or 't' (pthread_create),
11 |  * to have the library call fork() and dlopen() from its init
38 | do_dlopen(void)
40 |     TITLE("dlopen");
41 |     handle = dlopen("/lib64/libm.so.6", RTLD_LAZY);
42 |     printf("dlopen: handle = %p\n", handle);
130 | 	    do_dlopen();
{% endraw %}

```