---
name: "python"
layout: package
next_package: freeipmi
previous_package: etcd
languages: ['bash', 'cpp', 'python']
---
## 3.6.12
24 / 4070 files match

 - [pyconfig.h.in](#pyconfighin)
 - [configure.ac](#configureac)
 - [setup.py](#setuppy)
 - [Lib/test/test_sys.py](#libtesttest_syspy)
 - [Lib/ctypes/__init__.py](#libctypes__init__py)
 - [Doc/library/os.rst](#doclibraryosrst)
 - [Doc/library/sys.rst](#doclibrarysysrst)
 - [Doc/library/ctypes.rst](#doclibraryctypesrst)
 - [Doc/tutorial/modules.rst](#doctutorialmodulesrst)
 - [Doc/whatsnew/2.2.rst](#docwhatsnew22rst)
 - [Doc/whatsnew/2.5.rst](#docwhatsnew25rst)
 - [Doc/whatsnew/3.3.rst](#docwhatsnew33rst)
 - [Python/dynload_shlib.c](#pythondynload_shlibc)
 - [Python/sysmodule.c](#pythonsysmodulec)
 - [Python/pystate.c](#pythonpystatec)
 - [Include/pystate.h](#includepystateh)
 - [Modules/_ctypes/ctypes_dlfcn.h](#modules_ctypesctypes_dlfcnh)
 - [Modules/_ctypes/callproc.c](#modules_ctypescallprocc)
 - [Modules/_ctypes/darwin/dlfcn.h](#modules_ctypesdarwindlfcnh)
 - [Modules/_ctypes/darwin/dlfcn_simple.c](#modules_ctypesdarwindlfcn_simplec)
 - [Modules/_ctypes/libffi/ltmain.sh](#modules_ctypeslibffiltmainsh)
 - [Modules/_ctypes/libffi/aclocal.m4](#modules_ctypeslibffiaclocalm4)
 - [Modules/_ctypes/libffi/m4/libtool.m4](#modules_ctypeslibffim4libtoolm4)
 - [Modules/_ctypes/libffi/m4/ltoptions.m4](#modules_ctypeslibffim4ltoptionsm4)

### pyconfig.h.in

```

{% raw %}
256 | /* Define to 1 if you have the `dlopen' function. */
257 | #undef HAVE_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
2776 | AC_CHECK_LIB(dl, dlopen)	# Dynamic linking for SunOS/Solaris and SYSV
3478 | # the dlopen() function means we might want to use dynload_shlib.o. some
3479 | # platforms, such as AIX, have dlopen(), but don't want to use it.
3480 | AC_CHECK_FUNCS(dlopen)
3489 | 	AIX*) # Use dynload_shlib.c and dlopen() if we have it; otherwise dynload_aix.c
3490 | 	if test "$ac_cv_func_dlopen" = yes
3496 | 	# Use dynload_next.c only on 10.2 and below, which don't have native dlopen()
3499 | 	# use dynload_shlib.c and dlopen() if we have it; otherwise stub
3501 | 	if test "$ac_cv_func_dlopen" = yes
{% endraw %}

```
### setup.py

```python

{% raw %}
2097 |             # for dlopen, see bpo-32647
{% endraw %}

```
### Lib/test/test_sys.py

```python

{% raw %}
315 |     @unittest.skipUnless(hasattr(sys, "setdlopenflags"),
316 |                          'test needs sys.setdlopenflags()')
317 |     def test_dlopenflags(self):
318 |         self.assertTrue(hasattr(sys, "getdlopenflags"))
319 |         self.assertRaises(TypeError, sys.getdlopenflags, 42)
320 |         oldflags = sys.getdlopenflags()
321 |         self.assertRaises(TypeError, sys.setdlopenflags)
322 |         sys.setdlopenflags(oldflags+1)
323 |         self.assertEqual(sys.getdlopenflags(), oldflags+1)
324 |         sys.setdlopenflags(oldflags)
{% endraw %}

```
### Lib/ctypes/__init__.py

```python

{% raw %}
106 |     from _ctypes import LoadLibrary as _dlopen
132 |     from _ctypes import dlopen as _dlopen
347 |             self._handle = _dlopen(self._name, mode)
{% endraw %}

```
### Doc/library/os.rst

```

{% raw %}
3950 |    Flags for use with the :func:`~sys.setdlopenflags` and
3951 |    :func:`~sys.getdlopenflags` functions.  See the Unix manual page
3952 |    :manpage:`dlopen(3)` for what the different flags mean.
{% endraw %}

```
### Doc/library/sys.rst

```

{% raw %}
423 | .. function:: getdlopenflags()
426 |    :c:func:`dlopen` calls.  Symbolic names for the flag values can be
991 | .. function:: setdlopenflags(n)
993 |    Set the flags used by the interpreter for :c:func:`dlopen` calls, such as when
996 |    ``sys.setdlopenflags(0)``.  To share symbols across extension modules, call as
997 |    ``sys.setdlopenflags(os.RTLD_GLOBAL)``.  Symbolic names for the flag values
{% endraw %}

```
### Doc/library/ctypes.rst

```

{% raw %}
1370 | parameter, otherwise the underlying platforms ``dlopen`` or ``LoadLibrary``
1375 | details, consult the :manpage:`dlopen(3)` manpage.  On Windows, *mode* is
{% endraw %}

```
### Doc/tutorial/modules.rst

```

{% raw %}
316 |     'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
322 |     'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
{% endraw %}

```
### Doc/whatsnew/2.2.rst

```

{% raw %}
1244 | * On platforms where Python uses the C :c:func:`dlopen` function  to load
1245 |   extension modules, it's now possible to set the flags used  by :c:func:`dlopen`
1246 |   using the :func:`sys.getdlopenflags` and :func:`sys.setdlopenflags` functions.
{% endraw %}

```
### Doc/whatsnew/2.5.rst

```

{% raw %}
2210 |   :c:func:`dlopen` function instead of MacOS-specific functions.
{% endraw %}

```
### Doc/whatsnew/3.3.rst

```

{% raw %}
1696 |   :func:`sys.setdlopenflags` function, and supersede the similar constants
{% endraw %}

```
### Python/dynload_shlib.c

```cpp

{% raw %}
62 |     int dlopenflags=0;
92 |     dlopenflags = PyThreadState_GET()->interp->dlopenflags;
94 |     handle = dlopen(pathname, dlopenflags);
102 |             error = "unknown dlopen() error";
{% endraw %}

```
### Python/sysmodule.c

```cpp

{% raw %}
1023 | #ifdef HAVE_DLOPEN
1025 | sys_setdlopenflags(PyObject *self, PyObject *args)
1029 |     if (!PyArg_ParseTuple(args, "i:setdlopenflags", &new_val))
1033 |     tstate->interp->dlopenflags = new_val;
1038 | PyDoc_STRVAR(setdlopenflags_doc,
1039 | "setdlopenflags(n) -> None\n\
1041 | Set the flags used by the interpreter for dlopen calls, such as when the\n\
1044 | sys.setdlopenflags(0).  To share symbols across extension modules, call as\n\
1045 | sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag modules\n\
1049 | sys_getdlopenflags(PyObject *self, PyObject *args)
1054 |     return PyLong_FromLong(tstate->interp->dlopenflags);
1057 | PyDoc_STRVAR(getdlopenflags_doc,
1058 | "getdlopenflags() -> int\n\
1060 | Return the current value of the flags that are used for dlopen calls.\n\
1063 | #endif  /* HAVE_DLOPEN */
1366 | #ifdef HAVE_DLOPEN
1367 |     {"getdlopenflags", (PyCFunction)sys_getdlopenflags, METH_NOARGS,
1368 |      getdlopenflags_doc},
1415 | #ifdef HAVE_DLOPEN
1416 |     {"setdlopenflags", sys_setdlopenflags, METH_VARARGS,
1417 |      setdlopenflags_doc},
1644 | getdlopenflags() -- returns flags to be used for dlopen() calls\n\
1651 | setdlopenflags() -- set the flags to be used for dlopen() calls\n\
{% endraw %}

```
### Python/pystate.c

```cpp

{% raw %}
23 | #ifdef HAVE_DLOPEN
103 | #ifdef HAVE_DLOPEN
105 |         interp->dlopenflags = RTLD_NOW;
107 |         interp->dlopenflags = RTLD_LAZY;
{% endraw %}

```
### Include/pystate.h

```cpp

{% raw %}
42 | #ifdef HAVE_DLOPEN
43 |     int dlopenflags;
{% endraw %}

```
### Modules/_ctypes/ctypes_dlfcn.h

```cpp

{% raw %}
15 | #define ctypes_dlopen dlopen
{% endraw %}

```
### Modules/_ctypes/callproc.c

```cpp

{% raw %}
1362 |     if (!PyArg_ParseTuple(args, "O|i:dlopen", &name, &mode))
1376 |     handle = ctypes_dlopen(name_str, mode);
1381 |             errmsg = "dlopen() error";
1826 |     {"dlopen", py_dl_open, METH_VARARGS,
1827 |      "dlopen(name, flag={RTLD_GLOBAL|RTLD_LOCAL}) open a shared library"},
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn.h

```cpp

{% raw %}
55 | extern void * (*ctypes_dlopen)(const char *path, int mode);
61 | extern void * dlopen(const char *path, int mode);
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn_simple.c

```cpp

{% raw %}
51 | #define DARWIN_HAS_DLOPEN
52 | extern void * dlopen(const char *path, int mode) __attribute__((weak_import));
59 | #ifndef DARWIN_HAS_DLOPEN
60 | #define dlopen darwin_dlopen
67 | void * (*ctypes_dlopen)(const char *path, int mode);
74 | /* Mac OS X 10.3+ has dlopen, so strip all this dead code to avoid warnings */
107 | /* darwin_dlopen */
108 | static void *darwin_dlopen(const char *path, int mode)
254 |     if (dlopen != NULL) {
256 |         ctypes_dlopen = dlopen;
263 |         ctypes_dlopen = darwin_dlopen;
{% endraw %}

```
### Modules/_ctypes/libffi/ltmain.sh

```bash

{% raw %}
2161 |     opt_dlopen=
2222 |         --dlopen|-dlopen)
2223 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2337 |       # Only execute mode is allowed to have -dlopen flags.
2338 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2339 |         func_error "unrecognized option '-dlopen'"
3557 |   -dlopen FILE      add the directory containing FILE to the library path
3559 | This mode sets the library path environment variable according to '-dlopen'
3614 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3623 |   -module           build a library that can dlopened
3730 |     # Handle -dlopen flags immediately.
3731 |     for file in $opt_dlopen; do
3750 | 	# Skip this library if it cannot be dlopened.
3777 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6439 | 	    dlopen_self=$dlopen_self_static
6445 | 	    dlopen_self=$dlopen_self_static
6451 | 	    dlopen_self=$dlopen_self_static
6509 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6599 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6761 |       -dlopen)
7170 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7238 | 	  # This library was specified with -dlopen.
7355 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7366 | 	passes="conv scan dlopen dlpreopen link"
7392 | 	dlopen) libs=$dlfiles ;;
7420 |       if test dlopen = "$pass"; then
7640 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7641 | 	      # If there is no dlopen support or we're linking statically,
7669 | 	dlopen=
7699 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7745 | 	# This library was specified with -dlopen.
7746 | 	if test dlopen = "$pass"; then
7748 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7750 | 	     test yes != "$dlopen_support" ||
7753 | 	    # If there is no dlname, no dlopen support or we're linking
7762 | 	fi # $pass = dlopen
7818 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7820 | 	      # We recover the dlopen module name by 'saving' the la file
7844 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
7973 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
7974 | 	  dlopenmodule=
7977 | 	      dlopenmodule=$dlpremoduletest
7981 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8078 | 		    # if the lib is a (non-dlopened) module then we cannot
8082 | 		      if test "X$dlopenmodule" != "X$lib"; then
8234 | 	      echo "*** a static module, that should work as long as the dlopening application"
8235 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8379 |       if test dlopen != "$pass"; then
8478 | 	func_warning "'-dlopen' is ignored for archives"
8545 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9233 | 	    echo "*** a static module, that should work as long as the dlopening"
9234 | 	    echo "*** application is linked with the -dlopen flag."
9252 | 	    echo "*** or is declared to -dlopen it."
9864 | 	func_warning "'-dlopen' is ignored for objects"
9982 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
9983 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10664 | # The name that we can dlopen(3).
10693 | # Files to dlopen/dlpreopen
10694 | dlopen='$dlfiles'
{% endraw %}

```
### Modules/_ctypes/libffi/aclocal.m4

```

{% raw %}
221 | 			  _LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"])],
222 | 	  [nonrecursive], [_LT_SHELL_INIT([lt_dlopen_dir="$lt_ltdl_dir"; lt_libobj_prefix="$lt_ltdl_dir/"])],
396 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
440 | eval "LTDLOPEN=\"$libname_spec\""
441 | AC_SUBST([LTDLOPEN])
462 | # LT_SYS_DLOPEN_DEPLIBS
464 | AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS],
466 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
467 |   [lt_cv_sys_dlopen_deplibs],
468 |   [# PORTME does your system automatically load deplibs for dlopen?
472 |   lt_cv_sys_dlopen_deplibs=unknown
477 |     lt_cv_sys_dlopen_deplibs=unknown
480 |     lt_cv_sys_dlopen_deplibs=yes
485 |       lt_cv_sys_dlopen_deplibs=no
492 |     lt_cv_sys_dlopen_deplibs=yes
495 |     lt_cv_sys_dlopen_deplibs=yes
499 |     lt_cv_sys_dlopen_deplibs=yes
502 |     lt_cv_sys_dlopen_deplibs=yes
505 |     lt_cv_sys_dlopen_deplibs=yes
510 |     lt_cv_sys_dlopen_deplibs=unknown
514 |     # at 6.2 and later dlopen does load deplibs.
515 |     lt_cv_sys_dlopen_deplibs=yes
518 |     lt_cv_sys_dlopen_deplibs=yes
521 |     lt_cv_sys_dlopen_deplibs=yes
524 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
527 |     lt_cv_sys_dlopen_deplibs=no
530 |     # dlopen *does* load deplibs and with the right loader patch applied
536 |     lt_cv_sys_dlopen_deplibs=unknown
543 |     lt_cv_sys_dlopen_deplibs=yes
546 |     lt_cv_sys_dlopen_deplibs=yes
549 |     lt_cv_sys_dlopen_deplibs=yes
552 |     libltdl_cv_sys_dlopen_deplibs=yes
556 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
557 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
558 |     [Define if the OS needs help to load dependent libraries for dlopen().])
560 | ])# LT_SYS_DLOPEN_DEPLIBS
563 | AU_ALIAS([AC_LTDL_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS])
565 | dnl AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [])
649 | AC_CACHE_CHECK([whether libtool supports -dlopen/-dlpreopen],
673 | LIBADD_DLOPEN=
674 | AC_SEARCH_LIBS([dlopen], [dl],
677 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
678 | 	  LIBADD_DLOPEN="-ldl"
680 | 	libltdl_cv_lib_dl_dlopen="yes"
681 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
685 |     ]], [[dlopen(0, 0);]])],
688 | 	    libltdl_cv_func_dlopen="yes"
689 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
690 | 	[AC_CHECK_LIB([svld], [dlopen],
693 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
694 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
695 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
698 |   LIBS="$LIBS $LIBADD_DLOPEN"
702 | AC_SUBST([LIBADD_DLOPEN])
708 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
712 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
722 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
725 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
729 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
736 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
752 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
814 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
815 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
820 |           LIBS="$LIBS $LIBADD_DLOPEN"
821 | 	  _LT_TRY_DLOPEN_SELF(
{% endraw %}

```
### Modules/_ctypes/libffi/m4/libtool.m4

```

{% raw %}
1794 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1797 | m4_defun([_LT_TRY_DLOPEN_SELF],
1855 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1888 | ])# _LT_TRY_DLOPEN_SELF
1891 | # LT_SYS_DLOPEN_SELF
1893 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1895 | if test yes != "$enable_dlopen"; then
1896 |   enable_dlopen=unknown
1897 |   enable_dlopen_self=unknown
1898 |   enable_dlopen_self_static=unknown
1900 |   lt_cv_dlopen=no
1901 |   lt_cv_dlopen_libs=
1905 |     lt_cv_dlopen=load_add_on
1906 |     lt_cv_dlopen_libs=
1907 |     lt_cv_dlopen_self=yes
1911 |     lt_cv_dlopen=LoadLibrary
1912 |     lt_cv_dlopen_libs=
1916 |     lt_cv_dlopen=dlopen
1917 |     lt_cv_dlopen_libs=
1922 |     AC_CHECK_LIB([dl], [dlopen],
1923 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1924 |     lt_cv_dlopen=dyld
1925 |     lt_cv_dlopen_libs=
1926 |     lt_cv_dlopen_self=yes
1933 |     lt_cv_dlopen=dlopen
1934 |     lt_cv_dlopen_libs=
1935 |     lt_cv_dlopen_self=no
1940 | 	  [lt_cv_dlopen=shl_load],
1942 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1943 | 	[AC_CHECK_FUNC([dlopen],
1944 | 	      [lt_cv_dlopen=dlopen],
1945 | 	  [AC_CHECK_LIB([dl], [dlopen],
1946 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1947 | 	    [AC_CHECK_LIB([svld], [dlopen],
1948 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1950 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1959 |   if test no = "$lt_cv_dlopen"; then
1960 |     enable_dlopen=no
1962 |     enable_dlopen=yes
1965 |   case $lt_cv_dlopen in
1966 |   dlopen)
1974 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1976 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1977 | 	  lt_cv_dlopen_self, [dnl
1978 | 	  _LT_TRY_DLOPEN_SELF(
1979 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1980 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1983 |     if test yes = "$lt_cv_dlopen_self"; then
1985 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1986 | 	  lt_cv_dlopen_self_static, [dnl
1987 | 	  _LT_TRY_DLOPEN_SELF(
1988 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1989 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1999 |   case $lt_cv_dlopen_self in
2000 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2001 |   *) enable_dlopen_self=unknown ;;
2004 |   case $lt_cv_dlopen_self_static in
2005 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2006 |   *) enable_dlopen_self_static=unknown ;;
2009 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2010 | 	 [Whether dlopen is supported])
2011 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2012 | 	 [Whether dlopen of programs is supported])
2013 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2014 | 	 [Whether dlopen of statically linked programs is supported])
2015 | ])# LT_SYS_DLOPEN_SELF
2018 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2020 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5785 |     [Compiler flag to allow reflexive dlopens])
5898 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### Modules/_ctypes/libffi/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the 'dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```