---
name: "libquo"
layout: package
next_package: cyrus-sasl
previous_package: libxshmfence
languages: ['cpp']
---
## master
7 / 308 files match

 - [src/hwloc/configure.ac](#srchwlocconfigureac)
 - [src/hwloc/config/libtool.m4](#srchwlocconfiglibtoolm4)
 - [src/hwloc/config/ltoptions.m4](#srchwlocconfigltoptionsm4)
 - [src/hwloc/config/hwloc.m4](#srchwlocconfighwlocm4)
 - [src/hwloc/include/hwloc/plugins.h](#srchwlocincludehwlocpluginsh)
 - [src/hwloc/hwloc/components.c](#srchwlochwloccomponentsc)
 - [src/hwloc/contrib/hwloc-valgrind.supp](#srchwloccontribhwloc-valgrindsupp)

### src/hwloc/configure.ac

```

{% raw %}
88 | LT_INIT([dlopen win32-dll])
{% endraw %}

```
### src/hwloc/config/libtool.m4

```

{% raw %}
1821 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1824 | m4_defun([_LT_TRY_DLOPEN_SELF],
1882 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1915 | ])# _LT_TRY_DLOPEN_SELF
1918 | # LT_SYS_DLOPEN_SELF
1920 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1922 | if test yes != "$enable_dlopen"; then
1923 |   enable_dlopen=unknown
1924 |   enable_dlopen_self=unknown
1925 |   enable_dlopen_self_static=unknown
1927 |   lt_cv_dlopen=no
1928 |   lt_cv_dlopen_libs=
1932 |     lt_cv_dlopen=load_add_on
1933 |     lt_cv_dlopen_libs=
1934 |     lt_cv_dlopen_self=yes
1938 |     lt_cv_dlopen=LoadLibrary
1939 |     lt_cv_dlopen_libs=
1943 |     lt_cv_dlopen=dlopen
1944 |     lt_cv_dlopen_libs=
1949 |     AC_CHECK_LIB([dl], [dlopen],
1950 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1951 |     lt_cv_dlopen=dyld
1952 |     lt_cv_dlopen_libs=
1953 |     lt_cv_dlopen_self=yes
1960 |     lt_cv_dlopen=dlopen
1961 |     lt_cv_dlopen_libs=
1962 |     lt_cv_dlopen_self=no
1967 | 	  [lt_cv_dlopen=shl_load],
1969 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1970 | 	[AC_CHECK_FUNC([dlopen],
1971 | 	      [lt_cv_dlopen=dlopen],
1972 | 	  [AC_CHECK_LIB([dl], [dlopen],
1973 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1974 | 	    [AC_CHECK_LIB([svld], [dlopen],
1975 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1977 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1986 |   if test no = "$lt_cv_dlopen"; then
1987 |     enable_dlopen=no
1989 |     enable_dlopen=yes
1992 |   case $lt_cv_dlopen in
1993 |   dlopen)
2001 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2003 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2004 | 	  lt_cv_dlopen_self, [dnl
2005 | 	  _LT_TRY_DLOPEN_SELF(
2006 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2007 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2010 |     if test yes = "$lt_cv_dlopen_self"; then
2012 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2013 | 	  lt_cv_dlopen_self_static, [dnl
2014 | 	  _LT_TRY_DLOPEN_SELF(
2015 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2016 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2026 |   case $lt_cv_dlopen_self in
2027 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2028 |   *) enable_dlopen_self=unknown ;;
2031 |   case $lt_cv_dlopen_self_static in
2032 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2033 |   *) enable_dlopen_self_static=unknown ;;
2036 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2037 | 	 [Whether dlopen is supported])
2038 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2039 | 	 [Whether dlopen of programs is supported])
2040 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2041 | 	 [Whether dlopen of statically linked programs is supported])
2042 | ])# LT_SYS_DLOPEN_SELF
2045 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2047 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6122 |     [Compiler flag to allow reflexive dlopens])
6235 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/hwloc/config/ltoptions.m4

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
### src/hwloc/config/hwloc.m4

```

{% raw %}
1136 |       AC_CHECK_LIB([ltdl], [lt_dlopenext],
1369 |   save_lt_cv_dlopen="$lt_cv_dlopen"
1370 |   save_lt_cv_dlopen_libs="$lt_cv_dlopen_libs"
1371 |   save_lt_cv_dlopen_self="$lt_cv_dlopen_self"
1373 |   # code stolen from LT_SYS_DLOPEN_SELF in libtool.m4
1376 |     lt_cv_dlopen="load_add_on"
1377 |     lt_cv_dlopen_libs=
1378 |     lt_cv_dlopen_self=yes
1382 |     lt_cv_dlopen="LoadLibrary"
1383 |     lt_cv_dlopen_libs=
1387 |     lt_cv_dlopen="dlopen"
1388 |     lt_cv_dlopen_libs=
1393 |     AC_CHECK_LIB([dl], [dlopen],
1394 |                 [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1395 |     lt_cv_dlopen="dyld"
1396 |     lt_cv_dlopen_libs=
1397 |     lt_cv_dlopen_self=yes
1403 |           [lt_cv_dlopen="shl_load"],
1405 |             [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1406 |         [AC_CHECK_FUNC([dlopen],
1407 |               [lt_cv_dlopen="dlopen"],
1408 |           [AC_CHECK_LIB([dl], [dlopen],
1409 |                 [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1410 |             [AC_CHECK_LIB([svld], [dlopen],
1411 |                   [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1413 |                     [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1421 |   # end of code stolen from LT_SYS_DLOPEN_SELF in libtool.m4
1424 |   HWLOC_LIBS_PRIVATE="$HWLOC_LIBS_PRIVATE $lt_cv_dlopen_libs"
1427 |   lt_cv_dlopen="$save_lt_cv_dlopen"
1428 |   lt_cv_dlopen_libs="$save_lt_cv_dlopen_libs"
1429 |   lt_cv_dlopen_self="$save_lt_cv_dlopen_self"
{% endraw %}

```
### src/hwloc/include/hwloc/plugins.h

```cpp

{% raw %}
408 |  * loaded hwloc (e.g. OpenCL implementations using dlopen with RTLD_LAZY).
422 |   handle = lt_dlopen(NULL);
{% endraw %}

```
### src/hwloc/hwloc/components.c

```cpp

{% raw %}
99 |   /* dlopen and get the component structure */
100 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### src/hwloc/contrib/hwloc-valgrind.supp

```

{% raw %}
32 | # ltdl dlopen global state?
34 |    ltdl_dlopen_doit_leak
40 |    fun:dlopen_doit
{% endraw %}

```