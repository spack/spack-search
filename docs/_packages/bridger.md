---
name: "bridger"
layout: package
next_package: sosflow
previous_package: udunits
languages: ['bash']
---
## 2014-12-01
15 / 1865 files match

 - [config.status](#configstatus)
 - [autom4te.cache/output.3](#autom4tecacheoutput3)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.7](#autom4tecacheoutput7)
 - [autom4te.cache/traces.3](#autom4tecachetraces3)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/output.5](#autom4tecacheoutput5)
 - [autom4te.cache/traces.8t](#autom4tecachetraces8t)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [autom4te.cache/traces.5](#autom4tecachetraces5)
 - [autom4te.cache/traces.4](#autom4tecachetraces4)
 - [autom4te.cache/output.4](#autom4tecacheoutput4)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### config.status

```

{% raw %}
587 | enable_dlopen='unknown'
588 | enable_dlopen_self='unknown'
589 | enable_dlopen_self_static='unknown'
1745 | # Whether dlopen is supported.
1746 | dlopen_support=$enable_dlopen
1748 | # Whether dlopen of programs is supported.
1749 | dlopen_self=$enable_dlopen_self
1751 | # Whether dlopen of statically linked programs is supported.
1752 | dlopen_self_static=$enable_dlopen_self_static
1792 | # Compiler flag to allow reflexive dlopens.
2177 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.3

```

{% raw %}
8641 |         enable_dlopen=no
11839 |   if test "x$enable_dlopen" != xyes; then
11840 |   enable_dlopen=unknown
11841 |   enable_dlopen_self=unknown
11842 |   enable_dlopen_self_static=unknown
11844 |   lt_cv_dlopen=no
11845 |   lt_cv_dlopen_libs=
11849 |     lt_cv_dlopen="load_add_on"
11850 |     lt_cv_dlopen_libs=
11851 |     lt_cv_dlopen_self=yes
11855 |     lt_cv_dlopen="LoadLibrary"
11856 |     lt_cv_dlopen_libs=
11860 |     lt_cv_dlopen="dlopen"
11861 |     lt_cv_dlopen_libs=
11866 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11867 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11868 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11886 | char dlopen ();
11890 | return dlopen ();
11916 |   ac_cv_lib_dl_dlopen=yes
11921 | 	ac_cv_lib_dl_dlopen=no
11929 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11930 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11931 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11932 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11935 |     lt_cv_dlopen="dyld"
11936 |     lt_cv_dlopen_libs=
11937 |     lt_cv_dlopen_self=yes
12030 |   lt_cv_dlopen="shl_load"
12098 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
12100 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
12101 | $as_echo_n "checking for dlopen... " >&6; }
12102 | if test "${ac_cv_func_dlopen+set}" = set; then
12111 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
12113 | #define dlopen innocuous_dlopen
12116 |     which can conflict with char dlopen (); below.
12126 | #undef dlopen
12134 | char dlopen ();
12138 | #if defined __stub_dlopen || defined __stub___dlopen
12145 | return dlopen ();
12171 |   ac_cv_func_dlopen=yes
12176 | 	ac_cv_func_dlopen=no
12183 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
12184 | $as_echo "$ac_cv_func_dlopen" >&6; }
12185 | if test "x$ac_cv_func_dlopen" = x""yes; then
12186 |   lt_cv_dlopen="dlopen"
12188 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12189 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12190 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12208 | char dlopen ();
12212 | return dlopen ();
12238 |   ac_cv_lib_dl_dlopen=yes
12243 | 	ac_cv_lib_dl_dlopen=no
12251 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12252 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12253 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
12254 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12256 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
12257 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12258 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
12276 | char dlopen ();
12280 | return dlopen ();
12306 |   ac_cv_lib_svld_dlopen=yes
12311 | 	ac_cv_lib_svld_dlopen=no
12319 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
12320 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12321 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
12322 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12390 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12411 |   if test "x$lt_cv_dlopen" != xno; then
12412 |     enable_dlopen=yes
12414 |     enable_dlopen=no
12417 |   case $lt_cv_dlopen in
12418 |   dlopen)
12426 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12428 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12429 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12430 | if test "${lt_cv_dlopen_self+set}" = set; then
12434 |   lt_cv_dlopen_self=cross
12483 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12506 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12507 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12508 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12512 |     lt_cv_dlopen_self=no
12519 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12520 | $as_echo "$lt_cv_dlopen_self" >&6; }
12522 |     if test "x$lt_cv_dlopen_self" = xyes; then
12524 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12525 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12526 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12530 |   lt_cv_dlopen_self_static=cross
12579 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12602 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12603 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12604 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12608 |     lt_cv_dlopen_self_static=no
12615 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
12616 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12625 |   case $lt_cv_dlopen_self in
12626 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12627 |   *) enable_dlopen_self=unknown ;;
12630 |   case $lt_cv_dlopen_self_static in
12631 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12632 |   *) enable_dlopen_self_static=unknown ;;
17941 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
17942 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
17943 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
19227 | # Whether dlopen is supported.
19228 | dlopen_support=$enable_dlopen
19230 | # Whether dlopen of programs is supported.
19231 | dlopen_self=$enable_dlopen_self
19233 | # Whether dlopen of statically linked programs is supported.
19234 | dlopen_self_static=$enable_dlopen_self_static
19274 | # Compiler flag to allow reflexive dlopens.
19659 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.0

