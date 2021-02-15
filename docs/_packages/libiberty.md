---
name: "libiberty"
layout: package
next_package: lesstif
previous_package: atk
languages: ['cpp', 'bash']
---
## 2.31.1
60 / 21078 files match

 - [libtool.m4](#libtoolm4)
 - [ltoptions.m4](#ltoptionsm4)
 - [ltmain.sh](#ltmainsh)
 - [config/plugins.m4](#configpluginsm4)
 - [config/tcl.m4](#configtclm4)
 - [config/gcc-plugin.m4](#configgcc-pluginm4)
 - [config/lib-link.m4](#configlib-linkm4)
 - [elfcpp/elfcpp.h](#elfcppelfcpph)
 - [include/gcc-c-interface.h](#includegcc-c-interfaceh)
 - [include/gcc-cp-interface.h](#includegcc-cp-interfaceh)
 - [include/elf/mips.h](#includeelfmipsh)
 - [include/aout/sun4.h](#includeaoutsun4h)
 - [bfd/elf32-frv.c](#bfdelf32-frvc)
 - [bfd/configure.ac](#bfdconfigureac)
 - [bfd/elf64-ppc.c](#bfdelf64-ppcc)
 - [bfd/Makefile.am](#bfdmakefileam)
 - [bfd/plugin.c](#bfdpluginc)
 - [bfd/Makefile.in](#bfdmakefilein)
 - [bfd/doc/Makefile.in](#bfddocmakefilein)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [gold/plugin.h](#goldpluginh)
 - [gold/layout.cc](#goldlayoutcc)
 - [gold/configure.ac](#goldconfigureac)
 - [gold/options.h](#goldoptionsh)
 - [gold/plugin.cc](#goldplugincc)
 - [gold/po/zh_CN.po](#goldpozh_cnpo)
 - [gold/po/uk.po](#goldpoukpo)
 - [gold/po/es.po](#goldpoespo)
 - [gold/po/vi.po](#goldpovipo)
 - [gold/po/gold.pot](#goldpogoldpot)
 - [gold/po/sv.po](#goldposvpo)
 - [gold/po/fi.po](#goldpofipo)
 - [gold/po/it.po](#goldpoitpo)
 - [gold/po/ja.po](#goldpojapo)
 - [gold/po/fr.po](#goldpofrpo)
 - [gold/po/id.po](#goldpoidpo)
 - [gold/testsuite/ifuncmod3.c](#goldtestsuiteifuncmod3c)
 - [gold/testsuite/ifuncmain3.c](#goldtestsuiteifuncmain3c)
 - [ld/ld.texi](#ldldtexi)
 - [ld/configure.ac](#ldconfigureac)
 - [ld/ld.1](#ldld1)
 - [ld/lexsup.c](#ldlexsupc)
 - [ld/plugin.c](#ldpluginc)
 - [ld/ld.info](#ldldinfo)
 - [ld/po/uk.po](#ldpoukpo)
 - [ld/po/ld.pot](#ldpoldpot)
 - [ld/po/es.po](#ldpoespo)
 - [ld/po/bg.po](#ldpobgpo)
 - [ld/po/tr.po](#ldpotrpo)
 - [ld/po/pt_BR.po](#ldpopt_brpo)
 - [ld/emultempl/elf32.em](#ldemultemplelf32em)
 - [ld/testsuite/lib/ld-lib.exp](#ldtestsuitelibld-libexp)
 - [ld/testsuite/ld-elf/dl1main.c](#ldtestsuiteld-elfdl1mainc)
 - [ld/testsuite/ld-elf/dl6dmain.c](#ldtestsuiteld-elfdl6dmainc)
 - [ld/testsuite/ld-elf/dl6bmain.c](#ldtestsuiteld-elfdl6bmainc)
 - [ld/testsuite/ld-elf/shared.exp](#ldtestsuiteld-elfsharedexp)
 - [ld/testsuite/ld-elf/dl6amain.c](#ldtestsuiteld-elfdl6amainc)
 - [ld/testsuite/ld-elf/dl6cmain.c](#ldtestsuiteld-elfdl6cmainc)
 - [ld/testsuite/ld-elf/pr21964-2c.c](#ldtestsuiteld-elfpr21964-2cc)
 - [ld/testsuite/ld-plugin/plugin.exp](#ldtestsuiteld-pluginpluginexp)

### libtool.m4

```

{% raw %}
1614 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1617 | m4_defun([_LT_TRY_DLOPEN_SELF],
1675 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1708 | ])# _LT_TRY_DLOPEN_SELF
1711 | # LT_SYS_DLOPEN_SELF
1713 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1715 | if test "x$enable_dlopen" != xyes; then
1716 |   enable_dlopen=unknown
1717 |   enable_dlopen_self=unknown
1718 |   enable_dlopen_self_static=unknown
1720 |   lt_cv_dlopen=no
1721 |   lt_cv_dlopen_libs=
1725 |     lt_cv_dlopen="load_add_on"
1726 |     lt_cv_dlopen_libs=
1727 |     lt_cv_dlopen_self=yes
1731 |     lt_cv_dlopen="LoadLibrary"
1732 |     lt_cv_dlopen_libs=
1736 |     lt_cv_dlopen="dlopen"
1737 |     lt_cv_dlopen_libs=
1742 |     AC_CHECK_LIB([dl], [dlopen],
1743 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1744 |     lt_cv_dlopen="dyld"
1745 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen_self=yes
1752 | 	  [lt_cv_dlopen="shl_load"],
1754 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1755 | 	[AC_CHECK_FUNC([dlopen],
1756 | 	      [lt_cv_dlopen="dlopen"],
1757 | 	  [AC_CHECK_LIB([dl], [dlopen],
1758 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1759 | 	    [AC_CHECK_LIB([svld], [dlopen],
1760 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1762 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1771 |   if test "x$lt_cv_dlopen" != xno; then
1772 |     enable_dlopen=yes
1774 |     enable_dlopen=no
1777 |   case $lt_cv_dlopen in
1778 |   dlopen)
1786 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1788 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1789 | 	  lt_cv_dlopen_self, [dnl
1790 | 	  _LT_TRY_DLOPEN_SELF(
1791 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1792 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1795 |     if test "x$lt_cv_dlopen_self" = xyes; then
1797 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1798 | 	  lt_cv_dlopen_self_static, [dnl
1799 | 	  _LT_TRY_DLOPEN_SELF(
1800 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1801 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1811 |   case $lt_cv_dlopen_self in
1812 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1813 |   *) enable_dlopen_self=unknown ;;
1816 |   case $lt_cv_dlopen_self_static in
1817 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1818 |   *) enable_dlopen_self_static=unknown ;;
1821 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1822 | 	 [Whether dlopen is supported])
1823 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1824 | 	 [Whether dlopen of programs is supported])
1825 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1826 | 	 [Whether dlopen of statically linked programs is supported])
1827 | ])# LT_SYS_DLOPEN_SELF
1830 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1832 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5263 |     [Compiler flag to allow reflexive dlopens])
5379 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### ltoptions.m4

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
### ltmain.sh

```bash

{% raw %}
895 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
957 |       -dlopen=*|--mode=*|--tag=*)
1047 |   # Only execute mode is allowed to have -dlopen flags.
1049 |     func_error "unrecognized option \`-dlopen'"
1683 |   -dlopen FILE      add the directory containing FILE to the library path
1685 | This mode sets the library path environment variable according to \`-dlopen'
1740 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1749 |   -module           build a library that can dlopened
1855 |     # Handle -dlopen flags immediately.
1872 | 	# Skip this library if it cannot be dlopened.
1899 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
4322 | 	    dlopen_self=$dlopen_self_static
4328 | 	    dlopen_self=$dlopen_self_static
4334 | 	    dlopen_self=$dlopen_self_static
4392 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
4476 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4638 |       -dlopen)
5029 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5096 | 	  # This library was specified with -dlopen.
5211 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
5222 | 	passes="conv scan dlopen dlpreopen link"
5248 | 	dlopen) libs="$dlfiles" ;;
5275 |       if test "$pass" = dlopen; then
5487 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5488 | 	      # If there is no dlopen support or we're linking statically,
5518 | 	dlopen=
5548 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5588 | 	# This library was specified with -dlopen.
5589 | 	if test "$pass" = dlopen; then
5591 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5594 | 	     test "$dlopen_support" != yes ||
5596 | 	    # If there is no dlname, no dlopen support or we're linking
5605 | 	fi # $pass = dlopen
5663 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5789 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5790 | 	  dlopenmodule=""
5793 | 	      dlopenmodule="$dlpremoduletest"
5797 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5894 | 		    # if the lib is a (non-dlopened) module then we can not
5898 | 		      if test "X$dlopenmodule" != "X$lib"; then
6050 | 	      echo "*** a static module, that should work as long as the dlopening application"
6051 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
6187 |       if test "$pass" != dlopen; then
6286 | 	func_warning "\`-dlopen' is ignored for archives"
6353 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7015 | 	    echo "*** a static module, that should work as long as the dlopening"
7016 | 	    echo "*** application is linked with the -dlopen flag."
7034 | 	    echo "*** or is declared to -dlopen it."
7607 | 	func_warning "\`-dlopen' is ignored for objects"
7722 |         && test "$dlopen_support" = unknown \
7723 | 	&& test "$dlopen_self" = unknown \
7724 | 	&& test "$dlopen_self_static" = unknown && \
7725 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8364 | # The name that we can dlopen(3).
8393 | # Files to dlopen/dlpreopen
8394 | dlopen='$dlfiles'
{% endraw %}

```
### config/plugins.m4

```

{% raw %}
12 | 	   AC_MSG_ERROR([Building with plugin support requires a host that supports dlopen.])
{% endraw %}

```
### config/tcl.m4

```

{% raw %}
1032 |     AC_CHECK_LIB(dl, dlopen, have_dl=yes, have_dl=no)
1772 | 	    # dlopen is in -lc on QNX
1789 | 	    # Note, dlopen is available only on SCO 3.2.5 and greater. However,
{% endraw %}

```
### config/gcc-plugin.m4

```

{% raw %}
84 |      AC_SEARCH_LIBS([dlopen], [dl])
85 |      if test x"$ac_cv_search_dlopen" = x"-ldl"; then
109 |      if test x"$have_pic_shared" != x"yes" -o x"$ac_cv_search_dlopen" = x"no"; then
{% endraw %}

```
### config/lib-link.m4

```

{% raw %}
377 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### elfcpp/elfcpp.h

```cpp

{% raw %}
867 |   // Default suffix of DSO to be added by rld on dlopen() calls.
{% endraw %}

```
### include/gcc-c-interface.h

```cpp

{% raw %}
187 | /* The name of the .so that the compiler builds.  We dlopen this
{% endraw %}

```
### include/gcc-cp-interface.h

```cpp

{% raw %}
472 | /* The name of the .so that the compiler builds.  We dlopen this
{% endraw %}

```
### include/elf/mips.h

```cpp

{% raw %}
739 | /* Default suffix of DSO to be added by rld on dlopen() calls.  */
{% endraw %}

```
### include/aout/sun4.h

```cpp

{% raw %}
90 |      ld.so and probably by dlopen.  */
{% endraw %}

```
### bfd/elf32-frv.c

```cpp

{% raw %}
4473 |      suitable for dlopening.  This mark will remain even if we relax
4476 |      dlopening executables.  */
5650 |      that can't be dlopened.  */
{% endraw %}

```
### bfd/configure.ac

```

{% raw %}
41 | LT_INIT([dlopen])
1061 | AC_SUBST(lt_cv_dlopen_libs)
{% endraw %}

```
### bfd/elf64-ppc.c

```cpp

{% raw %}
8478 |      An app that "cleverly" uses dlopen to only load necessary
{% endraw %}

```
### bfd/Makefile.am

```

{% raw %}
58 | LIBDL = @lt_cv_dlopen_libs@
{% endraw %}

```
### bfd/plugin.c

```cpp

{% raw %}
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
227 |   plugin_handle = dlopen (pname, RTLD_NOW);
{% endraw %}

```
### bfd/Makefile.in

```

{% raw %}
431 | lt_cv_dlopen_libs = @lt_cv_dlopen_libs@
482 | @PLUGINS_TRUE@LIBDL = @lt_cv_dlopen_libs@
{% endraw %}

```
### bfd/doc/Makefile.in

```

{% raw %}
369 | lt_cv_dlopen_libs = @lt_cv_dlopen_libs@
{% endraw %}

```
### intl/libgnuintl.h

```cpp

{% raw %}
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
81 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### gold/plugin.h

```cpp

{% raw %}
125 |   // The shared library handle returned by dlopen.
{% endraw %}

```
### gold/layout.cc

```cpp

{% raw %}
5340 |   if (parameters->options().nodlopen())
{% endraw %}

```
### gold/configure.ac

```

{% raw %}
608 | AC_SEARCH_LIBS(dlopen, [dl dld])
609 | case "$ac_cv_search_dlopen" in
610 |   no*) DLOPEN_LIBS="";;
611 |   *)   DLOPEN_LIBS="$ac_cv_search_dlopen";;
613 | AC_SUBST(DLOPEN_LIBS)
{% endraw %}

```
### gold/options.h

```cpp

{% raw %}
1479 |   DEFINE_bool(nodlopen, options::DASH_Z, '\0', false,
1480 | 	      N_("Mark DSO not available to dlopen"),
{% endraw %}

```
### gold/plugin.cc

```cpp

{% raw %}
47 | dlopen(const char *file, int mode ATTRIBUTE_UNUSED)
198 |   this->handle_ = dlopen(this->filename_.c_str(), RTLD_NOW);
{% endraw %}

```
### gold/po/zh_CN.po

```

{% raw %}
2743 | msgid "Mark DSO not available to dlopen"
{% endraw %}

```
### gold/po/uk.po

```

{% raw %}
3143 | msgid "Mark DSO not available to dlopen"
3144 | msgstr "позначити DSO як такий, що недоступний для dlopen"
{% endraw %}

```
### gold/po/es.po

```

{% raw %}
3102 | msgid "Mark DSO not available to dlopen"
3103 | msgstr "Marca el DSO como no disponible para dlopen"
{% endraw %}

```
### gold/po/vi.po

```

{% raw %}
1737 | msgid "Mark DSO not available to dlopen"
1738 | msgstr "Đánh dấu DSO không sẵn sàng cho dlopen"
{% endraw %}

```
### gold/po/gold.pot

```

{% raw %}
3187 | msgid "Mark DSO not available to dlopen"
{% endraw %}

```
### gold/po/sv.po

```

{% raw %}
2684 | msgid "Mark DSO not available to dlopen"
{% endraw %}

```
### gold/po/fi.po

```

{% raw %}
2594 | msgid "Mark DSO not available to dlopen"
2595 | msgstr "Merkitse, että dynaamisesti jaettu objekti ei ole saatavilla funktiolle dlopen"
{% endraw %}

```
### gold/po/it.po

```

{% raw %}
1720 | msgid "Mark DSO not available to dlopen"
1721 | msgstr "Marca DSO come non disponibile per dlopen"
{% endraw %}

```
### gold/po/ja.po

```

{% raw %}
1713 | msgid "Mark DSO not available to dlopen"
{% endraw %}

```
### gold/po/fr.po

```

{% raw %}
3147 | msgid "Mark DSO not available to dlopen"
3148 | msgstr "Marquer le DSO comme non disponible pour dlopen()"
{% endraw %}

```
### gold/po/id.po

```

{% raw %}
1719 | msgid "Mark DSO not available to dlopen"
1720 | msgstr "Tandai DSO tidak tersedia di dlopen"
{% endraw %}

```
### gold/testsuite/ifuncmod3.c

```cpp

{% raw %}
0 | /* Test STT_GNU_IFUNC symbols with dlopen.  */
{% endraw %}

```
### gold/testsuite/ifuncmain3.c

```cpp

{% raw %}
0 | /* Test STT_GNU_IFUNC symbols with dlopen:
45 |   void *h = dlopen ("ifuncmod3.so", RTLD_LAZY);
{% endraw %}

```
### ld/ld.texi

```

{% raw %}
514 | If you use @code{dlopen} to load a dynamic object which needs to refer
1206 | @item nodlopen
1207 | Specify that the object is not available to @code{dlopen}.
1231 | when the shared library is loaded by dlopen, instead of deferring
{% endraw %}

```
### ld/configure.ac

```

{% raw %}
266 | AC_SEARCH_LIBS([dlopen], [dl])
{% endraw %}

```
### ld/ld.1

```

{% raw %}
412 | If you use \f(CW\*(C`dlopen\*(C'\fR to load a dynamic object which needs to refer
1079 | .IP "\fBnodlopen\fR" 4
1080 | .IX Item "nodlopen"
1081 | Specify that the object is not available to \f(CW\*(C`dlopen\*(C'\fR.
1105 | when the shared library is loaded by dlopen, instead of deferring
{% endraw %}

```
### ld/lexsup.c

```cpp

{% raw %}
1779 |   -z nodlopen                 Mark DSO not available to dlopen\n"));
{% endraw %}

```
### ld/plugin.c

```cpp

{% raw %}
77 |   /* The shared library handle returned by dlopen.  */
183 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
243 |   newplug->dlhandle = dlopen (plugin, RTLD_NOW);
{% endraw %}

```
### ld/ld.info

```

{% raw %}
305 |      If you use 'dlopen' to load a dynamic object which needs to refer
873 |      'nodlopen'
874 |           Specify that the object is not available to 'dlopen'.
899 |           dlopen, instead of deferring function call resolution to the
{% endraw %}

```
### ld/po/uk.po

```

{% raw %}
2070 | msgid "  -z nodlopen                 Mark DSO not available to dlopen\n"
2071 | msgstr "  -z nodlopen                 позначити DSO як недоступний для dlopen\n"
{% endraw %}

```
### ld/po/ld.pot

```

{% raw %}
2043 | msgid "  -z nodlopen                 Mark DSO not available to dlopen\n"
{% endraw %}

```
### ld/po/es.po

```

{% raw %}
2078 | msgid "  -z nodlopen                 Mark DSO not available to dlopen\n"
2079 | msgstr "  -z nodlopen                 Indica que el DSO no está disponible para dlopen\n"
{% endraw %}

```
### ld/po/bg.po

```

{% raw %}
2061 | msgid "  -z nodlopen                 Mark DSO not available to dlopen\n"
{% endraw %}

```
### ld/po/tr.po

```

{% raw %}
2393 | msgid "  -z nodlopen                 Mark DSO not available to dlopen\n"
{% endraw %}

```
### ld/po/pt_BR.po

```

{% raw %}
2233 | msgid "  -z nodlopen                 Mark DSO not available to dlopen\n"
2234 | msgstr "  -z nodlopen                 Marca o DSO como não disponível para dlopen\n"
{% endraw %}

```
### ld/emultempl/elf32.em

```

{% raw %}
2792 |       else if (strcmp (optarg, "nodlopen") == 0)
{% endraw %}

```
### ld/testsuite/lib/ld-lib.exp

```

{% raw %}
2229 | 	puts $f "  dlopen (\"dummy.so\", RTLD_NOW);"
{% endraw %}

```
### ld/testsuite/ld-elf/dl1main.c

```cpp

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl1.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl1.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6dmain.c

```cpp

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6d.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6d.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6bmain.c

```cpp

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6b.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6b.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/shared.exp

```

{% raw %}
902 | # These tests require dlopen support.
903 | set dlopen_run_tests [list \
904 |     [list "Run dl1a with --dynamic-list=dl1.list and dlopen on libdl1.so" \
907 |     [list "Run dl1b with --dynamic-list-data and dlopen on libdl1.so" \
910 |     [list "Run dl6a1 with --dynamic-list-data and dlopen on libdl6a.so" \
913 |     [list "Run dl6a2 with -Bsymbolic-functions and dlopen on libdl6a.so" \
916 |     [list "Run dl6a3 with -Bsymbolic and dlopen on libdl6a.so" \
919 |     [list "Run dl6a4 with -Bsymbolic --dynamic-list-data and dlopen on libdl6a.so" \
922 |     [list "Run dl6a5 with -Bsymbolic-functions --dynamic-list-cpp-new and dlopen on libdl6a.so" \
925 |     [list "Run dl6a6 with --dynamic-list-cpp-new -Bsymbolic-functions and dlopen on libdl6a.so" \
928 |     [list "Run dl6a7 with --dynamic-list-data -Bsymbolic and dlopen on libdl6a.so" \
931 |     [list "Run dl6b1 with --dynamic-list-data and dlopen on libdl6b.so" \
934 |     [list "Run dl6b2 with dlopen on libdl6b.so" \
937 |     [list "Run dl6c1 with --dynamic-list-data and dlopen on libdl6c.so" \
940 |     [list "Run dl6d1 with --dynamic-list-data and dlopen on libdl6d.so" \
955 |   run_ld_link_exec_tests $dlopen_run_tests "*-*-netbsdelf*"
{% endraw %}

```
### ld/testsuite/ld-elf/dl6amain.c

```cpp

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6a.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6a.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6cmain.c

```cpp

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6c.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6c.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-2c.c

```cpp

{% raw %}
14 |   dl = dlopen("pr21964-2b.so", RTLD_LAZY);
{% endraw %}

```
### ld/testsuite/ld-plugin/plugin.exp

```

{% raw %}
38 | # Look for the name we can dlopen in the test plugin's libtool control script.
{% endraw %}

```