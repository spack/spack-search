---
name: "libmesh"
layout: package
next_package: arrayfire
previous_package: libzmq
languages: ['cpp', 'bash']
---
## master
118 / 9244 files match

 - [aclocal.m4](#aclocalm4)
 - [Makefile.in](#makefilein)
 - [include/libmesh_config.h.in](#includelibmesh_confighin)
 - [include/Makefile.in](#includemakefilein)
 - [include/libmesh/Makefile.in](#includelibmeshmakefilein)
 - [tests/Makefile.in](#testsmakefilein)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/libmesh_compiler_features.m4](#m4libmesh_compiler_featuresm4)
 - [m4/dlopen.m4](#m4dlopenm4)
 - [m4/fparser.m4](#m4fparserm4)
 - [examples/Makefile.in](#examplesmakefilein)
 - [examples/systems_of_equations/systems_of_equations_ex7/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex7makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex3/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex3makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex4/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex4makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex5/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex5makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex1/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex1makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex2/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex2makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex6/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex6makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex9/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex9makefilein)
 - [examples/systems_of_equations/systems_of_equations_ex8/Makefile.in](#examplessystems_of_equationssystems_of_equations_ex8makefilein)
 - [examples/fem_system/fem_system_ex5/Makefile.in](#examplesfem_systemfem_system_ex5makefilein)
 - [examples/fem_system/fem_system_ex4/Makefile.in](#examplesfem_systemfem_system_ex4makefilein)
 - [examples/fem_system/fem_system_ex1/Makefile.in](#examplesfem_systemfem_system_ex1makefilein)
 - [examples/fem_system/fem_system_ex2/Makefile.in](#examplesfem_systemfem_system_ex2makefilein)
 - [examples/fem_system/fem_system_ex3/Makefile.in](#examplesfem_systemfem_system_ex3makefilein)
 - [examples/adaptivity/adaptivity_ex2/Makefile.in](#examplesadaptivityadaptivity_ex2makefilein)
 - [examples/adaptivity/adaptivity_ex4/Makefile.in](#examplesadaptivityadaptivity_ex4makefilein)
 - [examples/adaptivity/adaptivity_ex1/Makefile.in](#examplesadaptivityadaptivity_ex1makefilein)
 - [examples/adaptivity/adaptivity_ex5/Makefile.in](#examplesadaptivityadaptivity_ex5makefilein)
 - [examples/adaptivity/adaptivity_ex3/Makefile.in](#examplesadaptivityadaptivity_ex3makefilein)
 - [examples/introduction/introduction_ex2/Makefile.in](#examplesintroductionintroduction_ex2makefilein)
 - [examples/introduction/introduction_ex1/Makefile.in](#examplesintroductionintroduction_ex1makefilein)
 - [examples/introduction/introduction_ex5/Makefile.in](#examplesintroductionintroduction_ex5makefilein)
 - [examples/introduction/introduction_ex4/Makefile.in](#examplesintroductionintroduction_ex4makefilein)
 - [examples/introduction/introduction_ex3/Makefile.in](#examplesintroductionintroduction_ex3makefilein)
 - [examples/reduced_basis/reduced_basis_ex4/Makefile.in](#examplesreduced_basisreduced_basis_ex4makefilein)
 - [examples/reduced_basis/reduced_basis_ex5/Makefile.in](#examplesreduced_basisreduced_basis_ex5makefilein)
 - [examples/reduced_basis/reduced_basis_ex7/Makefile.in](#examplesreduced_basisreduced_basis_ex7makefilein)
 - [examples/reduced_basis/reduced_basis_ex2/Makefile.in](#examplesreduced_basisreduced_basis_ex2makefilein)
 - [examples/reduced_basis/reduced_basis_ex6/Makefile.in](#examplesreduced_basisreduced_basis_ex6makefilein)
 - [examples/reduced_basis/reduced_basis_ex3/Makefile.in](#examplesreduced_basisreduced_basis_ex3makefilein)
 - [examples/reduced_basis/reduced_basis_ex1/Makefile.in](#examplesreduced_basisreduced_basis_ex1makefilein)
 - [examples/subdomains/subdomains_ex1/Makefile.in](#examplessubdomainssubdomains_ex1makefilein)
 - [examples/subdomains/subdomains_ex3/Makefile.in](#examplessubdomainssubdomains_ex3makefilein)
 - [examples/subdomains/subdomains_ex2/Makefile.in](#examplessubdomainssubdomains_ex2makefilein)
 - [examples/optimization/optimization_ex2/Makefile.in](#examplesoptimizationoptimization_ex2makefilein)
 - [examples/optimization/optimization_ex1/Makefile.in](#examplesoptimizationoptimization_ex1makefilein)
 - [examples/vector_fe/vector_fe_ex3/Makefile.in](#examplesvector_fevector_fe_ex3makefilein)
 - [examples/vector_fe/vector_fe_ex1/Makefile.in](#examplesvector_fevector_fe_ex1makefilein)
 - [examples/vector_fe/vector_fe_ex2/Makefile.in](#examplesvector_fevector_fe_ex2makefilein)
 - [examples/vector_fe/vector_fe_ex5/Makefile.in](#examplesvector_fevector_fe_ex5makefilein)
 - [examples/vector_fe/vector_fe_ex4/Makefile.in](#examplesvector_fevector_fe_ex4makefilein)
 - [examples/transient/transient_ex2/Makefile.in](#examplestransienttransient_ex2makefilein)
 - [examples/transient/transient_ex1/Makefile.in](#examplestransienttransient_ex1makefilein)
 - [examples/adjoints/adjoints_ex3/Makefile.in](#examplesadjointsadjoints_ex3makefilein)
 - [examples/adjoints/adjoints_ex7/Makefile.in](#examplesadjointsadjoints_ex7makefilein)
 - [examples/adjoints/adjoints_ex2/Makefile.in](#examplesadjointsadjoints_ex2makefilein)
 - [examples/adjoints/adjoints_ex4/Makefile.in](#examplesadjointsadjoints_ex4makefilein)
 - [examples/adjoints/adjoints_ex6/Makefile.in](#examplesadjointsadjoints_ex6makefilein)
 - [examples/adjoints/adjoints_ex5/Makefile.in](#examplesadjointsadjoints_ex5makefilein)
 - [examples/adjoints/adjoints_ex1/Makefile.in](#examplesadjointsadjoints_ex1makefilein)
 - [examples/eigenproblems/eigenproblems_ex1/Makefile.in](#exampleseigenproblemseigenproblems_ex1makefilein)
 - [examples/eigenproblems/eigenproblems_ex2/Makefile.in](#exampleseigenproblemseigenproblems_ex2makefilein)
 - [examples/eigenproblems/eigenproblems_ex3/Makefile.in](#exampleseigenproblemseigenproblems_ex3makefilein)
 - [examples/solution_transfer/solution_transfer_ex1/Makefile.in](#examplessolution_transfersolution_transfer_ex1makefilein)
 - [examples/miscellaneous/miscellaneous_ex5/Makefile.in](#examplesmiscellaneousmiscellaneous_ex5makefilein)
 - [examples/miscellaneous/miscellaneous_ex13/Makefile.in](#examplesmiscellaneousmiscellaneous_ex13makefilein)
 - [examples/miscellaneous/miscellaneous_ex2/Makefile.in](#examplesmiscellaneousmiscellaneous_ex2makefilein)
 - [examples/miscellaneous/miscellaneous_ex12/Makefile.in](#examplesmiscellaneousmiscellaneous_ex12makefilein)
 - [examples/miscellaneous/miscellaneous_ex1/Makefile.in](#examplesmiscellaneousmiscellaneous_ex1makefilein)
 - [examples/miscellaneous/miscellaneous_ex3/Makefile.in](#examplesmiscellaneousmiscellaneous_ex3makefilein)
 - [examples/miscellaneous/miscellaneous_ex9/Makefile.in](#examplesmiscellaneousmiscellaneous_ex9makefilein)
 - [examples/miscellaneous/miscellaneous_ex6/Makefile.in](#examplesmiscellaneousmiscellaneous_ex6makefilein)
 - [examples/miscellaneous/miscellaneous_ex11/Makefile.in](#examplesmiscellaneousmiscellaneous_ex11makefilein)
 - [examples/miscellaneous/miscellaneous_ex4/Makefile.in](#examplesmiscellaneousmiscellaneous_ex4makefilein)
 - [examples/miscellaneous/miscellaneous_ex10/Makefile.in](#examplesmiscellaneousmiscellaneous_ex10makefilein)
 - [examples/miscellaneous/miscellaneous_ex8/Makefile.in](#examplesmiscellaneousmiscellaneous_ex8makefilein)
 - [examples/miscellaneous/miscellaneous_ex7/Makefile.in](#examplesmiscellaneousmiscellaneous_ex7makefilein)
 - [examples/miscellaneous/miscellaneous_ex14/Makefile.in](#examplesmiscellaneousmiscellaneous_ex14makefilein)
 - [contrib/Makefile.in](#contribmakefilein)
 - [contrib/fparser/fparser_ad.cc](#contribfparserfparser_adcc)
 - [contrib/fparser/Makefile.in](#contribfparsermakefilein)
 - [contrib/fparser/extrasrc/Makefile.in](#contribfparserextrasrcmakefilein)
 - [contrib/metaphysicl/m4/libtool.m4](#contribmetaphysiclm4libtoolm4)
 - [contrib/metaphysicl/m4/ltoptions.m4](#contribmetaphysiclm4ltoptionsm4)
 - [contrib/metaphysicl/build-aux/ltmain.sh](#contribmetaphysiclbuild-auxltmainsh)
 - [contrib/capnproto/Makefile.in](#contribcapnprotomakefilein)
 - [contrib/nemesis/Lib/Makefile.in](#contribnemesislibmakefilein)
 - [contrib/qhull/2012.1/Makefile.in](#contribqhull20121makefilein)
 - [contrib/gzstream/Makefile.in](#contribgzstreammakefilein)
 - [contrib/nanoflann/Makefile.in](#contribnanoflannmakefilein)
 - [contrib/netcdf/netcdf-c-4.6.2/configure.ac](#contribnetcdfnetcdf-c-462configureac)
 - [contrib/netcdf/netcdf-c-4.6.2/ltmain.sh](#contribnetcdfnetcdf-c-462ltmainsh)
 - [contrib/netcdf/netcdf-c-4.6.2/m4/libtool.m4](#contribnetcdfnetcdf-c-462m4libtoolm4)
 - [contrib/netcdf/netcdf-c-4.6.2/m4/ltoptions.m4](#contribnetcdfnetcdf-c-462m4ltoptionsm4)
 - [contrib/boost/include/Makefile.in](#contribboostincludemakefilein)
 - [contrib/exodusii/5.22b/nemesis/Makefile.in](#contribexodusii522bnemesismakefilein)
 - [contrib/exodusii/5.22b/exodus/Makefile.in](#contribexodusii522bexodusmakefilein)
 - [contrib/exodusii/Lib/Makefile.in](#contribexodusiilibmakefilein)
 - [contrib/sfcurves/Makefile.in](#contribsfcurvesmakefilein)
 - [contrib/libHilbert/Makefile.in](#contriblibhilbertmakefilein)
 - [contrib/triangle/Makefile.in](#contribtrianglemakefilein)
 - [contrib/laspack/Makefile.in](#contriblaspackmakefilein)
 - [contrib/parmetis/Makefile.in](#contribparmetismakefilein)
 - [contrib/tecplot/tecio/Makefile.in](#contribtecplotteciomakefilein)
 - [contrib/tecplot/binary/Makefile.in](#contribtecplotbinarymakefilein)
 - [contrib/eigen/3.3.9/Makefile.in](#contribeigen339makefilein)
 - [contrib/eigen/3.2.9/Makefile.in](#contribeigen329makefilein)
 - [contrib/gmv/Makefile.in](#contribgmvmakefilein)
 - [contrib/tetgen/Makefile.in](#contribtetgenmakefilein)
 - [contrib/metis/Makefile.in](#contribmetismakefilein)
 - [contrib/timpi/m4/libtool.m4](#contribtimpim4libtoolm4)
 - [contrib/timpi/m4/ltoptions.m4](#contribtimpim4ltoptionsm4)
 - [contrib/timpi/build-aux/ltmain.sh](#contribtimpibuild-auxltmainsh)
 - [build-aux/ltmain.sh](#build-auxltmainsh)
 - [doc/Makefile.in](#docmakefilein)
 - [doc/html/Makefile.in](#dochtmlmakefilein)

### aclocal.m4

```

{% raw %}
1202 | m4_include([m4/dlopen.m4])
{% endraw %}

```
### Makefile.in

```

{% raw %}
152 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### include/libmesh_config.h.in

```

{% raw %}
350 | /* define if the compiler supports dlopen/dlsym/dlclose */
351 | #undef HAVE_DLOPEN
{% endraw %}

```
### include/Makefile.in

```

{% raw %}
121 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### include/libmesh/Makefile.in

```

{% raw %}
135 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### tests/Makefile.in

```

{% raw %}
149 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### m4/libtool.m4

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
### m4/libmesh_compiler_features.m4

```

{% raw %}
225 | AX_CXX_DLOPEN
228 | AS_IF([test "$ac_cv_cxx_dlopen" = yes],
229 |       [AC_DEFINE(HAVE_DLOPEN, 1, [define if the compiler supports dlopen/dlsym/dlclose])])
{% endraw %}

```
### m4/dlopen.m4

```

{% raw %}
1 | dnl check for a working dlopen/dlsym/dlclose implementation
3 | AC_DEFUN([AX_CXX_DLOPEN],
5 |   ac_cv_cxx_dlopen=no
8 |   AC_SEARCH_LIBS([dlopen], [dl dld], [ac_cv_cxx_dlopen=yes], [ac_cv_cxx_dlopen=no])
10 |   dnl dlopen cannot be used if we are configured with
13 |   dnl warning: Using 'dlopen' in statically linked applications
18 |   AS_IF([test "x$enableallstatic" = "xyes"], [ac_cv_cxx_dlopen=no])
21 |   AS_IF([test "x$ac_cv_cxx_dlopen" = "xyes"],
23 |           AC_MSG_CHECKING([whether the c++ compiler supports dlopen/dlsym/dlclose])
31 |              // Try all possible ways of naming libraries.  dlopen() will search
37 |              // To catch the output of dlopen
43 |                  handle = dlopen(lib_names[i], RTLD_LAZY);
66 |             ac_cv_cxx_dlopen=yes
71 |             ac_cv_cxx_dlopen=no
{% endraw %}

```
### m4/fparser.m4

```

{% raw %}
58 |           AC_CACHE_CHECK([for dlopen support], [ac_cv_cxx_dlopen], AX_CXX_DLOPEN)
60 |           dnl JIT requires dlopen, use the result of the AX_CXX_DLOPEN test.
61 |           AS_IF([test "x$ac_cv_cxx_dlopen" = "xyes"],
68 |                   AC_MSG_RESULT(<<< dlopen() not found, configuring library without fparser JIT compilation support >>>)
{% endraw %}

```
### examples/Makefile.in

```

{% raw %}
119 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex7/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex3/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex4/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex5/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex2/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex6/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex9/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/systems_of_equations/systems_of_equations_ex8/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/fem_system/fem_system_ex5/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/fem_system/fem_system_ex4/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/fem_system/fem_system_ex1/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/fem_system/fem_system_ex2/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/fem_system/fem_system_ex3/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adaptivity/adaptivity_ex2/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adaptivity/adaptivity_ex4/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adaptivity/adaptivity_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adaptivity/adaptivity_ex5/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adaptivity/adaptivity_ex3/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/introduction/introduction_ex2/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/introduction/introduction_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/introduction/introduction_ex5/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/introduction/introduction_ex4/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/introduction/introduction_ex3/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex4/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex5/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex7/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex2/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex6/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex3/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/reduced_basis/reduced_basis_ex1/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/subdomains/subdomains_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/subdomains/subdomains_ex3/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/subdomains/subdomains_ex2/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/optimization/optimization_ex2/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/optimization/optimization_ex1/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/vector_fe/vector_fe_ex3/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/vector_fe/vector_fe_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/vector_fe/vector_fe_ex2/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/vector_fe/vector_fe_ex5/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/vector_fe/vector_fe_ex4/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/transient/transient_ex2/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/transient/transient_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex3/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex7/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex2/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex4/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex6/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex5/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/adjoints/adjoints_ex1/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/eigenproblems/eigenproblems_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/eigenproblems/eigenproblems_ex2/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/eigenproblems/eigenproblems_ex3/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/solution_transfer/solution_transfer_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex5/Makefile.in

```

{% raw %}
130 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex13/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex2/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex12/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex1/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex3/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex9/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex6/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex11/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex4/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex10/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex8/Makefile.in

```

{% raw %}
127 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex7/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### examples/miscellaneous/miscellaneous_ex14/Makefile.in

```

{% raw %}
126 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/Makefile.in

```

{% raw %}
247 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/fparser/fparser_ad.cc

```cpp

{% raw %}
1102 |   _lib = dlopen(libname.c_str(), RTLD_NOW);
1146 |   // add a .so extension to the object (needed by dlopen on mac)
1156 |   _lib = dlopen(_object_so.c_str(), RTLD_NOW);
{% endraw %}

```
### contrib/fparser/Makefile.in

```

{% raw %}
141 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/fparser/extrasrc/Makefile.in

```

{% raw %}
123 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/metaphysicl/m4/libtool.m4

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
### contrib/metaphysicl/m4/ltoptions.m4

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
### contrib/metaphysicl/build-aux/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### contrib/capnproto/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/nemesis/Lib/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/qhull/2012.1/Makefile.in

```

{% raw %}
128 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/gzstream/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/nanoflann/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/netcdf/netcdf-c-4.6.2/configure.ac

```

{% raw %}
1006 |    AC_SEARCH_LIBS([dlopen], [dl dld], [], [])
{% endraw %}

```
### contrib/netcdf/netcdf-c-4.6.2/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### contrib/netcdf/netcdf-c-4.6.2/m4/libtool.m4

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
### contrib/netcdf/netcdf-c-4.6.2/m4/ltoptions.m4

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
### contrib/boost/include/Makefile.in

```

{% raw %}
121 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/exodusii/5.22b/nemesis/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/exodusii/5.22b/exodus/Makefile.in

```

{% raw %}
134 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/exodusii/Lib/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/sfcurves/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/libHilbert/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/triangle/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/laspack/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/parmetis/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/tecplot/tecio/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/tecplot/binary/Makefile.in

```

{% raw %}
120 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/eigen/3.3.9/Makefile.in

```

{% raw %}
122 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/eigen/3.2.9/Makefile.in

```

{% raw %}
122 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/gmv/Makefile.in

```

{% raw %}
124 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/tetgen/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/metis/Makefile.in

```

{% raw %}
125 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### contrib/timpi/m4/libtool.m4

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
### contrib/timpi/m4/ltoptions.m4

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
### contrib/timpi/build-aux/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7343 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7411 | 	  # This library was specified with -dlopen.
7531 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7542 | 	passes="conv scan dlopen dlpreopen link"
7568 | 	dlopen) libs=$dlfiles ;;
7596 |       if test dlopen = "$pass"; then
7816 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7817 | 	      # If there is no dlopen support or we're linking statically,
7845 | 	dlopen=
7875 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7921 | 	# This library was specified with -dlopen.
7922 | 	if test dlopen = "$pass"; then
7924 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7926 | 	     test yes != "$dlopen_support" ||
7929 | 	    # If there is no dlname, no dlopen support or we're linking
7938 | 	fi # $pass = dlopen
7994 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7996 | 	      # We recover the dlopen module name by 'saving' the la file
8020 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8149 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8150 | 	  dlopenmodule=
8153 | 	      dlopenmodule=$dlpremoduletest
8157 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8254 | 		    # if the lib is a (non-dlopened) module then we cannot
8258 | 		      if test "X$dlopenmodule" != "X$lib"; then
8410 | 	      echo "*** a static module, that should work as long as the dlopening application"
8411 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8555 |       if test dlopen != "$pass"; then
8685 | 	func_warning "'-dlopen' is ignored for archives"
8752 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9446 | 	    echo "*** a static module, that should work as long as the dlopening"
9447 | 	    echo "*** application is linked with the -dlopen flag."
9465 | 	    echo "*** or is declared to -dlopen it."
10077 | 	func_warning "'-dlopen' is ignored for objects"
10197 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10198 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10879 | # The name that we can dlopen(3).
10908 | # Files to dlopen/dlpreopen
10909 | dlopen='$dlfiles'
{% endraw %}

```
### doc/Makefile.in

```

{% raw %}
118 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```
### doc/html/Makefile.in

```

{% raw %}
122 | 	$(top_srcdir)/m4/demangle.m4 $(top_srcdir)/m4/dlopen.m4 \
{% endraw %}

```