```

{% raw %}
8215 |         enable_dlopen=no
11427 |   if test "x$enable_dlopen" != xyes; then
11428 |   enable_dlopen=unknown
11429 |   enable_dlopen_self=unknown
11430 |   enable_dlopen_self_static=unknown
11432 |   lt_cv_dlopen=no
11433 |   lt_cv_dlopen_libs=
11437 |     lt_cv_dlopen="load_add_on"
11438 |     lt_cv_dlopen_libs=
11439 |     lt_cv_dlopen_self=yes
11443 |     lt_cv_dlopen="LoadLibrary"
11444 |     lt_cv_dlopen_libs=
11448 |     lt_cv_dlopen="dlopen"
11449 |     lt_cv_dlopen_libs=
11454 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11455 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11456 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11474 | char dlopen ();
11478 | return dlopen ();
11504 |   ac_cv_lib_dl_dlopen=yes
11509 | 	ac_cv_lib_dl_dlopen=no
11517 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11518 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11519 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11520 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11523 |     lt_cv_dlopen="dyld"
11524 |     lt_cv_dlopen_libs=
11525 |     lt_cv_dlopen_self=yes
11618 |   lt_cv_dlopen="shl_load"
11686 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11688 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
11689 | $as_echo_n "checking for dlopen... " >&6; }
11690 | if test "${ac_cv_func_dlopen+set}" = set; then
11699 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
11701 | #define dlopen innocuous_dlopen
11704 |     which can conflict with char dlopen (); below.
11714 | #undef dlopen
11722 | char dlopen ();
11726 | #if defined __stub_dlopen || defined __stub___dlopen
11733 | return dlopen ();
11759 |   ac_cv_func_dlopen=yes
11764 | 	ac_cv_func_dlopen=no
11771 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
11772 | $as_echo "$ac_cv_func_dlopen" >&6; }
11773 | if test "x$ac_cv_func_dlopen" = x""yes; then
11774 |   lt_cv_dlopen="dlopen"
11776 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11777 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11778 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11796 | char dlopen ();
11800 | return dlopen ();
11826 |   ac_cv_lib_dl_dlopen=yes
11831 | 	ac_cv_lib_dl_dlopen=no
11839 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11840 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11841 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11842 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11844 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
11845 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11846 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
11864 | char dlopen ();
11868 | return dlopen ();
11894 |   ac_cv_lib_svld_dlopen=yes
11899 | 	ac_cv_lib_svld_dlopen=no
11907 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
11908 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11909 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
11910 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
11978 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
11999 |   if test "x$lt_cv_dlopen" != xno; then
12000 |     enable_dlopen=yes
12002 |     enable_dlopen=no
12005 |   case $lt_cv_dlopen in
12006 |   dlopen)
12014 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12016 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12017 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12018 | if test "${lt_cv_dlopen_self+set}" = set; then
12022 |   lt_cv_dlopen_self=cross
12071 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12094 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12095 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12096 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12100 |     lt_cv_dlopen_self=no
12107 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12108 | $as_echo "$lt_cv_dlopen_self" >&6; }
12110 |     if test "x$lt_cv_dlopen_self" = xyes; then
12112 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12113 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12114 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12118 |   lt_cv_dlopen_self_static=cross
12167 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12190 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12191 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12192 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12196 |     lt_cv_dlopen_self_static=no
12203 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
12204 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12213 |   case $lt_cv_dlopen_self in
12214 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12215 |   *) enable_dlopen_self=unknown ;;
12218 |   case $lt_cv_dlopen_self_static in
12219 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12220 |   *) enable_dlopen_self_static=unknown ;;
19076 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
19077 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
19078 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
20362 | # Whether dlopen is supported.
20363 | dlopen_support=$enable_dlopen
20365 | # Whether dlopen of programs is supported.
20366 | dlopen_self=$enable_dlopen_self
20368 | # Whether dlopen of statically linked programs is supported.
20369 | dlopen_self_static=$enable_dlopen_self_static
20409 | # Compiler flag to allow reflexive dlopens.
20794 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.7

```

{% raw %}
8795 |         enable_dlopen=no
11993 |   if test "x$enable_dlopen" != xyes; then
11994 |   enable_dlopen=unknown
11995 |   enable_dlopen_self=unknown
11996 |   enable_dlopen_self_static=unknown
11998 |   lt_cv_dlopen=no
11999 |   lt_cv_dlopen_libs=
12003 |     lt_cv_dlopen="load_add_on"
12004 |     lt_cv_dlopen_libs=
12005 |     lt_cv_dlopen_self=yes
12009 |     lt_cv_dlopen="LoadLibrary"
12010 |     lt_cv_dlopen_libs=
12014 |     lt_cv_dlopen="dlopen"
12015 |     lt_cv_dlopen_libs=
12020 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12021 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12022 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12040 | char dlopen ();
12044 | return dlopen ();
12070 |   ac_cv_lib_dl_dlopen=yes
12075 | 	ac_cv_lib_dl_dlopen=no
12083 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12084 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12085 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
12086 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12089 |     lt_cv_dlopen="dyld"
12090 |     lt_cv_dlopen_libs=
12091 |     lt_cv_dlopen_self=yes
12184 |   lt_cv_dlopen="shl_load"
12252 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
12254 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
12255 | $as_echo_n "checking for dlopen... " >&6; }
12256 | if test "${ac_cv_func_dlopen+set}" = set; then
12265 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
12267 | #define dlopen innocuous_dlopen
12270 |     which can conflict with char dlopen (); below.
12280 | #undef dlopen
12288 | char dlopen ();
12292 | #if defined __stub_dlopen || defined __stub___dlopen
12299 | return dlopen ();
12325 |   ac_cv_func_dlopen=yes
12330 | 	ac_cv_func_dlopen=no
12337 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
12338 | $as_echo "$ac_cv_func_dlopen" >&6; }
12339 | if test "x$ac_cv_func_dlopen" = x""yes; then
12340 |   lt_cv_dlopen="dlopen"
12342 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
12343 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
12344 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
12362 | char dlopen ();
12366 | return dlopen ();
12392 |   ac_cv_lib_dl_dlopen=yes
12397 | 	ac_cv_lib_dl_dlopen=no
12405 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
12406 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
12407 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
12408 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
12410 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
12411 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
12412 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
12430 | char dlopen ();
12434 | return dlopen ();
12460 |   ac_cv_lib_svld_dlopen=yes
12465 | 	ac_cv_lib_svld_dlopen=no
12473 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
12474 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
12475 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
12476 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12544 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12565 |   if test "x$lt_cv_dlopen" != xno; then
12566 |     enable_dlopen=yes
12568 |     enable_dlopen=no
12571 |   case $lt_cv_dlopen in
12572 |   dlopen)
12580 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12582 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12583 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12584 | if test "${lt_cv_dlopen_self+set}" = set; then
12588 |   lt_cv_dlopen_self=cross
12637 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12660 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12661 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12662 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12666 |     lt_cv_dlopen_self=no
12673 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12674 | $as_echo "$lt_cv_dlopen_self" >&6; }
12676 |     if test "x$lt_cv_dlopen_self" = xyes; then
12678 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12679 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12680 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12684 |   lt_cv_dlopen_self_static=cross
12733 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12756 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12757 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12758 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12762 |     lt_cv_dlopen_self_static=no
12769 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
12770 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12779 |   case $lt_cv_dlopen_self in
12780 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12781 |   *) enable_dlopen_self=unknown ;;
12784 |   case $lt_cv_dlopen_self_static in
12785 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12786 |   *) enable_dlopen_self_static=unknown ;;
19815 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
19816 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
19817 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
21102 | # Whether dlopen is supported.
21103 | dlopen_support=$enable_dlopen
21105 | # Whether dlopen of programs is supported.
21106 | dlopen_self=$enable_dlopen_self
21108 | # Whether dlopen of statically linked programs is supported.
21109 | dlopen_self_static=$enable_dlopen_self_static
21149 | # Compiler flag to allow reflexive dlopens.
21534 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.3

