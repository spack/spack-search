---
name: "mono"
layout: package
next_package: pangomm
previous_package: py-cyvcf2
languages: ['cpp', 'bash']
---
## 5.10.1.57
46 / 82201 files match

 - [winconfig.h](#winconfigh)
 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [mono/metadata/loader.c](#monometadataloaderc)
 - [mono/utils/mono-dl-posix.c](#monoutilsmono-dl-posixc)
 - [mono/utils/mono-dl.c](#monoutilsmono-dlc)
 - [mono/mini/method-to-ir.c](#monominimethod-to-irc)
 - [mono/mini/mini-darwin.c](#monominimini-darwinc)
 - [mono/eglib/gmodule-unix.c](#monoeglibgmodule-unixc)
 - [libgc/pthread_support.c](#libgcpthread_supportc)
 - [libgc/configure.ac](#libgcconfigureac)
 - [libgc/win32_threads.c](#libgcwin32_threadsc)
 - [libgc/threadlibs.c](#libgcthreadlibsc)
 - [libgc/ltmain.sh](#libgcltmainsh)
 - [libgc/dyn_load.c](#libgcdyn_loadc)
 - [libgc/Makefile.am](#libgcmakefileam)
 - [libgc/gc_dlopen.c](#libgcgc_dlopenc)
 - [libgc/pthread_stop_world.c](#libgcpthread_stop_worldc)
 - [libgc/Makefile.in](#libgcmakefilein)
 - [libgc/include/gc_pthread_redirects.h](#libgcincludegc_pthread_redirectsh)
 - [libgc/m4/libtool.m4](#libgcm4libtoolm4)
 - [libgc/m4/ltoptions.m4](#libgcm4ltoptionsm4)
 - [libgc/m4/lib-link.m4](#libgcm4lib-linkm4)
 - [libgc/doc/README.changes](#libgcdocreadmechanges)
 - [libgc/doc/README.linux](#libgcdocreadmelinux)
 - [libgc/doc/README.solaris2](#libgcdocreadmesolaris2)
 - [runtime/monodis-wrapper.in](#runtimemonodis-wrapperin)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [external/corefx/src/System.Data.Odbc/tests/System.Data.Odbc.Tests.csproj](#externalcorefxsrcsystemdataodbctestssystemdataodbctestscsproj)
 - [external/corefx/src/System.Data.Odbc/tests/Helpers.cs](#externalcorefxsrcsystemdataodbctestshelperscs)
 - [external/corefx/src/Native/Unix/System.Security.Cryptography.Native/opensslshim.cpp](#externalcorefxsrcnativeunixsystemsecuritycryptographynativeopensslshimcpp)
 - [external/corefx/src/Native/Unix/System.Security.Cryptography.Native/CMakeLists.txt](#externalcorefxsrcnativeunixsystemsecuritycryptographynativecmakeliststxt)
 - [external/corefx/src/Common/src/Interop/Unix/libdl/Interop.dlopen.cs](#externalcorefxsrccommonsrcinteropunixlibdlinteropdlopencs)
 - [external/corefx/src/System.Drawing.Common/src/System.Drawing.Common.csproj](#externalcorefxsrcsystemdrawingcommonsrcsystemdrawingcommoncsproj)
 - [external/corefx/src/System.Drawing.Common/src/System/Drawing/GdiplusNative.Unix.cs](#externalcorefxsrcsystemdrawingcommonsrcsystemdrawinggdiplusnativeunixcs)
 - [external/corefx/src/System.Drawing.Common/src/System/Drawing/Printing/LibcupsNative.cs](#externalcorefxsrcsystemdrawingcommonsrcsystemdrawingprintinglibcupsnativecs)
 - [external/corefx/src/System.Drawing.Common/tests/Helpers.cs](#externalcorefxsrcsystemdrawingcommontestshelperscs)
 - [external/corert/src/Native/System.Private.CoreLib.Native/pal_dynamicload.cpp](#externalcorertsrcnativesystemprivatecorelibnativepal_dynamicloadcpp)
 - [man/mono-config.5](#manmono-config5)
 - [mcs/class/System/Mono.AppleTls/Certificate.cs](#mcsclasssystemmonoappletlscertificatecs)
 - [mcs/class/System/Mono.AppleTls/Items.cs](#mcsclasssystemmonoappletlsitemscs)
 - [mcs/class/System/System.Net/MacProxy.cs](#mcsclasssystemsystemnetmacproxycs)
 - [mcs/class/System/System.Net.NetworkInformation/NetworkChange.cs](#mcsclasssystemsystemnetnetworkinformationnetworkchangecs)

### winconfig.h

```cpp

{% raw %}
174 | /* dlopen-based dynamic loader available */
{% endraw %}

```
### config.h.in

```

{% raw %}
295 | /* dlopen-based dynamic loader available */
{% endraw %}

```
### configure.ac

```

{% raw %}
1580 | 	AC_CHECK_FUNC(dlopen, DL_LIB="",
1581 | 		AC_CHECK_LIB(dl, dlopen, DL_LIB="-ldl", dl_support=no)
1587 | 		AC_DEFINE(HAVE_DL_LOADER,1,[dlopen-based dynamic loader available])
1595 | 			  handle = dlopen ((void*)0, 0);
3943 | AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### ltmain.sh

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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### mono/metadata/loader.c

```cpp

{% raw %}
1251 | 		/* we allow a special name to dlopen from the running process namespace */
{% endraw %}

```
### mono/utils/mono-dl-posix.c

```cpp

{% raw %}
68 | 	return dlopen (file, flags);
{% endraw %}

```
### mono/utils/mono-dl.c

```cpp

{% raw %}
71 |  * parse a libtool .la file and return the path of the file to dlopen ()
174 | 		/* This platform does not support dlopen */
{% endraw %}

```
### mono/mini/method-to-ir.c

```cpp

{% raw %}
11700 | 						 * on platforms which don't support dlopen ().
{% endraw %}

```
### mono/mini/mini-darwin.c

```cpp

{% raw %}
70 | /* This is #define'd by Boehm GC to _GC_dlopen. */
71 | #undef dlopen
73 | void* dlopen(const char* path, int mode);
87 | 		void *handle = dlopen ("/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation", RTLD_LAZY);
{% endraw %}

```
### mono/eglib/gmodule-unix.c

```cpp

{% raw %}
59 | 	handle = dlopen (file, f);
{% endraw %}

```
### libgc/pthread_support.c

```cpp

{% raw %}
195 | /* work around a dlopen issue (bug #75390), undefs to avoid warnings with redefinitions */
{% endraw %}

```
### libgc/configure.ac

```

{% raw %}
262 |     AC_CHECK_LIB(dl, dlopen, THREADDLLIBS="$THREADDLLIBS -ldl")
330 |     if test x"${ac_cv_lib_dl_dlopen}" != xyes ; then
331 |        AC_MSG_WARN(OpenBSD/Alpha without dlopen(). Shared library support is disabled)
{% endraw %}

```
### libgc/win32_threads.c

```cpp

{% raw %}
14 | # undef dlopen 
{% endraw %}

```
### libgc/threadlibs.c

```cpp

{% raw %}
7 | 	printf("-Wl,--wrap -Wl,dlopen "
{% endraw %}

```
### libgc/ltmain.sh

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
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### libgc/dyn_load.c

```cpp

{% raw %}
21 |  * that this is a bug in the design of the dlopen interface.  THIS CODE
37 | /* BTL: avoid circular redefinition of dlopen if GC_SOLARIS_THREADS defined */
39 |       && defined(dlopen) && !defined(GC_USE_LD_WRAP)
40 |     /* To support threads in Solaris, gc.h interposes on dlopen by       */
41 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
42 |     /* However, both GC_FirstDLOpenedLinkMap() and GC_dlopen() use the   */
43 |     /* real system dlopen() in their implementation. We first remove     */
44 |     /* gc.h's dlopen definition and restore it later, after GC_dlopen(). */
45 | #   undef dlopen
46 | #   define GC_must_restore_redefined_dlopen
48 | #   undef GC_must_restore_redefined_dlopen
137 | GC_FirstDLOpenedLinkMap()
152 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
178 | /* BTL: added to fix circular dlopen definition if GC_SOLARIS_THREADS defined */
179 | # if defined(GC_must_restore_redefined_dlopen)
180 | #   define dlopen GC_dlopen
190 | GC_FirstDLOpenedLinkMap()
227 | 	--> fix mutual exclusion with dlopen
228 | #   endif  /* We assume M3 programs don't call dlopen for now */
234 |   struct link_map *lm = GC_FirstDLOpenedLinkMap();
237 |   for (lm = GC_FirstDLOpenedLinkMap();
507 | GC_FirstDLOpenedLinkMap()
546 |   lm = GC_FirstDLOpenedLinkMap();
547 |   for (lm = GC_FirstDLOpenedLinkMap();
{% endraw %}

```
### libgc/Makefile.am

```

{% raw %}
45 | dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c headers.c \
{% endraw %}

```
### libgc/gc_dlopen.c

```cpp

{% raw %}
21 |  * dlopen.  Of course this fails if the collector is in a dynamic
30 | # if defined(dlopen) && !defined(GC_USE_LD_WRAP)
31 |     /* To support various threads pkgs, gc.h interposes on dlopen by     */
32 |     /* defining "dlopen" to be "GC_dlopen", which is implemented below.  */
33 |     /* However, both GC_FirstDLOpenedLinkMap() and GC_dlopen() use the   */
34 |     /* real system dlopen() in their implementation. We first remove     */
35 |     /* gc.h's dlopen definition and restore it later, after GC_dlopen(). */
36 | #   undef dlopen
41 |   /* This is invoked prior to a dlopen call to avoid synchronization	*/
43 |   /* code in dlopen may try to allocate.				*/
44 |   /* This solution risks heap growth in the presence of many dlopen	*/
48 |   static void disable_gc_for_dlopen()
58 |   /* Redefine dlopen to guarantee mutual exclusion with	*/
65 |   void * __wrap_dlopen(const char *path, int mode)
67 |   void * GC_dlopen(path, mode)
75 |       disable_gc_for_dlopen();
78 |       result = (void *)__real_dlopen(path, mode);
80 |       result = dlopen(path, mode);
83 |       GC_enable(); /* undoes disable_gc_for_dlopen */
{% endraw %}

```
### libgc/pthread_stop_world.c

```cpp

{% raw %}
13 | /* work around a dlopen issue (bug #75390), undefs to avoid warnings with redefinitions */
{% endraw %}

```
### libgc/Makefile.in

```

{% raw %}
116 | 	checksums.c dbg_mlc.c dyn_load.c finalize.c gc_dlopen.c \
127 | 	dbg_mlc.lo dyn_load.lo finalize.lo gc_dlopen.lo gcj_mlc.lo \
146 | 	checksums.c dbg_mlc.c dyn_load.c finalize.c gc_dlopen.c \
155 | 	checksums.lo dbg_mlc.lo dyn_load.lo finalize.lo gc_dlopen.lo \
471 | dyn_load.c finalize.c gc_dlopen.c gcj_mlc.c headers.c \
635 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/gc_dlopen.Plo@am__quote@
{% endraw %}

```
### libgc/include/gc_pthread_redirects.h

```cpp

{% raw %}
23 |   void * GC_dlopen(const char *path, int mode);
44 | # define dlopen GC_dlopen
86 | # define dlopen GC_dlopen
{% endraw %}

```
### libgc/m4/libtool.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5676 |     [Compiler flag to allow reflexive dlopens])
5789 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libgc/m4/ltoptions.m4

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
### libgc/m4/lib-link.m4

```

{% raw %}
515 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### libgc/doc/README.changes

```

{% raw %}
932 |  - Added an attempt at a more general solution to dlopen races/deadlocks.
933 |    GC_dlopen now temporarily disables collection.  Still not ideal, but ...
2253 |  - A dynamic libgc.so references dlopen unconditionally, but doesn't link
{% endraw %}

```
### libgc/doc/README.linux

```

{% raw %}
39 |    (for ld) --wrap read --wrap dlopen --wrap pthread_create \
43 |    (for gcc) -Wl,--wrap -Wl,read -Wl,--wrap -Wl,dlopen -Wl,--wrap \
50 | 4) Dlopen() disables collection during its execution.  (It can't run
53 |    user startup code may run as part of dlopen().)  Under unusual
{% endraw %}

```
### libgc/doc/README.solaris2

```

{% raw %}
25 | thr_join, thr_suspend, thr_continue, or dlopen.  Gc.h macro defines
39 | Since 5.0 alpha5, dlopen disables collection temporarily,
{% endraw %}

```
### runtime/monodis-wrapper.in

```

{% raw %}
4 | exec "$r/libtool" --mode=execute -dlopen "$r/mono/mini/libmono-2.0.la" "$r/mono/dis/monodis" "$@"
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5676 |     [Compiler flag to allow reflexive dlopens])
5789 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

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
### m4/lib-link.m4

```

{% raw %}
515 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### external/corefx/src/System.Data.Odbc/tests/System.Data.Odbc.Tests.csproj

```

{% raw %}
28 |     <Compile Include="$(CommonPath)\Interop\Unix\libdl\Interop.dlopen.cs">
29 |       <Link>Common\Interop\Unix\libdl\Interop.dlopen.cs</Link>
{% endraw %}

```
### external/corefx/src/System.Data.Odbc/tests/Helpers.cs

```

{% raw %}
24 |                 Interop.Libdl.dlopen(Interop.Libraries.Odbc32, Interop.Libdl.RTLD_NOW) != IntPtr.Zero;
{% endraw %}

```
### external/corefx/src/Native/Unix/System.Security.Cryptography.Native/opensslshim.cpp

```

{% raw %}
20 |     libssl = dlopen("libssl.so.1.0.0", RTLD_LAZY);
24 |         libssl = dlopen("libssl.so.10", RTLD_LAZY);
30 |         libssl = dlopen("libssl.so.1.0.2", RTLD_LAZY);
{% endraw %}

```
### external/corefx/src/Native/Unix/System.Security.Cryptography.Native/CMakeLists.txt

```

{% raw %}
84 |     # Link with libdl.so to get the dlopen / dlsym / dlclose
{% endraw %}

```
### external/corefx/src/Common/src/Interop/Unix/libdl/Interop.dlopen.cs

```

{% raw %}
14 |         public static extern IntPtr dlopen(string fileName, int flag);
{% endraw %}

```
### external/corefx/src/System.Drawing.Common/src/System.Drawing.Common.csproj

```

{% raw %}
338 |     <Compile Include="$(CommonPath)\Interop\Unix\libdl\Interop.dlopen.cs">
339 |       <Link>Common\Interop\Unix\libdl\Interop.dlopen.cs</Link>
{% endraw %}

```
### external/corefx/src/System.Drawing.Common/src/System/Drawing/GdiplusNative.Unix.cs

```

{% raw %}
34 |                     lib = Interop.Libdl.dlopen(libraryName, Interop.Libdl.RTLD_NOW);
43 |                     lib = Interop.Libdl.dlopen(libraryName, Interop.Libdl.RTLD_NOW);
46 |                         lib = Interop.Libdl.dlopen("libgdiplus.so.0", Interop.Libdl.RTLD_NOW);
60 |                         lib = Interop.Libdl.dlopen(searchPath, Interop.Libdl.RTLD_NOW);
{% endraw %}

```
### external/corefx/src/System.Drawing.Common/src/System/Drawing/Printing/LibcupsNative.cs

```

{% raw %}
17 |             IntPtr lib = Interop.Libdl.dlopen("libcups.so", Interop.Libdl.RTLD_NOW);
20 |                 lib = Interop.Libdl.dlopen("libcups.so.2", Interop.Libdl.RTLD_NOW);
{% endraw %}

```
### external/corefx/src/System.Drawing.Common/tests/Helpers.cs

```

{% raw %}
32 |                     nativeLib = dlopen("libgdiplus.dylib", RTLD_NOW);
36 |                     nativeLib = dlopen("libgdiplus.so", RTLD_NOW);
39 |                         nativeLib = dlopen("libgdiplus.so.0", RTLD_NOW);
95 |         private static extern IntPtr dlopen(string libName, int flags);
{% endraw %}

```
### external/corert/src/Native/System.Private.CoreLib.Native/pal_dynamicload.cpp

```

{% raw %}
8 |     return dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### man/mono-config.5

```

{% raw %}
47 | loading routines (dlopen etc.), so you may want to check the manpages for that, too.
{% endraw %}

```
### mcs/class/System/Mono.AppleTls/Certificate.cs

```

{% raw %}
206 | 			var handle = CFObject.dlopen (AppleTlsContext.SecurityLibrary, 0);
{% endraw %}

```
### mcs/class/System/Mono.AppleTls/Items.cs

```

{% raw %}
71 | 			var handle = CFObject.dlopen (AppleTlsContext.SecurityLibrary, 0);
249 | 			var handle = CFObject.dlopen (AppleTlsContext.SecurityLibrary, 0);
307 | 			var handle = CFObject.dlopen (AppleTlsContext.SecurityLibrary, 0);
330 | 			var handle = CFObject.dlopen (AppleTlsContext.SecurityLibrary, 0);
{% endraw %}

```
### mcs/class/System/System.Net/MacProxy.cs

```

{% raw %}
46 | 		public static extern IntPtr dlopen (string path, int mode);
143 | 			var handle = dlopen (CoreFoundationLibrary, 0);
453 | 			var handle = dlopen (CoreFoundationLibrary, 0);
641 | 			IntPtr handle = CFObject.dlopen (CFNetwork.CFNetworkLibrary, 0);
776 | 			IntPtr handle = CFObject.dlopen (CFNetwork.CFNetworkLibrary, 0);
1270 | 			var handle = CFObject.dlopen (CFObject.CoreFoundationLibrary, 0);
{% endraw %}

```
### mcs/class/System/System.Net.NetworkInformation/NetworkChange.cs

```

{% raw %}
139 | 		static extern IntPtr dlopen (string path, int mode);
267 | 			var cfLibHandle = dlopen (CORE_FOUNDATION_LIB, 0);
{% endraw %}

```