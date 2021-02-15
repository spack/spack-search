---
name: "kbd"
layout: package
next_package: libpng
previous_package: boost
languages: []
---
## 2.2.0
3 / 969 files match

 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)

### m4/libtool.m4

```

{% raw %}
1841 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1844 | m4_defun([_LT_TRY_DLOPEN_SELF],
1902 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1935 | ])# _LT_TRY_DLOPEN_SELF
1938 | # LT_SYS_DLOPEN_SELF
1940 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1942 | if test yes != "$enable_dlopen"; then
1943 |   enable_dlopen=unknown
1944 |   enable_dlopen_self=unknown
1945 |   enable_dlopen_self_static=unknown
1947 |   lt_cv_dlopen=no
1948 |   lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen=load_add_on
1953 |     lt_cv_dlopen_libs=
1954 |     lt_cv_dlopen_self=yes
1958 |     lt_cv_dlopen=LoadLibrary
1959 |     lt_cv_dlopen_libs=
1963 |     lt_cv_dlopen=dlopen
1964 |     lt_cv_dlopen_libs=
1969 |     AC_CHECK_LIB([dl], [dlopen],
1970 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1971 |     lt_cv_dlopen=dyld
1972 |     lt_cv_dlopen_libs=
1973 |     lt_cv_dlopen_self=yes
1980 |     lt_cv_dlopen=dlopen
1981 |     lt_cv_dlopen_libs=
1982 |     lt_cv_dlopen_self=no
1987 | 	  [lt_cv_dlopen=shl_load],
1989 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1990 | 	[AC_CHECK_FUNC([dlopen],
1991 | 	      [lt_cv_dlopen=dlopen],
1992 | 	  [AC_CHECK_LIB([dl], [dlopen],
1993 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1994 | 	    [AC_CHECK_LIB([svld], [dlopen],
1995 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1997 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2006 |   if test no = "$lt_cv_dlopen"; then
2007 |     enable_dlopen=no
2009 |     enable_dlopen=yes
2012 |   case $lt_cv_dlopen in
2013 |   dlopen)
2021 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2023 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2024 | 	  lt_cv_dlopen_self, [dnl
2025 | 	  _LT_TRY_DLOPEN_SELF(
2026 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2027 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2030 |     if test yes = "$lt_cv_dlopen_self"; then
2032 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2033 | 	  lt_cv_dlopen_self_static, [dnl
2034 | 	  _LT_TRY_DLOPEN_SELF(
2035 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2036 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2046 |   case $lt_cv_dlopen_self in
2047 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2048 |   *) enable_dlopen_self=unknown ;;
2051 |   case $lt_cv_dlopen_self_static in
2052 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2053 |   *) enable_dlopen_self_static=unknown ;;
2056 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2057 | 	 [Whether dlopen is supported])
2058 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2059 | 	 [Whether dlopen of programs is supported])
2060 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2061 | 	 [Whether dlopen of statically linked programs is supported])
2062 | ])# LT_SYS_DLOPEN_SELF
2065 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2067 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6160 |     [Compiler flag to allow reflexive dlopens])
6273 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

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
### m4/lib-link.m4

```

{% raw %}
377 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```