```

{% raw %}
438 | m4trace:/usr/share/aclocal/libtool.m4:1724: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
439 | if test "x$enable_dlopen" != xyes; then
440 |   enable_dlopen=unknown
441 |   enable_dlopen_self=unknown
442 |   enable_dlopen_self_static=unknown
444 |   lt_cv_dlopen=no
445 |   lt_cv_dlopen_libs=
449 |     lt_cv_dlopen="load_add_on"
450 |     lt_cv_dlopen_libs=
451 |     lt_cv_dlopen_self=yes
455 |     lt_cv_dlopen="LoadLibrary"
456 |     lt_cv_dlopen_libs=
460 |     lt_cv_dlopen="dlopen"
461 |     lt_cv_dlopen_libs=
466 |     AC_CHECK_LIB([dl], [dlopen],
467 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
468 |     lt_cv_dlopen="dyld"
469 |     lt_cv_dlopen_libs=
470 |     lt_cv_dlopen_self=yes
476 | 	  [lt_cv_dlopen="shl_load"],
478 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
479 | 	[AC_CHECK_FUNC([dlopen],
480 | 	      [lt_cv_dlopen="dlopen"],
481 | 	  [AC_CHECK_LIB([dl], [dlopen],
482 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
483 | 	    [AC_CHECK_LIB([svld], [dlopen],
484 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
486 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
495 |   if test "x$lt_cv_dlopen" != xno; then
496 |     enable_dlopen=yes
498 |     enable_dlopen=no
501 |   case $lt_cv_dlopen in
502 |   dlopen)
510 |     LIBS="$lt_cv_dlopen_libs $LIBS"
512 |     AC_CACHE_CHECK([whether a program can dlopen itself],
513 | 	  lt_cv_dlopen_self, [dnl
514 | 	  _LT_TRY_DLOPEN_SELF(
515 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
516 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
519 |     if test "x$lt_cv_dlopen_self" = xyes; then
521 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
522 | 	  lt_cv_dlopen_self_static, [dnl
523 | 	  _LT_TRY_DLOPEN_SELF(
524 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
525 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
535 |   case $lt_cv_dlopen_self in
536 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
537 |   *) enable_dlopen_self=unknown ;;
540 |   case $lt_cv_dlopen_self_static in
541 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
542 |   *) enable_dlopen_self_static=unknown ;;
545 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
546 | 	 [Whether dlopen is supported])
547 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
548 | 	 [Whether dlopen of programs is supported])
549 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
550 | 	 [Whether dlopen of statically linked programs is supported])
552 | m4trace:/usr/share/aclocal/libtool.m4:1841: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
553 | m4trace:/usr/share/aclocal/libtool.m4:1841: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
555 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1014 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1052 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
1053 | AC_SUBST([LTDLOPEN])
1055 | m4trace:/usr/share/aclocal/ltdl.m4:437: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1056 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1057 |   [lt_cv_sys_dlopen_deplibs],
1058 |   [# PORTME does your system automatically load deplibs for dlopen?
1062 |   lt_cv_sys_dlopen_deplibs=unknown
1067 |     lt_cv_sys_dlopen_deplibs=unknown
1070 |     lt_cv_sys_dlopen_deplibs=yes
1075 |       lt_cv_sys_dlopen_deplibs=no
1082 |     lt_cv_sys_dlopen_deplibs=yes
1085 |     lt_cv_sys_dlopen_deplibs=yes
1089 |     lt_cv_sys_dlopen_deplibs=yes
1092 |     lt_cv_sys_dlopen_deplibs=yes
1095 |     lt_cv_sys_dlopen_deplibs=yes
1100 |     lt_cv_sys_dlopen_deplibs=unknown
1104 |     # at 6.2 and later dlopen does load deplibs.
1105 |     lt_cv_sys_dlopen_deplibs=yes
1108 |     lt_cv_sys_dlopen_deplibs=yes
1111 |     lt_cv_sys_dlopen_deplibs=yes
1114 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1117 |     lt_cv_sys_dlopen_deplibs=no
1120 |     # dlopen *does* load deplibs and with the right loader patch applied
1126 |     lt_cv_sys_dlopen_deplibs=unknown
1133 |     lt_cv_sys_dlopen_deplibs=yes
1136 |     lt_cv_sys_dlopen_deplibs=yes
1139 |     lt_cv_sys_dlopen_deplibs=yes
1142 |     libltdl_cv_sys_dlopen_deplibs=yes
1146 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
1147 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1148 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1151 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1152 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1154 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1213 | LIBADD_DLOPEN=
1214 | AC_SEARCH_LIBS([dlopen], [dl],
1217 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
1218 | 	  LIBADD_DLOPEN="-ldl"
1220 | 	libltdl_cv_lib_dl_dlopen="yes"
1221 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1225 |     ]], [[dlopen(0, 0);]])],
1228 | 	    libltdl_cv_func_dlopen="yes"
1229 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1230 | 	[AC_CHECK_LIB([svld], [dlopen],
1233 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
1234 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1235 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
1238 |   LIBS="$LIBS $LIBADD_DLOPEN"
1242 | AC_SUBST([LIBADD_DLOPEN])
1248 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1252 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1262 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1265 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1269 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1276 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1292 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1341 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
1342 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
1347 |           LIBS="$LIBS $LIBADD_DLOPEN"
1348 | 	  _LT_TRY_DLOPEN_SELF(
1366 | m4trace:/usr/share/aclocal/ltoptions.m4:110: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1369 | put the `dlopen' option into LT_INIT's first parameter.])
1371 | m4trace:/usr/share/aclocal/ltoptions.m4:110: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1373 | _LT_SET_OPTION([LT_INIT], [dlopen])
1376 | put the `dlopen' option into LT_INIT's first parameter.])
1468 | m4trace:/usr/share/aclocal/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2381 | m4trace:configure.ac:17: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
8278 |         enable_dlopen=no
11476 |   if test "x$enable_dlopen" != xyes; then
11477 |   enable_dlopen=unknown
11478 |   enable_dlopen_self=unknown
11479 |   enable_dlopen_self_static=unknown
11481 |   lt_cv_dlopen=no
11482 |   lt_cv_dlopen_libs=
11486 |     lt_cv_dlopen="load_add_on"
11487 |     lt_cv_dlopen_libs=
11488 |     lt_cv_dlopen_self=yes
11492 |     lt_cv_dlopen="LoadLibrary"
11493 |     lt_cv_dlopen_libs=
11497 |     lt_cv_dlopen="dlopen"
11498 |     lt_cv_dlopen_libs=
11503 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11504 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11505 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11523 | char dlopen ();
11527 | return dlopen ();
11553 |   ac_cv_lib_dl_dlopen=yes
11558 | 	ac_cv_lib_dl_dlopen=no
11566 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11567 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11568 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11569 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11572 |     lt_cv_dlopen="dyld"
11573 |     lt_cv_dlopen_libs=
11574 |     lt_cv_dlopen_self=yes
11667 |   lt_cv_dlopen="shl_load"
11735 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11737 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
11738 | $as_echo_n "checking for dlopen... " >&6; }
11739 | if test "${ac_cv_func_dlopen+set}" = set; then
11748 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
11750 | #define dlopen innocuous_dlopen
11753 |     which can conflict with char dlopen (); below.
11763 | #undef dlopen
11771 | char dlopen ();
11775 | #if defined __stub_dlopen || defined __stub___dlopen
11782 | return dlopen ();
11808 |   ac_cv_func_dlopen=yes
11813 | 	ac_cv_func_dlopen=no
11820 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
11821 | $as_echo "$ac_cv_func_dlopen" >&6; }
11822 | if test "x$ac_cv_func_dlopen" = x""yes; then
11823 |   lt_cv_dlopen="dlopen"
11825 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11826 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11827 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11845 | char dlopen ();
11849 | return dlopen ();
11875 |   ac_cv_lib_dl_dlopen=yes
11880 | 	ac_cv_lib_dl_dlopen=no
11888 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11889 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11890 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11891 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11893 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
11894 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11895 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
11913 | char dlopen ();
11917 | return dlopen ();
11943 |   ac_cv_lib_svld_dlopen=yes
11948 | 	ac_cv_lib_svld_dlopen=no
11956 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
11957 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11958 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
11959 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12027 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12048 |   if test "x$lt_cv_dlopen" != xno; then
12049 |     enable_dlopen=yes
12051 |     enable_dlopen=no
12054 |   case $lt_cv_dlopen in
12055 |   dlopen)
12063 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12065 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12066 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12067 | if test "${lt_cv_dlopen_self+set}" = set; then
12071 |   lt_cv_dlopen_self=cross
12120 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12143 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12144 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12145 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12149 |     lt_cv_dlopen_self=no
12156 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12157 | $as_echo "$lt_cv_dlopen_self" >&6; }
12159 |     if test "x$lt_cv_dlopen_self" = xyes; then
12161 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12162 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12163 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12167 |   lt_cv_dlopen_self_static=cross
12216 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12239 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12240 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12241 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12245 |     lt_cv_dlopen_self_static=no
12252 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
12253 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12262 |   case $lt_cv_dlopen_self in
12263 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12264 |   *) enable_dlopen_self=unknown ;;
12267 |   case $lt_cv_dlopen_self_static in
12268 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12269 |   *) enable_dlopen_self_static=unknown ;;
19569 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
19570 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
19571 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
20856 | # Whether dlopen is supported.
20857 | dlopen_support=$enable_dlopen
20859 | # Whether dlopen of programs is supported.
20860 | dlopen_self=$enable_dlopen_self
20862 | # Whether dlopen of statically linked programs is supported.
20863 | dlopen_self_static=$enable_dlopen_self_static
20903 | # Compiler flag to allow reflexive dlopens.
21288 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.5

```

