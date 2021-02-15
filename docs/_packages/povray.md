---
name: "povray"
layout: package
next_package: gtkorvo-cercs-env
previous_package: glfw
languages: ['bash']
---
## 3.7.0.8
11 / 11556 files match

 - [libraries/jpeg/ltmain.sh](#librariesjpegltmainsh)
 - [libraries/jpeg/aclocal.m4](#librariesjpegaclocalm4)
 - [libraries/openexr/ltmain.sh](#librariesopenexrltmainsh)
 - [libraries/openexr/aclocal.m4](#librariesopenexraclocalm4)
 - [libraries/tiff/aclocal.m4](#librariestiffaclocalm4)
 - [libraries/tiff/config/ltmain.sh](#librariestiffconfigltmainsh)
 - [libraries/tiff/m4/libtool.m4](#librariestiffm4libtoolm4)
 - [libraries/tiff/m4/ltoptions.m4](#librariestiffm4ltoptionsm4)
 - [libraries/ilmbase/ltmain.sh](#librariesilmbaseltmainsh)
 - [libraries/ilmbase/aclocal.m4](#librariesilmbaseaclocalm4)
 - [libraries/ilmbase/CMakeLists.txt](#librariesilmbasecmakeliststxt)

### libraries/jpeg/ltmain.sh

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
### libraries/jpeg/aclocal.m4

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
5672 |     [Compiler flag to allow reflexive dlopens])
5781 |   LT_SYS_DLOPEN_SELF
8053 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8085 | # dlopen
8087 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8090 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8091 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8094 | put the `dlopen' option into LT_INIT's first parameter.])
8098 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8559 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### libraries/openexr/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1505 |   -dlopen FILE      add the directory containing FILE to the library path
1507 | This mode sets the library path environment variable according to \`-dlopen'
1560 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1569 |   -module           build a library that can dlopened
1644 |     # Handle -dlopen flags immediately.
1661 | 	# Skip this library if it cannot be dlopened.
1688 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4121 | 	    dlopen_self=$dlopen_self_static
4127 | 	    dlopen_self=$dlopen_self_static
4133 | 	    dlopen_self=$dlopen_self_static
4186 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4270 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4427 |       -dlopen)
4814 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4881 | 	  # This library was specified with -dlopen.
4996 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5007 | 	passes="conv scan dlopen dlpreopen link"
5033 | 	dlopen) libs="$dlfiles" ;;
5059 |       if test "$pass" = dlopen; then
5271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5272 | 	      # If there is no dlopen support or we're linking statically,
5302 | 	dlopen=
5332 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5372 | 	# This library was specified with -dlopen.
5373 | 	if test "$pass" = dlopen; then
5375 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5378 | 	     test "$dlopen_support" != yes ||
5380 | 	    # If there is no dlname, no dlopen support or we're linking
5389 | 	fi # $pass = dlopen
5447 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5573 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5574 | 	  dlopenmodule=""
5577 | 	      dlopenmodule="$dlpremoduletest"
5581 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5678 | 		    # if the lib is a (non-dlopened) module then we can not
5682 | 		      if test "X$dlopenmodule" != "X$lib"; then
5834 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5835 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5970 |       if test "$pass" != dlopen; then
6069 | 	func_warning "\`-dlopen' is ignored for archives"
6136 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6798 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6799 | 	    $ECHO "*** application is linked with the -dlopen flag."
6817 | 	    $ECHO "*** or is declared to -dlopen it."
7384 | 	func_warning "\`-dlopen' is ignored for objects"
7499 |         && test "$dlopen_support" = unknown \
7500 | 	&& test "$dlopen_self" = unknown \
7501 | 	&& test "$dlopen_self_static" = unknown && \
7502 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8134 | # The name that we can dlopen(3).
8163 | # Files to dlopen/dlpreopen
8164 | dlopen='$dlfiles'
{% endraw %}

```
### libraries/openexr/aclocal.m4

```

{% raw %}
1649 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1652 | m4_defun([_LT_TRY_DLOPEN_SELF],
1704 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1733 | ])# _LT_TRY_DLOPEN_SELF
1736 | # LT_SYS_DLOPEN_SELF
1738 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1740 | if test "x$enable_dlopen" != xyes; then
1741 |   enable_dlopen=unknown
1742 |   enable_dlopen_self=unknown
1743 |   enable_dlopen_self_static=unknown
1745 |   lt_cv_dlopen=no
1746 |   lt_cv_dlopen_libs=
1750 |     lt_cv_dlopen="load_add_on"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1756 |     lt_cv_dlopen="LoadLibrary"
1757 |     lt_cv_dlopen_libs=
1761 |     lt_cv_dlopen="dlopen"
1762 |     lt_cv_dlopen_libs=
1767 |     AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1769 |     lt_cv_dlopen="dyld"
1770 |     lt_cv_dlopen_libs=
1771 |     lt_cv_dlopen_self=yes
1777 | 	  [lt_cv_dlopen="shl_load"],
1779 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1780 | 	[AC_CHECK_FUNC([dlopen],
1781 | 	      [lt_cv_dlopen="dlopen"],
1782 | 	  [AC_CHECK_LIB([dl], [dlopen],
1783 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1784 | 	    [AC_CHECK_LIB([svld], [dlopen],
1785 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1787 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1796 |   if test "x$lt_cv_dlopen" != xno; then
1797 |     enable_dlopen=yes
1799 |     enable_dlopen=no
1802 |   case $lt_cv_dlopen in
1803 |   dlopen)
1811 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1813 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1814 | 	  lt_cv_dlopen_self, [dnl
1815 | 	  _LT_TRY_DLOPEN_SELF(
1816 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1817 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1820 |     if test "x$lt_cv_dlopen_self" = xyes; then
1822 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1823 | 	  lt_cv_dlopen_self_static, [dnl
1824 | 	  _LT_TRY_DLOPEN_SELF(
1825 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1826 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1836 |   case $lt_cv_dlopen_self in
1837 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1838 |   *) enable_dlopen_self=unknown ;;
1841 |   case $lt_cv_dlopen_self_static in
1842 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1843 |   *) enable_dlopen_self_static=unknown ;;
1846 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1847 | 	 [Whether dlopen is supported])
1848 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1849 | 	 [Whether dlopen of programs is supported])
1850 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1851 | 	 [Whether dlopen of statically linked programs is supported])
1852 | ])# LT_SYS_DLOPEN_SELF
1855 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1857 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5173 |     [Compiler flag to allow reflexive dlopens])
5285 |   LT_SYS_DLOPEN_SELF
7435 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7467 | # dlopen
7469 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7472 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7473 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7476 | put the `dlopen' option into LT_INIT's first parameter.])
7480 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7926 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### libraries/tiff/aclocal.m4

```

{% raw %}
205 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
820 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
823 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
879 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
908 | ])# _LT_AC_TRY_DLOPEN_SELF
911 | # AC_LIBTOOL_DLOPEN_SELF
913 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
915 | if test "x$enable_dlopen" != xyes; then
916 |   enable_dlopen=unknown
917 |   enable_dlopen_self=unknown
918 |   enable_dlopen_self_static=unknown
920 |   lt_cv_dlopen=no
921 |   lt_cv_dlopen_libs=
925 |     lt_cv_dlopen="load_add_on"
926 |     lt_cv_dlopen_libs=
927 |     lt_cv_dlopen_self=yes
931 |     lt_cv_dlopen="LoadLibrary"
932 |     lt_cv_dlopen_libs=
936 |     lt_cv_dlopen="dlopen"
937 |     lt_cv_dlopen_libs=
942 |     AC_CHECK_LIB([dl], [dlopen],
943 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
944 |     lt_cv_dlopen="dyld"
945 |     lt_cv_dlopen_libs=
946 |     lt_cv_dlopen_self=yes
952 | 	  [lt_cv_dlopen="shl_load"],
954 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
955 | 	[AC_CHECK_FUNC([dlopen],
956 | 	      [lt_cv_dlopen="dlopen"],
957 | 	  [AC_CHECK_LIB([dl], [dlopen],
958 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
959 | 	    [AC_CHECK_LIB([svld], [dlopen],
960 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
962 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
971 |   if test "x$lt_cv_dlopen" != xno; then
972 |     enable_dlopen=yes
974 |     enable_dlopen=no
977 |   case $lt_cv_dlopen in
978 |   dlopen)
986 |     LIBS="$lt_cv_dlopen_libs $LIBS"
988 |     AC_CACHE_CHECK([whether a program can dlopen itself],
989 | 	  lt_cv_dlopen_self, [dnl
990 | 	  _LT_AC_TRY_DLOPEN_SELF(
991 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
992 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
995 |     if test "x$lt_cv_dlopen_self" = xyes; then
997 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
998 |     	  lt_cv_dlopen_self_static, [dnl
999 | 	  _LT_AC_TRY_DLOPEN_SELF(
1000 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1001 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1011 |   case $lt_cv_dlopen_self in
1012 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1013 |   *) enable_dlopen_self=unknown ;;
1016 |   case $lt_cv_dlopen_self_static in
1017 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1018 |   *) enable_dlopen_self_static=unknown ;;
1021 | ])# AC_LIBTOOL_DLOPEN_SELF
1882 | # AC_LIBTOOL_DLOPEN
1884 | # enable checks for dlopen support
1885 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1887 | ])# AC_LIBTOOL_DLOPEN
2675 | AC_LIBTOOL_DLOPEN_SELF
4346 | # Whether dlopen is supported.
4347 | dlopen_support=$enable_dlopen
4349 | # Whether dlopen of programs is supported.
4350 | dlopen_self=$enable_dlopen_self
4352 | # Whether dlopen of statically linked programs is supported.
4353 | dlopen_self_static=$enable_dlopen_self_static
4361 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### libraries/tiff/config/ltmain.sh

```bash

{% raw %}
723 |   -dlopen FILE      add the directory containing FILE to the library path
725 | This mode sets the library path environment variable according to \`-dlopen'
778 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
787 |   -module           build a library that can dlopened
896 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
946 |       -dlopen=*|--mode=*|--tag=*)
1976 |     # Handle -dlopen flags immediately.
1993 | 	# Skip this library if it cannot be dlopened.
2018 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
2687 | 	    dlopen_self=$dlopen_self_static
2695 | 	    dlopen_self=$dlopen_self_static
2747 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
2831 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
2983 |       -dlopen)
3353 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3419 | 	  # This library was specified with -dlopen.
3534 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
3545 | 	passes="conv scan dlopen dlpreopen link"
3571 | 	dlopen) libs="$dlfiles" ;;
3597 |       if test "$pass" = dlopen; then
3804 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
3805 | 	      # If there is no dlopen support or we're linking statically,
3835 | 	dlopen=
3871 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
3911 | 	# This library was specified with -dlopen.
3912 | 	if test "$pass" = dlopen; then
3914 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
3917 | 	     test "$dlopen_support" != yes ||
3919 | 	    # If there is no dlname, no dlopen support or we're linking
3928 | 	fi # $pass = dlopen
3986 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
4110 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
4111 | 	  dlopenmodule=""
4114 | 	      dlopenmodule="$dlpremoduletest"
4118 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
4214 | 		    # if the lib is a (non-dlopened) module then we can not
4218 | 		      if test "X$dlopenmodule" != "X$lib"; then
4368 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
4369 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
4494 |       if test "$pass" != dlopen; then
4593 | 	func_warning "\`-dlopen' is ignored for archives"
4659 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
5293 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
5294 | 	    $ECHO "*** application is linked with the -dlopen flag."
5312 | 	    $ECHO "*** or is declared to -dlopen it."
5817 | 	func_warning "\`-dlopen' is ignored for objects"
5927 |         && test "$dlopen_support" = unknown \
5928 | 	&& test "$dlopen_self" = unknown \
5929 | 	&& test "$dlopen_self_static" = unknown && \
5930 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
7041 | # The name that we can dlopen(3).
7070 | # Files to dlopen/dlpreopen
7071 | dlopen='$dlfiles'
7279 |   # Only execute mode is allowed to have -dlopen flags.
7281 |     func_error "unrecognized option \`-dlopen'"
{% endraw %}

```
### libraries/tiff/m4/libtool.m4

```

{% raw %}
1483 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1486 | m4_defun([_LT_TRY_DLOPEN_SELF],
1542 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1571 | ])# _LT_TRY_DLOPEN_SELF
1574 | # LT_SYS_DLOPEN_SELF
1576 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1578 | if test "x$enable_dlopen" != xyes; then
1579 |   enable_dlopen=unknown
1580 |   enable_dlopen_self=unknown
1581 |   enable_dlopen_self_static=unknown
1583 |   lt_cv_dlopen=no
1584 |   lt_cv_dlopen_libs=
1588 |     lt_cv_dlopen="load_add_on"
1589 |     lt_cv_dlopen_libs=
1590 |     lt_cv_dlopen_self=yes
1594 |     lt_cv_dlopen="LoadLibrary"
1595 |     lt_cv_dlopen_libs=
1599 |     lt_cv_dlopen="dlopen"
1600 |     lt_cv_dlopen_libs=
1605 |     AC_CHECK_LIB([dl], [dlopen],
1606 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1607 |     lt_cv_dlopen="dyld"
1608 |     lt_cv_dlopen_libs=
1609 |     lt_cv_dlopen_self=yes
1615 | 	  [lt_cv_dlopen="shl_load"],
1617 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
1618 | 	[AC_CHECK_FUNC([dlopen],
1619 | 	      [lt_cv_dlopen="dlopen"],
1620 | 	  [AC_CHECK_LIB([dl], [dlopen],
1621 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1622 | 	    [AC_CHECK_LIB([svld], [dlopen],
1623 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1625 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
1634 |   if test "x$lt_cv_dlopen" != xno; then
1635 |     enable_dlopen=yes
1637 |     enable_dlopen=no
1640 |   case $lt_cv_dlopen in
1641 |   dlopen)
1649 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1651 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1652 | 	  lt_cv_dlopen_self, [dnl
1653 | 	  _LT_TRY_DLOPEN_SELF(
1654 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1655 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1658 |     if test "x$lt_cv_dlopen_self" = xyes; then
1660 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1661 |     	  lt_cv_dlopen_self_static, [dnl
1662 | 	  _LT_TRY_DLOPEN_SELF(
1663 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1664 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1674 |   case $lt_cv_dlopen_self in
1675 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1676 |   *) enable_dlopen_self=unknown ;;
1679 |   case $lt_cv_dlopen_self_static in
1680 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1681 |   *) enable_dlopen_self_static=unknown ;;
1684 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1685 | 	 [Whether dlopen is supported])
1686 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1687 | 	 [Whether dlopen of programs is supported])
1688 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1689 | 	 [Whether dlopen of statically linked programs is supported])
1690 | ])# LT_SYS_DLOPEN_SELF
1693 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1695 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
4913 |     [Compiler flag to allow reflexive dlopens])
5022 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### libraries/tiff/m4/ltoptions.m4

```

{% raw %}
65 | _LT_UNLESS_OPTIONS([dlopen], [enable_dlopen=no
97 | # dlopen
99 | LT_OPTION_DEFINE([dlopen], [enable_dlopen=yes
102 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
103 | [_LT_SET_OPTION([dlopen])
106 | put the `dlopen' option into LT_INIT's first parameter.])
110 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### libraries/ilmbase/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1505 |   -dlopen FILE      add the directory containing FILE to the library path
1507 | This mode sets the library path environment variable according to \`-dlopen'
1560 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1569 |   -module           build a library that can dlopened
1644 |     # Handle -dlopen flags immediately.
1661 | 	# Skip this library if it cannot be dlopened.
1688 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4121 | 	    dlopen_self=$dlopen_self_static
4127 | 	    dlopen_self=$dlopen_self_static
4133 | 	    dlopen_self=$dlopen_self_static
4186 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4270 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4427 |       -dlopen)
4814 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4881 | 	  # This library was specified with -dlopen.
4996 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5007 | 	passes="conv scan dlopen dlpreopen link"
5033 | 	dlopen) libs="$dlfiles" ;;
5059 |       if test "$pass" = dlopen; then
5271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5272 | 	      # If there is no dlopen support or we're linking statically,
5302 | 	dlopen=
5332 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5372 | 	# This library was specified with -dlopen.
5373 | 	if test "$pass" = dlopen; then
5375 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5378 | 	     test "$dlopen_support" != yes ||
5380 | 	    # If there is no dlname, no dlopen support or we're linking
5389 | 	fi # $pass = dlopen
5447 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5573 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5574 | 	  dlopenmodule=""
5577 | 	      dlopenmodule="$dlpremoduletest"
5581 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5678 | 		    # if the lib is a (non-dlopened) module then we can not
5682 | 		      if test "X$dlopenmodule" != "X$lib"; then
5834 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5835 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5970 |       if test "$pass" != dlopen; then
6069 | 	func_warning "\`-dlopen' is ignored for archives"
6136 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6798 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6799 | 	    $ECHO "*** application is linked with the -dlopen flag."
6817 | 	    $ECHO "*** or is declared to -dlopen it."
7384 | 	func_warning "\`-dlopen' is ignored for objects"
7499 |         && test "$dlopen_support" = unknown \
7500 | 	&& test "$dlopen_self" = unknown \
7501 | 	&& test "$dlopen_self_static" = unknown && \
7502 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8134 | # The name that we can dlopen(3).
8163 | # Files to dlopen/dlpreopen
8164 | dlopen='$dlfiles'
{% endraw %}

```
### libraries/ilmbase/aclocal.m4

```

{% raw %}
1649 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1652 | m4_defun([_LT_TRY_DLOPEN_SELF],
1704 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1733 | ])# _LT_TRY_DLOPEN_SELF
1736 | # LT_SYS_DLOPEN_SELF
1738 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1740 | if test "x$enable_dlopen" != xyes; then
1741 |   enable_dlopen=unknown
1742 |   enable_dlopen_self=unknown
1743 |   enable_dlopen_self_static=unknown
1745 |   lt_cv_dlopen=no
1746 |   lt_cv_dlopen_libs=
1750 |     lt_cv_dlopen="load_add_on"
1751 |     lt_cv_dlopen_libs=
1752 |     lt_cv_dlopen_self=yes
1756 |     lt_cv_dlopen="LoadLibrary"
1757 |     lt_cv_dlopen_libs=
1761 |     lt_cv_dlopen="dlopen"
1762 |     lt_cv_dlopen_libs=
1767 |     AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1769 |     lt_cv_dlopen="dyld"
1770 |     lt_cv_dlopen_libs=
1771 |     lt_cv_dlopen_self=yes
1777 | 	  [lt_cv_dlopen="shl_load"],
1779 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1780 | 	[AC_CHECK_FUNC([dlopen],
1781 | 	      [lt_cv_dlopen="dlopen"],
1782 | 	  [AC_CHECK_LIB([dl], [dlopen],
1783 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1784 | 	    [AC_CHECK_LIB([svld], [dlopen],
1785 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1787 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1796 |   if test "x$lt_cv_dlopen" != xno; then
1797 |     enable_dlopen=yes
1799 |     enable_dlopen=no
1802 |   case $lt_cv_dlopen in
1803 |   dlopen)
1811 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1813 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1814 | 	  lt_cv_dlopen_self, [dnl
1815 | 	  _LT_TRY_DLOPEN_SELF(
1816 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1817 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1820 |     if test "x$lt_cv_dlopen_self" = xyes; then
1822 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1823 | 	  lt_cv_dlopen_self_static, [dnl
1824 | 	  _LT_TRY_DLOPEN_SELF(
1825 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1826 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1836 |   case $lt_cv_dlopen_self in
1837 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1838 |   *) enable_dlopen_self=unknown ;;
1841 |   case $lt_cv_dlopen_self_static in
1842 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1843 |   *) enable_dlopen_self_static=unknown ;;
1846 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1847 | 	 [Whether dlopen is supported])
1848 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1849 | 	 [Whether dlopen of programs is supported])
1850 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1851 | 	 [Whether dlopen of statically linked programs is supported])
1852 | ])# LT_SYS_DLOPEN_SELF
1855 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1857 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5173 |     [Compiler flag to allow reflexive dlopens])
5285 |   LT_SYS_DLOPEN_SELF
7435 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7467 | # dlopen
7469 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7472 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7473 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7476 | put the `dlopen' option into LT_INIT's first parameter.])
7480 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7926 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### libraries/ilmbase/CMakeLists.txt

```

{% raw %}
62 |    GET_TARGET_PROPERTY_WITH_DEFAULT(_target_dlopen ${_target} LT_DLOPEN "")
70 |    FILE(APPEND ${_laname} "# The name that we can dlopen(3).\n")
88 |    FILE(APPEND ${_laname} "# Files to dlopen/dlpreopen\n")
89 |    FILE(APPEND ${_laname} "dlopen='${_target_dlopen}'\n")
{% endraw %}

```