---
name: "cunit"
layout: package
next_package: ilmbase
previous_package: enchant
languages: []
---
## 2.1-3
2 / 177 files match

 - [config.status](#configstatus)
 - [aclocal.m4](#aclocalm4)

### config.status

```

{% raw %}
678 | enable_dlopen='unknown'
679 | enable_dlopen_self='unknown'
680 | enable_dlopen_self_static='unknown'
1763 | # Whether dlopen is supported.
1764 | dlopen_support=$enable_dlopen
1766 | # Whether dlopen of programs is supported.
1767 | dlopen_self=$enable_dlopen_self
1769 | # Whether dlopen of statically linked programs is supported.
1770 | dlopen_self_static=$enable_dlopen_self_static
1814 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### aclocal.m4

```

{% raw %}
1808 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1811 | m4_defun([_LT_TRY_DLOPEN_SELF],
1869 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1902 | ])# _LT_TRY_DLOPEN_SELF
1905 | # LT_SYS_DLOPEN_SELF
1907 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1909 | if test yes != "$enable_dlopen"; then
1910 |   enable_dlopen=unknown
1911 |   enable_dlopen_self=unknown
1912 |   enable_dlopen_self_static=unknown
1914 |   lt_cv_dlopen=no
1915 |   lt_cv_dlopen_libs=
1919 |     lt_cv_dlopen=load_add_on
1920 |     lt_cv_dlopen_libs=
1921 |     lt_cv_dlopen_self=yes
1925 |     lt_cv_dlopen=LoadLibrary
1926 |     lt_cv_dlopen_libs=
1930 |     lt_cv_dlopen=dlopen
1931 |     lt_cv_dlopen_libs=
1936 |     AC_CHECK_LIB([dl], [dlopen],
1937 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1938 |     lt_cv_dlopen=dyld
1939 |     lt_cv_dlopen_libs=
1940 |     lt_cv_dlopen_self=yes
1947 |     lt_cv_dlopen=dlopen
1948 |     lt_cv_dlopen_libs=
1949 |     lt_cv_dlopen_self=no
1954 | 	  [lt_cv_dlopen=shl_load],
1956 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1957 | 	[AC_CHECK_FUNC([dlopen],
1958 | 	      [lt_cv_dlopen=dlopen],
1959 | 	  [AC_CHECK_LIB([dl], [dlopen],
1960 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1961 | 	    [AC_CHECK_LIB([svld], [dlopen],
1962 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1964 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1973 |   if test no = "$lt_cv_dlopen"; then
1974 |     enable_dlopen=no
1976 |     enable_dlopen=yes
1979 |   case $lt_cv_dlopen in
1980 |   dlopen)
1988 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1990 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1991 | 	  lt_cv_dlopen_self, [dnl
1992 | 	  _LT_TRY_DLOPEN_SELF(
1993 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1994 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1997 |     if test yes = "$lt_cv_dlopen_self"; then
1999 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2000 | 	  lt_cv_dlopen_self_static, [dnl
2001 | 	  _LT_TRY_DLOPEN_SELF(
2002 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2003 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2013 |   case $lt_cv_dlopen_self in
2014 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2015 |   *) enable_dlopen_self=unknown ;;
2018 |   case $lt_cv_dlopen_self_static in
2019 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2020 |   *) enable_dlopen_self_static=unknown ;;
2023 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2024 | 	 [Whether dlopen is supported])
2025 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2026 | 	 [Whether dlopen of programs is supported])
2027 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2028 | 	 [Whether dlopen of statically linked programs is supported])
2029 | ])# LT_SYS_DLOPEN_SELF
2032 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2034 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5799 |     [Compiler flag to allow reflexive dlopens])
5908 |   LT_SYS_DLOPEN_SELF
8060 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
8092 | # dlopen
8094 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
8097 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
8098 | [_LT_SET_OPTION([LT_INIT], [dlopen])
8101 | put the 'dlopen' option into LT_INIT's first parameter.])
8105 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
8566 | m4_ifndef([_LT_AC_TRY_DLOPEN_SELF],	[AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])])
{% endraw %}

```