{% raw %}
8313 |         enable_dlopen=no
11511 |   if test "x$enable_dlopen" != xyes; then
11512 |   enable_dlopen=unknown
11513 |   enable_dlopen_self=unknown
11514 |   enable_dlopen_self_static=unknown
11516 |   lt_cv_dlopen=no
11517 |   lt_cv_dlopen_libs=
11521 |     lt_cv_dlopen="load_add_on"
11522 |     lt_cv_dlopen_libs=
11523 |     lt_cv_dlopen_self=yes
11527 |     lt_cv_dlopen="LoadLibrary"
11528 |     lt_cv_dlopen_libs=
11532 |     lt_cv_dlopen="dlopen"
11533 |     lt_cv_dlopen_libs=
11538 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11539 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11540 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11558 | char dlopen ();
11562 | return dlopen ();
11588 |   ac_cv_lib_dl_dlopen=yes
11593 | 	ac_cv_lib_dl_dlopen=no
11601 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11602 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11603 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11604 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11607 |     lt_cv_dlopen="dyld"
11608 |     lt_cv_dlopen_libs=
11609 |     lt_cv_dlopen_self=yes
11702 |   lt_cv_dlopen="shl_load"
11770 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11772 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
11773 | $as_echo_n "checking for dlopen... " >&6; }
11774 | if test "${ac_cv_func_dlopen+set}" = set; then
11783 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
11785 | #define dlopen innocuous_dlopen
11788 |     which can conflict with char dlopen (); below.
11798 | #undef dlopen
11806 | char dlopen ();
11810 | #if defined __stub_dlopen || defined __stub___dlopen
11817 | return dlopen ();
11843 |   ac_cv_func_dlopen=yes
11848 | 	ac_cv_func_dlopen=no
11855 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
11856 | $as_echo "$ac_cv_func_dlopen" >&6; }
11857 | if test "x$ac_cv_func_dlopen" = x""yes; then
11858 |   lt_cv_dlopen="dlopen"
11860 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11861 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11862 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11880 | char dlopen ();
11884 | return dlopen ();
11910 |   ac_cv_lib_dl_dlopen=yes
11915 | 	ac_cv_lib_dl_dlopen=no
11923 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11924 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11925 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11926 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11928 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
11929 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11930 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
11948 | char dlopen ();
11952 | return dlopen ();
11978 |   ac_cv_lib_svld_dlopen=yes
11983 | 	ac_cv_lib_svld_dlopen=no
11991 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
11992 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11993 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
11994 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12062 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12083 |   if test "x$lt_cv_dlopen" != xno; then
12084 |     enable_dlopen=yes
12086 |     enable_dlopen=no
12089 |   case $lt_cv_dlopen in
12090 |   dlopen)
12098 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12100 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12101 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12102 | if test "${lt_cv_dlopen_self+set}" = set; then
12106 |   lt_cv_dlopen_self=cross
12155 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12178 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12179 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12180 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12184 |     lt_cv_dlopen_self=no
12191 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12192 | $as_echo "$lt_cv_dlopen_self" >&6; }
12194 |     if test "x$lt_cv_dlopen_self" = xyes; then
12196 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12197 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12198 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12202 |   lt_cv_dlopen_self_static=cross
12251 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12274 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12275 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12276 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12280 |     lt_cv_dlopen_self_static=no
12287 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
12288 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12297 |   case $lt_cv_dlopen_self in
12298 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12299 |   *) enable_dlopen_self=unknown ;;
12302 |   case $lt_cv_dlopen_self_static in
12303 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12304 |   *) enable_dlopen_self_static=unknown ;;
19604 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
19605 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
19606 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
20891 | # Whether dlopen is supported.
20892 | dlopen_support=$enable_dlopen
20894 | # Whether dlopen of programs is supported.
20895 | dlopen_self=$enable_dlopen_self
20897 | # Whether dlopen of statically linked programs is supported.
20898 | dlopen_self_static=$enable_dlopen_self_static
20938 | # Compiler flag to allow reflexive dlopens.
21323 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.8t

