---
name: "gdb"
layout: package
next_package: dcmtk
previous_package: photos
languages: ['cpp', 'bash']
---
## 7.10.1
63 / 10755 files match

 - [libtool.m4](#libtoolm4)
 - [md5.sum](#md5sum)
 - [ltoptions.m4](#ltoptionsm4)
 - [ltmain.sh](#ltmainsh)
 - [sim/common/acinclude.m4](#simcommonacincludem4)
 - [sim/common/Make-common.in](#simcommonmake-commonin)
 - [sim/bfin/configure.ac](#simbfinconfigureac)
 - [sim/bfin/gui.c](#simbfinguic)
 - [config/plugins.m4](#configpluginsm4)
 - [config/tcl.m4](#configtclm4)
 - [config/lib-link.m4](#configlib-linkm4)
 - [include/gcc-c-interface.h](#includegcc-c-interfaceh)
 - [include/elf/mips.h](#includeelfmipsh)
 - [include/aout/sun4.h](#includeaoutsun4h)
 - [bfd/elf32-frv.c](#bfdelf32-frvc)
 - [bfd/configure.ac](#bfdconfigureac)
 - [bfd/Makefile.am](#bfdmakefileam)
 - [bfd/plugin.c](#bfdpluginc)
 - [bfd/Makefile.in](#bfdmakefilein)
 - [bfd/doc/Makefile.in](#bfddocmakefilein)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [readline/aclocal.m4](#readlineaclocalm4)
 - [gdb/breakpoint.c](#gdbbreakpointc)
 - [gdb/gdb-dlfcn.h](#gdbgdb-dlfcnh)
 - [gdb/linux-thread-db.c](#gdblinux-thread-dbc)
 - [gdb/jit.c](#gdbjitc)
 - [gdb/configure.ac](#gdbconfigureac)
 - [gdb/ppc64-tdep.c](#gdbppc64-tdepc)
 - [gdb/sol-thread.c](#gdbsol-threadc)
 - [gdb/gdb-dlfcn.c](#gdbgdb-dlfcnc)
 - [gdb/ia64-libunwind-tdep.c](#gdbia64-libunwind-tdepc)
 - [gdb/compile/compile-c-support.c](#gdbcompilecompile-c-supportc)
 - [gdb/gdbserver/thread-db.c](#gdbgdbserverthread-dbc)
 - [gdb/gdbserver/configure.ac](#gdbgdbserverconfigureac)
 - [gdb/po/gdb.pot](#gdbpogdbpot)
 - [gdb/doc/gdb.info-3](#gdbdocgdbinfo-3)
 - [gdb/doc/gdb.texinfo](#gdbdocgdbtexinfo)
 - [gdb/testsuite/gdb.cp/infcall-dlopen.cc](#gdbtestsuitegdbcpinfcall-dlopencc)
 - [gdb/testsuite/gdb.cp/infcall-dlopen.exp](#gdbtestsuitegdbcpinfcall-dlopenexp)
 - [gdb/testsuite/gdb.cp/Makefile.in](#gdbtestsuitegdbcpmakefilein)
 - [gdb/testsuite/gdb.base/jit-so.exp](#gdbtestsuitegdbbasejit-soexp)
 - [gdb/testsuite/gdb.base/info-shared.c](#gdbtestsuitegdbbaseinfo-sharedc)
 - [gdb/testsuite/gdb.base/catch-load.c](#gdbtestsuitegdbbasecatch-loadc)
 - [gdb/testsuite/gdb.base/catch-load.exp](#gdbtestsuitegdbbasecatch-loadexp)
 - [gdb/testsuite/gdb.base/solib-disc.c](#gdbtestsuitegdbbasesolib-discc)
 - [gdb/testsuite/gdb.base/solib-disc.exp](#gdbtestsuitegdbbasesolib-discexp)
 - [gdb/testsuite/gdb.base/watchpoint-solib.exp](#gdbtestsuitegdbbasewatchpoint-solibexp)
 - [gdb/testsuite/gdb.base/watchpoint-solib.c](#gdbtestsuitegdbbasewatchpoint-solibc)
 - [gdb/testsuite/gdb.base/jit-dlmain.c](#gdbtestsuitegdbbasejit-dlmainc)
 - [gdb/testsuite/gdb.base/break-probes.c](#gdbtestsuitegdbbasebreak-probesc)
 - [gdb/testsuite/gdb.base/sym-file.exp](#gdbtestsuitegdbbasesym-fileexp)
 - [gdb/testsuite/gdb.base/unload.exp](#gdbtestsuitegdbbaseunloadexp)
 - [gdb/testsuite/gdb.base/unload.c](#gdbtestsuitegdbbaseunloadc)
 - [gdb/testsuite/gdb.threads/dlopen-libpthread.c](#gdbtestsuitegdbthreadsdlopen-libpthreadc)
 - [gdb/testsuite/gdb.threads/dlopen-libpthread.exp](#gdbtestsuitegdbthreadsdlopen-libpthreadexp)
 - [gdb/testsuite/gdb.threads/create-fail.exp](#gdbtestsuitegdbthreadscreate-failexp)
 - [gdb/testsuite/gdb.perf/solib.c](#gdbtestsuitegdbperfsolibc)
 - [gdb/testsuite/gdb.trace/change-loc.c](#gdbtestsuitegdbtracechange-locc)
 - [gdb/testsuite/gdb.trace/pending.c](#gdbtestsuitegdbtracependingc)
 - [gdb/testsuite/gdb.mi/mi-pending.c](#gdbtestsuitegdbmimi-pendingc)
 - [gdb/testsuite/gdb.mi/mi-catch-load.exp](#gdbtestsuitegdbmimi-catch-loadexp)
 - [gdb/testsuite/gdb.mi/mi-catch-load.c](#gdbtestsuitegdbmimi-catch-loadc)
 - [gdb/testsuite/gdb.mi/pending.c](#gdbtestsuitegdbmipendingc)

### libtool.m4

```

{% raw %}
1614 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1617 | m4_defun([_LT_TRY_DLOPEN_SELF],
1675 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1708 | ])# _LT_TRY_DLOPEN_SELF
1711 | # LT_SYS_DLOPEN_SELF
1713 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1715 | if test "x$enable_dlopen" != xyes; then
1716 |   enable_dlopen=unknown
1717 |   enable_dlopen_self=unknown
1718 |   enable_dlopen_self_static=unknown
1720 |   lt_cv_dlopen=no
1721 |   lt_cv_dlopen_libs=
1725 |     lt_cv_dlopen="load_add_on"
1726 |     lt_cv_dlopen_libs=
1727 |     lt_cv_dlopen_self=yes
1731 |     lt_cv_dlopen="LoadLibrary"
1732 |     lt_cv_dlopen_libs=
1736 |     lt_cv_dlopen="dlopen"
1737 |     lt_cv_dlopen_libs=
1742 |     AC_CHECK_LIB([dl], [dlopen],
1743 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1744 |     lt_cv_dlopen="dyld"
1745 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen_self=yes
1752 | 	  [lt_cv_dlopen="shl_load"],
1754 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1755 | 	[AC_CHECK_FUNC([dlopen],
1756 | 	      [lt_cv_dlopen="dlopen"],
1757 | 	  [AC_CHECK_LIB([dl], [dlopen],
1758 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1759 | 	    [AC_CHECK_LIB([svld], [dlopen],
1760 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1762 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1771 |   if test "x$lt_cv_dlopen" != xno; then
1772 |     enable_dlopen=yes
1774 |     enable_dlopen=no
1777 |   case $lt_cv_dlopen in
1778 |   dlopen)
1786 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1788 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1789 | 	  lt_cv_dlopen_self, [dnl
1790 | 	  _LT_TRY_DLOPEN_SELF(
1791 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1792 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1795 |     if test "x$lt_cv_dlopen_self" = xyes; then
1797 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1798 | 	  lt_cv_dlopen_self_static, [dnl
1799 | 	  _LT_TRY_DLOPEN_SELF(
1800 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1801 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1811 |   case $lt_cv_dlopen_self in
1812 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1813 |   *) enable_dlopen_self=unknown ;;
1816 |   case $lt_cv_dlopen_self_static in
1817 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1818 |   *) enable_dlopen_self_static=unknown ;;
1821 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1822 | 	 [Whether dlopen is supported])
1823 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1824 | 	 [Whether dlopen of programs is supported])
1825 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1826 | 	 [Whether dlopen of statically linked programs is supported])
1827 | ])# LT_SYS_DLOPEN_SELF
1830 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1832 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5263 |     [Compiler flag to allow reflexive dlopens])
5379 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### md5.sum

```

{% raw %}
2323 | a7c2c6b952b068007c503da1f2aafacc  gdb/testsuite/gdb.threads/dlopen-libpthread.exp
2415 | aa61e41da21e07191a4ea22e45396c02  gdb/testsuite/gdb.threads/dlopen-libpthread.c
2440 | cd24e61275a3331463e1c810ca036ee6  gdb/testsuite/gdb.threads/dlopen-libpthread-lib.c
4500 | 0aa4763f8924318eaee5c9f4a83bf6b6  gdb/testsuite/gdb.cp/infcall-dlopen-lib.cc
4646 | d8eb2f4b229c048d6f9c14b57bb23e09  gdb/testsuite/gdb.cp/infcall-dlopen.cc
4658 | 26eab14f643ef0e99faad7e20d07937b  gdb/testsuite/gdb.cp/infcall-dlopen.exp
{% endraw %}

```
### ltoptions.m4

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
### ltmain.sh

```bash

{% raw %}
895 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
957 |       -dlopen=*|--mode=*|--tag=*)
1047 |   # Only execute mode is allowed to have -dlopen flags.
1049 |     func_error "unrecognized option \`-dlopen'"
1683 |   -dlopen FILE      add the directory containing FILE to the library path
1685 | This mode sets the library path environment variable according to \`-dlopen'
1740 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1749 |   -module           build a library that can dlopened
1855 |     # Handle -dlopen flags immediately.
1872 | 	# Skip this library if it cannot be dlopened.
1899 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4322 | 	    dlopen_self=$dlopen_self_static
4328 | 	    dlopen_self=$dlopen_self_static
4334 | 	    dlopen_self=$dlopen_self_static
4392 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4476 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4638 |       -dlopen)
5029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5096 | 	  # This library was specified with -dlopen.
5211 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5222 | 	passes="conv scan dlopen dlpreopen link"
5248 | 	dlopen) libs="$dlfiles" ;;
5275 |       if test "$pass" = dlopen; then
5487 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5488 | 	      # If there is no dlopen support or we're linking statically,
5518 | 	dlopen=
5548 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5588 | 	# This library was specified with -dlopen.
5589 | 	if test "$pass" = dlopen; then
5591 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5594 | 	     test "$dlopen_support" != yes ||
5596 | 	    # If there is no dlname, no dlopen support or we're linking
5605 | 	fi # $pass = dlopen
5663 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5789 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5790 | 	  dlopenmodule=""
5793 | 	      dlopenmodule="$dlpremoduletest"
5797 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5894 | 		    # if the lib is a (non-dlopened) module then we can not
5898 | 		      if test "X$dlopenmodule" != "X$lib"; then
6050 | 	      echo "*** a static module, that should work as long as the dlopening application"
6051 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6187 |       if test "$pass" != dlopen; then
6286 | 	func_warning "\`-dlopen' is ignored for archives"
6353 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7015 | 	    echo "*** a static module, that should work as long as the dlopening"
7016 | 	    echo "*** application is linked with the -dlopen flag."
7034 | 	    echo "*** or is declared to -dlopen it."
7607 | 	func_warning "\`-dlopen' is ignored for objects"
7722 |         && test "$dlopen_support" = unknown \
7723 | 	&& test "$dlopen_self" = unknown \
7724 | 	&& test "$dlopen_self_static" = unknown && \
7725 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8364 | # The name that we can dlopen(3).
8393 | # Files to dlopen/dlpreopen
8394 | dlopen='$dlfiles'
{% endraw %}

```
### sim/common/acinclude.m4

```

{% raw %}
104 | LT_INIT([dlopen])
105 | AC_SUBST(lt_cv_dlopen_libs)
{% endraw %}

```
### sim/common/Make-common.in

```

{% raw %}
60 | lt_cv_dlopen_libs = @lt_cv_dlopen_libs@
263 | @PLUGINS_TRUE@LIBDL = @lt_cv_dlopen_libs@
{% endraw %}

```
### sim/bfin/configure.ac

```

{% raw %}
60 | 	AC_CHECK_LIB(dl, dlopen, [
{% endraw %}

```
### sim/bfin/gui.c

```cpp

{% raw %}
80 |   sdl.handle = dlopen ("libSDL-1.2.so.0", RTLD_LAZY);
{% endraw %}

```
### config/plugins.m4

```

{% raw %}
12 | 	   AC_MSG_ERROR([Building with plugin support requires a host that supports dlopen.])
18 |     AC_SEARCH_LIBS([dlopen], [dl])
{% endraw %}

```
### config/tcl.m4

```

{% raw %}
1032 |     AC_CHECK_LIB(dl, dlopen, have_dl=yes, have_dl=no)
1772 | 	    # dlopen is in -lc on QNX
1789 | 	    # Note, dlopen is available only on SCO 3.2.5 and greater. However,
{% endraw %}

```
### config/lib-link.m4

```

{% raw %}
377 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### include/gcc-c-interface.h

```cpp

{% raw %}
196 | /* The name of the .so that the compiler builds.  We dlopen this
{% endraw %}

```
### include/elf/mips.h

```cpp

{% raw %}
733 | /* Default suffix of DSO to be added by rld on dlopen() calls.  */
{% endraw %}

```
### include/aout/sun4.h

```cpp

{% raw %}
90 |      ld.so and probably by dlopen.  */
{% endraw %}

```
### bfd/elf32-frv.c

```cpp

{% raw %}
4478 |      suitable for dlopening.  This mark will remain even if we relax
4481 |      dlopening executables.  */
5654 |      that can't be dlopened.  */
{% endraw %}

```
### bfd/configure.ac

```

{% raw %}
42 | LT_INIT([dlopen])
1136 | AC_SUBST(lt_cv_dlopen_libs)
{% endraw %}

```
### bfd/Makefile.am

```

{% raw %}
57 | LIBDL = @lt_cv_dlopen_libs@
{% endraw %}

```
### bfd/plugin.c

```cpp

{% raw %}
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
216 |   plugin_handle = dlopen (pname, RTLD_NOW);
{% endraw %}

```
### bfd/Makefile.in

```

{% raw %}
313 | lt_cv_dlopen_libs = @lt_cv_dlopen_libs@
362 | @PLUGINS_TRUE@LIBDL = @lt_cv_dlopen_libs@
{% endraw %}

```
### bfd/doc/Makefile.in

```

{% raw %}
268 | lt_cv_dlopen_libs = @lt_cv_dlopen_libs@
{% endraw %}

```
### intl/libgnuintl.h

```cpp

{% raw %}
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
81 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### readline/aclocal.m4

```

{% raw %}
3280 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### gdb/breakpoint.c

```cpp

{% raw %}
13088 |      over a dlopen call and solib_add is resetting the breakpoints.
{% endraw %}

```
### gdb/gdb-dlfcn.h

```cpp

{% raw %}
26 | void *gdb_dlopen (const char *filename);
{% endraw %}

```
### gdb/linux-thread-db.c

```cpp

{% raw %}
142 |   /* Handle from dlopen for libthread_db.so.  */
145 |   /* Absolute pathname from gdb_realpath to disk file used for dlopen-ing
225 |    THREAD_DB_LIST.  HANDLE is the handle returned by dlopen'ing
266 |    LIBTHREAD_DB_SO's dlopen'ed handle.  */
665 | /* Attempt to initialize dlopen()ed libthread_db, described by INFO.
840 |   handle = dlopen (library, RTLD_NOW);
844 | 	fprintf_unfiltered (gdb_stdlog, _("dlopen failed: %s.\n"), dlerror ());
953 |    dlopen(file_without_path) will look.
{% endraw %}

```
### gdb/jit.c

```cpp

{% raw %}
176 |   so = gdb_dlopen (file_name);
{% endraw %}

```
### gdb/configure.ac

```

{% raw %}
670 | AC_SEARCH_LIBS(dlopen, dl)
1814 |          AC_CHECK_LIB(dl, dlopen)
2137 |     AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### gdb/ppc64-tdep.c

```cpp

{% raw %}
573 | 	 dlopen, but ld.so has not yet applied the relocations.
{% endraw %}

```
### gdb/sol-thread.c

```cpp

{% raw %}
100 | /* Pointers to routines from libthread_db resolved by dlopen().  */
1246 |   dlhandle = dlopen ("libthread_db.so.1", RTLD_NOW);
{% endraw %}

```
### gdb/gdb-dlfcn.c

```cpp

{% raw %}
34 | gdb_dlopen (const char *filename)
36 |   gdb_assert_not_reached ("gdb_dlopen should not be called on this platform.");
67 | gdb_dlopen (const char *filename)
71 |   result = dlopen (filename, RTLD_NOW);
{% endraw %}

```
### gdb/ia64-libunwind-tdep.c

```cpp

{% raw %}
496 |   handle = dlopen (LIBUNWIND_SO, RTLD_NOW);
501 |       handle = dlopen (LIBUNWIND_SO_7, RTLD_NOW);
{% endraw %}

```
### gdb/compile/compile-c-support.c

```cpp

{% raw %}
79 |    /* gdb_dlopen will call error () on an error, so no need to check
81 |   handle = gdb_dlopen (STRINGIFY (GCC_C_FE_LIBCC));
{% endraw %}

```
### gdb/gdbserver/thread-db.c

```cpp

{% raw %}
54 |   /* Handle of the libthread_db from dlopen.  */
707 |   handle = dlopen (library, RTLD_NOW);
711 | 	debug_printf ("dlopen failed: %s.\n", dlerror ());
742 |    dlopen(file_without_path) will look.
{% endraw %}

```
### gdb/gdbserver/configure.ac

```

{% raw %}
362 | AC_CHECK_LIB(dl, dlopen)
369 |   if test "$ac_cv_lib_dl_dlopen" = "yes"; then
{% endraw %}

```
### gdb/po/gdb.pot

```

{% raw %}
16235 | msgid "dlopen failed: %s.\n"
{% endraw %}

```
### gdb/doc/gdb.info-3

```

{% raw %}
2268 |      On most Unix systems, the function is 'dlopen'.  You'll use the
2271 |           (gdb) call dlopen ("libinproctrace.so", ...)
2273 |      Note that on most Unix systems, for the 'dlopen' function to be
{% endraw %}

```
### gdb/doc/gdb.texinfo

```

{% raw %}
19574 | systems, the function is @code{dlopen}.  You'll use the @code{call}
19578 | (@value{GDBP}) call dlopen ("libinproctrace.so", ...)
19581 | Note that on most Unix systems, for the @code{dlopen} function to be
{% endraw %}

```
### gdb/testsuite/gdb.cp/infcall-dlopen.cc

```cpp

{% raw %}
23 |   void *h = dlopen (filename, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.cp/infcall-dlopen.exp

```

{% raw %}
23 | standard_testfile .cc infcall-dlopen-lib.cc
25 | set lib_dlopen [shlib_target_file ${testfile}.so]
40 |     gdb_test "p openlib (\"${lib_dlopen}\")" " = 1" "test $i"
{% endraw %}

```
### gdb/testsuite/gdb.cp/Makefile.in

```

{% raw %}
7 | 	gdb2384 hang infcall-dlopen inherit koenig local m-data m-static \
{% endraw %}

```
### gdb/testsuite/gdb.base/jit-so.exp

```

{% raw %}
44 | set binfile2_dlopen [shlib_target_file ${testfile2}.so]
71 | 	global verbose testfile srcfile2 binfile2 binfile2_dlopen solib_binfile_target solib_binfile_test_msg
86 | 	gdb_breakpoint [gdb_get_line_number "break here before-dlopen" ]
87 | 	gdb_continue_to_breakpoint "break here before-dlopen"
90 | 	gdb_test_no_output "set var jit_libname = \"$binfile2_dlopen\""
92 | 	gdb_breakpoint [gdb_get_line_number "break here after-dlopen" ]
93 | 	gdb_continue_to_breakpoint "break here after-dlopen"
{% endraw %}

```
### gdb/testsuite/gdb.base/info-shared.c

```cpp

{% raw %}
30 |   handle1 = dlopen (SHLIB1_NAME, RTLD_LAZY);
34 |   handle2 = dlopen (SHLIB2_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/catch-load.c

```cpp

{% raw %}
21 | #define dlopen(name, mode) LoadLibrary (TEXT (name))
35 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/catch-load.exp

```

{% raw %}
35 | set binfile2_dlopen [shlib_target_file ${testfile2}.so]
48 | 	global verbose testfile testfile2 binfile2 binfile2_dlopen
61 | 	gdb_test_no_output "set var libname = \"$binfile2_dlopen\""
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-disc.c

```cpp

{% raw %}
22 | #define dlopen(name, mode) LoadLibrary (name)
35 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-disc.exp

```

{% raw %}
35 | set lib_dlopen [shlib_target_file ${libname}]
44 | set exec_opts [list debug shlib_load additional_flags=-DSHLIB_NAME=\"${lib_dlopen}\"]
{% endraw %}

```
### gdb/testsuite/gdb.base/watchpoint-solib.exp

```

{% raw %}
32 | set lib_dlopen [shlib_target_file ${libname}]
40 | set exec_opts [list debug shlib_load additional_flags=-DSHLIB_NAME=\"${lib_dlopen}\"]
{% endraw %}

```
### gdb/testsuite/gdb.base/watchpoint-solib.c

```cpp

{% raw %}
22 | #define dlopen(name, mode) LoadLibrary (TEXT (name))
39 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/jit-dlmain.c

```cpp

{% raw %}
10 |   h = NULL;  /* break here before-dlopen  */
11 |   h = dlopen (jit_libname, RTLD_LAZY);
17 |   h = h;  /* break here after-dlopen */
{% endraw %}

```
### gdb/testsuite/gdb.base/break-probes.c

```cpp

{% raw %}
22 |   void *handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/sym-file.exp

```

{% raw %}
57 | set lib_dlopen [shlib_target_file ${lib_basename}.so]
60 |  -DSHLIB_NAME\\=\"$lib_dlopen\""]
{% endraw %}

```
### gdb/testsuite/gdb.base/unload.exp

```

{% raw %}
39 | set lib_dlopen [shlib_target_file ${libname}]
40 | set lib_dlopen2 [shlib_target_file ${libname2}]
49 | set exec_opts [list debug shlib_load additional_flags=-DSHLIB_NAME=\"${lib_dlopen}\" additional_flags=-DSHLIB_NAME2=\"${lib_dlopen2}\"]
{% endraw %}

```
### gdb/testsuite/gdb.base/unload.c

```cpp

{% raw %}
22 | #define dlopen(name, mode) LoadLibrary (TEXT (name))
42 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
69 |   handle = dlopen (SHLIB_NAME2, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.threads/dlopen-libpthread.c

```cpp

{% raw %}
36 |   h = dlopen (filename, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.threads/dlopen-libpthread.exp

```

{% raw %}
21 | set testfile "dlopen-libpthread"
27 | set lib_dlopen [shlib_target_file ${executable}.so]
65 | gdb_test "set variable filename=\"$lib_dlopen\""
{% endraw %}

```
### gdb/testsuite/gdb.threads/create-fail.exp

```

{% raw %}
17 | # cancelled.  The spawned child may trigger a dlopen (for libgcc_s)
{% endraw %}

```
### gdb/testsuite/gdb.perf/solib.c

```cpp

{% raw %}
22 | #define dlopen(name, mode) LoadLibrary (TEXT (name))
47 |       handles[i] = dlopen (libname, RTLD_LAZY);
50 | 	  printf ("ERROR on dlopen %s\n", libname);
{% endraw %}

```
### gdb/testsuite/gdb.trace/change-loc.c

```cpp

{% raw %}
38 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.trace/pending.c

```cpp

{% raw %}
37 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-pending.c

```cpp

{% raw %}
31 |   h = dlopen (libname, RTLD_LAZY);  /* set breakpoint here */
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-catch-load.exp

```

{% raw %}
41 | set binfile2_dlopen [shlib_target_file ${testfile2}.so]
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-catch-load.c

```cpp

{% raw %}
21 | #define dlopen(name, mode) LoadLibrary (TEXT (name))
34 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.mi/pending.c

```cpp

{% raw %}
38 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```