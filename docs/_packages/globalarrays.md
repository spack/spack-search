---
name: "globalarrays"
layout: package
next_package: kitty
previous_package: grep
languages: ['cpp', 'bash']
---
## 5.6.4
25 / 1410 files match

 - [comex/autom4te.cache/output.0](#comexautom4tecacheoutput0)
 - [comex/autom4te.cache/output.1](#comexautom4tecacheoutput1)
 - [comex/autom4te.cache/output.2](#comexautom4tecacheoutput2)
 - [comex/autom4te.cache/traces.0](#comexautom4tecachetraces0)
 - [comex/autom4te.cache/traces.2](#comexautom4tecachetraces2)
 - [comex/m4/libtool.m4](#comexm4libtoolm4)
 - [comex/m4/ltoptions.m4](#comexm4ltoptionsm4)
 - [comex/build-aux/ltmain.sh](#comexbuild-auxltmainsh)
 - [comex/src-ofi/ofi.h](#comexsrc-ofiofih)
 - [armci/autom4te.cache/output.0](#armciautom4tecacheoutput0)
 - [armci/autom4te.cache/output.1](#armciautom4tecacheoutput1)
 - [armci/autom4te.cache/output.2](#armciautom4tecacheoutput2)
 - [armci/autom4te.cache/traces.0](#armciautom4tecachetraces0)
 - [armci/autom4te.cache/traces.2](#armciautom4tecachetraces2)
 - [armci/m4/libtool.m4](#armcim4libtoolm4)
 - [armci/m4/ltoptions.m4](#armcim4ltoptionsm4)
 - [armci/build-aux/ltmain.sh](#armcibuild-auxltmainsh)
 - [autom4te.cache/output.0](#autom4tecacheoutput0)
 - [autom4te.cache/output.1](#autom4tecacheoutput1)
 - [autom4te.cache/output.2](#autom4tecacheoutput2)
 - [autom4te.cache/traces.0](#autom4tecachetraces0)
 - [autom4te.cache/traces.2](#autom4tecachetraces2)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### comex/autom4te.cache/output.0

```

{% raw %}
20601 |         enable_dlopen=no
24219 |   if test yes != "$enable_dlopen"; then
24220 |   enable_dlopen=unknown
24221 |   enable_dlopen_self=unknown
24222 |   enable_dlopen_self_static=unknown
24224 |   lt_cv_dlopen=no
24225 |   lt_cv_dlopen_libs=
24229 |     lt_cv_dlopen=load_add_on
24230 |     lt_cv_dlopen_libs=
24231 |     lt_cv_dlopen_self=yes
24235 |     lt_cv_dlopen=LoadLibrary
24236 |     lt_cv_dlopen_libs=
24240 |     lt_cv_dlopen=dlopen
24241 |     lt_cv_dlopen_libs=
24246 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24247 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24248 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24262 | char dlopen ();
24266 | return dlopen ();
24272 |   ac_cv_lib_dl_dlopen=yes
24274 |   ac_cv_lib_dl_dlopen=no
24280 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24281 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24282 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24283 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24286 |     lt_cv_dlopen=dyld
24287 |     lt_cv_dlopen_libs=
24288 |     lt_cv_dlopen_self=yes
24297 |     lt_cv_dlopen=dlopen
24298 |     lt_cv_dlopen_libs=
24299 |     lt_cv_dlopen_self=no
24305 |   lt_cv_dlopen=shl_load
24344 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
24346 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
24347 | if test "x$ac_cv_func_dlopen" = xyes; then :
24348 |   lt_cv_dlopen=dlopen
24350 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24351 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24352 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24366 | char dlopen ();
24370 | return dlopen ();
24376 |   ac_cv_lib_dl_dlopen=yes
24378 |   ac_cv_lib_dl_dlopen=no
24384 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24385 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24386 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24387 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24389 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
24390 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
24391 | if ${ac_cv_lib_svld_dlopen+:} false; then :
24405 | char dlopen ();
24409 | return dlopen ();
24415 |   ac_cv_lib_svld_dlopen=yes
24417 |   ac_cv_lib_svld_dlopen=no
24423 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
24424 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
24425 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
24426 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
24465 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
24486 |   if test no = "$lt_cv_dlopen"; then
24487 |     enable_dlopen=no
24489 |     enable_dlopen=yes
24492 |   case $lt_cv_dlopen in
24493 |   dlopen)
24501 |     LIBS="$lt_cv_dlopen_libs $LIBS"
24503 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
24504 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
24505 | if ${lt_cv_dlopen_self+:} false; then :
24509 |   lt_cv_dlopen_self=cross
24564 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24591 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
24592 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
24593 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
24597 |     lt_cv_dlopen_self=no
24604 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
24605 | $as_echo "$lt_cv_dlopen_self" >&6; }
24607 |     if test yes = "$lt_cv_dlopen_self"; then
24609 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
24610 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
24611 | if ${lt_cv_dlopen_self_static+:} false; then :
24615 |   lt_cv_dlopen_self_static=cross
24670 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24697 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
24698 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
24699 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
24703 |     lt_cv_dlopen_self_static=no
24710 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
24711 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
24720 |   case $lt_cv_dlopen_self in
24721 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
24722 |   *) enable_dlopen_self=unknown ;;
24725 |   case $lt_cv_dlopen_self_static in
24726 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
24727 |   *) enable_dlopen_self_static=unknown ;;
25850 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25851 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25852 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27004 | # Whether dlopen is supported.
27005 | dlopen_support=$enable_dlopen
27007 | # Whether dlopen of programs is supported.
27008 | dlopen_self=$enable_dlopen_self
27010 | # Whether dlopen of statically linked programs is supported.
27011 | dlopen_self_static=$enable_dlopen_self_static
27055 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### comex/autom4te.cache/output.1

```

{% raw %}
20601 |         enable_dlopen=no
24219 |   if test yes != "$enable_dlopen"; then
24220 |   enable_dlopen=unknown
24221 |   enable_dlopen_self=unknown
24222 |   enable_dlopen_self_static=unknown
24224 |   lt_cv_dlopen=no
24225 |   lt_cv_dlopen_libs=
24229 |     lt_cv_dlopen=load_add_on
24230 |     lt_cv_dlopen_libs=
24231 |     lt_cv_dlopen_self=yes
24235 |     lt_cv_dlopen=LoadLibrary
24236 |     lt_cv_dlopen_libs=
24240 |     lt_cv_dlopen=dlopen
24241 |     lt_cv_dlopen_libs=
24246 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24247 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24248 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24262 | char dlopen ();
24266 | return dlopen ();
24272 |   ac_cv_lib_dl_dlopen=yes
24274 |   ac_cv_lib_dl_dlopen=no
24280 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24281 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24282 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24283 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24286 |     lt_cv_dlopen=dyld
24287 |     lt_cv_dlopen_libs=
24288 |     lt_cv_dlopen_self=yes
24297 |     lt_cv_dlopen=dlopen
24298 |     lt_cv_dlopen_libs=
24299 |     lt_cv_dlopen_self=no
24305 |   lt_cv_dlopen=shl_load
24344 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
24346 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
24347 | if test "x$ac_cv_func_dlopen" = xyes; then :
24348 |   lt_cv_dlopen=dlopen
24350 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24351 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24352 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24366 | char dlopen ();
24370 | return dlopen ();
24376 |   ac_cv_lib_dl_dlopen=yes
24378 |   ac_cv_lib_dl_dlopen=no
24384 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24385 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24386 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24387 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24389 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
24390 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
24391 | if ${ac_cv_lib_svld_dlopen+:} false; then :
24405 | char dlopen ();
24409 | return dlopen ();
24415 |   ac_cv_lib_svld_dlopen=yes
24417 |   ac_cv_lib_svld_dlopen=no
24423 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
24424 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
24425 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
24426 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
24465 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
24486 |   if test no = "$lt_cv_dlopen"; then
24487 |     enable_dlopen=no
24489 |     enable_dlopen=yes
24492 |   case $lt_cv_dlopen in
24493 |   dlopen)
24501 |     LIBS="$lt_cv_dlopen_libs $LIBS"
24503 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
24504 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
24505 | if ${lt_cv_dlopen_self+:} false; then :
24509 |   lt_cv_dlopen_self=cross
24564 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24591 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
24592 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
24593 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
24597 |     lt_cv_dlopen_self=no
24604 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
24605 | $as_echo "$lt_cv_dlopen_self" >&6; }
24607 |     if test yes = "$lt_cv_dlopen_self"; then
24609 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
24610 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
24611 | if ${lt_cv_dlopen_self_static+:} false; then :
24615 |   lt_cv_dlopen_self_static=cross
24670 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24697 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
24698 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
24699 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
24703 |     lt_cv_dlopen_self_static=no
24710 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
24711 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
24720 |   case $lt_cv_dlopen_self in
24721 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
24722 |   *) enable_dlopen_self=unknown ;;
24725 |   case $lt_cv_dlopen_self_static in
24726 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
24727 |   *) enable_dlopen_self_static=unknown ;;
25850 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25851 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25852 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27004 | # Whether dlopen is supported.
27005 | dlopen_support=$enable_dlopen
27007 | # Whether dlopen of programs is supported.
27008 | dlopen_self=$enable_dlopen_self
27010 | # Whether dlopen of statically linked programs is supported.
27011 | dlopen_self_static=$enable_dlopen_self_static
27055 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### comex/autom4te.cache/output.2

```

{% raw %}
20601 |         enable_dlopen=no
24219 |   if test yes != "$enable_dlopen"; then
24220 |   enable_dlopen=unknown
24221 |   enable_dlopen_self=unknown
24222 |   enable_dlopen_self_static=unknown
24224 |   lt_cv_dlopen=no
24225 |   lt_cv_dlopen_libs=
24229 |     lt_cv_dlopen=load_add_on
24230 |     lt_cv_dlopen_libs=
24231 |     lt_cv_dlopen_self=yes
24235 |     lt_cv_dlopen=LoadLibrary
24236 |     lt_cv_dlopen_libs=
24240 |     lt_cv_dlopen=dlopen
24241 |     lt_cv_dlopen_libs=
24246 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24247 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24248 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24262 | char dlopen ();
24266 | return dlopen ();
24272 |   ac_cv_lib_dl_dlopen=yes
24274 |   ac_cv_lib_dl_dlopen=no
24280 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24281 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24282 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24283 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24286 |     lt_cv_dlopen=dyld
24287 |     lt_cv_dlopen_libs=
24288 |     lt_cv_dlopen_self=yes
24297 |     lt_cv_dlopen=dlopen
24298 |     lt_cv_dlopen_libs=
24299 |     lt_cv_dlopen_self=no
24305 |   lt_cv_dlopen=shl_load
24344 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
24346 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
24347 | if test "x$ac_cv_func_dlopen" = xyes; then :
24348 |   lt_cv_dlopen=dlopen
24350 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24351 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24352 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24366 | char dlopen ();
24370 | return dlopen ();
24376 |   ac_cv_lib_dl_dlopen=yes
24378 |   ac_cv_lib_dl_dlopen=no
24384 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24385 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24386 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24387 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24389 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
24390 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
24391 | if ${ac_cv_lib_svld_dlopen+:} false; then :
24405 | char dlopen ();
24409 | return dlopen ();
24415 |   ac_cv_lib_svld_dlopen=yes
24417 |   ac_cv_lib_svld_dlopen=no
24423 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
24424 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
24425 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
24426 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
24465 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
24486 |   if test no = "$lt_cv_dlopen"; then
24487 |     enable_dlopen=no
24489 |     enable_dlopen=yes
24492 |   case $lt_cv_dlopen in
24493 |   dlopen)
24501 |     LIBS="$lt_cv_dlopen_libs $LIBS"
24503 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
24504 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
24505 | if ${lt_cv_dlopen_self+:} false; then :
24509 |   lt_cv_dlopen_self=cross
24564 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24591 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
24592 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
24593 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
24597 |     lt_cv_dlopen_self=no
24604 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
24605 | $as_echo "$lt_cv_dlopen_self" >&6; }
24607 |     if test yes = "$lt_cv_dlopen_self"; then
24609 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
24610 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
24611 | if ${lt_cv_dlopen_self_static+:} false; then :
24615 |   lt_cv_dlopen_self_static=cross
24670 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24697 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
24698 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
24699 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
24703 |     lt_cv_dlopen_self_static=no
24710 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
24711 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
24720 |   case $lt_cv_dlopen_self in
24721 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
24722 |   *) enable_dlopen_self=unknown ;;
24725 |   case $lt_cv_dlopen_self_static in
24726 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
24727 |   *) enable_dlopen_self_static=unknown ;;
25850 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25851 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25852 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27004 | # Whether dlopen is supported.
27005 | dlopen_support=$enable_dlopen
27007 | # Whether dlopen of programs is supported.
27008 | dlopen_self=$enable_dlopen_self
27010 | # Whether dlopen of statically linked programs is supported.
27011 | dlopen_self_static=$enable_dlopen_self_static
27055 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### comex/autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
412 | if test yes != "$enable_dlopen"; then
413 |   enable_dlopen=unknown
414 |   enable_dlopen_self=unknown
415 |   enable_dlopen_self_static=unknown
417 |   lt_cv_dlopen=no
418 |   lt_cv_dlopen_libs=
422 |     lt_cv_dlopen=load_add_on
423 |     lt_cv_dlopen_libs=
424 |     lt_cv_dlopen_self=yes
428 |     lt_cv_dlopen=LoadLibrary
429 |     lt_cv_dlopen_libs=
433 |     lt_cv_dlopen=dlopen
434 |     lt_cv_dlopen_libs=
439 |     AC_CHECK_LIB([dl], [dlopen],
440 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
441 |     lt_cv_dlopen=dyld
442 |     lt_cv_dlopen_libs=
443 |     lt_cv_dlopen_self=yes
450 |     lt_cv_dlopen=dlopen
451 |     lt_cv_dlopen_libs=
452 |     lt_cv_dlopen_self=no
457 | 	  [lt_cv_dlopen=shl_load],
459 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
460 | 	[AC_CHECK_FUNC([dlopen],
461 | 	      [lt_cv_dlopen=dlopen],
462 | 	  [AC_CHECK_LIB([dl], [dlopen],
463 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
464 | 	    [AC_CHECK_LIB([svld], [dlopen],
465 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
467 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
476 |   if test no = "$lt_cv_dlopen"; then
477 |     enable_dlopen=no
479 |     enable_dlopen=yes
482 |   case $lt_cv_dlopen in
483 |   dlopen)
491 |     LIBS="$lt_cv_dlopen_libs $LIBS"
493 |     AC_CACHE_CHECK([whether a program can dlopen itself],
494 | 	  lt_cv_dlopen_self, [dnl
495 | 	  _LT_TRY_DLOPEN_SELF(
496 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
497 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
500 |     if test yes = "$lt_cv_dlopen_self"; then
502 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
503 | 	  lt_cv_dlopen_self_static, [dnl
504 | 	  _LT_TRY_DLOPEN_SELF(
505 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
506 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
516 |   case $lt_cv_dlopen_self in
517 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
518 |   *) enable_dlopen_self=unknown ;;
521 |   case $lt_cv_dlopen_self_static in
522 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
523 |   *) enable_dlopen_self_static=unknown ;;
526 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
527 | 	 [Whether dlopen is supported])
528 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
529 | 	 [Whether dlopen of programs is supported])
530 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
531 | 	 [Whether dlopen of statically linked programs is supported])
533 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1134 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1135 |   [lt_cv_sys_dlopen_deplibs],
1136 |   [# PORTME does your system automatically load deplibs for dlopen?
1140 |   lt_cv_sys_dlopen_deplibs=unknown
1145 |     lt_cv_sys_dlopen_deplibs=unknown
1148 |     lt_cv_sys_dlopen_deplibs=yes
1153 |       lt_cv_sys_dlopen_deplibs=no
1158 |     lt_cv_sys_dlopen_deplibs=yes
1163 |     lt_cv_sys_dlopen_deplibs=yes
1166 |     lt_cv_sys_dlopen_deplibs=yes
1170 |     lt_cv_sys_dlopen_deplibs=yes
1173 |     lt_cv_sys_dlopen_deplibs=yes
1176 |     lt_cv_sys_dlopen_deplibs=yes
1181 |     lt_cv_sys_dlopen_deplibs=unknown
1185 |     # at 6.2 and later dlopen does load deplibs.
1186 |     lt_cv_sys_dlopen_deplibs=yes
1189 |     lt_cv_sys_dlopen_deplibs=yes
1192 |     lt_cv_sys_dlopen_deplibs=yes
1195 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1198 |     lt_cv_sys_dlopen_deplibs=no
1201 |     # dlopen *does* load deplibs and with the right loader patch applied
1207 |     lt_cv_sys_dlopen_deplibs=unknown
1214 |     lt_cv_sys_dlopen_deplibs=yes
1217 |     lt_cv_sys_dlopen_deplibs=yes
1220 |     lt_cv_sys_dlopen_deplibs=yes
1223 |     libltdl_cv_sys_dlopen_deplibs=yes
1227 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1228 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1229 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1232 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1235 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1307 | LIBADD_DLOPEN=
1308 | AC_SEARCH_LIBS([dlopen], [dl],
1311 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1312 | 	  LIBADD_DLOPEN=-ldl
1314 | 	libltdl_cv_lib_dl_dlopen=yes
1315 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1319 |     ]], [[dlopen(0, 0);]])],
1322 | 	    libltdl_cv_func_dlopen=yes
1323 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1324 | 	[AC_CHECK_LIB([svld], [dlopen],
1327 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1328 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1329 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1332 |   LIBS="$LIBS $LIBADD_DLOPEN"
1336 | AC_SUBST([LIBADD_DLOPEN])
1342 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1346 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1356 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1359 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1363 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1370 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1386 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1438 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
1443 |       LIBS="$LIBS $LIBADD_DLOPEN"
1501 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1543 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4426 | m4trace:configure.ac:181: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### comex/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
3142 | m4trace:m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
3143 | if test yes != "$enable_dlopen"; then
3144 |   enable_dlopen=unknown
3145 |   enable_dlopen_self=unknown
3146 |   enable_dlopen_self_static=unknown
3148 |   lt_cv_dlopen=no
3149 |   lt_cv_dlopen_libs=
3153 |     lt_cv_dlopen=load_add_on
3154 |     lt_cv_dlopen_libs=
3155 |     lt_cv_dlopen_self=yes
3159 |     lt_cv_dlopen=LoadLibrary
3160 |     lt_cv_dlopen_libs=
3164 |     lt_cv_dlopen=dlopen
3165 |     lt_cv_dlopen_libs=
3170 |     AC_CHECK_LIB([dl], [dlopen],
3171 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
3172 |     lt_cv_dlopen=dyld
3173 |     lt_cv_dlopen_libs=
3174 |     lt_cv_dlopen_self=yes
3181 |     lt_cv_dlopen=dlopen
3182 |     lt_cv_dlopen_libs=
3183 |     lt_cv_dlopen_self=no
3188 | 	  [lt_cv_dlopen=shl_load],
3190 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
3191 | 	[AC_CHECK_FUNC([dlopen],
3192 | 	      [lt_cv_dlopen=dlopen],
3193 | 	  [AC_CHECK_LIB([dl], [dlopen],
3194 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
3195 | 	    [AC_CHECK_LIB([svld], [dlopen],
3196 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
3198 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
3207 |   if test no = "$lt_cv_dlopen"; then
3208 |     enable_dlopen=no
3210 |     enable_dlopen=yes
3213 |   case $lt_cv_dlopen in
3214 |   dlopen)
3222 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3224 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3225 | 	  lt_cv_dlopen_self, [dnl
3226 | 	  _LT_TRY_DLOPEN_SELF(
3227 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3228 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3231 |     if test yes = "$lt_cv_dlopen_self"; then
3233 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3234 | 	  lt_cv_dlopen_self_static, [dnl
3235 | 	  _LT_TRY_DLOPEN_SELF(
3236 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3237 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3247 |   case $lt_cv_dlopen_self in
3248 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3249 |   *) enable_dlopen_self=unknown ;;
3252 |   case $lt_cv_dlopen_self_static in
3253 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3254 |   *) enable_dlopen_self_static=unknown ;;
3257 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3258 | 	 [Whether dlopen is supported])
3259 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3260 | 	 [Whether dlopen of programs is supported])
3261 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3262 | 	 [Whether dlopen of statically linked programs is supported])
3264 | m4trace:m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3265 | m4trace:m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
3267 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3576 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
3579 | put the 'dlopen' option into LT_INIT's first parameter.])
3581 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
3583 | _LT_SET_OPTION([LT_INIT], [dlopen])
3586 | put the 'dlopen' option into LT_INIT's first parameter.])
3678 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4426 | m4trace:configure.ac:181: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### comex/m4/libtool.m4

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
### comex/m4/ltoptions.m4

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
### comex/build-aux/ltmain.sh

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
### comex/src-ofi/ofi.h

```cpp

{% raw %}
97 |     ld_table.handle = dlopen(env_data.library_path, RTLD_NOW);
{% endraw %}

```
### armci/autom4te.cache/output.0

```

{% raw %}
25694 |         enable_dlopen=no
29312 |   if test yes != "$enable_dlopen"; then
29313 |   enable_dlopen=unknown
29314 |   enable_dlopen_self=unknown
29315 |   enable_dlopen_self_static=unknown
29317 |   lt_cv_dlopen=no
29318 |   lt_cv_dlopen_libs=
29322 |     lt_cv_dlopen=load_add_on
29323 |     lt_cv_dlopen_libs=
29324 |     lt_cv_dlopen_self=yes
29328 |     lt_cv_dlopen=LoadLibrary
29329 |     lt_cv_dlopen_libs=
29333 |     lt_cv_dlopen=dlopen
29334 |     lt_cv_dlopen_libs=
29339 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29340 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29341 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29355 | char dlopen ();
29359 | return dlopen ();
29365 |   ac_cv_lib_dl_dlopen=yes
29367 |   ac_cv_lib_dl_dlopen=no
29373 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29374 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29375 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29376 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29379 |     lt_cv_dlopen=dyld
29380 |     lt_cv_dlopen_libs=
29381 |     lt_cv_dlopen_self=yes
29390 |     lt_cv_dlopen=dlopen
29391 |     lt_cv_dlopen_libs=
29392 |     lt_cv_dlopen_self=no
29398 |   lt_cv_dlopen=shl_load
29437 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
29439 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
29440 | if test "x$ac_cv_func_dlopen" = xyes; then :
29441 |   lt_cv_dlopen=dlopen
29443 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29444 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29445 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29459 | char dlopen ();
29463 | return dlopen ();
29469 |   ac_cv_lib_dl_dlopen=yes
29471 |   ac_cv_lib_dl_dlopen=no
29477 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29478 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29479 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29480 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29482 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
29483 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
29484 | if ${ac_cv_lib_svld_dlopen+:} false; then :
29498 | char dlopen ();
29502 | return dlopen ();
29508 |   ac_cv_lib_svld_dlopen=yes
29510 |   ac_cv_lib_svld_dlopen=no
29516 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
29517 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
29518 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
29519 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
29558 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
29579 |   if test no = "$lt_cv_dlopen"; then
29580 |     enable_dlopen=no
29582 |     enable_dlopen=yes
29585 |   case $lt_cv_dlopen in
29586 |   dlopen)
29594 |     LIBS="$lt_cv_dlopen_libs $LIBS"
29596 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
29597 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
29598 | if ${lt_cv_dlopen_self+:} false; then :
29602 |   lt_cv_dlopen_self=cross
29657 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29684 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
29685 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
29686 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
29690 |     lt_cv_dlopen_self=no
29697 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
29698 | $as_echo "$lt_cv_dlopen_self" >&6; }
29700 |     if test yes = "$lt_cv_dlopen_self"; then
29702 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
29703 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
29704 | if ${lt_cv_dlopen_self_static+:} false; then :
29708 |   lt_cv_dlopen_self_static=cross
29763 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29790 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
29791 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
29792 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
29796 |     lt_cv_dlopen_self_static=no
29803 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
29804 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
29813 |   case $lt_cv_dlopen_self in
29814 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
29815 |   *) enable_dlopen_self=unknown ;;
29818 |   case $lt_cv_dlopen_self_static in
29819 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
29820 |   *) enable_dlopen_self_static=unknown ;;
34988 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
34989 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
34990 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
36239 | # Whether dlopen is supported.
36240 | dlopen_support=$enable_dlopen
36242 | # Whether dlopen of programs is supported.
36243 | dlopen_self=$enable_dlopen_self
36245 | # Whether dlopen of statically linked programs is supported.
36246 | dlopen_self_static=$enable_dlopen_self_static
36290 | # Compiler flag to allow reflexive dlopens.
36532 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### armci/autom4te.cache/output.1

```

{% raw %}
25694 |         enable_dlopen=no
29312 |   if test yes != "$enable_dlopen"; then
29313 |   enable_dlopen=unknown
29314 |   enable_dlopen_self=unknown
29315 |   enable_dlopen_self_static=unknown
29317 |   lt_cv_dlopen=no
29318 |   lt_cv_dlopen_libs=
29322 |     lt_cv_dlopen=load_add_on
29323 |     lt_cv_dlopen_libs=
29324 |     lt_cv_dlopen_self=yes
29328 |     lt_cv_dlopen=LoadLibrary
29329 |     lt_cv_dlopen_libs=
29333 |     lt_cv_dlopen=dlopen
29334 |     lt_cv_dlopen_libs=
29339 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29340 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29341 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29355 | char dlopen ();
29359 | return dlopen ();
29365 |   ac_cv_lib_dl_dlopen=yes
29367 |   ac_cv_lib_dl_dlopen=no
29373 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29374 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29375 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29376 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29379 |     lt_cv_dlopen=dyld
29380 |     lt_cv_dlopen_libs=
29381 |     lt_cv_dlopen_self=yes
29390 |     lt_cv_dlopen=dlopen
29391 |     lt_cv_dlopen_libs=
29392 |     lt_cv_dlopen_self=no
29398 |   lt_cv_dlopen=shl_load
29437 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
29439 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
29440 | if test "x$ac_cv_func_dlopen" = xyes; then :
29441 |   lt_cv_dlopen=dlopen
29443 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29444 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29445 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29459 | char dlopen ();
29463 | return dlopen ();
29469 |   ac_cv_lib_dl_dlopen=yes
29471 |   ac_cv_lib_dl_dlopen=no
29477 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29478 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29479 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29480 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29482 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
29483 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
29484 | if ${ac_cv_lib_svld_dlopen+:} false; then :
29498 | char dlopen ();
29502 | return dlopen ();
29508 |   ac_cv_lib_svld_dlopen=yes
29510 |   ac_cv_lib_svld_dlopen=no
29516 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
29517 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
29518 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
29519 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
29558 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
29579 |   if test no = "$lt_cv_dlopen"; then
29580 |     enable_dlopen=no
29582 |     enable_dlopen=yes
29585 |   case $lt_cv_dlopen in
29586 |   dlopen)
29594 |     LIBS="$lt_cv_dlopen_libs $LIBS"
29596 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
29597 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
29598 | if ${lt_cv_dlopen_self+:} false; then :
29602 |   lt_cv_dlopen_self=cross
29657 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29684 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
29685 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
29686 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
29690 |     lt_cv_dlopen_self=no
29697 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
29698 | $as_echo "$lt_cv_dlopen_self" >&6; }
29700 |     if test yes = "$lt_cv_dlopen_self"; then
29702 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
29703 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
29704 | if ${lt_cv_dlopen_self_static+:} false; then :
29708 |   lt_cv_dlopen_self_static=cross
29763 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29790 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
29791 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
29792 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
29796 |     lt_cv_dlopen_self_static=no
29803 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
29804 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
29813 |   case $lt_cv_dlopen_self in
29814 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
29815 |   *) enable_dlopen_self=unknown ;;
29818 |   case $lt_cv_dlopen_self_static in
29819 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
29820 |   *) enable_dlopen_self_static=unknown ;;
34988 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
34989 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
34990 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
36239 | # Whether dlopen is supported.
36240 | dlopen_support=$enable_dlopen
36242 | # Whether dlopen of programs is supported.
36243 | dlopen_self=$enable_dlopen_self
36245 | # Whether dlopen of statically linked programs is supported.
36246 | dlopen_self_static=$enable_dlopen_self_static
36290 | # Compiler flag to allow reflexive dlopens.
36532 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### armci/autom4te.cache/output.2

```

{% raw %}
25694 |         enable_dlopen=no
29312 |   if test yes != "$enable_dlopen"; then
29313 |   enable_dlopen=unknown
29314 |   enable_dlopen_self=unknown
29315 |   enable_dlopen_self_static=unknown
29317 |   lt_cv_dlopen=no
29318 |   lt_cv_dlopen_libs=
29322 |     lt_cv_dlopen=load_add_on
29323 |     lt_cv_dlopen_libs=
29324 |     lt_cv_dlopen_self=yes
29328 |     lt_cv_dlopen=LoadLibrary
29329 |     lt_cv_dlopen_libs=
29333 |     lt_cv_dlopen=dlopen
29334 |     lt_cv_dlopen_libs=
29339 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29340 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29341 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29355 | char dlopen ();
29359 | return dlopen ();
29365 |   ac_cv_lib_dl_dlopen=yes
29367 |   ac_cv_lib_dl_dlopen=no
29373 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29374 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29375 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29376 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29379 |     lt_cv_dlopen=dyld
29380 |     lt_cv_dlopen_libs=
29381 |     lt_cv_dlopen_self=yes
29390 |     lt_cv_dlopen=dlopen
29391 |     lt_cv_dlopen_libs=
29392 |     lt_cv_dlopen_self=no
29398 |   lt_cv_dlopen=shl_load
29437 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
29439 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
29440 | if test "x$ac_cv_func_dlopen" = xyes; then :
29441 |   lt_cv_dlopen=dlopen
29443 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29444 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29445 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29459 | char dlopen ();
29463 | return dlopen ();
29469 |   ac_cv_lib_dl_dlopen=yes
29471 |   ac_cv_lib_dl_dlopen=no
29477 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29478 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29479 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29480 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29482 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
29483 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
29484 | if ${ac_cv_lib_svld_dlopen+:} false; then :
29498 | char dlopen ();
29502 | return dlopen ();
29508 |   ac_cv_lib_svld_dlopen=yes
29510 |   ac_cv_lib_svld_dlopen=no
29516 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
29517 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
29518 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
29519 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
29558 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
29579 |   if test no = "$lt_cv_dlopen"; then
29580 |     enable_dlopen=no
29582 |     enable_dlopen=yes
29585 |   case $lt_cv_dlopen in
29586 |   dlopen)
29594 |     LIBS="$lt_cv_dlopen_libs $LIBS"
29596 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
29597 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
29598 | if ${lt_cv_dlopen_self+:} false; then :
29602 |   lt_cv_dlopen_self=cross
29657 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29684 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
29685 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
29686 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
29690 |     lt_cv_dlopen_self=no
29697 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
29698 | $as_echo "$lt_cv_dlopen_self" >&6; }
29700 |     if test yes = "$lt_cv_dlopen_self"; then
29702 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
29703 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
29704 | if ${lt_cv_dlopen_self_static+:} false; then :
29708 |   lt_cv_dlopen_self_static=cross
29763 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29790 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
29791 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
29792 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
29796 |     lt_cv_dlopen_self_static=no
29803 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
29804 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
29813 |   case $lt_cv_dlopen_self in
29814 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
29815 |   *) enable_dlopen_self=unknown ;;
29818 |   case $lt_cv_dlopen_self_static in
29819 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
29820 |   *) enable_dlopen_self_static=unknown ;;
34988 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
34989 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
34990 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
36239 | # Whether dlopen is supported.
36240 | dlopen_support=$enable_dlopen
36242 | # Whether dlopen of programs is supported.
36243 | dlopen_self=$enable_dlopen_self
36245 | # Whether dlopen of statically linked programs is supported.
36246 | dlopen_self_static=$enable_dlopen_self_static
36290 | # Compiler flag to allow reflexive dlopens.
36532 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### armci/autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
412 | if test yes != "$enable_dlopen"; then
413 |   enable_dlopen=unknown
414 |   enable_dlopen_self=unknown
415 |   enable_dlopen_self_static=unknown
417 |   lt_cv_dlopen=no
418 |   lt_cv_dlopen_libs=
422 |     lt_cv_dlopen=load_add_on
423 |     lt_cv_dlopen_libs=
424 |     lt_cv_dlopen_self=yes
428 |     lt_cv_dlopen=LoadLibrary
429 |     lt_cv_dlopen_libs=
433 |     lt_cv_dlopen=dlopen
434 |     lt_cv_dlopen_libs=
439 |     AC_CHECK_LIB([dl], [dlopen],
440 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
441 |     lt_cv_dlopen=dyld
442 |     lt_cv_dlopen_libs=
443 |     lt_cv_dlopen_self=yes
450 |     lt_cv_dlopen=dlopen
451 |     lt_cv_dlopen_libs=
452 |     lt_cv_dlopen_self=no
457 | 	  [lt_cv_dlopen=shl_load],
459 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
460 | 	[AC_CHECK_FUNC([dlopen],
461 | 	      [lt_cv_dlopen=dlopen],
462 | 	  [AC_CHECK_LIB([dl], [dlopen],
463 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
464 | 	    [AC_CHECK_LIB([svld], [dlopen],
465 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
467 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
476 |   if test no = "$lt_cv_dlopen"; then
477 |     enable_dlopen=no
479 |     enable_dlopen=yes
482 |   case $lt_cv_dlopen in
483 |   dlopen)
491 |     LIBS="$lt_cv_dlopen_libs $LIBS"
493 |     AC_CACHE_CHECK([whether a program can dlopen itself],
494 | 	  lt_cv_dlopen_self, [dnl
495 | 	  _LT_TRY_DLOPEN_SELF(
496 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
497 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
500 |     if test yes = "$lt_cv_dlopen_self"; then
502 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
503 | 	  lt_cv_dlopen_self_static, [dnl
504 | 	  _LT_TRY_DLOPEN_SELF(
505 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
506 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
516 |   case $lt_cv_dlopen_self in
517 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
518 |   *) enable_dlopen_self=unknown ;;
521 |   case $lt_cv_dlopen_self_static in
522 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
523 |   *) enable_dlopen_self_static=unknown ;;
526 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
527 | 	 [Whether dlopen is supported])
528 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
529 | 	 [Whether dlopen of programs is supported])
530 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
531 | 	 [Whether dlopen of statically linked programs is supported])
533 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1134 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1135 |   [lt_cv_sys_dlopen_deplibs],
1136 |   [# PORTME does your system automatically load deplibs for dlopen?
1140 |   lt_cv_sys_dlopen_deplibs=unknown
1145 |     lt_cv_sys_dlopen_deplibs=unknown
1148 |     lt_cv_sys_dlopen_deplibs=yes
1153 |       lt_cv_sys_dlopen_deplibs=no
1158 |     lt_cv_sys_dlopen_deplibs=yes
1163 |     lt_cv_sys_dlopen_deplibs=yes
1166 |     lt_cv_sys_dlopen_deplibs=yes
1170 |     lt_cv_sys_dlopen_deplibs=yes
1173 |     lt_cv_sys_dlopen_deplibs=yes
1176 |     lt_cv_sys_dlopen_deplibs=yes
1181 |     lt_cv_sys_dlopen_deplibs=unknown
1185 |     # at 6.2 and later dlopen does load deplibs.
1186 |     lt_cv_sys_dlopen_deplibs=yes
1189 |     lt_cv_sys_dlopen_deplibs=yes
1192 |     lt_cv_sys_dlopen_deplibs=yes
1195 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1198 |     lt_cv_sys_dlopen_deplibs=no
1201 |     # dlopen *does* load deplibs and with the right loader patch applied
1207 |     lt_cv_sys_dlopen_deplibs=unknown
1214 |     lt_cv_sys_dlopen_deplibs=yes
1217 |     lt_cv_sys_dlopen_deplibs=yes
1220 |     lt_cv_sys_dlopen_deplibs=yes
1223 |     libltdl_cv_sys_dlopen_deplibs=yes
1227 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1228 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1229 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1232 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1235 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1307 | LIBADD_DLOPEN=
1308 | AC_SEARCH_LIBS([dlopen], [dl],
1311 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1312 | 	  LIBADD_DLOPEN=-ldl
1314 | 	libltdl_cv_lib_dl_dlopen=yes
1315 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1319 |     ]], [[dlopen(0, 0);]])],
1322 | 	    libltdl_cv_func_dlopen=yes
1323 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1324 | 	[AC_CHECK_LIB([svld], [dlopen],
1327 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1328 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1329 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1332 |   LIBS="$LIBS $LIBADD_DLOPEN"
1336 | AC_SUBST([LIBADD_DLOPEN])
1342 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1346 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1356 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1359 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1363 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1370 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1386 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1438 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
1443 |       LIBS="$LIBS $LIBADD_DLOPEN"
1501 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1543 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5834 | m4trace:configure.ac:267: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### armci/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
4127 | m4trace:m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
4128 | if test yes != "$enable_dlopen"; then
4129 |   enable_dlopen=unknown
4130 |   enable_dlopen_self=unknown
4131 |   enable_dlopen_self_static=unknown
4133 |   lt_cv_dlopen=no
4134 |   lt_cv_dlopen_libs=
4138 |     lt_cv_dlopen=load_add_on
4139 |     lt_cv_dlopen_libs=
4140 |     lt_cv_dlopen_self=yes
4144 |     lt_cv_dlopen=LoadLibrary
4145 |     lt_cv_dlopen_libs=
4149 |     lt_cv_dlopen=dlopen
4150 |     lt_cv_dlopen_libs=
4155 |     AC_CHECK_LIB([dl], [dlopen],
4156 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
4157 |     lt_cv_dlopen=dyld
4158 |     lt_cv_dlopen_libs=
4159 |     lt_cv_dlopen_self=yes
4166 |     lt_cv_dlopen=dlopen
4167 |     lt_cv_dlopen_libs=
4168 |     lt_cv_dlopen_self=no
4173 | 	  [lt_cv_dlopen=shl_load],
4175 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
4176 | 	[AC_CHECK_FUNC([dlopen],
4177 | 	      [lt_cv_dlopen=dlopen],
4178 | 	  [AC_CHECK_LIB([dl], [dlopen],
4179 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
4180 | 	    [AC_CHECK_LIB([svld], [dlopen],
4181 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
4183 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
4192 |   if test no = "$lt_cv_dlopen"; then
4193 |     enable_dlopen=no
4195 |     enable_dlopen=yes
4198 |   case $lt_cv_dlopen in
4199 |   dlopen)
4207 |     LIBS="$lt_cv_dlopen_libs $LIBS"
4209 |     AC_CACHE_CHECK([whether a program can dlopen itself],
4210 | 	  lt_cv_dlopen_self, [dnl
4211 | 	  _LT_TRY_DLOPEN_SELF(
4212 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
4213 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
4216 |     if test yes = "$lt_cv_dlopen_self"; then
4218 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
4219 | 	  lt_cv_dlopen_self_static, [dnl
4220 | 	  _LT_TRY_DLOPEN_SELF(
4221 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
4222 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
4232 |   case $lt_cv_dlopen_self in
4233 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
4234 |   *) enable_dlopen_self=unknown ;;
4237 |   case $lt_cv_dlopen_self_static in
4238 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
4239 |   *) enable_dlopen_self_static=unknown ;;
4242 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
4243 | 	 [Whether dlopen is supported])
4244 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
4245 | 	 [Whether dlopen of programs is supported])
4246 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
4247 | 	 [Whether dlopen of statically linked programs is supported])
4249 | m4trace:m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4250 | m4trace:m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
4252 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4561 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
4564 | put the 'dlopen' option into LT_INIT's first parameter.])
4566 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
4568 | _LT_SET_OPTION([LT_INIT], [dlopen])
4571 | put the 'dlopen' option into LT_INIT's first parameter.])
4663 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5834 | m4trace:configure.ac:267: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### armci/m4/libtool.m4

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
### armci/m4/ltoptions.m4

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
### armci/build-aux/ltmain.sh

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
### autom4te.cache/output.0

```

{% raw %}
30539 |         enable_dlopen=no
34181 |   if test yes != "$enable_dlopen"; then
34182 |   enable_dlopen=unknown
34183 |   enable_dlopen_self=unknown
34184 |   enable_dlopen_self_static=unknown
34186 |   lt_cv_dlopen=no
34187 |   lt_cv_dlopen_libs=
34191 |     lt_cv_dlopen=load_add_on
34192 |     lt_cv_dlopen_libs=
34193 |     lt_cv_dlopen_self=yes
34197 |     lt_cv_dlopen=LoadLibrary
34198 |     lt_cv_dlopen_libs=
34202 |     lt_cv_dlopen=dlopen
34203 |     lt_cv_dlopen_libs=
34208 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34209 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34210 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34224 | char dlopen ();
34236 | return dlopen ();
34242 |   ac_cv_lib_dl_dlopen=yes
34244 |   ac_cv_lib_dl_dlopen=no
34250 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34251 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34252 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34253 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34256 |     lt_cv_dlopen=dyld
34257 |     lt_cv_dlopen_libs=
34258 |     lt_cv_dlopen_self=yes
34267 |     lt_cv_dlopen=dlopen
34268 |     lt_cv_dlopen_libs=
34269 |     lt_cv_dlopen_self=no
34275 |   lt_cv_dlopen=shl_load
34322 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
34324 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
34325 | if test "x$ac_cv_func_dlopen" = xyes; then :
34326 |   lt_cv_dlopen=dlopen
34328 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34329 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34330 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34344 | char dlopen ();
34356 | return dlopen ();
34362 |   ac_cv_lib_dl_dlopen=yes
34364 |   ac_cv_lib_dl_dlopen=no
34370 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34371 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34372 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34373 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34375 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
34376 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
34377 | if ${ac_cv_lib_svld_dlopen+:} false; then :
34391 | char dlopen ();
34403 | return dlopen ();
34409 |   ac_cv_lib_svld_dlopen=yes
34411 |   ac_cv_lib_svld_dlopen=no
34417 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
34418 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
34419 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
34420 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
34467 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
34488 |   if test no = "$lt_cv_dlopen"; then
34489 |     enable_dlopen=no
34491 |     enable_dlopen=yes
34494 |   case $lt_cv_dlopen in
34495 |   dlopen)
34503 |     LIBS="$lt_cv_dlopen_libs $LIBS"
34505 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
34506 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
34507 | if ${lt_cv_dlopen_self+:} false; then :
34511 |   lt_cv_dlopen_self=cross
34566 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34593 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
34594 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
34595 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
34599 |     lt_cv_dlopen_self=no
34606 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
34607 | $as_echo "$lt_cv_dlopen_self" >&6; }
34609 |     if test yes = "$lt_cv_dlopen_self"; then
34611 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
34612 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
34613 | if ${lt_cv_dlopen_self_static+:} false; then :
34617 |   lt_cv_dlopen_self_static=cross
34672 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34699 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
34700 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
34701 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
34705 |     lt_cv_dlopen_self_static=no
34712 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
34713 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
34722 |   case $lt_cv_dlopen_self in
34723 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
34724 |   *) enable_dlopen_self=unknown ;;
34727 |   case $lt_cv_dlopen_self_static in
34728 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
34729 |   *) enable_dlopen_self_static=unknown ;;
42903 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
42904 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
42905 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
44245 | # Whether dlopen is supported.
44246 | dlopen_support=$enable_dlopen
44248 | # Whether dlopen of programs is supported.
44249 | dlopen_self=$enable_dlopen_self
44251 | # Whether dlopen of statically linked programs is supported.
44252 | dlopen_self_static=$enable_dlopen_self_static
44296 | # Compiler flag to allow reflexive dlopens.
44538 | # Compiler flag to allow reflexive dlopens.
44691 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.1

```

{% raw %}
30539 |         enable_dlopen=no
34181 |   if test yes != "$enable_dlopen"; then
34182 |   enable_dlopen=unknown
34183 |   enable_dlopen_self=unknown
34184 |   enable_dlopen_self_static=unknown
34186 |   lt_cv_dlopen=no
34187 |   lt_cv_dlopen_libs=
34191 |     lt_cv_dlopen=load_add_on
34192 |     lt_cv_dlopen_libs=
34193 |     lt_cv_dlopen_self=yes
34197 |     lt_cv_dlopen=LoadLibrary
34198 |     lt_cv_dlopen_libs=
34202 |     lt_cv_dlopen=dlopen
34203 |     lt_cv_dlopen_libs=
34208 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34209 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34210 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34224 | char dlopen ();
34236 | return dlopen ();
34242 |   ac_cv_lib_dl_dlopen=yes
34244 |   ac_cv_lib_dl_dlopen=no
34250 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34251 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34252 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34253 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34256 |     lt_cv_dlopen=dyld
34257 |     lt_cv_dlopen_libs=
34258 |     lt_cv_dlopen_self=yes
34267 |     lt_cv_dlopen=dlopen
34268 |     lt_cv_dlopen_libs=
34269 |     lt_cv_dlopen_self=no
34275 |   lt_cv_dlopen=shl_load
34322 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
34324 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
34325 | if test "x$ac_cv_func_dlopen" = xyes; then :
34326 |   lt_cv_dlopen=dlopen
34328 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34329 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34330 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34344 | char dlopen ();
34356 | return dlopen ();
34362 |   ac_cv_lib_dl_dlopen=yes
34364 |   ac_cv_lib_dl_dlopen=no
34370 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34371 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34372 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34373 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34375 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
34376 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
34377 | if ${ac_cv_lib_svld_dlopen+:} false; then :
34391 | char dlopen ();
34403 | return dlopen ();
34409 |   ac_cv_lib_svld_dlopen=yes
34411 |   ac_cv_lib_svld_dlopen=no
34417 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
34418 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
34419 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
34420 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
34467 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
34488 |   if test no = "$lt_cv_dlopen"; then
34489 |     enable_dlopen=no
34491 |     enable_dlopen=yes
34494 |   case $lt_cv_dlopen in
34495 |   dlopen)
34503 |     LIBS="$lt_cv_dlopen_libs $LIBS"
34505 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
34506 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
34507 | if ${lt_cv_dlopen_self+:} false; then :
34511 |   lt_cv_dlopen_self=cross
34566 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34593 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
34594 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
34595 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
34599 |     lt_cv_dlopen_self=no
34606 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
34607 | $as_echo "$lt_cv_dlopen_self" >&6; }
34609 |     if test yes = "$lt_cv_dlopen_self"; then
34611 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
34612 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
34613 | if ${lt_cv_dlopen_self_static+:} false; then :
34617 |   lt_cv_dlopen_self_static=cross
34672 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34699 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
34700 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
34701 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
34705 |     lt_cv_dlopen_self_static=no
34712 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
34713 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
34722 |   case $lt_cv_dlopen_self in
34723 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
34724 |   *) enable_dlopen_self=unknown ;;
34727 |   case $lt_cv_dlopen_self_static in
34728 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
34729 |   *) enable_dlopen_self_static=unknown ;;
42903 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
42904 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
42905 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
44245 | # Whether dlopen is supported.
44246 | dlopen_support=$enable_dlopen
44248 | # Whether dlopen of programs is supported.
44249 | dlopen_self=$enable_dlopen_self
44251 | # Whether dlopen of statically linked programs is supported.
44252 | dlopen_self_static=$enable_dlopen_self_static
44296 | # Compiler flag to allow reflexive dlopens.
44538 | # Compiler flag to allow reflexive dlopens.
44691 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/output.2

```

{% raw %}
30539 |         enable_dlopen=no
34181 |   if test yes != "$enable_dlopen"; then
34182 |   enable_dlopen=unknown
34183 |   enable_dlopen_self=unknown
34184 |   enable_dlopen_self_static=unknown
34186 |   lt_cv_dlopen=no
34187 |   lt_cv_dlopen_libs=
34191 |     lt_cv_dlopen=load_add_on
34192 |     lt_cv_dlopen_libs=
34193 |     lt_cv_dlopen_self=yes
34197 |     lt_cv_dlopen=LoadLibrary
34198 |     lt_cv_dlopen_libs=
34202 |     lt_cv_dlopen=dlopen
34203 |     lt_cv_dlopen_libs=
34208 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34209 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34210 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34224 | char dlopen ();
34236 | return dlopen ();
34242 |   ac_cv_lib_dl_dlopen=yes
34244 |   ac_cv_lib_dl_dlopen=no
34250 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34251 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34252 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34253 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34256 |     lt_cv_dlopen=dyld
34257 |     lt_cv_dlopen_libs=
34258 |     lt_cv_dlopen_self=yes
34267 |     lt_cv_dlopen=dlopen
34268 |     lt_cv_dlopen_libs=
34269 |     lt_cv_dlopen_self=no
34275 |   lt_cv_dlopen=shl_load
34322 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
34324 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
34325 | if test "x$ac_cv_func_dlopen" = xyes; then :
34326 |   lt_cv_dlopen=dlopen
34328 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34329 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34330 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34344 | char dlopen ();
34356 | return dlopen ();
34362 |   ac_cv_lib_dl_dlopen=yes
34364 |   ac_cv_lib_dl_dlopen=no
34370 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34371 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34372 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34373 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34375 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
34376 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
34377 | if ${ac_cv_lib_svld_dlopen+:} false; then :
34391 | char dlopen ();
34403 | return dlopen ();
34409 |   ac_cv_lib_svld_dlopen=yes
34411 |   ac_cv_lib_svld_dlopen=no
34417 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
34418 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
34419 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
34420 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
34467 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
34488 |   if test no = "$lt_cv_dlopen"; then
34489 |     enable_dlopen=no
34491 |     enable_dlopen=yes
34494 |   case $lt_cv_dlopen in
34495 |   dlopen)
34503 |     LIBS="$lt_cv_dlopen_libs $LIBS"
34505 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
34506 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
34507 | if ${lt_cv_dlopen_self+:} false; then :
34511 |   lt_cv_dlopen_self=cross
34566 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34593 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
34594 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
34595 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
34599 |     lt_cv_dlopen_self=no
34606 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
34607 | $as_echo "$lt_cv_dlopen_self" >&6; }
34609 |     if test yes = "$lt_cv_dlopen_self"; then
34611 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
34612 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
34613 | if ${lt_cv_dlopen_self_static+:} false; then :
34617 |   lt_cv_dlopen_self_static=cross
34672 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34699 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
34700 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
34701 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
34705 |     lt_cv_dlopen_self_static=no
34712 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
34713 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
34722 |   case $lt_cv_dlopen_self in
34723 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
34724 |   *) enable_dlopen_self=unknown ;;
34727 |   case $lt_cv_dlopen_self_static in
34728 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
34729 |   *) enable_dlopen_self_static=unknown ;;
42903 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
42904 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
42905 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
44245 | # Whether dlopen is supported.
44246 | dlopen_support=$enable_dlopen
44248 | # Whether dlopen of programs is supported.
44249 | dlopen_self=$enable_dlopen_self
44251 | # Whether dlopen of statically linked programs is supported.
44252 | dlopen_self_static=$enable_dlopen_self_static
44296 | # Compiler flag to allow reflexive dlopens.
44538 | # Compiler flag to allow reflexive dlopens.
44691 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
412 | if test yes != "$enable_dlopen"; then
413 |   enable_dlopen=unknown
414 |   enable_dlopen_self=unknown
415 |   enable_dlopen_self_static=unknown
417 |   lt_cv_dlopen=no
418 |   lt_cv_dlopen_libs=
422 |     lt_cv_dlopen=load_add_on
423 |     lt_cv_dlopen_libs=
424 |     lt_cv_dlopen_self=yes
428 |     lt_cv_dlopen=LoadLibrary
429 |     lt_cv_dlopen_libs=
433 |     lt_cv_dlopen=dlopen
434 |     lt_cv_dlopen_libs=
439 |     AC_CHECK_LIB([dl], [dlopen],
440 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
441 |     lt_cv_dlopen=dyld
442 |     lt_cv_dlopen_libs=
443 |     lt_cv_dlopen_self=yes
450 |     lt_cv_dlopen=dlopen
451 |     lt_cv_dlopen_libs=
452 |     lt_cv_dlopen_self=no
457 | 	  [lt_cv_dlopen=shl_load],
459 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
460 | 	[AC_CHECK_FUNC([dlopen],
461 | 	      [lt_cv_dlopen=dlopen],
462 | 	  [AC_CHECK_LIB([dl], [dlopen],
463 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
464 | 	    [AC_CHECK_LIB([svld], [dlopen],
465 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
467 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
476 |   if test no = "$lt_cv_dlopen"; then
477 |     enable_dlopen=no
479 |     enable_dlopen=yes
482 |   case $lt_cv_dlopen in
483 |   dlopen)
491 |     LIBS="$lt_cv_dlopen_libs $LIBS"
493 |     AC_CACHE_CHECK([whether a program can dlopen itself],
494 | 	  lt_cv_dlopen_self, [dnl
495 | 	  _LT_TRY_DLOPEN_SELF(
496 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
497 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
500 |     if test yes = "$lt_cv_dlopen_self"; then
502 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
503 | 	  lt_cv_dlopen_self_static, [dnl
504 | 	  _LT_TRY_DLOPEN_SELF(
505 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
506 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
516 |   case $lt_cv_dlopen_self in
517 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
518 |   *) enable_dlopen_self=unknown ;;
521 |   case $lt_cv_dlopen_self_static in
522 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
523 |   *) enable_dlopen_self_static=unknown ;;
526 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
527 | 	 [Whether dlopen is supported])
528 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
529 | 	 [Whether dlopen of programs is supported])
530 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
531 | 	 [Whether dlopen of statically linked programs is supported])
533 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
1134 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
1135 |   [lt_cv_sys_dlopen_deplibs],
1136 |   [# PORTME does your system automatically load deplibs for dlopen?
1140 |   lt_cv_sys_dlopen_deplibs=unknown
1145 |     lt_cv_sys_dlopen_deplibs=unknown
1148 |     lt_cv_sys_dlopen_deplibs=yes
1153 |       lt_cv_sys_dlopen_deplibs=no
1158 |     lt_cv_sys_dlopen_deplibs=yes
1163 |     lt_cv_sys_dlopen_deplibs=yes
1166 |     lt_cv_sys_dlopen_deplibs=yes
1170 |     lt_cv_sys_dlopen_deplibs=yes
1173 |     lt_cv_sys_dlopen_deplibs=yes
1176 |     lt_cv_sys_dlopen_deplibs=yes
1181 |     lt_cv_sys_dlopen_deplibs=unknown
1185 |     # at 6.2 and later dlopen does load deplibs.
1186 |     lt_cv_sys_dlopen_deplibs=yes
1189 |     lt_cv_sys_dlopen_deplibs=yes
1192 |     lt_cv_sys_dlopen_deplibs=yes
1195 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
1198 |     lt_cv_sys_dlopen_deplibs=no
1201 |     # dlopen *does* load deplibs and with the right loader patch applied
1207 |     lt_cv_sys_dlopen_deplibs=unknown
1214 |     lt_cv_sys_dlopen_deplibs=yes
1217 |     lt_cv_sys_dlopen_deplibs=yes
1220 |     lt_cv_sys_dlopen_deplibs=yes
1223 |     libltdl_cv_sys_dlopen_deplibs=yes
1227 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
1228 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
1229 |     [Define if the OS needs help to load dependent libraries for dlopen().])
1232 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
1235 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1307 | LIBADD_DLOPEN=
1308 | AC_SEARCH_LIBS([dlopen], [dl],
1311 | 	if test "$ac_cv_search_dlopen" != "none required"; then
1312 | 	  LIBADD_DLOPEN=-ldl
1314 | 	libltdl_cv_lib_dl_dlopen=yes
1315 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1319 |     ]], [[dlopen(0, 0);]])],
1322 | 	    libltdl_cv_func_dlopen=yes
1323 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
1324 | 	[AC_CHECK_LIB([svld], [dlopen],
1327 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
1328 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
1329 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
1332 |   LIBS="$LIBS $LIBADD_DLOPEN"
1336 | AC_SUBST([LIBADD_DLOPEN])
1342 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
1346 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
1356 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
1359 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
1363 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
1370 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
1386 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
1438 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
1443 |       LIBS="$LIBS $LIBADD_DLOPEN"
1501 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
1543 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
7697 | m4trace:configure.ac:494: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
290 | AC_CACHE_CHECK([whether deplibs are loaded by dlopen],
291 |   [lt_cv_sys_dlopen_deplibs],
292 |   [# PORTME does your system automatically load deplibs for dlopen?
296 |   lt_cv_sys_dlopen_deplibs=unknown
301 |     lt_cv_sys_dlopen_deplibs=unknown
304 |     lt_cv_sys_dlopen_deplibs=yes
309 |       lt_cv_sys_dlopen_deplibs=no
314 |     lt_cv_sys_dlopen_deplibs=yes
319 |     lt_cv_sys_dlopen_deplibs=yes
322 |     lt_cv_sys_dlopen_deplibs=yes
326 |     lt_cv_sys_dlopen_deplibs=yes
329 |     lt_cv_sys_dlopen_deplibs=yes
332 |     lt_cv_sys_dlopen_deplibs=yes
337 |     lt_cv_sys_dlopen_deplibs=unknown
341 |     # at 6.2 and later dlopen does load deplibs.
342 |     lt_cv_sys_dlopen_deplibs=yes
345 |     lt_cv_sys_dlopen_deplibs=yes
348 |     lt_cv_sys_dlopen_deplibs=yes
351 |     # dlopen did load deplibs (at least at 4.x), but until the 5.x series,
354 |     lt_cv_sys_dlopen_deplibs=no
357 |     # dlopen *does* load deplibs and with the right loader patch applied
363 |     lt_cv_sys_dlopen_deplibs=unknown
370 |     lt_cv_sys_dlopen_deplibs=yes
373 |     lt_cv_sys_dlopen_deplibs=yes
376 |     lt_cv_sys_dlopen_deplibs=yes
379 |     libltdl_cv_sys_dlopen_deplibs=yes
383 | if test yes != "$lt_cv_sys_dlopen_deplibs"; then
384 |  AC_DEFINE([LTDL_DLOPEN_DEPLIBS], [1],
385 |     [Define if the OS needs help to load dependent libraries for dlopen().])
388 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.4/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
391 | m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
463 | LIBADD_DLOPEN=
464 | AC_SEARCH_LIBS([dlopen], [dl],
467 | 	if test "$ac_cv_search_dlopen" != "none required"; then
468 | 	  LIBADD_DLOPEN=-ldl
470 | 	libltdl_cv_lib_dl_dlopen=yes
471 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
475 |     ]], [[dlopen(0, 0);]])],
478 | 	    libltdl_cv_func_dlopen=yes
479 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"],
480 | 	[AC_CHECK_LIB([svld], [dlopen],
483 | 	        LIBADD_DLOPEN=-lsvld libltdl_cv_func_dlopen=yes
484 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dlopen.la"])])])
485 | if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"
488 |   LIBS="$LIBS $LIBADD_DLOPEN"
492 | AC_SUBST([LIBADD_DLOPEN])
498 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"],
502 | 	    LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}shl_load.la"
512 | 	LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dyld.la"])
515 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}load_add_on.la"
519 |   LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}loadlibrary.la"
526 | 		LT_DLLOADERS="$LT_DLLOADERS ${lt_dlopen_dir+$lt_dlopen_dir/}dld_link.la"])
542 | LIBADD_DL="$LIBADD_DLOPEN $LIBADD_SHL_LOAD"
594 |   if test yes = "$libltdl_cv_func_dlopen" || test yes = "$libltdl_cv_lib_dl_dlopen"; then
599 |       LIBS="$LIBS $LIBADD_DLOPEN"
657 |   void *handle = dlopen ("`pwd`/$libname$libltdl_cv_shlibext", RTLD_GLOBAL|RTLD_NOW);
5530 | m4trace:m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
5531 | if test yes != "$enable_dlopen"; then
5532 |   enable_dlopen=unknown
5533 |   enable_dlopen_self=unknown
5534 |   enable_dlopen_self_static=unknown
5536 |   lt_cv_dlopen=no
5537 |   lt_cv_dlopen_libs=
5541 |     lt_cv_dlopen=load_add_on
5542 |     lt_cv_dlopen_libs=
5543 |     lt_cv_dlopen_self=yes
5547 |     lt_cv_dlopen=LoadLibrary
5548 |     lt_cv_dlopen_libs=
5552 |     lt_cv_dlopen=dlopen
5553 |     lt_cv_dlopen_libs=
5558 |     AC_CHECK_LIB([dl], [dlopen],
5559 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
5560 |     lt_cv_dlopen=dyld
5561 |     lt_cv_dlopen_libs=
5562 |     lt_cv_dlopen_self=yes
5569 |     lt_cv_dlopen=dlopen
5570 |     lt_cv_dlopen_libs=
5571 |     lt_cv_dlopen_self=no
5576 | 	  [lt_cv_dlopen=shl_load],
5578 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
5579 | 	[AC_CHECK_FUNC([dlopen],
5580 | 	      [lt_cv_dlopen=dlopen],
5581 | 	  [AC_CHECK_LIB([dl], [dlopen],
5582 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
5583 | 	    [AC_CHECK_LIB([svld], [dlopen],
5584 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
5586 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
5595 |   if test no = "$lt_cv_dlopen"; then
5596 |     enable_dlopen=no
5598 |     enable_dlopen=yes
5601 |   case $lt_cv_dlopen in
5602 |   dlopen)
5610 |     LIBS="$lt_cv_dlopen_libs $LIBS"
5612 |     AC_CACHE_CHECK([whether a program can dlopen itself],
5613 | 	  lt_cv_dlopen_self, [dnl
5614 | 	  _LT_TRY_DLOPEN_SELF(
5615 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
5616 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
5619 |     if test yes = "$lt_cv_dlopen_self"; then
5621 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
5622 | 	  lt_cv_dlopen_self_static, [dnl
5623 | 	  _LT_TRY_DLOPEN_SELF(
5624 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
5625 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
5635 |   case $lt_cv_dlopen_self in
5636 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
5637 |   *) enable_dlopen_self=unknown ;;
5640 |   case $lt_cv_dlopen_self_static in
5641 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
5642 |   *) enable_dlopen_self_static=unknown ;;
5645 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
5646 | 	 [Whether dlopen is supported])
5647 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
5648 | 	 [Whether dlopen of programs is supported])
5649 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
5650 | 	 [Whether dlopen of statically linked programs is supported])
5652 | m4trace:m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
5653 | m4trace:m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
5655 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
5964 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
5967 | put the 'dlopen' option into LT_INIT's first parameter.])
5969 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
5971 | _LT_SET_OPTION([LT_INIT], [dlopen])
5974 | put the 'dlopen' option into LT_INIT's first parameter.])
6066 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
7697 | m4trace:configure.ac:494: -1- LT_SYS_DLOPEN_SELF
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