```

{% raw %}
855 | m4trace:m4/libtool.m4:1838: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
856 | if test "x$enable_dlopen" != xyes; then
857 |   enable_dlopen=unknown
858 |   enable_dlopen_self=unknown
859 |   enable_dlopen_self_static=unknown
861 |   lt_cv_dlopen=no
862 |   lt_cv_dlopen_libs=
866 |     lt_cv_dlopen="load_add_on"
867 |     lt_cv_dlopen_libs=
868 |     lt_cv_dlopen_self=yes
872 |     lt_cv_dlopen="LoadLibrary"
873 |     lt_cv_dlopen_libs=
877 |     lt_cv_dlopen="dlopen"
878 |     lt_cv_dlopen_libs=
883 |     AC_CHECK_LIB([dl], [dlopen],
884 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
885 |     lt_cv_dlopen="dyld"
886 |     lt_cv_dlopen_libs=
887 |     lt_cv_dlopen_self=yes
893 | 	  [lt_cv_dlopen="shl_load"],
895 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
896 | 	[AC_CHECK_FUNC([dlopen],
897 | 	      [lt_cv_dlopen="dlopen"],
898 | 	  [AC_CHECK_LIB([dl], [dlopen],
899 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
900 | 	    [AC_CHECK_LIB([svld], [dlopen],
901 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
903 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
912 |   if test "x$lt_cv_dlopen" != xno; then
913 |     enable_dlopen=yes
915 |     enable_dlopen=no
918 |   case $lt_cv_dlopen in
919 |   dlopen)
927 |     LIBS="$lt_cv_dlopen_libs $LIBS"
929 |     AC_CACHE_CHECK([whether a program can dlopen itself],
930 | 	  lt_cv_dlopen_self, [dnl
931 | 	  _LT_TRY_DLOPEN_SELF(
932 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
933 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
936 |     if test "x$lt_cv_dlopen_self" = xyes; then
938 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
939 | 	  lt_cv_dlopen_self_static, [dnl
940 | 	  _LT_TRY_DLOPEN_SELF(
941 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
942 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
952 |   case $lt_cv_dlopen_self in
953 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
954 |   *) enable_dlopen_self=unknown ;;
957 |   case $lt_cv_dlopen_self_static in
958 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
959 |   *) enable_dlopen_self_static=unknown ;;
962 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
963 | 	 [Whether dlopen is supported])
964 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
965 | 	 [Whether dlopen of programs is supported])
966 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
967 | 	 [Whether dlopen of statically linked programs is supported])
969 | m4trace:m4/libtool.m4:1841: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])
970 | m4trace:m4/libtool.m4:1841: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
972 | LT_SYS_DLOPEN_SELF($@)])
1253 | m4trace:m4/ltoptions.m4:115: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1256 | put the `dlopen' option into LT_INIT's first parameter.])
1258 | m4trace:m4/ltoptions.m4:115: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1260 | _LT_SET_OPTION([LT_INIT], [dlopen])
1263 | put the `dlopen' option into LT_INIT's first parameter.])
1355 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
244 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
282 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
283 | AC_SUBST([LTDLOPEN])
285 | m4trace:/usr/share/aclocal/ltdl.m4:437: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
286 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
287 |   [lt_cv_sys_dlopen_deplibs],
288 |   [# PORTME does your system automatically load deplibs for dlopen?
292 |   lt_cv_sys_dlopen_deplibs=unknown
297 |     lt_cv_sys_dlopen_deplibs=unknown
300 |     lt_cv_sys_dlopen_deplibs=yes
305 |       lt_cv_sys_dlopen_deplibs=no
312 |     lt_cv_sys_dlopen_deplibs=yes
315 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
325 |     lt_cv_sys_dlopen_deplibs=yes
330 |     lt_cv_sys_dlopen_deplibs=unknown
334 |     # at 6.2 and later dlopen does load deplibs.
335 |     lt_cv_sys_dlopen_deplibs=yes
338 |     lt_cv_sys_dlopen_deplibs=yes
341 |     lt_cv_sys_dlopen_deplibs=yes
344 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
347 |     lt_cv_sys_dlopen_deplibs=no
350 |     # dlopen *does* load deplibs and with the right loader patch applied
356 |     lt_cv_sys_dlopen_deplibs=unknown
363 |     lt_cv_sys_dlopen_deplibs=yes
366 |     lt_cv_sys_dlopen_deplibs=yes
369 |     lt_cv_sys_dlopen_deplibs=yes
372 |     libltdl_cv_sys_dlopen_deplibs=yes
376 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
377 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
378 |     [Define if the OS needs help to load dependent libraries for dlopen().])
381 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
382 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
384 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
443 | LIBADD_DLOPEN=
444 | AC_SEARCH_LIBS([dlopen], [dl],
447 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
448 | 	  LIBADD_DLOPEN="-ldl"
450 | 	libltdl_cv_lib_dl_dlopen="yes"
451 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
455 |     ]], [[dlopen(0, 0);]])],
458 | 	    libltdl_cv_func_dlopen="yes"
459 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
460 | 	[AC_CHECK_LIB([svld], [dlopen],
463 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
464 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
465 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
468 |   LIBS="$LIBS $LIBADD_DLOPEN"
472 | AC_SUBST([LIBADD_DLOPEN])
478 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
482 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
492 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
495 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
499 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
506 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
522 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
571 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
572 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
577 |           LIBS="$LIBS $LIBADD_DLOPEN"
578 | 	  _LT_TRY_DLOPEN_SELF(
1993 | m4trace:libtool.m4:1724: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1994 | if test "x$enable_dlopen" != xyes; then
1995 |   enable_dlopen=unknown
1996 |   enable_dlopen_self=unknown
1997 |   enable_dlopen_self_static=unknown
1999 |   lt_cv_dlopen=no
2000 |   lt_cv_dlopen_libs=
2004 |     lt_cv_dlopen="load_add_on"
2005 |     lt_cv_dlopen_libs=
2006 |     lt_cv_dlopen_self=yes
2010 |     lt_cv_dlopen="LoadLibrary"
2011 |     lt_cv_dlopen_libs=
2015 |     lt_cv_dlopen="dlopen"
2016 |     lt_cv_dlopen_libs=
2021 |     AC_CHECK_LIB([dl], [dlopen],
2022 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2023 |     lt_cv_dlopen="dyld"
2024 |     lt_cv_dlopen_libs=
2025 |     lt_cv_dlopen_self=yes
2031 | 	  [lt_cv_dlopen="shl_load"],
2033 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2034 | 	[AC_CHECK_FUNC([dlopen],
2035 | 	      [lt_cv_dlopen="dlopen"],
2036 | 	  [AC_CHECK_LIB([dl], [dlopen],
2037 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2038 | 	    [AC_CHECK_LIB([svld], [dlopen],
2039 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2041 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2050 |   if test "x$lt_cv_dlopen" != xno; then
2051 |     enable_dlopen=yes
2053 |     enable_dlopen=no
2056 |   case $lt_cv_dlopen in
2057 |   dlopen)
2065 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2067 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2068 | 	  lt_cv_dlopen_self, [dnl
2069 | 	  _LT_TRY_DLOPEN_SELF(
2070 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2071 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2074 |     if test "x$lt_cv_dlopen_self" = xyes; then
2076 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2077 | 	  lt_cv_dlopen_self_static, [dnl
2078 | 	  _LT_TRY_DLOPEN_SELF(
2079 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2080 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2090 |   case $lt_cv_dlopen_self in
2091 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2092 |   *) enable_dlopen_self=unknown ;;
2095 |   case $lt_cv_dlopen_self_static in
2096 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2097 |   *) enable_dlopen_self_static=unknown ;;
2100 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2101 | 	 [Whether dlopen is supported])
2102 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2103 | 	 [Whether dlopen of programs is supported])
2104 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2105 | 	 [Whether dlopen of statically linked programs is supported])
2107 | m4trace:libtool.m4:1841: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2108 | m4trace:libtool.m4:1841: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2110 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2391 | m4trace:ltoptions.m4:110: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2394 | put the `dlopen' option into LT_INIT's first parameter.])
2396 | m4trace:ltoptions.m4:110: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2398 | _LT_SET_OPTION([LT_INIT], [dlopen])
2401 | put the `dlopen' option into LT_INIT's first parameter.])
2493 | m4trace:lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2763 | m4trace:configure.ac:15: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/traces.5

```

