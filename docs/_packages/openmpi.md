---
name: "openmpi"
layout: package
next_package: py-vermin
previous_package: staden-io-lib
languages: ['cpp', 'bash']
---
## 1.7.5
70 / 7011 files match

 - [configure.ac](#configureac)
 - [config/libtool.m4](#configlibtoolm4)
 - [config/opal_configure_options.m4](#configopal_configure_optionsm4)
 - [config/opal_setup_libltdl.m4](#configopal_setup_libltdlm4)
 - [config/ltoptions.m4](#configltoptionsm4)
 - [config/ltmain.sh](#configltmainsh)
 - [config/libltdl-preopen-error.diff](#configlibltdl-preopen-errordiff)
 - [config/ltdl.m4](#configltdlm4)
 - [ompi/mca/btl/usnic/README.test](#ompimcabtlusnicreadmetest)
 - [ompi/mca/btl/usnic/btl_usnic_test.h](#ompimcabtlusnicbtl_usnic_testh)
 - [ompi/mca/btl/usnic/test/ompi_btl_usnic_run_tests.c](#ompimcabtlusnictestompi_btl_usnic_run_testsc)
 - [ompi/mca/btl/openib/connect/connect.h](#ompimcabtlopenibconnectconnecth)
 - [ompi/mca/common/cuda/common_cuda.c](#ompimcacommoncudacommon_cudac)
 - [ompi/mca/common/cuda/help-mpi-common-cuda.txt](#ompimcacommoncudahelp-mpi-common-cudatxt)
 - [ompi/mca/io/romio/romio/confdb/libtool.m4](#ompimcaioromioromioconfdblibtoolm4)
 - [ompi/mca/io/romio/romio/confdb/ltoptions.m4](#ompimcaioromioromioconfdbltoptionsm4)
 - [ompi/mca/io/romio/romio/confdb/ltmain.sh](#ompimcaioromioromioconfdbltmainsh)
 - [ompi/mpi/java/c/mpi_MPI.c](#ompimpijavacmpi_mpic)
 - [ompi/debuggers/dlopen_test.c](#ompidebuggersdlopen_testc)
 - [ompi/debuggers/Makefile.am](#ompidebuggersmakefileam)
 - [ompi/debuggers/ompi_msgq_dll.c](#ompidebuggersompi_msgq_dllc)
 - [ompi/debuggers/Makefile.in](#ompidebuggersmakefilein)
 - [ompi/contrib/vt/vt/config/ltmain.sh](#ompicontribvtvtconfigltmainsh)
 - [ompi/contrib/vt/vt/config/m4/libtool.m4](#ompicontribvtvtconfigm4libtoolm4)
 - [ompi/contrib/vt/vt/config/m4/ltoptions.m4](#ompicontribvtvtconfigm4ltoptionsm4)
 - [ompi/contrib/vt/vt/extlib/otf/config/ltmain.sh](#ompicontribvtvtextlibotfconfigltmainsh)
 - [ompi/contrib/vt/vt/extlib/otf/config/m4/libtool.m4](#ompicontribvtvtextlibotfconfigm4libtoolm4)
 - [ompi/contrib/vt/vt/extlib/otf/config/m4/ltoptions.m4](#ompicontribvtvtextlibotfconfigm4ltoptionsm4)
 - [ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c](#ompicontribvtvtvtlibvt_mallocwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_libwrap.c](#ompicontribvtvtvtlibvt_libwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_iowrap.c](#ompicontribvtvtvtlibvt_iowrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c](#ompicontribvtvtvtlibvt_plugin_cntrc)
 - [ompi/tools/ompi_info/param.c](#ompitoolsompi_infoparamc)
 - [oshmem/mca/memheap/base/memheap_base_static.c](#oshmemmcamemheapbasememheap_base_staticc)
 - [oshmem/tools/oshmem_info/param.c](#oshmemtoolsoshmem_infoparamc)
 - [orte/tools/orte-info/param.c](#ortetoolsorte-infoparamc)
 - [opal/Makefile.am](#opalmakefileam)
 - [opal/Makefile.in](#opalmakefilein)
 - [opal/mca/base/base.h](#opalmcabasebaseh)
 - [opal/mca/base/mca_base_component_repository.h](#opalmcabasemca_base_component_repositoryh)
 - [opal/mca/base/mca_base_open.c](#opalmcabasemca_base_openc)
 - [opal/mca/base/mca_base_component_find.c](#opalmcabasemca_base_component_findc)
 - [opal/mca/crs/self/configure.m4](#opalmcacrsselfconfigurem4)
 - [opal/mca/crs/self/help-opal-crs-self.txt](#opalmcacrsselfhelp-opal-crs-selftxt)
 - [opal/mca/crs/self/crs_self_module.c](#opalmcacrsselfcrs_self_modulec)
 - [opal/mca/hwloc/hwloc172/hwloc/config/hwloc.m4](#opalmcahwlochwloc172hwlocconfighwlocm4)
 - [opal/mca/hwloc/hwloc172/hwloc/src/components.c](#opalmcahwlochwloc172hwlocsrccomponentsc)
 - [opal/mca/hwloc/hwloc172/hwloc/contrib/hwloc-valgrind.supp](#opalmcahwlochwloc172hwloccontribhwloc-valgrindsupp)
 - [opal/mca/event/libevent2021/libevent/ltmain.sh](#opalmcaeventlibevent2021libeventltmainsh)
 - [opal/mca/event/libevent2021/libevent/m4/libtool.m4](#opalmcaeventlibevent2021libeventm4libtoolm4)
 - [opal/mca/event/libevent2021/libevent/m4/ltoptions.m4](#opalmcaeventlibevent2021libeventm4ltoptionsm4)
 - [opal/mca/memory/linux/hooks.c](#opalmcamemorylinuxhooksc)
 - [opal/mca/memory/linux/memory_linux_ptmalloc2.c](#opalmcamemorylinuxmemory_linux_ptmalloc2c)
 - [opal/util/lt_interface.h](#opalutillt_interfaceh)
 - [opal/util/lt_interface.c](#opalutillt_interfacec)
 - [opal/libltdl/configure.ac](#opallibltdlconfigureac)
 - [opal/libltdl/ltdl.h](#opallibltdlltdlh)
 - [opal/libltdl/ltdl.c](#opallibltdlltdlc)
 - [opal/libltdl/config-h.in](#opallibltdlconfig-hin)
 - [opal/libltdl/Makefile.am](#opallibltdlmakefileam)
 - [opal/libltdl/Makefile.in](#opallibltdlmakefilein)
 - [opal/libltdl/config/ltmain.sh](#opallibltdlconfigltmainsh)
 - [opal/libltdl/m4/libtool.m4](#opallibltdlm4libtoolm4)
 - [opal/libltdl/m4/ltoptions.m4](#opallibltdlm4ltoptionsm4)
 - [opal/libltdl/m4/ltdl.m4](#opallibltdlm4ltdlm4)
 - [opal/libltdl/loaders/preopen.c](#opallibltdlloaderspreopenc)
 - [opal/libltdl/loaders/dlopen.c](#opallibltdlloadersdlopenc)
 - [opal/libltdl/libltdl/lt__private.h](#opallibltdllibltdllt__privateh)
 - [opal/libltdl/libltdl/lt_error.h](#opallibltdllibltdllt_errorh)
 - [test/support/components.c](#testsupportcomponentsc)

### configure.ac

```

{% raw %}
1260 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### config/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### config/opal_configure_options.m4

```

{% raw %}
261 | # Do we want to allow DLOPEN?
264 | AC_MSG_CHECKING([if want dlopen support])
265 | AC_ARG_ENABLE([dlopen],
266 |     [AC_HELP_STRING([--enable-dlopen],
267 |                     [Whether build should attempt to use dlopen (or
269 |                      Disabling dlopen implies --disable-mca-dso.
271 | if test "$enable_dlopen" = "no" ; then
274 |     OPAL_ENABLE_DLOPEN_SUPPORT=0
277 |     OPAL_ENABLE_DLOPEN_SUPPORT=1
467 |          [Where to find libltdl (this option is ignored if --disable-dlopen is used).  DIR can take one of three values: "internal", "external", or a valid directory name.  "internal" (or no DIR value) forces Open MPI to use its internal copy of libltdl.  "external" forces Open MPI to use an external installation of libltdl.  Supplying a valid directory name also forces Open MPI to use an external installation of libltdl, and adds DIR/include, DIR/lib, and DIR/lib64 to the search path for headers and libraries.])])
{% endraw %}

```
### config/opal_setup_libltdl.m4

```

{% raw %}
40 |     AS_IF([test "$OPAL_ENABLE_DLOPEN_SUPPORT" = "0"],
41 |           [AC_MSG_WARN([libltdl support disabled (by --disable-dlopen)])
58 |               AC_MSG_WARN([--enable-dlopen (or --disable-dlopen was not specified)])
59 |               AC_MSG_WARN([Cannot have dlopen without libltdl])
93 |                                  [lt_dlopen],
132 |     AC_DEFINE_UNQUOTED(OPAL_WANT_LIBLTDL, $OPAL_ENABLE_DLOPEN_SUPPORT,
137 |     AM_CONDITIONAL(OPAL_HAVE_DLOPEN, 
138 |                    [test "$OPAL_ENABLE_DLOPEN_SUPPORT" = "1"])
186 |         AC_MSG_WARN([dynamic shared object loading, by configuring with --disable-dlopen.])
{% endraw %}

```
### config/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### config/libltdl-preopen-error.diff

```

{% raw %}
11 | +     lt_dlopenadvise() a DSO -- so if there was a real error when
{% endraw %}

```
### config/ltdl.m4

```

{% raw %}
199 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
200 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
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
470 |     lt_cv_sys_dlopen_deplibs=yes
473 |     lt_cv_sys_dlopen_deplibs=yes
477 |     lt_cv_sys_dlopen_deplibs=yes
480 |     lt_cv_sys_dlopen_deplibs=yes
483 |     lt_cv_sys_dlopen_deplibs=yes
488 |     lt_cv_sys_dlopen_deplibs=unknown
492 |     # at 6.2 and later dlopen does load deplibs.
493 |     lt_cv_sys_dlopen_deplibs=yes
496 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
505 |     lt_cv_sys_dlopen_deplibs=no
508 |     # dlopen *does* load deplibs and with the right loader patch applied
514 |     lt_cv_sys_dlopen_deplibs=unknown
521 |     lt_cv_sys_dlopen_deplibs=yes
524 |     lt_cv_sys_dlopen_deplibs=yes
527 |     lt_cv_sys_dlopen_deplibs=yes
530 |     libltdl_cv_sys_dlopen_deplibs=yes
534 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
535 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
536 |     [Define if the OS needs help to load dependent libraries for dlopen().])
538 | ])# LT_SYS_DLOPEN_DEPLIBS
541 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
543 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
627 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
651 | LIBADD_DLOPEN=
652 | AC_SEARCH_LIBS([dlopen], [dl],
655 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
656 | 	  LIBADD_DLOPEN="-ldl"
658 | 	libltdl_cv_lib_dl_dlopen="yes"
659 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
663 |     ]], [[dlopen(0, 0);]])],
666 | 	    libltdl_cv_func_dlopen="yes"
667 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
668 | 	[AC_CHECK_LIB([svld], [dlopen],
671 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
672 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
673 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
676 |   LIBS="$LIBS $LIBADD_DLOPEN"
680 | AC_SUBST([LIBADD_DLOPEN])
686 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
690 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
700 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
703 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
707 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
714 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
730 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
792 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
793 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
798 |           LIBS="$LIBS $LIBADD_DLOPEN"
799 | 	  _LT_TRY_DLOPEN_SELF(
{% endraw %}

```
### ompi/mca/btl/usnic/README.test

```

{% raw %}
47 | * Tests are registered at dlopen time via an
{% endraw %}

```
### ompi/mca/btl/usnic/btl_usnic_test.h

```cpp

{% raw %}
84 |  * dlopens the usnic BTL shared object.  See run_usnic_tests.c. */
{% endraw %}

```
### ompi/mca/btl/usnic/test/ompi_btl_usnic_run_tests.c

```cpp

{% raw %}
41 |     mpi_handle = dlopen("libmpi.so", RTLD_NOW|RTLD_GLOBAL);
77 |     usnic_handle = dlopen(path, RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### ompi/mca/btl/openib/connect/connect.h

```cpp

{% raw %}
15 |  * module-like instances of the implemented functionality (dlopen and
{% endraw %}

```
### ompi/mca/common/cuda/common_cuda.c

```cpp

{% raw %}
333 |             opal_show_help("help-mpi-common-cuda.txt", "dlopen disabled", true);
385 |                 libcuda_handle = opal_lt_dlopenadvise(cudalibs[i], advise);
420 |                 libcuda_handle = opal_lt_dlopen(cudalibs[i]);
449 |         opal_show_help("help-mpi-common-cuda.txt", "dlopen failed", true,
{% endraw %}

```
### ompi/mca/common/cuda/help-mpi-common-cuda.txt

```

{% raw %}
146 | [dlopen disabled] 
148 |  --disable-dlopen flag), and therefore cannot utilize CUDA support.  
160 | [dlopen failed]
{% endraw %}

```
### ompi/mca/io/romio/romio/confdb/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ompi/mca/io/romio/romio/confdb/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### ompi/mca/io/romio/romio/confdb/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### ompi/mpi/java/c/mpi_MPI.c

```cpp

{% raw %}
73 |  * One option, of course, is to build with --disable-dlopen.
79 |  * The other option is to explicitly dlopen libmpi ourselves
80 |  * and instruct dlopen to add all those symbols to the global
86 |  * thus making all symbols available to subsequent dlopen calls
91 |     if (NULL == (mpilibhandle = dlopen("libmpi." OPAL_DYN_LIB_SUFFIX,
{% endraw %}

```
### ompi/debuggers/dlopen_test.c

```cpp

{% raw %}
53 |        dlopen value.  If the dlopen value is '' (i.e., empty), then
54 |        there's nothing to dlopen (i.e., OMPI was built with
75 |         fprintf(stderr, "No test file to dlopen (perhaps --enable-static?); skipping\n");
85 |     printf("Trying to lt_dlopen file with dladvise_local: %s\n", filename);
94 |     dlhandle = lt_dlopenadvise(filename, dladvise);
97 |     dlhandle = lt_dlopenext(filename);
115 |     dlhandle = lt_dlopenadvise(filename, dladvise);
118 |     dlhandle = lt_dlopenext(filename);
{% endraw %}

```
### ompi/debuggers/Makefile.am

```

{% raw %}
23 | if OPAL_HAVE_DLOPEN
24 | check_PROGRAMS += dlopen_test
47 | dlopen_test_SOURCES = dlopen_test.c
48 | dlopen_test_CPPFLAGS = -I$(top_srcdir)/opal/libltdl
49 | dlopen_test_LDADD = $(top_builddir)/opal/libltdl/libltdlc.la
{% endraw %}

```
### ompi/debuggers/ompi_msgq_dll.c

```cpp

{% raw %}
106 |  * RTLD_NOW this undefined symbol causes the dlopen to fail since we do not 
{% endraw %}

```
### ompi/debuggers/Makefile.in

```

{% raw %}
74 | @OPAL_HAVE_DLOPEN_TRUE@am__append_1 = dlopen_test
396 | @OPAL_HAVE_DLOPEN_TRUE@am__EXEEXT_1 = dlopen_test$(EXEEXT)
397 | am_dlopen_test_OBJECTS = dlopen_test-dlopen_test.$(OBJEXT)
398 | dlopen_test_OBJECTS = $(am_dlopen_test_OBJECTS)
399 | dlopen_test_DEPENDENCIES = $(top_builddir)/opal/libltdl/libltdlc.la
441 | 	$(libompi_debugger_canary_la_SOURCES) $(dlopen_test_SOURCES) \
445 | 	$(libompi_debugger_canary_la_SOURCES) $(dlopen_test_SOURCES) \
1555 | dlopen_test_SOURCES = dlopen_test.c
1556 | dlopen_test_CPPFLAGS = -I$(top_srcdir)/opal/libltdl
1557 | dlopen_test_LDADD = $(top_builddir)/opal/libltdl/libltdlc.la
1678 | dlopen_test$(EXEEXT): $(dlopen_test_OBJECTS) $(dlopen_test_DEPENDENCIES) $(EXTRA_dlopen_test_DEPENDENCIES) 
1679 | 	@rm -f dlopen_test$(EXEEXT)
1680 | 	$(AM_V_CCLD)$(LINK) $(dlopen_test_OBJECTS) $(dlopen_test_LDADD) $(LIBS)
1691 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen_test-dlopen_test.Po@am__quote@
1743 | dlopen_test-dlopen_test.o: dlopen_test.c
1744 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(dlopen_test_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT dlopen_test-dlopen_test.o -MD -MP -MF $(DEPDIR)/dlopen_test-dlopen_test.Tpo -c -o dlopen_test-dlopen_test.o `test -f 'dlopen_test.c' || echo '$(srcdir)/'`dlopen_test.c
1745 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen_test-dlopen_test.Tpo $(DEPDIR)/dlopen_test-dlopen_test.Po
1746 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen_test.c' object='dlopen_test-dlopen_test.o' libtool=no @AMDEPBACKSLASH@
1748 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(dlopen_test_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o dlopen_test-dlopen_test.o `test -f 'dlopen_test.c' || echo '$(srcdir)/'`dlopen_test.c
1750 | dlopen_test-dlopen_test.obj: dlopen_test.c
1751 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(dlopen_test_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT dlopen_test-dlopen_test.obj -MD -MP -MF $(DEPDIR)/dlopen_test-dlopen_test.Tpo -c -o dlopen_test-dlopen_test.obj `if test -f 'dlopen_test.c'; then $(CYGPATH_W) 'dlopen_test.c'; else $(CYGPATH_W) '$(srcdir)/dlopen_test.c'; fi`
1752 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen_test-dlopen_test.Tpo $(DEPDIR)/dlopen_test-dlopen_test.Po
1753 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen_test.c' object='dlopen_test-dlopen_test.obj' libtool=no @AMDEPBACKSLASH@
1755 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(dlopen_test_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o dlopen_test-dlopen_test.obj `if test -f 'dlopen_test.c'; then $(CYGPATH_W) 'dlopen_test.c'; else $(CYGPATH_W) '$(srcdir)/dlopen_test.c'; fi`
{% endraw %}

```
### ompi/contrib/vt/vt/config/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### ompi/contrib/vt/vt/config/m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ompi/contrib/vt/vt/config/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### ompi/contrib/vt/vt/extlib/otf/config/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### ompi/contrib/vt/vt/extlib/otf/config/m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ompi/contrib/vt/vt/extlib/otf/config/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c

```cpp

{% raw %}
92 |      dlopen calls malloc which would result in an infinite recursion when
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_libwrap.c

```cpp

{% raw %}
159 |     libc_handle = dlopen(SHLIBC_PATHNAME,
173 |       printf("VampirTrace: FATAL: dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n",
177 |       vt_error_msg("dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n", dlerror());
262 |         (*lw)->handlev[i] = dlopen((*lw)->attr->shlibs[i],
272 |                    "dlopen(\"%s\") failed: %s",
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_iowrap.c

```cpp

{% raw %}
120 |       iolib_handle = dlopen( iolib_pathname,
127 |         printf("VampirTrace: FATAL: dlopen(\"%s\") error: %s\n", iolib_pathname, dlerror());
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c

```cpp

{% raw %}
211 |     /* now dlopen it */
212 |     handle = dlopen(buffer, RTLD_NOW);
{% endraw %}

```
### ompi/tools/ompi_info/param.c

```cpp

{% raw %}
592 |     opal_info_out("libltdl support", "option:dlopen", want_libltdl);
{% endraw %}

```
### oshmem/mca/memheap/base/memheap_base_static.c

```cpp

{% raw %}
101 |      * It does not support them in shared objects or in dlopen()
{% endraw %}

```
### oshmem/tools/oshmem_info/param.c

```cpp

{% raw %}
561 |     opal_info_out("libltdl support", "option:dlopen", want_libltdl);
{% endraw %}

```
### orte/tools/orte-info/param.c

```cpp

{% raw %}
428 |     orte_info_out("libltdl support", "option:dlopen", want_libltdl);
{% endraw %}

```
### opal/Makefile.am

```

{% raw %}
34 | # libltdl is included by variable because if --disable-dlopen was
{% endraw %}

```
### opal/Makefile.in

```

{% raw %}
1736 | # libltdl is included by variable because if --disable-dlopen was
{% endraw %}

```
### opal/mca/base/base.h

```cpp

{% raw %}
68 | OPAL_DECLSPEC extern bool mca_base_component_disable_dlopen;
{% endraw %}

```
### opal/mca/base/mca_base_component_repository.h

```cpp

{% raw %}
47 |  * One more case that this handles is the --disable-dlopen case.  In
51 |  * we configure with --disable-dlopen, then lt_dlhandle shouldn't be
{% endraw %}

```
### opal/mca/base/mca_base_open.c

```cpp

{% raw %}
48 | bool mca_base_component_disable_dlopen = false;
112 |     mca_base_component_disable_dlopen = false;
113 |     var_id = mca_base_var_register("opal", "mca", "base", "component_disable_dlopen",
118 |                                    &mca_base_component_disable_dlopen);
119 |     (void) mca_base_var_register_synonym(var_id, "opal", "mca", NULL, "component_disable_dlopen",
{% endraw %}

```
### opal/mca/base/mca_base_component_find.c

```cpp

{% raw %}
69 |  * Private types; only necessary when we're dlopening components.
202 |     if (open_dso_components && !mca_base_component_disable_dlopen) {
322 |  * generate dependencies, etc.  If we use the plain lt_dlopen()
576 |   component_handle = lt_dlopenadvise(target_file->filename, opal_mca_dladvise);
578 |   component_handle = lt_dlopenext(target_file->filename);
{% endraw %}

```
### opal/mca/crs/self/configure.m4

```

{% raw %}
34 |     # If they did not ask for dlopen support,
37 |         [AS_IF([test "$OPAL_ENABLE_DLOPEN_SUPPORT" = "1"],
{% endraw %}

```
### opal/mca/crs/self/help-opal-crs-self.txt

```

{% raw %}
20 | [self:lt_dlopen]
{% endraw %}

```
### opal/mca/crs/self/crs_self_module.c

```cpp

{% raw %}
577 |      * us to not have to dlopen/dlclose the executable. A bit of short hand
{% endraw %}

```
### opal/mca/hwloc/hwloc172/hwloc/config/hwloc.m4

```

{% raw %}
1022 |       AC_CHECK_LIB([ltdl], [lt_dlopenext],
1261 |   save_lt_cv_dlopen="$lt_cv_dlopen"
1262 |   save_lt_cv_dlopen_libs="$lt_cv_dlopen_libs"
1263 |   save_lt_cv_dlopen_self="$lt_cv_dlopen_self"
1265 |   # code stolen from LT_SYS_DLOPEN_SELF in libtool.m4
1268 |     lt_cv_dlopen="load_add_on"
1269 |     lt_cv_dlopen_libs=
1270 |     lt_cv_dlopen_self=yes
1274 |     lt_cv_dlopen="LoadLibrary"
1275 |     lt_cv_dlopen_libs=
1279 |     lt_cv_dlopen="dlopen"
1280 |     lt_cv_dlopen_libs=
1285 |     AC_CHECK_LIB([dl], [dlopen],
1286 |                 [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1287 |     lt_cv_dlopen="dyld"
1288 |     lt_cv_dlopen_libs=
1289 |     lt_cv_dlopen_self=yes
1295 |           [lt_cv_dlopen="shl_load"],
1297 |             [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1298 |         [AC_CHECK_FUNC([dlopen],
1299 |               [lt_cv_dlopen="dlopen"],
1300 |           [AC_CHECK_LIB([dl], [dlopen],
1301 |                 [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1302 |             [AC_CHECK_LIB([svld], [dlopen],
1303 |                   [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1305 |                     [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1313 |   # end of code stolen from LT_SYS_DLOPEN_SELF in libtool.m4
1316 |   HWLOC_LIBS_PRIVATE="$HWLOC_LIBS_PRIVATE $lt_cv_dlopen_libs"
1319 |   lt_cv_dlopen="$save_lt_cv_dlopen"
1320 |   lt_cv_dlopen_libs="$save_lt_cv_dlopen_libs"
1321 |   lt_cv_dlopen_self="$save_lt_cv_dlopen_self"
{% endraw %}

```
### opal/mca/hwloc/hwloc172/hwloc/src/components.c

```cpp

{% raw %}
85 |   /* dlopen and get the component structure */
86 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### opal/mca/hwloc/hwloc172/hwloc/contrib/hwloc-valgrind.supp

```

{% raw %}
32 | # ltdl dlopen global state?
34 |    ltdl_dlopen_doit_leak
40 |    fun:dlopen_doit
{% endraw %}

```
### opal/mca/event/libevent2021/libevent/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### opal/mca/event/libevent2021/libevent/m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### opal/mca/event/libevent2021/libevent/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### opal/mca/memory/linux/hooks.c

```cpp

{% raw %}
863 |    --enable-static --disable-dlopen, because we won't use
{% endraw %}

```
### opal/mca/memory/linux/memory_linux_ptmalloc2.c

```cpp

{% raw %}
36 |    use --disable-dlopen and therefore -Wl,--export-dynamic isn't used
{% endraw %}

```
### opal/util/lt_interface.h

```cpp

{% raw %}
64 | /* Portable libltdl versions of the system dlopen() API. */
65 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename);
66 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename);
70 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenadvise(const char *filename,
{% endraw %}

```
### opal/util/lt_interface.c

```cpp

{% raw %}
165 | /* Portable libltdl versions of the system dlopen() API. */
166 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename) {
173 |     handle->dlhandle = lt_dlopen(filename);
184 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename) {
191 |     handle->dlhandle = lt_dlopenext(filename);
228 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenadvise(const char *filename,
236 |     handle->dlhandle = lt_dlopenadvise(filename, advise->dladvise);
{% endraw %}

```
### opal/libltdl/configure.ac

```

{% raw %}
66 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### opal/libltdl/ltdl.h

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
### opal/libltdl/ltdl.c

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
485 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
521 |       error += tryall_dlopen_module (handle, (const char *) 0,
524 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
539 |      we want the preopened version of it, even if a dlopenable
541 |   if (old_name && tryall_dlopen (handle, old_name,
553 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
561 | 	  if (tryall_dlopen_module (handle, dir, objdir,
568 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
784 |   /* Try to dlopen the file, but do not continue searching in any
786 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
808 | #if !defined(LTDL_DLOPEN_DEPLIBS)
816 | #else /* defined(LTDL_DLOPEN_DEPLIBS) */
945 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
971 | #endif /* defined(LTDL_DLOPEN_DEPLIBS) */
1151 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1168 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1175 |   /* dlopen self? */
1187 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1306 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1473 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1616 | lt_dlopen (const char *filename)
1618 |   return lt_dlopenadvise (filename, NULL);
1627 | lt_dlopenext (const char *filename)
1633 |     handle = lt_dlopenadvise (filename, advise);
1641 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1661 |       /* Just incase we missed a code path in try_dlopen() that reports
1663 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1672 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1685 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1696 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1891 |    passing to lt_dlopenext.  The extensions are stripped so that
1894 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### opal/libltdl/config-h.in

```

{% raw %}
117 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
118 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### opal/libltdl/Makefile.am

```

{% raw %}
86 | libltdl_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
92 | libltdlc_la_CPPFLAGS	= -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
101 | EXTRA_LTLIBRARIES	       += dlopen.la \
108 | dlopen_la_SOURCES	= loaders/dlopen.c
109 | dlopen_la_LDFLAGS	= -module -avoid-version
110 | dlopen_la_LIBADD 	= $(LIBADD_DLOPEN)
{% endraw %}

```
### opal/libltdl/Makefile.in

```

{% raw %}
95 | dlopen_la_DEPENDENCIES = $(am__DEPENDENCIES_1)
96 | am_dlopen_la_OBJECTS = dlopen.lo
97 | dlopen_la_OBJECTS = $(am_dlopen_la_OBJECTS)
98 | dlopen_la_LINK = $(LIBTOOL) --tag=CC $(AM_LIBTOOLFLAGS) \
100 | 	$(dlopen_la_LDFLAGS) $(LDFLAGS) -o $@
155 | SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
159 | DIST_SOURCES = $(dld_link_la_SOURCES) $(dlopen_la_SOURCES) \
216 | LIBADD_DLOPEN = @LIBADD_DLOPEN@
223 | LTDLOPEN = @LTDLOPEN@
316 | EXTRA_LTLIBRARIES = dlopen.la dld_link.la dyld.la load_add_on.la \
347 | libltdl_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN) $(AM_CPPFLAGS)
352 | libltdlc_la_CPPFLAGS = -DLTDLOPEN=$(LTDLOPEN)c $(AM_CPPFLAGS)
356 | dlopen_la_SOURCES = loaders/dlopen.c
357 | dlopen_la_LDFLAGS = -module -avoid-version
358 | dlopen_la_LIBADD = $(LIBADD_DLOPEN)
469 | dlopen.la: $(dlopen_la_OBJECTS) $(dlopen_la_DEPENDENCIES) 
470 | 	$(dlopen_la_LINK)  $(dlopen_la_OBJECTS) $(dlopen_la_LIBADD) $(LIBS)
494 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen.Plo@am__quote@
540 | dlopen.lo: loaders/dlopen.c
541 | @am__fastdepCC_TRUE@	$(LIBTOOL)  --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -MT dlopen.lo -MD -MP -MF $(DEPDIR)/dlopen.Tpo -c -o dlopen.lo `test -f 'loaders/dlopen.c' || echo '$(srcdir)/'`loaders/dlopen.c
542 | @am__fastdepCC_TRUE@	$(am__mv) $(DEPDIR)/dlopen.Tpo $(DEPDIR)/dlopen.Plo
543 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	source='loaders/dlopen.c' object='dlopen.lo' libtool=yes @AMDEPBACKSLASH@
545 | @am__fastdepCC_FALSE@	$(LIBTOOL)  --tag=CC $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS) -c -o dlopen.lo `test -f 'loaders/dlopen.c' || echo '$(srcdir)/'`loaders/dlopen.c
{% endraw %}

```
### opal/libltdl/config/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### opal/libltdl/m4/libtool.m4

```

{% raw %}
1744 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1747 | m4_defun([_LT_TRY_DLOPEN_SELF],
1805 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1838 | ])# _LT_TRY_DLOPEN_SELF
1841 | # LT_SYS_DLOPEN_SELF
1843 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1845 | if test "x$enable_dlopen" != xyes; then
1846 |   enable_dlopen=unknown
1847 |   enable_dlopen_self=unknown
1848 |   enable_dlopen_self_static=unknown
1850 |   lt_cv_dlopen=no
1851 |   lt_cv_dlopen_libs=
1855 |     lt_cv_dlopen="load_add_on"
1856 |     lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen_self=yes
1861 |     lt_cv_dlopen="LoadLibrary"
1862 |     lt_cv_dlopen_libs=
1866 |     lt_cv_dlopen="dlopen"
1867 |     lt_cv_dlopen_libs=
1872 |     AC_CHECK_LIB([dl], [dlopen],
1873 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1874 |     lt_cv_dlopen="dyld"
1875 |     lt_cv_dlopen_libs=
1876 |     lt_cv_dlopen_self=yes
1882 | 	  [lt_cv_dlopen="shl_load"],
1884 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1885 | 	[AC_CHECK_FUNC([dlopen],
1886 | 	      [lt_cv_dlopen="dlopen"],
1887 | 	  [AC_CHECK_LIB([dl], [dlopen],
1888 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1889 | 	    [AC_CHECK_LIB([svld], [dlopen],
1890 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1892 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1901 |   if test "x$lt_cv_dlopen" != xno; then
1902 |     enable_dlopen=yes
1904 |     enable_dlopen=no
1907 |   case $lt_cv_dlopen in
1908 |   dlopen)
1916 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1918 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1919 | 	  lt_cv_dlopen_self, [dnl
1920 | 	  _LT_TRY_DLOPEN_SELF(
1921 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1922 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1925 |     if test "x$lt_cv_dlopen_self" = xyes; then
1927 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1928 | 	  lt_cv_dlopen_self_static, [dnl
1929 | 	  _LT_TRY_DLOPEN_SELF(
1930 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1931 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1941 |   case $lt_cv_dlopen_self in
1942 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1943 |   *) enable_dlopen_self=unknown ;;
1946 |   case $lt_cv_dlopen_self_static in
1947 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1948 |   *) enable_dlopen_self_static=unknown ;;
1951 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1952 | 	 [Whether dlopen is supported])
1953 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1954 | 	 [Whether dlopen of programs is supported])
1955 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1956 | 	 [Whether dlopen of statically linked programs is supported])
1957 | ])# LT_SYS_DLOPEN_SELF
1960 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1962 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5658 |     [Compiler flag to allow reflexive dlopens])
5771 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### opal/libltdl/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### opal/libltdl/m4/ltdl.m4

```

{% raw %}
199 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
200 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
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
470 |     lt_cv_sys_dlopen_deplibs=yes
473 |     lt_cv_sys_dlopen_deplibs=yes
477 |     lt_cv_sys_dlopen_deplibs=yes
480 |     lt_cv_sys_dlopen_deplibs=yes
483 |     lt_cv_sys_dlopen_deplibs=yes
488 |     lt_cv_sys_dlopen_deplibs=unknown
492 |     # at 6.2 and later dlopen does load deplibs.
493 |     lt_cv_sys_dlopen_deplibs=yes
496 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
505 |     lt_cv_sys_dlopen_deplibs=no
508 |     # dlopen *does* load deplibs and with the right loader patch applied
514 |     lt_cv_sys_dlopen_deplibs=unknown
521 |     lt_cv_sys_dlopen_deplibs=yes
524 |     lt_cv_sys_dlopen_deplibs=yes
527 |     lt_cv_sys_dlopen_deplibs=yes
530 |     libltdl_cv_sys_dlopen_deplibs=yes
534 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
535 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
536 |     [Define if the OS needs help to load dependent libraries for dlopen().])
538 | ])# LT_SYS_DLOPEN_DEPLIBS
541 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
543 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
627 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
651 | LIBADD_DLOPEN=
652 | AC_SEARCH_LIBS([dlopen], [dl],
655 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
656 | 	  LIBADD_DLOPEN="-ldl"
658 | 	libltdl_cv_lib_dl_dlopen="yes"
659 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
663 |     ]], [[dlopen(0, 0);]])],
666 | 	    libltdl_cv_func_dlopen="yes"
667 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
668 | 	[AC_CHECK_LIB([svld], [dlopen],
671 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
672 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
673 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
676 |   LIBS="$LIBS $LIBADD_DLOPEN"
680 | AC_SUBST([LIBADD_DLOPEN])
686 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
690 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
700 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
703 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
707 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
714 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
730 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
792 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
793 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
798 |           LIBS="$LIBS $LIBADD_DLOPEN"
799 | 	  _LT_TRY_DLOPEN_SELF(
{% endraw %}

```
### opal/libltdl/loaders/preopen.c

```cpp

{% raw %}
192 |      lt_dlopenadvise() a DSO -- so if there was a real error when
370 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### opal/libltdl/loaders/dlopen.c

```cpp

{% raw %}
0 | /* loader-dlopen.c --  dynamic linking with dlopen/dlsym
38 | #define get_vtable	dlopen_LTX_get_vtable
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### opal/libltdl/libltdl/lt__private.h

```cpp

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### opal/libltdl/libltdl/lt_error.h

```cpp

{% raw %}
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```
### test/support/components.c

```cpp

{% raw %}
34 | static bool try_dlopen(const char *dir, const char *fw, const char *comp,
60 |     if (try_dlopen(".", framework, component, comp_handle, &sym) ||
61 |         try_dlopen(dir_concat(BUILDDIR, "src/mca"), framework, 
63 |         try_dlopen(dir_concat(SRCDIR, "src/mca"), framework, 
66 |         /* Ok, dlopen'ed it.  Now call the component's open
127 | static bool try_dlopen(const char *dir, const char *fw, const char *comp,
147 |     comp_handle->tch_handle = lt_dlopen(NULL);
165 |     comp_handle->tch_handle = lt_dlopenext(file_name);
{% endraw %}

```