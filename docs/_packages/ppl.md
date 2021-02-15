---
name: "ppl"
layout: package
next_package: py-espresso
previous_package: tulip
languages: ['bash']
---
## 1.2
20 / 1541 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [interfaces/OCaml/tests/Makefile.am](#interfacesocamltestsmakefileam)
 - [interfaces/OCaml/tests/Makefile.in](#interfacesocamltestsmakefilein)
 - [interfaces/Prolog/Ciao/Makefile.am](#interfacesprologciaomakefileam)
 - [interfaces/Prolog/Ciao/Makefile.in](#interfacesprologciaomakefilein)
 - [interfaces/Prolog/SWI/Makefile.am](#interfacesprologswimakefileam)
 - [interfaces/Prolog/SWI/Makefile.in](#interfacesprologswimakefilein)
 - [interfaces/Prolog/GNU/Makefile.am](#interfacesprologgnumakefileam)
 - [interfaces/Prolog/GNU/Makefile.in](#interfacesprologgnumakefilein)
 - [interfaces/Prolog/SICStus/Makefile.am](#interfacesprologsicstusmakefileam)
 - [interfaces/Prolog/SICStus/Makefile.in](#interfacesprologsicstusmakefilein)
 - [interfaces/Prolog/YAP/Makefile.am](#interfacesprologyapmakefileam)
 - [interfaces/Prolog/YAP/Makefile.in](#interfacesprologyapmakefilein)
 - [interfaces/Prolog/XSB/Makefile.am](#interfacesprologxsbmakefileam)
 - [interfaces/Prolog/XSB/Makefile.in](#interfacesprologxsbmakefilein)
 - [interfaces/Java/tests/Makefile.am](#interfacesjavatestsmakefileam)
 - [interfaces/Java/tests/Makefile.in](#interfacesjavatestsmakefilein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)

### configure.ac

```

{% raw %}
855 | LT_INIT([dlopen,win32-dll])
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
### interfaces/OCaml/tests/Makefile.am

```

{% raw %}
37 | 	$(LIBTOOL) --mode=execute $(PPL_DLOPEN) $(CHECKER)
82 | PPL_DLOPEN = -dlopen ../../../src/libppl.la
{% endraw %}

```
### interfaces/OCaml/tests/Makefile.in

```

{% raw %}
627 | 	$(LIBTOOL) --mode=execute $(PPL_DLOPEN) $(CHECKER)
663 | PPL_DLOPEN = -dlopen ../../../src/libppl.la
{% endraw %}

```
### interfaces/Prolog/Ciao/Makefile.am

```

{% raw %}
258 | 		-dlopen ../../../src/libppl.la \
259 | 		-dlopen libppl_ciao.la \
270 | 		-dlopen ../../../src/libppl.la \
271 | 		-dlopen libppl_ciao.la \
279 | 		-dlopen ../../../src/libppl.la \
280 | 		-dlopen libppl_ciao.la \
287 | 		-dlopen ../../../src/libppl.la \
288 | 		-dlopen libppl_ciao.la \
{% endraw %}

```
### interfaces/Prolog/Ciao/Makefile.in

```

{% raw %}
1632 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1633 | @ENABLE_SHARED_TRUE@		-dlopen libppl_ciao.la \
1644 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1645 | @ENABLE_SHARED_TRUE@		-dlopen libppl_ciao.la \
1653 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1654 | @ENABLE_SHARED_TRUE@		-dlopen libppl_ciao.la \
1661 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1662 | @ENABLE_SHARED_TRUE@		-dlopen libppl_ciao.la \
{% endraw %}

```
### interfaces/Prolog/SWI/Makefile.am

```

{% raw %}
280 | 		-dlopen ../../../src/libppl.la \
281 | 		-dlopen libppl_swiprolog.la \
291 | 		-dlopen ../../../src/libppl.la \
292 | 		-dlopen libppl_swiprolog.la \
298 | 		-dlopen ../../../src/libppl.la \
299 | 		-dlopen libppl_swiprolog.la \
308 | 		-dlopen ../../../src/libppl.la \
309 | 		-dlopen libppl_swiprolog.la \
{% endraw %}

```
### interfaces/Prolog/SWI/Makefile.in

```

{% raw %}
1706 | 		-dlopen ../../../src/libppl.la \
1707 | 		-dlopen libppl_swiprolog.la \
1717 | 		-dlopen ../../../src/libppl.la \
1718 | 		-dlopen libppl_swiprolog.la \
1724 | 		-dlopen ../../../src/libppl.la \
1725 | 		-dlopen libppl_swiprolog.la \
1734 | 		-dlopen ../../../src/libppl.la \
1735 | 		-dlopen libppl_swiprolog.la \
{% endraw %}

```
### interfaces/Prolog/GNU/Makefile.am

```

{% raw %}
249 | 		-dlopen ../../../src/libppl.la \
250 | 		-dlopen libppl_gprolog.la \
259 | 		-dlopen ../../../src/libppl.la \
260 | 		-dlopen libppl_gprolog.la \
266 | 		-dlopen ../../../src/libppl.la \
267 | 		-dlopen libppl_gprolog.la \
281 | 		-dlopen ../../../src/libppl.la \
282 | 		-dlopen libppl_gprolog.la \
{% endraw %}

```
### interfaces/Prolog/GNU/Makefile.in

```

{% raw %}
1661 | 		-dlopen ../../../src/libppl.la \
1662 | 		-dlopen libppl_gprolog.la \
1671 | 		-dlopen ../../../src/libppl.la \
1672 | 		-dlopen libppl_gprolog.la \
1678 | 		-dlopen ../../../src/libppl.la \
1679 | 		-dlopen libppl_gprolog.la \
1693 | 		-dlopen ../../../src/libppl.la \
1694 | 		-dlopen libppl_gprolog.la \
{% endraw %}

```
### interfaces/Prolog/SICStus/Makefile.am

```

{% raw %}
256 | 		-dlopen ../../../src/libppl.la \
270 | 	  -dlopen ../../../src/libppl.la \
280 |           -dlopen ../../../src/libppl.la \
290 | 		-dlopen ../../../src/libppl.la \
{% endraw %}

```
### interfaces/Prolog/SICStus/Makefile.in

```

{% raw %}
1647 | 		-dlopen ../../../src/libppl.la \
1661 | 	  -dlopen ../../../src/libppl.la \
1671 |           -dlopen ../../../src/libppl.la \
1681 | 		-dlopen ../../../src/libppl.la \
{% endraw %}

```
### interfaces/Prolog/YAP/Makefile.am

```

{% raw %}
209 | 		-dlopen ../../../src/libppl.la \
210 | 		-dlopen ppl_yap.la \
222 | 		-dlopen ../../../src/libppl.la \
223 | 		-dlopen ppl_yap.la \
232 | 		-dlopen ../../../src/libppl.la \
233 | 		-dlopen ppl_yap.la \
247 | 		-dlopen ../../../src/libppl.la \
248 | 		-dlopen ppl_yap.la \
{% endraw %}

```
### interfaces/Prolog/YAP/Makefile.in

```

{% raw %}
1584 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1585 | @ENABLE_SHARED_TRUE@		-dlopen ppl_yap.la \
1597 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1598 | @ENABLE_SHARED_TRUE@		-dlopen ppl_yap.la \
1607 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1608 | @ENABLE_SHARED_TRUE@		-dlopen ppl_yap.la \
1622 | @ENABLE_SHARED_TRUE@		-dlopen ../../../src/libppl.la \
1623 | @ENABLE_SHARED_TRUE@		-dlopen ppl_yap.la \
{% endraw %}

```
### interfaces/Prolog/XSB/Makefile.am

```

{% raw %}
191 | 			-dlopen ../../../src/libppl.la \
235 | 		-dlopen ../../../src/libppl.la \
249 | 		-dlopen ../../../src/libppl.la \
265 | 		-dlopen ../../../src/libppl.la \
279 | 		-dlopen ../../../src/libppl.la \
{% endraw %}

```
### interfaces/Prolog/XSB/Makefile.in

```

{% raw %}
1575 | 			-dlopen ../../../src/libppl.la \
1589 | 		-dlopen ../../../src/libppl.la \
1603 | 		-dlopen ../../../src/libppl.la \
1619 | 		-dlopen ../../../src/libppl.la \
1633 | 		-dlopen ../../../src/libppl.la \
{% endraw %}

```
### interfaces/Java/tests/Makefile.am

```

{% raw %}
73 | PPL_DLOPEN = -dlopen ../../../src/libppl.la
76 | $(LIBTOOL) --mode=execute $(PPL_DLOPEN) $(PWL_DLOPEN) \
{% endraw %}

```
### interfaces/Java/tests/Makefile.in

```

{% raw %}
401 | @ENABLE_SHARED_TRUE@PPL_DLOPEN = -dlopen ../../../src/libppl.la
403 | @ENABLE_SHARED_TRUE@$(LIBTOOL) --mode=execute $(PPL_DLOPEN) $(PWL_DLOPEN) \
{% endraw %}

```
### m4/libtool.m4

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