{% raw %}
244 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
282 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
283 | AC_SUBST([LTDLOPEN])
285 | m4trace:/usr/share/aclocal/ltdl.m4:437: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
286 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
287 |   [lt_cv_sys_dlopen_deplibs],
288 |   [# PORTME does your system automatically load deplibs for dlopen?
292 |   lt_cv_sys_dlopen_deplibs=unknown
297 |     lt_cv_sys_dlopen_deplibs=unknown
300 |     lt_cv_sys_dlopen_deplibs=yes
305 |       lt_cv_sys_dlopen_deplibs=no
312 |     lt_cv_sys_dlopen_deplibs=yes
315 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
325 |     lt_cv_sys_dlopen_deplibs=yes
330 |     lt_cv_sys_dlopen_deplibs=unknown
334 |     # at 6.2 and later dlopen does load deplibs.
335 |     lt_cv_sys_dlopen_deplibs=yes
338 |     lt_cv_sys_dlopen_deplibs=yes
341 |     lt_cv_sys_dlopen_deplibs=yes
344 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
347 |     lt_cv_sys_dlopen_deplibs=no
350 |     # dlopen *does* load deplibs and with the right loader patch applied
356 |     lt_cv_sys_dlopen_deplibs=unknown
363 |     lt_cv_sys_dlopen_deplibs=yes
366 |     lt_cv_sys_dlopen_deplibs=yes
369 |     lt_cv_sys_dlopen_deplibs=yes
372 |     libltdl_cv_sys_dlopen_deplibs=yes
376 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
377 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
378 |     [Define if the OS needs help to load dependent libraries for dlopen().])
381 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
382 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
384 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
443 | LIBADD_DLOPEN=
444 | AC_SEARCH_LIBS([dlopen], [dl],
447 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
448 | 	  LIBADD_DLOPEN="-ldl"
450 | 	libltdl_cv_lib_dl_dlopen="yes"
451 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
455 |     ]], [[dlopen(0, 0);]])],
458 | 	    libltdl_cv_func_dlopen="yes"
459 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
460 | 	[AC_CHECK_LIB([svld], [dlopen],
463 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
464 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
465 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
468 |   LIBS="$LIBS $LIBADD_DLOPEN"
472 | AC_SUBST([LIBADD_DLOPEN])
478 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
482 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
492 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
495 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
499 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
506 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
522 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
571 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
572 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
577 |           LIBS="$LIBS $LIBADD_DLOPEN"
578 | 	  _LT_TRY_DLOPEN_SELF(
1993 | m4trace:m4/libtool.m4:1724: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1994 | if test "x$enable_dlopen" != xyes; then
1995 |   enable_dlopen=unknown
1996 |   enable_dlopen_self=unknown
1997 |   enable_dlopen_self_static=unknown
1999 |   lt_cv_dlopen=no
2000 |   lt_cv_dlopen_libs=
2004 |     lt_cv_dlopen="load_add_on"
2005 |     lt_cv_dlopen_libs=
2006 |     lt_cv_dlopen_self=yes
2010 |     lt_cv_dlopen="LoadLibrary"
2011 |     lt_cv_dlopen_libs=
2015 |     lt_cv_dlopen="dlopen"
2016 |     lt_cv_dlopen_libs=
2021 |     AC_CHECK_LIB([dl], [dlopen],
2022 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
2023 |     lt_cv_dlopen="dyld"
2024 |     lt_cv_dlopen_libs=
2025 |     lt_cv_dlopen_self=yes
2031 | 	  [lt_cv_dlopen="shl_load"],
2033 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
2034 | 	[AC_CHECK_FUNC([dlopen],
2035 | 	      [lt_cv_dlopen="dlopen"],
2036 | 	  [AC_CHECK_LIB([dl], [dlopen],
2037 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
2038 | 	    [AC_CHECK_LIB([svld], [dlopen],
2039 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
2041 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
2050 |   if test "x$lt_cv_dlopen" != xno; then
2051 |     enable_dlopen=yes
2053 |     enable_dlopen=no
2056 |   case $lt_cv_dlopen in
2057 |   dlopen)
2065 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2067 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2068 | 	  lt_cv_dlopen_self, [dnl
2069 | 	  _LT_TRY_DLOPEN_SELF(
2070 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2071 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2074 |     if test "x$lt_cv_dlopen_self" = xyes; then
2076 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2077 | 	  lt_cv_dlopen_self_static, [dnl
2078 | 	  _LT_TRY_DLOPEN_SELF(
2079 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2080 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2090 |   case $lt_cv_dlopen_self in
2091 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2092 |   *) enable_dlopen_self=unknown ;;
2095 |   case $lt_cv_dlopen_self_static in
2096 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2097 |   *) enable_dlopen_self_static=unknown ;;
2100 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2101 | 	 [Whether dlopen is supported])
2102 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2103 | 	 [Whether dlopen of programs is supported])
2104 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2105 | 	 [Whether dlopen of statically linked programs is supported])
2107 | m4trace:m4/libtool.m4:1841: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2108 | m4trace:m4/libtool.m4:1841: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
2110 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
2391 | m4trace:m4/ltoptions.m4:110: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
2394 | put the `dlopen' option into LT_INIT's first parameter.])
2396 | m4trace:m4/ltoptions.m4:110: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
2398 | _LT_SET_OPTION([LT_INIT], [dlopen])
2401 | put the `dlopen' option into LT_INIT's first parameter.])
2493 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2952 | m4trace:configure.ac:18: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/traces.4

```

{% raw %}
244 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
282 | LTDLOPEN=`eval "\\$ECHO \"$libname_spec\""`
283 | AC_SUBST([LTDLOPEN])
285 | m4trace:/usr/share/aclocal/ltdl.m4:437: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
286 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
287 |   [lt_cv_sys_dlopen_deplibs],
288 |   [# PORTME does your system automatically load deplibs for dlopen?
292 |   lt_cv_sys_dlopen_deplibs=unknown
297 |     lt_cv_sys_dlopen_deplibs=unknown
300 |     lt_cv_sys_dlopen_deplibs=yes
305 |       lt_cv_sys_dlopen_deplibs=no
312 |     lt_cv_sys_dlopen_deplibs=yes
315 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
325 |     lt_cv_sys_dlopen_deplibs=yes
330 |     lt_cv_sys_dlopen_deplibs=unknown
334 |     # at 6.2 and later dlopen does load deplibs.
335 |     lt_cv_sys_dlopen_deplibs=yes
338 |     lt_cv_sys_dlopen_deplibs=yes
341 |     lt_cv_sys_dlopen_deplibs=yes
344 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
347 |     lt_cv_sys_dlopen_deplibs=no
350 |     # dlopen *does* load deplibs and with the right loader patch applied
356 |     lt_cv_sys_dlopen_deplibs=unknown
363 |     lt_cv_sys_dlopen_deplibs=yes
366 |     lt_cv_sys_dlopen_deplibs=yes
369 |     lt_cv_sys_dlopen_deplibs=yes
372 |     libltdl_cv_sys_dlopen_deplibs=yes
376 | if test "$lt_cv_sys_dlopen_deplibs" != yes; then
377 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
378 |     [Define if the OS needs help to load dependent libraries for dlopen().])
381 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
382 | m4trace:/usr/share/aclocal/ltdl.m4:536: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
384 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
443 | LIBADD_DLOPEN=
444 | AC_SEARCH_LIBS([dlopen], [dl],
447 | 	if test "$ac_cv_search_dlopen" != "none required" ; then
448 | 	  LIBADD_DLOPEN="-ldl"
450 | 	libltdl_cv_lib_dl_dlopen="yes"
451 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
455 |     ]], [[dlopen(0, 0);]])],
458 | 	    libltdl_cv_func_dlopen="yes"
459 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
460 | 	[AC_CHECK_LIB([svld], [dlopen],
463 | 	        LIBADD_DLOPEN="-lsvld" libltdl_cv_func_dlopen="yes"
464 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
465 | if test x"$libltdl_cv_func_dlopen" = xyes || test x"$libltdl_cv_lib_dl_dlopen" = xyes
468 |   LIBS="$LIBS $LIBADD_DLOPEN"
472 | AC_SUBST([LIBADD_DLOPEN])
478 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
482 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
492 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
495 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
499 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
506 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
522 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
571 |   if test x"$libltdl_cv_func_dlopen" = xyes ||
572 |      test x"$libltdl_cv_lib_dl_dlopen" = xyes ; then
577 |           LIBS="$LIBS $LIBADD_DLOPEN"
578 | 	  _LT_TRY_DLOPEN_SELF(
1544 | m4trace:m4/libtool.m4:1724: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
1545 | if test "x$enable_dlopen" != xyes; then
1546 |   enable_dlopen=unknown
1547 |   enable_dlopen_self=unknown
1548 |   enable_dlopen_self_static=unknown
1550 |   lt_cv_dlopen=no
1551 |   lt_cv_dlopen_libs=
1555 |     lt_cv_dlopen="load_add_on"
1556 |     lt_cv_dlopen_libs=
1557 |     lt_cv_dlopen_self=yes
1561 |     lt_cv_dlopen="LoadLibrary"
1562 |     lt_cv_dlopen_libs=
1566 |     lt_cv_dlopen="dlopen"
1567 |     lt_cv_dlopen_libs=
1572 |     AC_CHECK_LIB([dl], [dlopen],
1573 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1574 |     lt_cv_dlopen="dyld"
1575 |     lt_cv_dlopen_libs=
1576 |     lt_cv_dlopen_self=yes
1582 | 	  [lt_cv_dlopen="shl_load"],
1584 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1585 | 	[AC_CHECK_FUNC([dlopen],
1586 | 	      [lt_cv_dlopen="dlopen"],
1587 | 	  [AC_CHECK_LIB([dl], [dlopen],
1588 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1589 | 	    [AC_CHECK_LIB([svld], [dlopen],
1590 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1592 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1601 |   if test "x$lt_cv_dlopen" != xno; then
1602 |     enable_dlopen=yes
1604 |     enable_dlopen=no
1607 |   case $lt_cv_dlopen in
1608 |   dlopen)
1616 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1618 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1619 | 	  lt_cv_dlopen_self, [dnl
1620 | 	  _LT_TRY_DLOPEN_SELF(
1621 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1622 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1625 |     if test "x$lt_cv_dlopen_self" = xyes; then
1627 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1628 | 	  lt_cv_dlopen_self_static, [dnl
1629 | 	  _LT_TRY_DLOPEN_SELF(
1630 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1631 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1641 |   case $lt_cv_dlopen_self in
1642 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1643 |   *) enable_dlopen_self=unknown ;;
1646 |   case $lt_cv_dlopen_self_static in
1647 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1648 |   *) enable_dlopen_self_static=unknown ;;
1651 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1652 | 	 [Whether dlopen is supported])
1653 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1654 | 	 [Whether dlopen of programs is supported])
1655 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1656 | 	 [Whether dlopen of statically linked programs is supported])
1658 | m4trace:m4/libtool.m4:1841: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1659 | m4trace:m4/libtool.m4:1841: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
1661 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1942 | m4trace:m4/ltoptions.m4:110: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1945 | put the `dlopen' option into LT_INIT's first parameter.])
1947 | m4trace:m4/ltoptions.m4:110: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1949 | _LT_SET_OPTION([LT_INIT], [dlopen])
1952 | put the `dlopen' option into LT_INIT's first parameter.])
2044 | m4trace:m4/lt~obsolete.m4:50: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
2953 | m4trace:configure.ac:18: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/output.4

```

{% raw %}
8278 |         enable_dlopen=no
11476 |   if test "x$enable_dlopen" != xyes; then
11477 |   enable_dlopen=unknown
11478 |   enable_dlopen_self=unknown
11479 |   enable_dlopen_self_static=unknown
11481 |   lt_cv_dlopen=no
11482 |   lt_cv_dlopen_libs=
11486 |     lt_cv_dlopen="load_add_on"
11487 |     lt_cv_dlopen_libs=
11488 |     lt_cv_dlopen_self=yes
11492 |     lt_cv_dlopen="LoadLibrary"
11493 |     lt_cv_dlopen_libs=
11497 |     lt_cv_dlopen="dlopen"
11498 |     lt_cv_dlopen_libs=
11503 |     { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11504 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11505 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11523 | char dlopen ();
11527 | return dlopen ();
11553 |   ac_cv_lib_dl_dlopen=yes
11558 | 	ac_cv_lib_dl_dlopen=no
11566 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11567 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11568 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11569 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11572 |     lt_cv_dlopen="dyld"
11573 |     lt_cv_dlopen_libs=
11574 |     lt_cv_dlopen_self=yes
11667 |   lt_cv_dlopen="shl_load"
11735 |   lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"
11737 |   { $as_echo "$as_me:$LINENO: checking for dlopen" >&5
11738 | $as_echo_n "checking for dlopen... " >&6; }
11739 | if test "${ac_cv_func_dlopen+set}" = set; then
11748 | /* Define dlopen to an innocuous variant, in case <limits.h> declares dlopen.
11750 | #define dlopen innocuous_dlopen
11753 |     which can conflict with char dlopen (); below.
11763 | #undef dlopen
11771 | char dlopen ();
11775 | #if defined __stub_dlopen || defined __stub___dlopen
11782 | return dlopen ();
11808 |   ac_cv_func_dlopen=yes
11813 | 	ac_cv_func_dlopen=no
11820 | { $as_echo "$as_me:$LINENO: result: $ac_cv_func_dlopen" >&5
11821 | $as_echo "$ac_cv_func_dlopen" >&6; }
11822 | if test "x$ac_cv_func_dlopen" = x""yes; then
11823 |   lt_cv_dlopen="dlopen"
11825 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -ldl" >&5
11826 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
11827 | if test "${ac_cv_lib_dl_dlopen+set}" = set; then
11845 | char dlopen ();
11849 | return dlopen ();
11875 |   ac_cv_lib_dl_dlopen=yes
11880 | 	ac_cv_lib_dl_dlopen=no
11888 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_dl_dlopen" >&5
11889 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
11890 | if test "x$ac_cv_lib_dl_dlopen" = x""yes; then
11891 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"
11893 |   { $as_echo "$as_me:$LINENO: checking for dlopen in -lsvld" >&5
11894 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
11895 | if test "${ac_cv_lib_svld_dlopen+set}" = set; then
11913 | char dlopen ();
11917 | return dlopen ();
11943 |   ac_cv_lib_svld_dlopen=yes
11948 | 	ac_cv_lib_svld_dlopen=no
11956 | { $as_echo "$as_me:$LINENO: result: $ac_cv_lib_svld_dlopen" >&5
11957 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
11958 | if test "x$ac_cv_lib_svld_dlopen" = x""yes; then
11959 |   lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"
12027 |   lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"
12048 |   if test "x$lt_cv_dlopen" != xno; then
12049 |     enable_dlopen=yes
12051 |     enable_dlopen=no
12054 |   case $lt_cv_dlopen in
12055 |   dlopen)
12063 |     LIBS="$lt_cv_dlopen_libs $LIBS"
12065 |     { $as_echo "$as_me:$LINENO: checking whether a program can dlopen itself" >&5
12066 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
12067 | if test "${lt_cv_dlopen_self+set}" = set; then
12071 |   lt_cv_dlopen_self=cross
12120 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12143 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
12144 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
12145 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
12149 |     lt_cv_dlopen_self=no
12156 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self" >&5
12157 | $as_echo "$lt_cv_dlopen_self" >&6; }
12159 |     if test "x$lt_cv_dlopen_self" = xyes; then
12161 |       { $as_echo "$as_me:$LINENO: checking whether a statically linked program can dlopen itself" >&5
12162 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
12163 | if test "${lt_cv_dlopen_self_static+set}" = set; then
12167 |   lt_cv_dlopen_self_static=cross
12216 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
12239 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
12240 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
12241 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
12245 |     lt_cv_dlopen_self_static=no
12252 | { $as_echo "$as_me:$LINENO: result: $lt_cv_dlopen_self_static" >&5
12253 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
12262 |   case $lt_cv_dlopen_self in
12263 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
12264 |   *) enable_dlopen_self=unknown ;;
12267 |   case $lt_cv_dlopen_self_static in
12268 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
12269 |   *) enable_dlopen_self_static=unknown ;;
19569 | enable_dlopen='`$ECHO "X$enable_dlopen" | $Xsed -e "$delay_single_quote_subst"`'
19570 | enable_dlopen_self='`$ECHO "X$enable_dlopen_self" | $Xsed -e "$delay_single_quote_subst"`'
19571 | enable_dlopen_self_static='`$ECHO "X$enable_dlopen_self_static" | $Xsed -e "$delay_single_quote_subst"`'
20856 | # Whether dlopen is supported.
20857 | dlopen_support=$enable_dlopen
20859 | # Whether dlopen of programs is supported.
20860 | dlopen_self=$enable_dlopen_self
20862 | # Whether dlopen of statically linked programs is supported.
20863 | dlopen_self_static=$enable_dlopen_self_static
20903 | # Compiler flag to allow reflexive dlopens.
21288 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1634 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1637 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5158 |     [Compiler flag to allow reflexive dlopens])
5274 |   LT_SYS_DLOPEN_SELF
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
### build-aux/ltmain.sh

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
5062 |       if test "$pass" = dlopen; then
5274 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
5275 | 	      # If there is no dlopen support or we're linking statically,
5305 | 	dlopen=
5335 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
5375 | 	# This library was specified with -dlopen.
5376 | 	if test "$pass" = dlopen; then
5378 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
5381 | 	     test "$dlopen_support" != yes ||
5383 | 	    # If there is no dlname, no dlopen support or we're linking
5392 | 	fi # $pass = dlopen
5450 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5576 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5577 | 	  dlopenmodule=""
5580 | 	      dlopenmodule="$dlpremoduletest"
5584 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5681 | 		    # if the lib is a (non-dlopened) module then we can not
5685 | 		      if test "X$dlopenmodule" != "X$lib"; then
5837 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5838 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5974 |       if test "$pass" != dlopen; then
6073 | 	func_warning "\`-dlopen' is ignored for archives"
6140 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6805 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6806 | 	    $ECHO "*** application is linked with the -dlopen flag."
6824 | 	    $ECHO "*** or is declared to -dlopen it."
7391 | 	func_warning "\`-dlopen' is ignored for objects"
7506 |         && test "$dlopen_support" = unknown \
7507 | 	&& test "$dlopen_self" = unknown \
7508 | 	&& test "$dlopen_self_static" = unknown && \
7509 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
8141 | # The name that we can dlopen(3).
8170 | # Files to dlopen/dlpreopen
8171 | dlopen='$dlfiles'
{% endraw %}

```