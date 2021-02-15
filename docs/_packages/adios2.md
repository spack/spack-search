---
name: "adios2"
layout: package
next_package: libpthread-stubs
previous_package: coin3d
languages: ['cmake', 'cpp', 'bash', 'pl']
---
## 2.3.1
20 / 1971 files match

 - [CTestCustom.cmake.in](#ctestcustomcmakein)
 - [thirdparty/enet/enet/ltmain.sh](#thirdpartyenetenetltmainsh)
 - [thirdparty/enet/enet/m4/libtool.m4](#thirdpartyenetenetm4libtoolm4)
 - [thirdparty/enet/enet/m4/ltoptions.m4](#thirdpartyenetenetm4ltoptionsm4)
 - [thirdparty/EVPath/EVPath/cm.c](#thirdpartyevpathevpathcmc)
 - [thirdparty/EVPath/EVPath/gen_interface.pl](#thirdpartyevpathevpathgen_interfacepl)
 - [thirdparty/EVPath/EVPath/cm_transport.c](#thirdpartyevpathevpathcm_transportc)
 - [thirdparty/EVPath/EVPath/evpath.supp](#thirdpartyevpathevpathevpathsupp)
 - [thirdparty/EVPath/EVPath/dlloader.c](#thirdpartyevpathevpathdlloaderc)
 - [thirdparty/EVPath/EVPath/dlloader.h](#thirdpartyevpathevpathdlloaderh)
 - [thirdparty/EVPath/EVPath/cm_util.c](#thirdpartyevpathevpathcm_utilc)
 - [thirdparty/EVPath/EVPath/response.c](#thirdpartyevpathevpathresponsec)
 - [thirdparty/EVPath/EVPath/cmake/CreateLibtoolFile.cmake](#thirdpartyevpathevpathcmakecreatelibtoolfilecmake)
 - [thirdparty/EVPath/EVPath/doc/cm.tex](#thirdpartyevpathevpathdoccmtex)
 - [thirdparty/ffs/ffs/cod/standard.c](#thirdpartyffsffscodstandardc)
 - [thirdparty/pybind11/pybind11/include/pybind11/detail/internals.h](#thirdpartypybind11pybind11includepybind11detailinternalsh)
 - [thirdparty/pybind11/pybind11/docs/faq.rst](#thirdpartypybind11pybind11docsfaqrst)
 - [thirdparty/KWSys/adios2sys/DynamicLoader.cxx](#thirdpartykwsysadios2sysdynamicloadercxx)
 - [thirdparty/KWSys/adios2sys/DynamicLoader.hxx.in](#thirdpartykwsysadios2sysdynamicloaderhxxin)
 - [thirdparty/KWSys/adios2sys/testDynamicLoader.cxx](#thirdpartykwsysadios2systestdynamicloadercxx)

### CTestCustom.cmake.in

```

{% raw %}
9 |   "H5PL\\.c.*dlopen.*glibc"
{% endraw %}

```
### thirdparty/enet/enet/ltmain.sh

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
### thirdparty/enet/enet/m4/libtool.m4

```

{% raw %}
1750 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1753 | m4_defun([_LT_TRY_DLOPEN_SELF],
1811 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1844 | ])# _LT_TRY_DLOPEN_SELF
1847 | # LT_SYS_DLOPEN_SELF
1849 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1851 | if test "x$enable_dlopen" != xyes; then
1852 |   enable_dlopen=unknown
1853 |   enable_dlopen_self=unknown
1854 |   enable_dlopen_self_static=unknown
1856 |   lt_cv_dlopen=no
1857 |   lt_cv_dlopen_libs=
1861 |     lt_cv_dlopen="load_add_on"
1862 |     lt_cv_dlopen_libs=
1863 |     lt_cv_dlopen_self=yes
1867 |     lt_cv_dlopen="LoadLibrary"
1868 |     lt_cv_dlopen_libs=
1872 |     lt_cv_dlopen="dlopen"
1873 |     lt_cv_dlopen_libs=
1878 |     AC_CHECK_LIB([dl], [dlopen],
1879 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1880 |     lt_cv_dlopen="dyld"
1881 |     lt_cv_dlopen_libs=
1882 |     lt_cv_dlopen_self=yes
1888 | 	  [lt_cv_dlopen="shl_load"],
1890 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1891 | 	[AC_CHECK_FUNC([dlopen],
1892 | 	      [lt_cv_dlopen="dlopen"],
1893 | 	  [AC_CHECK_LIB([dl], [dlopen],
1894 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1895 | 	    [AC_CHECK_LIB([svld], [dlopen],
1896 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1898 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1907 |   if test "x$lt_cv_dlopen" != xno; then
1908 |     enable_dlopen=yes
1910 |     enable_dlopen=no
1913 |   case $lt_cv_dlopen in
1914 |   dlopen)
1922 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1924 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1925 | 	  lt_cv_dlopen_self, [dnl
1926 | 	  _LT_TRY_DLOPEN_SELF(
1927 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1928 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1931 |     if test "x$lt_cv_dlopen_self" = xyes; then
1933 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1934 | 	  lt_cv_dlopen_self_static, [dnl
1935 | 	  _LT_TRY_DLOPEN_SELF(
1936 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1937 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1947 |   case $lt_cv_dlopen_self in
1948 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1949 |   *) enable_dlopen_self=unknown ;;
1952 |   case $lt_cv_dlopen_self_static in
1953 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1954 |   *) enable_dlopen_self_static=unknown ;;
1957 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1958 | 	 [Whether dlopen is supported])
1959 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1960 | 	 [Whether dlopen of programs is supported])
1961 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1962 | 	 [Whether dlopen of statically linked programs is supported])
1963 | ])# LT_SYS_DLOPEN_SELF
1966 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1968 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5668 |     [Compiler flag to allow reflexive dlopens])
5781 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### thirdparty/enet/enet/m4/ltoptions.m4

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
### thirdparty/EVPath/EVPath/cm.c

```cpp

{% raw %}
3581 |      handle = CMdlopen(cm->CMTrace_file, libname, 0);
{% endraw %}

```
### thirdparty/EVPath/EVPath/gen_interface.pl

```pl

{% raw %}
622 | #define lt_dlopen(x) dlopen(x, 0)
754 | 	h = lt_dlopen(NULL);
759 | 	    dh = dlopen(NULL, 0);
761 | 	printf("Querying dlopen()\\n");
766 | 	    dh = dlopen(NULL, RTLD_GLOBAL|RTLD_LAZY);
774 | 	printf("Try linking the program with either \\"-rdynamic\\" (GCC) or \\"-dlopen self\\" (libtool)\\n");
{% endraw %}

```
### thirdparty/EVPath/EVPath/cm_transport.c

```cpp

{% raw %}
134 |     handle = CMdlopen(cm->CMTrace_file, libname, 0);
{% endraw %}

```
### thirdparty/EVPath/EVPath/evpath.supp

```

{% raw %}
107 |    Anything under dlopen isn't our fault.
111 |    fun:CMdlopen
{% endraw %}

```
### thirdparty/EVPath/EVPath/dlloader.c

```cpp

{% raw %}
24 |     void *dlopen_handle;
28 | static int dlopen_verbose = -1;
31 | CMset_dlopen_verbose(int verbose)
33 |     dlopen_verbose = verbose;
37 | CMdlopen(void *CMTrace_filev, char *in_lib, int mode)
47 |     if (dlopen_verbose == -1) {
48 | 	dlopen_verbose = (getenv("CMTransportVerbose") != NULL);
51 |     if (dlopen_verbose) fprintf(CMTrace_file, "Trying to dlopen %s\n", in_lib);
57 | 	if (dlopen_verbose) fprintf(CMTrace_file, "Dlopen module name replaced, now %s\n", lib);
65 | 	handle = dlopen(tmp, RTLD_LAZY);
67 | 	if (dlopen_verbose) {
69 | 		fprintf(CMTrace_file, "Failed to dlopen %s, error is %s\n", tmp, err);
71 | 		fprintf(CMTrace_file, "DLopen of %s succeeded\n", tmp);
79 |         handle = dlopen(lib, RTLD_LAZY);
81 | 	if (dlopen_verbose) {
83 | 		fprintf(CMTrace_file, "Failed to dlopen %s, error is %s\n", tmp, err);
85 | 		fprintf(CMTrace_file, "DLopen of %s succeeded\n", tmp);
108 |     dlh->dlopen_handle = handle;
125 |     sym_val = dlsym(dlh->dlopen_handle, tmp);
128 | 	sym_val = dlsym(dlh->dlopen_handle, sym);
141 |     dlclose(dlh->dlopen_handle);
{% endraw %}

```
### thirdparty/EVPath/EVPath/dlloader.h

```cpp

{% raw %}
1 | #define lt_dlopen(x) CMdlopen(cm, x, 0)
7 | extern void* CMdlopen(void *CMTrace_file, char *library, int mode);
11 | extern void CMset_dlopen_verbose(int verbose);
{% endraw %}

```
### thirdparty/EVPath/EVPath/cm_util.c

```cpp

{% raw %}
26 | extern void CMset_dlopen_verbose(int verbose);
110 | 	CMset_dlopen_verbose(1);
{% endraw %}

```
### thirdparty/EVPath/EVPath/response.c

```cpp

{% raw %}
2067 |     handle = CMdlopen(cm->CMTrace_file, path, 0);
{% endraw %}

```
### thirdparty/EVPath/EVPath/cmake/CreateLibtoolFile.cmake

```cmake

{% raw %}
17 |    GET_TARGET_PROPERTY_WITH_DEFAULT(_target_dlopen ${_target} LT_DLOPEN "")
24 |    FILE(APPEND ${_laname} "# The name that we can dlopen(3).\n")
58 |    FILE(APPEND ${_laname} "# Files to dlopen/dlpreopen\n")
59 |    FILE(APPEND ${_laname} "dlopen='${_target_dlopen}'\n")
{% endraw %}

```
### thirdparty/EVPath/EVPath/doc/cm.tex

```

{% raw %}
442 | libraries is that CM uses program-controlled dynamic linking (dlopen-style)
444 | programs {\it cannot} use {\tt dlopen()}. If CM is unable to load its
{% endraw %}

```
### thirdparty/ffs/ffs/cod/standard.c

```cpp

{% raw %}
686 |     void *handle = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### thirdparty/pybind11/pybind11/include/pybind11/detail/internals.h

```cpp

{% raw %}
20 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```
### thirdparty/pybind11/pybind11/docs/faq.rst

```

{% raw %}
172 | typically using ``dlopen`` with the ``RTLD_LOCAL`` flag), this Python default
{% endraw %}

```
### thirdparty/KWSys/adios2sys/DynamicLoader.cxx

```

{% raw %}
22 | //   later) which use dlopen
400 | // later) which use dlopen
408 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### thirdparty/KWSys/adios2sys/DynamicLoader.hxx.in

```

{% raw %}
32 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### thirdparty/KWSys/adios2sys/testDynamicLoader.cxx

```

{% raw %}
89 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
99 |   // This one is actually fun to test, since dlopen is by default
101 |   res += TestDynamicLoader("foobar.lib", "dlopen", 0, 1, 0);
102 |   res += TestDynamicLoader("libdl.so", "dlopen", 1, 1, 1);
{% endraw %}

```