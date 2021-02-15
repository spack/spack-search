---
name: "ucx"
layout: package
next_package: py-sphinx
previous_package: harminv
languages: ['cpp', 'bash']
---
## 1.4.0
9 / 590 files match

 - [ltmain.sh](#ltmainsh)
 - [config/m4/libtool.m4](#configm4libtoolm4)
 - [config/m4/ucs.m4](#configm4ucsm4)
 - [config/m4/ltoptions.m4](#configm4ltoptionsm4)
 - [src/ucm/util/reloc.c](#srcucmutilrelocc)
 - [test/mpi/test_memhooks.c](#testmpitest_memhooksc)
 - [test/apps/Makefile.am](#testappsmakefileam)
 - [test/apps/dlopen.c](#testappsdlopenc)
 - [test/apps/Makefile.in](#testappsmakefilein)

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
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### config/m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6140 |     [Compiler flag to allow reflexive dlopens])
6253 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### config/m4/ucs.m4

```

{% raw %}
46 | 	AC_CHECK_LIB(dl, dlopen, LIBS="$LIBS -ldl", [AC_MSG_WARN([dl library not found])];BT=0)
{% endraw %}

```
### config/m4/ltoptions.m4

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
### src/ucm/util/reloc.c

```cpp

{% raw %}
48 | static void * (*ucm_reloc_orig_dlopen)(const char *, int) = NULL;
271 | static void *ucm_dlopen(const char *filename, int flag)
276 |     if (ucm_reloc_orig_dlopen == NULL) {
277 |         ucm_fatal("ucm_reloc_orig_dlopen is NULL");
281 |     handle = ucm_reloc_orig_dlopen(filename, flag);
285 |          * with our list of patches (including dlopen itself). This code is less
291 |             ucm_debug("in dlopen(), re-applying '%s' to %p", patch->symbol,
300 | static ucm_reloc_patch_t ucm_reloc_dlopen_patch = {
301 |     .symbol = "dlopen",
302 |     .value  = ucm_dlopen
326 | static ucs_status_t ucm_reloc_install_dlopen()
335 |     ucm_reloc_orig_dlopen = ucm_reloc_get_orig(ucm_reloc_dlopen_patch.symbol,
336 |                                                ucm_reloc_dlopen_patch.value);
338 |     status = ucm_reloc_apply_patch(&ucm_reloc_dlopen_patch);
343 |     ucs_list_add_tail(&ucm_reloc_patch_list, &ucm_reloc_dlopen_patch.list);
353 |     /* Take lock first to handle a possible race where dlopen() is called
358 |     status = ucm_reloc_install_dlopen();
{% endraw %}

```
### test/mpi/test_memhooks.c

```cpp

{% raw %}
107 |     void *dl = dlopen(lib_path, RTLD_LAZY);
{% endraw %}

```
### test/apps/Makefile.am

```

{% raw %}
13 | 	test_dlopen
18 | test_dlopen_SOURCES  = dlopen.c
19 | test_dlopen_CPPFLAGS = $(BASE_CPPFLAGS) -g -DUCP_LIB_PATH=$(abs_top_builddir)/src/ucp/$(objdir)/libucp.so
20 | test_dlopen_CFLAGS   = $(BASE_CFLAGS)
21 | test_dlopen_LDADD    = -ldl
{% endraw %}

```
### test/apps/dlopen.c

```cpp

{% raw %}
18 |     handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### test/apps/Makefile.in

```

{% raw %}
98 | noinst_PROGRAMS = test_dlopen$(EXEEXT)
131 | am_test_dlopen_OBJECTS = test_dlopen-dlopen.$(OBJEXT)
132 | test_dlopen_OBJECTS = $(am_test_dlopen_OBJECTS)
133 | test_dlopen_DEPENDENCIES =
138 | test_dlopen_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CC $(AM_LIBTOOLFLAGS) \
139 | 	$(LIBTOOLFLAGS) --mode=link $(CCLD) $(test_dlopen_CFLAGS) \
175 | SOURCES = $(test_dlopen_SOURCES)
176 | DIST_SOURCES = $(test_dlopen_SOURCES)
451 | test_dlopen_SOURCES = dlopen.c
452 | test_dlopen_CPPFLAGS = $(BASE_CPPFLAGS) -g -DUCP_LIB_PATH=$(abs_top_builddir)/src/ucp/$(objdir)/libucp.so
453 | test_dlopen_CFLAGS = $(BASE_CFLAGS)
454 | test_dlopen_LDADD = -ldl
498 | test_dlopen$(EXEEXT): $(test_dlopen_OBJECTS) $(test_dlopen_DEPENDENCIES) $(EXTRA_test_dlopen_DEPENDENCIES) 
499 | 	@rm -f test_dlopen$(EXEEXT)
500 | 	$(AM_V_CCLD)$(test_dlopen_LINK) $(test_dlopen_OBJECTS) $(test_dlopen_LDADD) $(LIBS)
508 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/test_dlopen-dlopen.Po@am__quote@
534 | test_dlopen-dlopen.o: dlopen.c
535 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(test_dlopen_CPPFLAGS) $(CPPFLAGS) $(test_dlopen_CFLAGS) $(CFLAGS) -MT test_dlopen-dlopen.o -MD -MP -MF $(DEPDIR)/test_dlopen-dlopen.Tpo -c -o test_dlopen-dlopen.o `test -f 'dlopen.c' || echo '$(srcdir)/'`dlopen.c
536 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/test_dlopen-dlopen.Tpo $(DEPDIR)/test_dlopen-dlopen.Po
537 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen.c' object='test_dlopen-dlopen.o' libtool=no @AMDEPBACKSLASH@
539 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(test_dlopen_CPPFLAGS) $(CPPFLAGS) $(test_dlopen_CFLAGS) $(CFLAGS) -c -o test_dlopen-dlopen.o `test -f 'dlopen.c' || echo '$(srcdir)/'`dlopen.c
541 | test_dlopen-dlopen.obj: dlopen.c
542 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(test_dlopen_CPPFLAGS) $(CPPFLAGS) $(test_dlopen_CFLAGS) $(CFLAGS) -MT test_dlopen-dlopen.obj -MD -MP -MF $(DEPDIR)/test_dlopen-dlopen.Tpo -c -o test_dlopen-dlopen.obj `if test -f 'dlopen.c'; then $(CYGPATH_W) 'dlopen.c'; else $(CYGPATH_W) '$(srcdir)/dlopen.c'; fi`
543 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/test_dlopen-dlopen.Tpo $(DEPDIR)/test_dlopen-dlopen.Po
544 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen.c' object='test_dlopen-dlopen.obj' libtool=no @AMDEPBACKSLASH@
546 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(test_dlopen_CPPFLAGS) $(CPPFLAGS) $(test_dlopen_CFLAGS) $(CFLAGS) -c -o test_dlopen-dlopen.obj `if test -f 'dlopen.c'; then $(CYGPATH_W) 'dlopen.c'; else $(CYGPATH_W) '$(srcdir)/dlopen.c'; fi`
{% endraw %}

```