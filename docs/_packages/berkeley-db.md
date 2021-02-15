---
name: "berkeley-db"
layout: package
next_package: qthreads
previous_package: libssh
languages: ['html', 'cpp', 'bash']
---
## 6.1.29
25 / 9619 files match

 - [src/dbinc/mutex_int.h](#srcdbincmutex_inth)
 - [dist/ltmain.sh](#distltmainsh)
 - [dist/aclocal/libtool.m4](#distaclocallibtoolm4)
 - [dist/aclocal/ltoptions.m4](#distaclocalltoptionsm4)
 - [dist/aclocal/sosuffix.m4](#distaclocalsosuffixm4)
 - [dist/validate/s_chk_spell.dict](#distvalidates_chk_spelldict)
 - [lang/sql/jdbc/ltmain.sh](#langsqljdbcltmainsh)
 - [lang/sql/jdbc/aclocal.m4](#langsqljdbcaclocalm4)
 - [lang/sql/sqlite/configure.ac](#langsqlsqliteconfigureac)
 - [lang/sql/sqlite/ltmain.sh](#langsqlsqliteltmainsh)
 - [lang/sql/sqlite/aclocal.m4](#langsqlsqliteaclocalm4)
 - [lang/sql/sqlite/src/os_unix.c](#langsqlsqlitesrcos_unixc)
 - [lang/sql/sqlite/test/loadext.test](#langsqlsqlitetestloadexttest)
 - [lang/sql/sqlite/autoconf/configure.ac](#langsqlsqliteautoconfconfigureac)
 - [lang/sql/sqlite/autoconf/ltmain.sh](#langsqlsqliteautoconfltmainsh)
 - [lang/sql/odbc/sqlite4odbc.c](#langsqlodbcsqlite4odbcc)
 - [lang/sql/odbc/sqlite3odbc.c](#langsqlodbcsqlite3odbcc)
 - [lang/sql/odbc/zipfile.c](#langsqlodbczipfilec)
 - [lang/sql/odbc/sqliteodbc.c](#langsqlodbcsqliteodbcc)
 - [lang/sql/odbc/ltmain.sh](#langsqlodbcltmainsh)
 - [lang/sql/odbc/configure.in](#langsqlodbcconfigurein)
 - [lang/sql/odbc/aclocal.m4](#langsqlodbcaclocalm4)
 - [lang/sql/generated/sqlite3.c](#langsqlgeneratedsqlite3c)
 - [docs/installation/build_unix_notes.html](#docsinstallationbuild_unix_noteshtml)
 - [docs/programmer_reference/solaris.txt](#docsprogrammer_referencesolaristxt)

### src/dbinc/mutex_int.h

```cpp

{% raw %}
120 |  * dlopen to load the DB library), the pwrite64 interface would be translated
{% endraw %}

```
### dist/ltmain.sh

```bash

{% raw %}
1078 |       --dlopen|-dlopen)
1080 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1201 |     # Only execute mode is allowed to have -dlopen flags.
1202 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1203 |       func_error "unrecognized option \`-dlopen'"
2351 |   -dlopen FILE      add the directory containing FILE to the library path
2353 | This mode sets the library path environment variable according to \`-dlopen'
2408 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2417 |   -module           build a library that can dlopened
2523 |     # Handle -dlopen flags immediately.
2524 |     for file in $opt_dlopen; do
2543 | 	# Skip this library if it cannot be dlopened.
2570 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5171 | 	    dlopen_self=$dlopen_self_static
5177 | 	    dlopen_self=$dlopen_self_static
5183 | 	    dlopen_self=$dlopen_self_static
5241 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5325 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5487 |       -dlopen)
5889 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5957 | 	  # This library was specified with -dlopen.
6074 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6085 | 	passes="conv scan dlopen dlpreopen link"
6111 | 	dlopen) libs="$dlfiles" ;;
6139 |       if test "$pass" = dlopen; then
6357 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6358 | 	      # If there is no dlopen support or we're linking statically,
6388 | 	dlopen=
6418 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6464 | 	# This library was specified with -dlopen.
6465 | 	if test "$pass" = dlopen; then
6467 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6470 | 	     test "$dlopen_support" != yes ||
6472 | 	    # If there is no dlname, no dlopen support or we're linking
6481 | 	fi # $pass = dlopen
6537 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6539 | 	      # We recover the dlopen module name by 'saving' the la file
6563 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6692 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6693 | 	  dlopenmodule=""
6696 | 	      dlopenmodule="$dlpremoduletest"
6700 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6797 | 		    # if the lib is a (non-dlopened) module then we can not
6801 | 		      if test "X$dlopenmodule" != "X$lib"; then
6953 | 	      echo "*** a static module, that should work as long as the dlopening application"
6954 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7098 |       if test "$pass" != dlopen; then
7197 | 	func_warning "\`-dlopen' is ignored for archives"
7264 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7939 | 	    echo "*** a static module, that should work as long as the dlopening"
7940 | 	    echo "*** application is linked with the -dlopen flag."
7958 | 	    echo "*** or is declared to -dlopen it."
8568 | 	func_warning "\`-dlopen' is ignored for objects"
8686 |         && test "$dlopen_support" = unknown \
8687 | 	&& test "$dlopen_self" = unknown \
8688 | 	&& test "$dlopen_self_static" = unknown && \
8689 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9367 | # The name that we can dlopen(3).
9396 | # Files to dlopen/dlpreopen
9397 | dlopen='$dlfiles'
{% endraw %}

```
### dist/aclocal/libtool.m4

```

{% raw %}
1682 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1685 | m4_defun([_LT_TRY_DLOPEN_SELF],
1743 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1776 | ])# _LT_TRY_DLOPEN_SELF
1779 | # LT_SYS_DLOPEN_SELF
1781 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1783 | if test "x$enable_dlopen" != xyes; then
1784 |   enable_dlopen=unknown
1785 |   enable_dlopen_self=unknown
1786 |   enable_dlopen_self_static=unknown
1788 |   lt_cv_dlopen=no
1789 |   lt_cv_dlopen_libs=
1793 |     lt_cv_dlopen="load_add_on"
1794 |     lt_cv_dlopen_libs=
1795 |     lt_cv_dlopen_self=yes
1799 |     lt_cv_dlopen="LoadLibrary"
1800 |     lt_cv_dlopen_libs=
1804 |     lt_cv_dlopen="dlopen"
1805 |     lt_cv_dlopen_libs=
1810 |     AC_CHECK_LIB([dl], [dlopen],
1811 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1812 |     lt_cv_dlopen="dyld"
1813 |     lt_cv_dlopen_libs=
1814 |     lt_cv_dlopen_self=yes
1820 | 	  [lt_cv_dlopen="shl_load"],
1822 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1823 | 	[AC_CHECK_FUNC([dlopen],
1824 | 	      [lt_cv_dlopen="dlopen"],
1825 | 	  [AC_CHECK_LIB([dl], [dlopen],
1826 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1827 | 	    [AC_CHECK_LIB([svld], [dlopen],
1828 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1830 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1839 |   if test "x$lt_cv_dlopen" != xno; then
1840 |     enable_dlopen=yes
1842 |     enable_dlopen=no
1845 |   case $lt_cv_dlopen in
1846 |   dlopen)
1854 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1856 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1857 | 	  lt_cv_dlopen_self, [dnl
1858 | 	  _LT_TRY_DLOPEN_SELF(
1859 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1860 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1863 |     if test "x$lt_cv_dlopen_self" = xyes; then
1865 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1866 | 	  lt_cv_dlopen_self_static, [dnl
1867 | 	  _LT_TRY_DLOPEN_SELF(
1868 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1869 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1879 |   case $lt_cv_dlopen_self in
1880 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1881 |   *) enable_dlopen_self=unknown ;;
1884 |   case $lt_cv_dlopen_self_static in
1885 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1886 |   *) enable_dlopen_self_static=unknown ;;
1889 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1890 | 	 [Whether dlopen is supported])
1891 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1892 | 	 [Whether dlopen of programs is supported])
1893 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1894 | 	 [Whether dlopen of statically linked programs is supported])
1895 | ])# LT_SYS_DLOPEN_SELF
1898 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1900 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5585 |     [Compiler flag to allow reflexive dlopens])
5701 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### dist/aclocal/ltoptions.m4

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
### dist/aclocal/sosuffix.m4

```

{% raw %}
33 | # shared library extension used for general linking, not dlopen.
44 | # shared library extension used for dlopen'ed modules.
{% endraw %}

```
### dist/validate/s_chk_spell.dict

```

{% raw %}
1374 | dlopen
6384 | xDlOpen
{% endraw %}

```
### lang/sql/jdbc/ltmain.sh

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
### lang/sql/jdbc/aclocal.m4

```

{% raw %}
1641 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1644 | m4_defun([_LT_TRY_DLOPEN_SELF],
1696 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1725 | ])# _LT_TRY_DLOPEN_SELF
1728 | # LT_SYS_DLOPEN_SELF
1730 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1732 | if test "x$enable_dlopen" != xyes; then
1733 |   enable_dlopen=unknown
1734 |   enable_dlopen_self=unknown
1735 |   enable_dlopen_self_static=unknown
1737 |   lt_cv_dlopen=no
1738 |   lt_cv_dlopen_libs=
1742 |     lt_cv_dlopen="load_add_on"
1743 |     lt_cv_dlopen_libs=
1744 |     lt_cv_dlopen_self=yes
1748 |     lt_cv_dlopen="LoadLibrary"
1749 |     lt_cv_dlopen_libs=
1753 |     lt_cv_dlopen="dlopen"
1754 |     lt_cv_dlopen_libs=
1759 |     AC_CHECK_LIB([dl], [dlopen],
1760 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1761 |     lt_cv_dlopen="dyld"
1762 |     lt_cv_dlopen_libs=
1763 |     lt_cv_dlopen_self=yes
1769 | 	  [lt_cv_dlopen="shl_load"],
1771 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1772 | 	[AC_CHECK_FUNC([dlopen],
1773 | 	      [lt_cv_dlopen="dlopen"],
1774 | 	  [AC_CHECK_LIB([dl], [dlopen],
1775 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1776 | 	    [AC_CHECK_LIB([svld], [dlopen],
1777 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1779 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1788 |   if test "x$lt_cv_dlopen" != xno; then
1789 |     enable_dlopen=yes
1791 |     enable_dlopen=no
1794 |   case $lt_cv_dlopen in
1795 |   dlopen)
1803 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1805 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1806 | 	  lt_cv_dlopen_self, [dnl
1807 | 	  _LT_TRY_DLOPEN_SELF(
1808 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1809 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1812 |     if test "x$lt_cv_dlopen_self" = xyes; then
1814 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1815 | 	  lt_cv_dlopen_self_static, [dnl
1816 | 	  _LT_TRY_DLOPEN_SELF(
1817 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1818 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1828 |   case $lt_cv_dlopen_self in
1829 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1830 |   *) enable_dlopen_self=unknown ;;
1833 |   case $lt_cv_dlopen_self_static in
1834 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1835 |   *) enable_dlopen_self_static=unknown ;;
1838 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1839 | 	 [Whether dlopen is supported])
1840 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1841 | 	 [Whether dlopen of programs is supported])
1842 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1843 | 	 [Whether dlopen of statically linked programs is supported])
1844 | ])# LT_SYS_DLOPEN_SELF
1847 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1849 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5165 |     [Compiler flag to allow reflexive dlopens])
5277 |   LT_SYS_DLOPEN_SELF
7427 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7459 | # dlopen
7461 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7464 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7465 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7468 | put the `dlopen' option into LT_INIT's first parameter.])
7472 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7918 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### lang/sql/sqlite/configure.ac

```

{% raw %}
628 |   AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### lang/sql/sqlite/ltmain.sh

```bash

{% raw %}
744 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
794 |       -dlopen=*|--mode=*|--tag=*)
883 |   # Only execute mode is allowed to have -dlopen flags.
885 |     func_error "unrecognized option \`-dlopen'"
1512 |   -dlopen FILE      add the directory containing FILE to the library path
1514 | This mode sets the library path environment variable according to \`-dlopen'
1567 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1576 |   -module           build a library that can dlopened
1651 |     # Handle -dlopen flags immediately.
1668 | 	# Skip this library if it cannot be dlopened.
1695 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4128 | 	    dlopen_self=$dlopen_self_static
4134 | 	    dlopen_self=$dlopen_self_static
4140 | 	    dlopen_self=$dlopen_self_static
4193 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4277 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4434 |       -dlopen)
4821 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4888 | 	  # This library was specified with -dlopen.
5003 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5014 | 	passes="conv scan dlopen dlpreopen link"
5040 | 	dlopen) libs="$dlfiles" ;;
5066 |       if test "$pass" = dlopen; then
5278 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5279 | 	      # If there is no dlopen support or we're linking statically,
5309 | 	dlopen=
5339 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5379 | 	# This library was specified with -dlopen.
5380 | 	if test "$pass" = dlopen; then
5382 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5385 | 	     test "$dlopen_support" != yes ||
5387 | 	    # If there is no dlname, no dlopen support or we're linking
5396 | 	fi # $pass = dlopen
5454 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5580 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5581 | 	  dlopenmodule=""
5584 | 	      dlopenmodule="$dlpremoduletest"
5588 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5685 | 		    # if the lib is a (non-dlopened) module then we can not
5689 | 		      if test "X$dlopenmodule" != "X$lib"; then
5841 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5842 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5977 |       if test "$pass" != dlopen; then
6076 | 	func_warning "\`-dlopen' is ignored for archives"
6143 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6805 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6806 | 	    $ECHO "*** application is linked with the -dlopen flag."
6824 | 	    $ECHO "*** or is declared to -dlopen it."
7391 | 	func_warning "\`-dlopen' is ignored for objects"
7506 |         && test "$dlopen_support" = unknown \
7507 | 	&& test "$dlopen_self" = unknown \
7508 | 	&& test "$dlopen_self_static" = unknown && \
7509 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8189 | # The name that we can dlopen(3).
8218 | # Files to dlopen/dlpreopen
8219 | dlopen='$dlfiles'
{% endraw %}

```
### lang/sql/sqlite/aclocal.m4

```

{% raw %}
1641 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1644 | m4_defun([_LT_TRY_DLOPEN_SELF],
1696 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1725 | ])# _LT_TRY_DLOPEN_SELF
1728 | # LT_SYS_DLOPEN_SELF
1730 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1732 | if test "x$enable_dlopen" != xyes; then
1733 |   enable_dlopen=unknown
1734 |   enable_dlopen_self=unknown
1735 |   enable_dlopen_self_static=unknown
1737 |   lt_cv_dlopen=no
1738 |   lt_cv_dlopen_libs=
1742 |     lt_cv_dlopen="load_add_on"
1743 |     lt_cv_dlopen_libs=
1744 |     lt_cv_dlopen_self=yes
1748 |     lt_cv_dlopen="LoadLibrary"
1749 |     lt_cv_dlopen_libs=
1753 |     lt_cv_dlopen="dlopen"
1754 |     lt_cv_dlopen_libs=
1759 |     AC_CHECK_LIB([dl], [dlopen],
1760 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1761 |     lt_cv_dlopen="dyld"
1762 |     lt_cv_dlopen_libs=
1763 |     lt_cv_dlopen_self=yes
1769 | 	  [lt_cv_dlopen="shl_load"],
1771 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1772 | 	[AC_CHECK_FUNC([dlopen],
1773 | 	      [lt_cv_dlopen="dlopen"],
1774 | 	  [AC_CHECK_LIB([dl], [dlopen],
1775 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1776 | 	    [AC_CHECK_LIB([svld], [dlopen],
1777 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1779 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1788 |   if test "x$lt_cv_dlopen" != xno; then
1789 |     enable_dlopen=yes
1791 |     enable_dlopen=no
1794 |   case $lt_cv_dlopen in
1795 |   dlopen)
1803 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1805 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1806 | 	  lt_cv_dlopen_self, [dnl
1807 | 	  _LT_TRY_DLOPEN_SELF(
1808 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1809 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1812 |     if test "x$lt_cv_dlopen_self" = xyes; then
1814 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1815 | 	  lt_cv_dlopen_self_static, [dnl
1816 | 	  _LT_TRY_DLOPEN_SELF(
1817 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1818 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1828 |   case $lt_cv_dlopen_self in
1829 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1830 |   *) enable_dlopen_self=unknown ;;
1833 |   case $lt_cv_dlopen_self_static in
1834 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1835 |   *) enable_dlopen_self_static=unknown ;;
1838 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1839 | 	 [Whether dlopen is supported])
1840 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1841 | 	 [Whether dlopen of programs is supported])
1842 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1843 | 	 [Whether dlopen of statically linked programs is supported])
1844 | ])# LT_SYS_DLOPEN_SELF
1847 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1849 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5175 |     [Compiler flag to allow reflexive dlopens])
5287 |   LT_SYS_DLOPEN_SELF
7437 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
7469 | # dlopen
7471 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
7474 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
7475 | [_LT_SET_OPTION([LT_INIT], [dlopen])
7478 | put the `dlopen' option into LT_INIT's first parameter.])
7482 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
7928 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```
### lang/sql/sqlite/src/os_unix.c

```cpp

{% raw %}
5984 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
5986 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
5991 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
6034 |   #define unixDlOpen  0
7408 |     unixDlOpen,           /* xDlOpen */                     \
{% endraw %}

```
### lang/sql/sqlite/test/loadext.test

```

{% raw %}
63 |   set dlerror_nosuchfile {dlopen(%s, 10): image not found}
64 |   set dlerror_notadll    {dlopen(%1$s, 10): no suitable image found.*}
{% endraw %}

```
### lang/sql/sqlite/autoconf/configure.ac

```

{% raw %}
71 |   AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### lang/sql/sqlite/autoconf/ltmain.sh

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
### lang/sql/odbc/sqlite4odbc.c

```cpp

{% raw %}
1230 | #ifdef USE_DLOPEN_FOR_GPPS
1238 |  * dlopen(), in theory this makes the driver independent from the
1249 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
1251 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
1254 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
1257 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
19787 |     libsqlite4_so = dlopen("libsqlite4.so.0", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### lang/sql/odbc/sqlite3odbc.c

```cpp

{% raw %}
1247 | #ifdef USE_DLOPEN_FOR_GPPS
1255 |  * dlopen(), in theory this makes the driver independent from the
1266 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
1268 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
1271 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
1274 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
20504 |     libsqlite3_so = dlopen("libsqlite3.so.0", RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### lang/sql/odbc/zipfile.c

```cpp

{% raw %}
1921 | mem_dlopen(sqlite3_vfs *vfs, const char *name)
2028 |     mem_dlopen,		/* xDlOpen */
{% endraw %}

```
### lang/sql/odbc/sqliteodbc.c

```cpp

{% raw %}
732 | #ifdef USE_DLOPEN_FOR_GPPS
740 |  * dlopen(), in theory this makes the driver independent from the
751 |     lib = dlopen("libodbcinst.so.1", RTLD_LAZY);
753 | 	lib = dlopen("libodbcinst.so", RTLD_LAZY);
756 | 	lib = dlopen("libiodbcinst.so.2", RTLD_LAZY);
759 | 	lib = dlopen("libiodbcinst.so", RTLD_LAZY);
{% endraw %}

```
### lang/sql/odbc/ltmain.sh

```bash

{% raw %}
542 |   -dlopen)
543 |     prevopt="-dlopen"
627 |   # Only execute mode is allowed to have -dlopen flags.
629 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1168 | 	    dlopen_self=$dlopen_self_static
1174 | 	    dlopen_self=$dlopen_self_static
1180 |         dlopen_self=$dlopen_self_static
1237 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1329 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1486 |       -dlopen)
1873 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1946 | 	  # This library was specified with -dlopen.
2087 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2099 | 	passes="conv scan dlopen dlpreopen link"
2112 | 	dlopen) libs="$dlfiles" ;;
2117 |       if test "$pass" = dlopen; then
2296 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2297 | 	      # If there is no dlopen support or we're linking statically,
2330 | 	dlopen=
2351 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2394 | 	# This library was specified with -dlopen.
2395 | 	if test "$pass" = dlopen; then
2397 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2401 | 	     test "$dlopen_support" != yes ||
2403 | 	    # If there is no dlname, no dlopen support or we're linking
2412 | 	fi # $pass = dlopen
2465 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2842 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2843 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2994 |       if test "$pass" != dlopen; then
3095 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3162 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3797 | 	    $echo "*** a static module, that should work as long as the dlopening"
3798 | 	    $echo "*** application is linked with the -dlopen flag."
3816 | 	    $echo "*** or is declared to -dlopen it."
4226 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4360 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4361 | 	   test "$dlopen_self_static" = unknown; then
4362 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5712 | # The name that we can dlopen(3).
5735 | # Files to dlopen/dlpreopen
5736 | dlopen='$dlfiles'
6351 |     # Handle -dlopen flags immediately.
6380 | 	# Skip this library if it cannot be dlopened.
6405 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6768 |   -dlopen FILE      add the directory containing FILE to the library path
6770 | This mode sets the library path environment variable according to \`-dlopen'
6819 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6828 |   -module           build a library that can dlopened
{% endraw %}

```
### lang/sql/odbc/configure.in

```

{% raw %}
584 | # Experimental: dlopen for resolving SQLGetPrivateProfileString dynamically
586 | AC_CHECK_LIB(dl,dlopen,DLOPENFORGPPS=1,DLOPENFORGPPS=0)
587 | if test "$DLOPENFORGPPS" = "1" ; then
588 |    AC_MSG_CHECKING([for SQLGetPrivateProfileString via dlopen])
600 |    lib = dlopen("libodbcinst.so", RTLD_LAZY);
602 |       lib = dlopen("libiodbcinst.so", RTLD_LAZY);
611 |    ODBC_FLAGS="$ODBC_FLAGS -DUSE_DLOPEN_FOR_GPPS"
701 | # Experimental: dlopen for resolving SQLite3/SQLite4 symbols
703 | AC_ARG_WITH(dls,[  --with-dls              dlopen SQLite3/SQLite4 lib],
705 | if test "$DLOPENFORGPPS" = "1" ; then
{% endraw %}

```
### lang/sql/odbc/aclocal.m4

```

{% raw %}
199 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
814 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
817 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
873 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
902 | ])# _LT_AC_TRY_DLOPEN_SELF
905 | # AC_LIBTOOL_DLOPEN_SELF
907 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
909 | if test "x$enable_dlopen" != xyes; then
910 |   enable_dlopen=unknown
911 |   enable_dlopen_self=unknown
912 |   enable_dlopen_self_static=unknown
914 |   lt_cv_dlopen=no
915 |   lt_cv_dlopen_libs=
919 |     lt_cv_dlopen="load_add_on"
920 |     lt_cv_dlopen_libs=
921 |     lt_cv_dlopen_self=yes
925 |     lt_cv_dlopen="LoadLibrary"
926 |     lt_cv_dlopen_libs=
930 |     lt_cv_dlopen="dlopen"
931 |     lt_cv_dlopen_libs=
936 |     AC_CHECK_LIB([dl], [dlopen],
937 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
938 |     lt_cv_dlopen="dyld"
939 |     lt_cv_dlopen_libs=
940 |     lt_cv_dlopen_self=yes
946 | 	  [lt_cv_dlopen="shl_load"],
948 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
949 | 	[AC_CHECK_FUNC([dlopen],
950 | 	      [lt_cv_dlopen="dlopen"],
951 | 	  [AC_CHECK_LIB([dl], [dlopen],
952 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
953 | 	    [AC_CHECK_LIB([svld], [dlopen],
954 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
956 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
965 |   if test "x$lt_cv_dlopen" != xno; then
966 |     enable_dlopen=yes
968 |     enable_dlopen=no
971 |   case $lt_cv_dlopen in
972 |   dlopen)
980 |     LIBS="$lt_cv_dlopen_libs $LIBS"
982 |     AC_CACHE_CHECK([whether a program can dlopen itself],
983 | 	  lt_cv_dlopen_self, [dnl
984 | 	  _LT_AC_TRY_DLOPEN_SELF(
985 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
986 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
989 |     if test "x$lt_cv_dlopen_self" = xyes; then
991 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
992 |     	  lt_cv_dlopen_self_static, [dnl
993 | 	  _LT_AC_TRY_DLOPEN_SELF(
994 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
995 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1005 |   case $lt_cv_dlopen_self in
1006 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1007 |   *) enable_dlopen_self=unknown ;;
1010 |   case $lt_cv_dlopen_self_static in
1011 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1012 |   *) enable_dlopen_self_static=unknown ;;
1015 | ])# AC_LIBTOOL_DLOPEN_SELF
1905 | # AC_LIBTOOL_DLOPEN
1907 | # enable checks for dlopen support
1908 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1910 | ])# AC_LIBTOOL_DLOPEN
2702 | AC_LIBTOOL_DLOPEN_SELF
4384 | # Whether dlopen is supported.
4385 | dlopen_support=$enable_dlopen
4387 | # Whether dlopen of programs is supported.
4388 | dlopen_self=$enable_dlopen_self
4390 | # Whether dlopen of statically linked programs is supported.
4391 | dlopen_self_static=$enable_dlopen_self_static
4399 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### lang/sql/generated/sqlite3.c

```cpp

{% raw %}
1180 |   void *(*xDlOpen)(sqlite3_vfs*, const char *zFilename);
9764 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *, const char *);
15423 | SQLITE_PRIVATE void *sqlite3OsDlOpen(sqlite3_vfs *pVfs, const char *zPath){
15424 |   return pVfs->xDlOpen(pVfs, zPath);
29304 | static void *unixDlOpen(sqlite3_vfs *NotUsed, const char *zFilename){
29306 |   return dlopen(zFilename, RTLD_NOW | RTLD_GLOBAL);
29311 | ** unixDlOpen() fails (returns a null pointer). If a more detailed error
29354 |   #define unixDlOpen  0
30728 |     unixDlOpen,           /* xDlOpen */                     \
36149 | static void *winDlOpen(sqlite3_vfs *pVfs, const char *zFilename){
36184 |   #define winDlOpen  0
36367 |     winDlOpen,           /* xDlOpen */
36392 |     winDlOpen,           /* xDlOpen */
86648 |   handle = sqlite3OsDlOpen(pVfs, zFile);
86653 |     handle = sqlite3OsDlOpen(pVfs, zAltFile);
{% endraw %}

```
### docs/installation/build_unix_notes.html

```html

{% raw %}
174 |                 when applications (for example, tclsh) use dlopen to
186 |                 your application is using dlopen to dynamically load
{% endraw %}

```
### docs/programmer_reference/solaris.txt

```

{% raw %}
51 | 	lib_handle = dlopen(NULL, RTLD_NOW);
{% endraw %}

```