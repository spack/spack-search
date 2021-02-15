---
name: "aspell"
layout: package
next_package: gmp
previous_package: perl-dbd-sqlite
languages: ['cpp', 'bash']
---
## 0.60.6.1
35 / 535 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [common/errors.hpp](#commonerrorshpp)
 - [common/errors.cpp](#commonerrorscpp)
 - [lib/find_speller.cpp](#libfind_spellercpp)
 - [interfaces/cc/aspell.h](#interfacesccaspellh)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [po/cs.po](#pocspo)
 - [po/zh_CN.po](#pozh_cnpo)
 - [po/uk.po](#poukpo)
 - [po/sk.po](#poskpo)
 - [po/sr.po](#posrpo)
 - [po/rw.po](#porwpo)
 - [po/ms.po](#pomspo)
 - [po/ca.po](#pocapo)
 - [po/nl.po](#ponlpo)
 - [po/ga.po](#pogapo)
 - [po/vi.po](#povipo)
 - [po/sl.po](#poslpo)
 - [po/sv.po](#posvpo)
 - [po/aspell.pot](#poaspellpot)
 - [po/fi.po](#pofipo)
 - [po/tg.po](#potgpo)
 - [po/en_GB.po](#poen_gbpo)
 - [po/ast.po](#poastpo)
 - [po/ja.po](#pojapo)
 - [po/wa.po](#powapo)
 - [po/id.po](#poidpo)
 - [po/be.po](#pobepo)
 - [po/mn.po](#pomnpo)
 - [po/de.po](#podepo)
 - [po/da.po](#podapo)
 - [auto/mk-src.in](#automk-srcin)

### configure.ac

```

{% raw %}
94 | AC_LIBTOOL_DLOPEN
100 | AC_CHECK_FUNC(dlopen,,
101 |               AC_CHECK_LIB(dl, dlopen,,[enable_compile_in_filters=yes]))
166 | AC_CHECK_LIB(dl, dlopen)
{% endraw %}

```
### ltmain.sh

```bash

{% raw %}
716 |   -dlopen FILE      add the directory containing FILE to the library path
718 | This mode sets the library path environment variable according to \`-dlopen'
771 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
780 |   -module           build a library that can dlopened
888 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
938 |       -dlopen=*|--mode=*|--tag=*)
1029 |   # Only execute mode is allowed to have -dlopen flags.
1031 |     func_error "unrecognized option \`-dlopen'"
2033 |     # Handle -dlopen flags immediately.
2050 | 	# Skip this library if it cannot be dlopened.
2077 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
3580 | 	    dlopen_self=$dlopen_self_static
3589 | 	    dlopen_self=$dlopen_self_static
3595 | 	    dlopen_self=$dlopen_self_static
3648 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
3732 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3885 |       -dlopen)
4263 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4330 | 	  # This library was specified with -dlopen.
4445 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
4456 | 	passes="conv scan dlopen dlpreopen link"
4482 | 	dlopen) libs="$dlfiles" ;;
4508 |       if test "$pass" = dlopen; then
4720 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
4721 | 	      # If there is no dlopen support or we're linking statically,
4751 | 	dlopen=
4781 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
4821 | 	# This library was specified with -dlopen.
4822 | 	if test "$pass" = dlopen; then
4824 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
4827 | 	     test "$dlopen_support" != yes ||
4829 | 	    # If there is no dlname, no dlopen support or we're linking
4838 | 	fi # $pass = dlopen
4896 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5022 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5023 | 	  dlopenmodule=""
5026 | 	      dlopenmodule="$dlpremoduletest"
5030 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5126 | 		    # if the lib is a (non-dlopened) module then we can not
5130 | 		      if test "X$dlopenmodule" != "X$lib"; then
5282 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5283 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5420 |       if test "$pass" != dlopen; then
5519 | 	func_warning "\`-dlopen' is ignored for archives"
5586 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6224 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6225 | 	    $ECHO "*** application is linked with the -dlopen flag."
6243 | 	    $ECHO "*** or is declared to -dlopen it."
6799 | 	func_warning "\`-dlopen' is ignored for objects"
6914 |         && test "$dlopen_support" = unknown \
6915 | 	&& test "$dlopen_self" = unknown \
6916 | 	&& test "$dlopen_self_static" = unknown && \
6917 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
7536 | # The name that we can dlopen(3).
7565 | # Files to dlopen/dlpreopen
7566 | dlopen='$dlfiles'
{% endraw %}

```
### common/errors.hpp

```

{% raw %}
72 | extern "C" const ErrorInfo * const   aerror_cant_dlopen_file;
159 | static const ErrorInfo * const   cant_dlopen_file = aerror_cant_dlopen_file;
{% endraw %}

```
### common/errors.cpp

```

{% raw %}
464 | static const ErrorInfo aerror_cant_dlopen_file_obj = {
466 |   N_("dlopen returned \"%return:1\"."), // mesg
470 | extern "C" const ErrorInfo * const aerror_cant_dlopen_file = &aerror_cant_dlopen_file_obj;
{% endraw %}

```
### lib/find_speller.cpp

```

{% raw %}
77 |     lt_dlhandle h = lt_dlopen (libname.c_str());
{% endraw %}

```
### interfaces/cc/aspell.h

```cpp

{% raw %}
295 | extern const struct AspellErrorInfo * const   aerror_cant_dlopen_file;
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1621 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1624 | m4_defun([_LT_TRY_DLOPEN_SELF],
1680 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1709 | ])# _LT_TRY_DLOPEN_SELF
1712 | # LT_SYS_DLOPEN_SELF
1714 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1716 | if test "x$enable_dlopen" != xyes; then
1717 |   enable_dlopen=unknown
1718 |   enable_dlopen_self=unknown
1719 |   enable_dlopen_self_static=unknown
1721 |   lt_cv_dlopen=no
1722 |   lt_cv_dlopen_libs=
1726 |     lt_cv_dlopen="load_add_on"
1727 |     lt_cv_dlopen_libs=
1728 |     lt_cv_dlopen_self=yes
1732 |     lt_cv_dlopen="LoadLibrary"
1733 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen="dlopen"
1738 |     lt_cv_dlopen_libs=
1743 |     AC_CHECK_LIB([dl], [dlopen],
1744 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1745 |     lt_cv_dlopen="dyld"
1746 |     lt_cv_dlopen_libs=
1747 |     lt_cv_dlopen_self=yes
1753 | 	  [lt_cv_dlopen="shl_load"],
1755 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1756 | 	[AC_CHECK_FUNC([dlopen],
1757 | 	      [lt_cv_dlopen="dlopen"],
1758 | 	  [AC_CHECK_LIB([dl], [dlopen],
1759 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1760 | 	    [AC_CHECK_LIB([svld], [dlopen],
1761 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1763 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1772 |   if test "x$lt_cv_dlopen" != xno; then
1773 |     enable_dlopen=yes
1775 |     enable_dlopen=no
1778 |   case $lt_cv_dlopen in
1779 |   dlopen)
1787 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1789 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1790 | 	  lt_cv_dlopen_self, [dnl
1791 | 	  _LT_TRY_DLOPEN_SELF(
1792 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1793 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1796 |     if test "x$lt_cv_dlopen_self" = xyes; then
1798 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1799 | 	  lt_cv_dlopen_self_static, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1802 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1812 |   case $lt_cv_dlopen_self in
1813 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1814 |   *) enable_dlopen_self=unknown ;;
1817 |   case $lt_cv_dlopen_self_static in
1818 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1819 |   *) enable_dlopen_self_static=unknown ;;
1822 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1823 | 	 [Whether dlopen is supported])
1824 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1825 | 	 [Whether dlopen of programs is supported])
1826 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1827 | 	 [Whether dlopen of statically linked programs is supported])
1828 | ])# LT_SYS_DLOPEN_SELF
1831 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1833 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5111 |     [Compiler flag to allow reflexive dlopens])
5227 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### m4/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
394 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### po/cs.po

```

{% raw %}
547 | msgid "dlopen returned \"%return:1\"."
548 | msgstr "dlopen vrátilo \"%return:1\"."
{% endraw %}

```
### po/zh_CN.po

```

{% raw %}
534 | msgid "dlopen returned \"%return:1\"."
535 | msgstr "dlopen 返回了“%return:1”。"
{% endraw %}

```
### po/uk.po

```

{% raw %}
551 | msgid "dlopen returned \"%return:1\"."
552 | msgstr "dlopen повернув \"%return:1\"."
{% endraw %}

```
### po/sk.po

```

{% raw %}
555 | msgid "dlopen returned \"%return:1\"."
556 | msgstr "dlopen vrátil \"%return:1\"."
{% endraw %}

```
### po/sr.po

```

{% raw %}
552 | msgid "dlopen returned \"%return:1\"."
553 | msgstr "%where:1: \"%filter:2\" dlopen је вратио \"%return:3\"."
{% endraw %}

```
### po/rw.po

```

{% raw %}
638 | msgid "dlopen returned \"%return:1\"."
{% endraw %}

```
### po/ms.po

```

{% raw %}
543 | msgid "dlopen returned \"%return:1\"."
{% endraw %}

```
### po/ca.po

```

{% raw %}
553 | msgid "dlopen returned \"%return:1\"."
554 | msgstr "dlopen ha tornat «%return:1»."
{% endraw %}

```
### po/nl.po

```

{% raw %}
556 | msgid "dlopen returned \"%return:1\"."
557 | msgstr "dlopen() gaf \"%return:1\" terug."
{% endraw %}

```
### po/ga.po

```

{% raw %}
559 | msgid "dlopen returned \"%return:1\"."
560 | msgstr "D'aisfhill dlopen \"%return:1\"."
{% endraw %}

```
### po/vi.po

```

{% raw %}
556 | msgid "dlopen returned \"%return:1\"."
557 | msgstr "lệnh dlopen đã trả lời « %return:1 »."
{% endraw %}

```
### po/sl.po

```

{% raw %}
556 | msgid "dlopen returned \"%return:1\"."
557 | msgstr "dlopen je vrnil \"%return:1\"."
{% endraw %}

```
### po/sv.po

```

{% raw %}
543 | msgid "dlopen returned \"%return:1\"."
{% endraw %}

```
### po/aspell.pot

```

{% raw %}
534 | msgid "dlopen returned \"%return:1\"."
{% endraw %}

```
### po/fi.po

```

{% raw %}
556 | msgid "dlopen returned \"%return:1\"."
557 | msgstr "dlopen palautti ”%return:1”."
{% endraw %}

```
### po/tg.po

```

{% raw %}
566 | msgid "dlopen returned \"%return:1\"."
567 | msgstr "%where:1: \"%filter:2\" dlopen гардонид \"%return:3\"-ро."
{% endraw %}

```
### po/en_GB.po

```

{% raw %}
558 | msgid "dlopen returned \"%return:1\"."
559 | msgstr "dlopen returned \"%return:1\"."
{% endraw %}

```
### po/ast.po

```

{% raw %}
559 | msgid "dlopen returned \"%return:1\"."
560 | msgstr "dlopen tornó «%return:1»."
{% endraw %}

```
### po/ja.po

```

{% raw %}
558 | msgid "dlopen returned \"%return:1\"."
559 | msgstr "dlopen が \"%return:1\" を返した。"
{% endraw %}

```
### po/wa.po

```

{% raw %}
541 | msgid "dlopen returned \"%return:1\"."
542 | msgstr "dlopen() a rtourné «%return:1»."
{% endraw %}

```
### po/id.po

```

{% raw %}
556 | msgid "dlopen returned \"%return:1\"."
557 | msgstr "dlopen mengembalikan \"%return:1\"."
{% endraw %}

```
### po/be.po

```

{% raw %}
555 | msgid "dlopen returned \"%return:1\"."
556 | msgstr "%where:1: \"%filter:2\" dlopen вярнула \"%return:3\"."
{% endraw %}

```
### po/mn.po

```

{% raw %}
570 | msgid "dlopen returned \"%return:1\"."
571 | msgstr "dlopen \"%return:1\" буцаалаа."
{% endraw %}

```
### po/de.po

```

{% raw %}
559 | msgid "dlopen returned \"%return:1\"."
560 | msgstr "dlopen gab »%return:1« zurück."
{% endraw %}

```
### po/da.po

```

{% raw %}
565 | msgid "dlopen returned \"%return:1\"."
566 | msgstr "systemkaldet dlopen returnerede »%return:1«."
{% endraw %}

```
### auto/mk-src.in

```

{% raw %}
529 | 		cant dlopen file
530 | 			mesg => dlopen returned "%return".
{% endraw %}

```