---
name: "nwchem"
layout: package
next_package: tixi
previous_package: efivar
languages: ['cpp', 'bash']
---
## 6.8.1
26 / 20838 files match

 - [src/cca/aclocal.m4](#srcccaaclocalm4)
 - [src/tools/ga-5.6.5/comex/autom4te.cache/output.0](#srctoolsga-565comexautom4tecacheoutput0)
 - [src/tools/ga-5.6.5/comex/autom4te.cache/output.1](#srctoolsga-565comexautom4tecacheoutput1)
 - [src/tools/ga-5.6.5/comex/autom4te.cache/output.2](#srctoolsga-565comexautom4tecacheoutput2)
 - [src/tools/ga-5.6.5/comex/autom4te.cache/traces.0](#srctoolsga-565comexautom4tecachetraces0)
 - [src/tools/ga-5.6.5/comex/autom4te.cache/traces.2](#srctoolsga-565comexautom4tecachetraces2)
 - [src/tools/ga-5.6.5/comex/m4/libtool.m4](#srctoolsga-565comexm4libtoolm4)
 - [src/tools/ga-5.6.5/comex/m4/ltoptions.m4](#srctoolsga-565comexm4ltoptionsm4)
 - [src/tools/ga-5.6.5/comex/build-aux/ltmain.sh](#srctoolsga-565comexbuild-auxltmainsh)
 - [src/tools/ga-5.6.5/comex/src-ofi/ofi.h](#srctoolsga-565comexsrc-ofiofih)
 - [src/tools/ga-5.6.5/armci/autom4te.cache/output.0](#srctoolsga-565armciautom4tecacheoutput0)
 - [src/tools/ga-5.6.5/armci/autom4te.cache/output.1](#srctoolsga-565armciautom4tecacheoutput1)
 - [src/tools/ga-5.6.5/armci/autom4te.cache/output.2](#srctoolsga-565armciautom4tecacheoutput2)
 - [src/tools/ga-5.6.5/armci/autom4te.cache/traces.0](#srctoolsga-565armciautom4tecachetraces0)
 - [src/tools/ga-5.6.5/armci/autom4te.cache/traces.2](#srctoolsga-565armciautom4tecachetraces2)
 - [src/tools/ga-5.6.5/armci/m4/libtool.m4](#srctoolsga-565armcim4libtoolm4)
 - [src/tools/ga-5.6.5/armci/m4/ltoptions.m4](#srctoolsga-565armcim4ltoptionsm4)
 - [src/tools/ga-5.6.5/armci/build-aux/ltmain.sh](#srctoolsga-565armcibuild-auxltmainsh)
 - [src/tools/ga-5.6.5/autom4te.cache/output.0](#srctoolsga-565autom4tecacheoutput0)
 - [src/tools/ga-5.6.5/autom4te.cache/output.1](#srctoolsga-565autom4tecacheoutput1)
 - [src/tools/ga-5.6.5/autom4te.cache/output.2](#srctoolsga-565autom4tecacheoutput2)
 - [src/tools/ga-5.6.5/autom4te.cache/traces.0](#srctoolsga-565autom4tecachetraces0)
 - [src/tools/ga-5.6.5/autom4te.cache/traces.2](#srctoolsga-565autom4tecachetraces2)
 - [src/tools/ga-5.6.5/m4/libtool.m4](#srctoolsga-565m4libtoolm4)
 - [src/tools/ga-5.6.5/m4/ltoptions.m4](#srctoolsga-565m4ltoptionsm4)
 - [src/tools/ga-5.6.5/build-aux/ltmain.sh](#srctoolsga-565build-auxltmainsh)

### src/cca/aclocal.m4

```

{% raw %}
545 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### src/tools/ga-5.6.5/comex/autom4te.cache/output.0

```

{% raw %}
20605 |         enable_dlopen=no
24223 |   if test yes != "$enable_dlopen"; then
24224 |   enable_dlopen=unknown
24225 |   enable_dlopen_self=unknown
24226 |   enable_dlopen_self_static=unknown
24228 |   lt_cv_dlopen=no
24229 |   lt_cv_dlopen_libs=
24233 |     lt_cv_dlopen=load_add_on
24234 |     lt_cv_dlopen_libs=
24235 |     lt_cv_dlopen_self=yes
24239 |     lt_cv_dlopen=LoadLibrary
24240 |     lt_cv_dlopen_libs=
24244 |     lt_cv_dlopen=dlopen
24245 |     lt_cv_dlopen_libs=
24250 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24251 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24252 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24266 | char dlopen ();
24270 | return dlopen ();
24276 |   ac_cv_lib_dl_dlopen=yes
24278 |   ac_cv_lib_dl_dlopen=no
24284 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24285 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24286 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24287 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24290 |     lt_cv_dlopen=dyld
24291 |     lt_cv_dlopen_libs=
24292 |     lt_cv_dlopen_self=yes
24301 |     lt_cv_dlopen=dlopen
24302 |     lt_cv_dlopen_libs=
24303 |     lt_cv_dlopen_self=no
24309 |   lt_cv_dlopen=shl_load
24348 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
24350 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
24351 | if test "x$ac_cv_func_dlopen" = xyes; then :
24352 |   lt_cv_dlopen=dlopen
24354 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24355 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24356 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24370 | char dlopen ();
24374 | return dlopen ();
24380 |   ac_cv_lib_dl_dlopen=yes
24382 |   ac_cv_lib_dl_dlopen=no
24388 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24389 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24390 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24391 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24393 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
24394 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
24395 | if ${ac_cv_lib_svld_dlopen+:} false; then :
24409 | char dlopen ();
24413 | return dlopen ();
24419 |   ac_cv_lib_svld_dlopen=yes
24421 |   ac_cv_lib_svld_dlopen=no
24427 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
24428 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
24429 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
24430 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
24469 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
24490 |   if test no = "$lt_cv_dlopen"; then
24491 |     enable_dlopen=no
24493 |     enable_dlopen=yes
24496 |   case $lt_cv_dlopen in
24497 |   dlopen)
24505 |     LIBS="$lt_cv_dlopen_libs $LIBS"
24507 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
24508 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
24509 | if ${lt_cv_dlopen_self+:} false; then :
24513 |   lt_cv_dlopen_self=cross
24568 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24595 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
24596 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
24597 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
24601 |     lt_cv_dlopen_self=no
24608 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
24609 | $as_echo "$lt_cv_dlopen_self" >&6; }
24611 |     if test yes = "$lt_cv_dlopen_self"; then
24613 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
24614 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
24615 | if ${lt_cv_dlopen_self_static+:} false; then :
24619 |   lt_cv_dlopen_self_static=cross
24674 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24701 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
24702 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
24703 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
24707 |     lt_cv_dlopen_self_static=no
24714 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
24715 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
24724 |   case $lt_cv_dlopen_self in
24725 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
24726 |   *) enable_dlopen_self=unknown ;;
24729 |   case $lt_cv_dlopen_self_static in
24730 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
24731 |   *) enable_dlopen_self_static=unknown ;;
25854 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25855 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25856 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27008 | # Whether dlopen is supported.
27009 | dlopen_support=$enable_dlopen
27011 | # Whether dlopen of programs is supported.
27012 | dlopen_self=$enable_dlopen_self
27014 | # Whether dlopen of statically linked programs is supported.
27015 | dlopen_self_static=$enable_dlopen_self_static
27059 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/comex/autom4te.cache/output.1

```

{% raw %}
20605 |         enable_dlopen=no
24223 |   if test yes != "$enable_dlopen"; then
24224 |   enable_dlopen=unknown
24225 |   enable_dlopen_self=unknown
24226 |   enable_dlopen_self_static=unknown
24228 |   lt_cv_dlopen=no
24229 |   lt_cv_dlopen_libs=
24233 |     lt_cv_dlopen=load_add_on
24234 |     lt_cv_dlopen_libs=
24235 |     lt_cv_dlopen_self=yes
24239 |     lt_cv_dlopen=LoadLibrary
24240 |     lt_cv_dlopen_libs=
24244 |     lt_cv_dlopen=dlopen
24245 |     lt_cv_dlopen_libs=
24250 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24251 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24252 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24266 | char dlopen ();
24270 | return dlopen ();
24276 |   ac_cv_lib_dl_dlopen=yes
24278 |   ac_cv_lib_dl_dlopen=no
24284 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24285 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24286 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24287 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24290 |     lt_cv_dlopen=dyld
24291 |     lt_cv_dlopen_libs=
24292 |     lt_cv_dlopen_self=yes
24301 |     lt_cv_dlopen=dlopen
24302 |     lt_cv_dlopen_libs=
24303 |     lt_cv_dlopen_self=no
24309 |   lt_cv_dlopen=shl_load
24348 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
24350 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
24351 | if test "x$ac_cv_func_dlopen" = xyes; then :
24352 |   lt_cv_dlopen=dlopen
24354 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24355 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24356 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24370 | char dlopen ();
24374 | return dlopen ();
24380 |   ac_cv_lib_dl_dlopen=yes
24382 |   ac_cv_lib_dl_dlopen=no
24388 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24389 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24390 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24391 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24393 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
24394 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
24395 | if ${ac_cv_lib_svld_dlopen+:} false; then :
24409 | char dlopen ();
24413 | return dlopen ();
24419 |   ac_cv_lib_svld_dlopen=yes
24421 |   ac_cv_lib_svld_dlopen=no
24427 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
24428 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
24429 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
24430 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
24469 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
24490 |   if test no = "$lt_cv_dlopen"; then
24491 |     enable_dlopen=no
24493 |     enable_dlopen=yes
24496 |   case $lt_cv_dlopen in
24497 |   dlopen)
24505 |     LIBS="$lt_cv_dlopen_libs $LIBS"
24507 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
24508 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
24509 | if ${lt_cv_dlopen_self+:} false; then :
24513 |   lt_cv_dlopen_self=cross
24568 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24595 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
24596 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
24597 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
24601 |     lt_cv_dlopen_self=no
24608 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
24609 | $as_echo "$lt_cv_dlopen_self" >&6; }
24611 |     if test yes = "$lt_cv_dlopen_self"; then
24613 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
24614 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
24615 | if ${lt_cv_dlopen_self_static+:} false; then :
24619 |   lt_cv_dlopen_self_static=cross
24674 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24701 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
24702 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
24703 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
24707 |     lt_cv_dlopen_self_static=no
24714 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
24715 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
24724 |   case $lt_cv_dlopen_self in
24725 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
24726 |   *) enable_dlopen_self=unknown ;;
24729 |   case $lt_cv_dlopen_self_static in
24730 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
24731 |   *) enable_dlopen_self_static=unknown ;;
25854 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25855 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25856 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27008 | # Whether dlopen is supported.
27009 | dlopen_support=$enable_dlopen
27011 | # Whether dlopen of programs is supported.
27012 | dlopen_self=$enable_dlopen_self
27014 | # Whether dlopen of statically linked programs is supported.
27015 | dlopen_self_static=$enable_dlopen_self_static
27059 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/comex/autom4te.cache/output.2

```

{% raw %}
20605 |         enable_dlopen=no
24223 |   if test yes != "$enable_dlopen"; then
24224 |   enable_dlopen=unknown
24225 |   enable_dlopen_self=unknown
24226 |   enable_dlopen_self_static=unknown
24228 |   lt_cv_dlopen=no
24229 |   lt_cv_dlopen_libs=
24233 |     lt_cv_dlopen=load_add_on
24234 |     lt_cv_dlopen_libs=
24235 |     lt_cv_dlopen_self=yes
24239 |     lt_cv_dlopen=LoadLibrary
24240 |     lt_cv_dlopen_libs=
24244 |     lt_cv_dlopen=dlopen
24245 |     lt_cv_dlopen_libs=
24250 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24251 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24252 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24266 | char dlopen ();
24270 | return dlopen ();
24276 |   ac_cv_lib_dl_dlopen=yes
24278 |   ac_cv_lib_dl_dlopen=no
24284 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24285 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24286 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24287 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24290 |     lt_cv_dlopen=dyld
24291 |     lt_cv_dlopen_libs=
24292 |     lt_cv_dlopen_self=yes
24301 |     lt_cv_dlopen=dlopen
24302 |     lt_cv_dlopen_libs=
24303 |     lt_cv_dlopen_self=no
24309 |   lt_cv_dlopen=shl_load
24348 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
24350 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
24351 | if test "x$ac_cv_func_dlopen" = xyes; then :
24352 |   lt_cv_dlopen=dlopen
24354 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
24355 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
24356 | if ${ac_cv_lib_dl_dlopen+:} false; then :
24370 | char dlopen ();
24374 | return dlopen ();
24380 |   ac_cv_lib_dl_dlopen=yes
24382 |   ac_cv_lib_dl_dlopen=no
24388 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
24389 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
24390 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
24391 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
24393 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
24394 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
24395 | if ${ac_cv_lib_svld_dlopen+:} false; then :
24409 | char dlopen ();
24413 | return dlopen ();
24419 |   ac_cv_lib_svld_dlopen=yes
24421 |   ac_cv_lib_svld_dlopen=no
24427 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
24428 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
24429 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
24430 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
24469 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
24490 |   if test no = "$lt_cv_dlopen"; then
24491 |     enable_dlopen=no
24493 |     enable_dlopen=yes
24496 |   case $lt_cv_dlopen in
24497 |   dlopen)
24505 |     LIBS="$lt_cv_dlopen_libs $LIBS"
24507 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
24508 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
24509 | if ${lt_cv_dlopen_self+:} false; then :
24513 |   lt_cv_dlopen_self=cross
24568 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24595 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
24596 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
24597 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
24601 |     lt_cv_dlopen_self=no
24608 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
24609 | $as_echo "$lt_cv_dlopen_self" >&6; }
24611 |     if test yes = "$lt_cv_dlopen_self"; then
24613 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
24614 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
24615 | if ${lt_cv_dlopen_self_static+:} false; then :
24619 |   lt_cv_dlopen_self_static=cross
24674 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
24701 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
24702 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
24703 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
24707 |     lt_cv_dlopen_self_static=no
24714 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
24715 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
24724 |   case $lt_cv_dlopen_self in
24725 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
24726 |   *) enable_dlopen_self=unknown ;;
24729 |   case $lt_cv_dlopen_self_static in
24730 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
24731 |   *) enable_dlopen_self_static=unknown ;;
25854 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
25855 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
25856 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
27008 | # Whether dlopen is supported.
27009 | dlopen_support=$enable_dlopen
27011 | # Whether dlopen of programs is supported.
27012 | dlopen_self=$enable_dlopen_self
27014 | # Whether dlopen of statically linked programs is supported.
27015 | dlopen_self_static=$enable_dlopen_self_static
27059 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/comex/autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
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
533 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
1232 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
1543 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4430 | m4trace:configure.ac:181: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/tools/ga-5.6.5/comex/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
388 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
3144 | m4trace:m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
3145 | if test yes != "$enable_dlopen"; then
3146 |   enable_dlopen=unknown
3147 |   enable_dlopen_self=unknown
3148 |   enable_dlopen_self_static=unknown
3150 |   lt_cv_dlopen=no
3151 |   lt_cv_dlopen_libs=
3155 |     lt_cv_dlopen=load_add_on
3156 |     lt_cv_dlopen_libs=
3157 |     lt_cv_dlopen_self=yes
3161 |     lt_cv_dlopen=LoadLibrary
3162 |     lt_cv_dlopen_libs=
3166 |     lt_cv_dlopen=dlopen
3167 |     lt_cv_dlopen_libs=
3172 |     AC_CHECK_LIB([dl], [dlopen],
3173 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
3174 |     lt_cv_dlopen=dyld
3175 |     lt_cv_dlopen_libs=
3176 |     lt_cv_dlopen_self=yes
3183 |     lt_cv_dlopen=dlopen
3184 |     lt_cv_dlopen_libs=
3185 |     lt_cv_dlopen_self=no
3190 | 	  [lt_cv_dlopen=shl_load],
3192 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
3193 | 	[AC_CHECK_FUNC([dlopen],
3194 | 	      [lt_cv_dlopen=dlopen],
3195 | 	  [AC_CHECK_LIB([dl], [dlopen],
3196 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
3197 | 	    [AC_CHECK_LIB([svld], [dlopen],
3198 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
3200 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
3209 |   if test no = "$lt_cv_dlopen"; then
3210 |     enable_dlopen=no
3212 |     enable_dlopen=yes
3215 |   case $lt_cv_dlopen in
3216 |   dlopen)
3224 |     LIBS="$lt_cv_dlopen_libs $LIBS"
3226 |     AC_CACHE_CHECK([whether a program can dlopen itself],
3227 | 	  lt_cv_dlopen_self, [dnl
3228 | 	  _LT_TRY_DLOPEN_SELF(
3229 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
3230 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
3233 |     if test yes = "$lt_cv_dlopen_self"; then
3235 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
3236 | 	  lt_cv_dlopen_self_static, [dnl
3237 | 	  _LT_TRY_DLOPEN_SELF(
3238 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
3239 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
3249 |   case $lt_cv_dlopen_self in
3250 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
3251 |   *) enable_dlopen_self=unknown ;;
3254 |   case $lt_cv_dlopen_self_static in
3255 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
3256 |   *) enable_dlopen_self_static=unknown ;;
3259 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
3260 | 	 [Whether dlopen is supported])
3261 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
3262 | 	 [Whether dlopen of programs is supported])
3263 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
3264 | 	 [Whether dlopen of statically linked programs is supported])
3266 | m4trace:m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3267 | m4trace:m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
3269 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
3578 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
3581 | put the 'dlopen' option into LT_INIT's first parameter.])
3583 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
3585 | _LT_SET_OPTION([LT_INIT], [dlopen])
3588 | put the 'dlopen' option into LT_INIT's first parameter.])
3680 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
4430 | m4trace:configure.ac:181: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/tools/ga-5.6.5/comex/m4/libtool.m4

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
### src/tools/ga-5.6.5/comex/m4/ltoptions.m4

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
### src/tools/ga-5.6.5/comex/build-aux/ltmain.sh

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
### src/tools/ga-5.6.5/comex/src-ofi/ofi.h

```cpp

{% raw %}
97 |     ld_table.handle = dlopen(env_data.library_path, RTLD_NOW);
{% endraw %}

```
### src/tools/ga-5.6.5/armci/autom4te.cache/output.0

```

{% raw %}
25698 |         enable_dlopen=no
29316 |   if test yes != "$enable_dlopen"; then
29317 |   enable_dlopen=unknown
29318 |   enable_dlopen_self=unknown
29319 |   enable_dlopen_self_static=unknown
29321 |   lt_cv_dlopen=no
29322 |   lt_cv_dlopen_libs=
29326 |     lt_cv_dlopen=load_add_on
29327 |     lt_cv_dlopen_libs=
29328 |     lt_cv_dlopen_self=yes
29332 |     lt_cv_dlopen=LoadLibrary
29333 |     lt_cv_dlopen_libs=
29337 |     lt_cv_dlopen=dlopen
29338 |     lt_cv_dlopen_libs=
29343 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29344 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29345 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29359 | char dlopen ();
29363 | return dlopen ();
29369 |   ac_cv_lib_dl_dlopen=yes
29371 |   ac_cv_lib_dl_dlopen=no
29377 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29378 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29379 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29380 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29383 |     lt_cv_dlopen=dyld
29384 |     lt_cv_dlopen_libs=
29385 |     lt_cv_dlopen_self=yes
29394 |     lt_cv_dlopen=dlopen
29395 |     lt_cv_dlopen_libs=
29396 |     lt_cv_dlopen_self=no
29402 |   lt_cv_dlopen=shl_load
29441 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
29443 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
29444 | if test "x$ac_cv_func_dlopen" = xyes; then :
29445 |   lt_cv_dlopen=dlopen
29447 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29448 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29449 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29463 | char dlopen ();
29467 | return dlopen ();
29473 |   ac_cv_lib_dl_dlopen=yes
29475 |   ac_cv_lib_dl_dlopen=no
29481 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29482 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29483 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29484 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29486 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
29487 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
29488 | if ${ac_cv_lib_svld_dlopen+:} false; then :
29502 | char dlopen ();
29506 | return dlopen ();
29512 |   ac_cv_lib_svld_dlopen=yes
29514 |   ac_cv_lib_svld_dlopen=no
29520 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
29521 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
29522 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
29523 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
29562 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
29583 |   if test no = "$lt_cv_dlopen"; then
29584 |     enable_dlopen=no
29586 |     enable_dlopen=yes
29589 |   case $lt_cv_dlopen in
29590 |   dlopen)
29598 |     LIBS="$lt_cv_dlopen_libs $LIBS"
29600 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
29601 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
29602 | if ${lt_cv_dlopen_self+:} false; then :
29606 |   lt_cv_dlopen_self=cross
29661 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29688 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
29689 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
29690 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
29694 |     lt_cv_dlopen_self=no
29701 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
29702 | $as_echo "$lt_cv_dlopen_self" >&6; }
29704 |     if test yes = "$lt_cv_dlopen_self"; then
29706 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
29707 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
29708 | if ${lt_cv_dlopen_self_static+:} false; then :
29712 |   lt_cv_dlopen_self_static=cross
29767 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29794 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
29795 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
29796 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
29800 |     lt_cv_dlopen_self_static=no
29807 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
29808 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
29817 |   case $lt_cv_dlopen_self in
29818 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
29819 |   *) enable_dlopen_self=unknown ;;
29822 |   case $lt_cv_dlopen_self_static in
29823 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
29824 |   *) enable_dlopen_self_static=unknown ;;
34992 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
34993 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
34994 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
36243 | # Whether dlopen is supported.
36244 | dlopen_support=$enable_dlopen
36246 | # Whether dlopen of programs is supported.
36247 | dlopen_self=$enable_dlopen_self
36249 | # Whether dlopen of statically linked programs is supported.
36250 | dlopen_self_static=$enable_dlopen_self_static
36294 | # Compiler flag to allow reflexive dlopens.
36536 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/armci/autom4te.cache/output.1

```

{% raw %}
25698 |         enable_dlopen=no
29316 |   if test yes != "$enable_dlopen"; then
29317 |   enable_dlopen=unknown
29318 |   enable_dlopen_self=unknown
29319 |   enable_dlopen_self_static=unknown
29321 |   lt_cv_dlopen=no
29322 |   lt_cv_dlopen_libs=
29326 |     lt_cv_dlopen=load_add_on
29327 |     lt_cv_dlopen_libs=
29328 |     lt_cv_dlopen_self=yes
29332 |     lt_cv_dlopen=LoadLibrary
29333 |     lt_cv_dlopen_libs=
29337 |     lt_cv_dlopen=dlopen
29338 |     lt_cv_dlopen_libs=
29343 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29344 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29345 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29359 | char dlopen ();
29363 | return dlopen ();
29369 |   ac_cv_lib_dl_dlopen=yes
29371 |   ac_cv_lib_dl_dlopen=no
29377 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29378 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29379 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29380 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29383 |     lt_cv_dlopen=dyld
29384 |     lt_cv_dlopen_libs=
29385 |     lt_cv_dlopen_self=yes
29394 |     lt_cv_dlopen=dlopen
29395 |     lt_cv_dlopen_libs=
29396 |     lt_cv_dlopen_self=no
29402 |   lt_cv_dlopen=shl_load
29441 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
29443 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
29444 | if test "x$ac_cv_func_dlopen" = xyes; then :
29445 |   lt_cv_dlopen=dlopen
29447 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29448 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29449 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29463 | char dlopen ();
29467 | return dlopen ();
29473 |   ac_cv_lib_dl_dlopen=yes
29475 |   ac_cv_lib_dl_dlopen=no
29481 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29482 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29483 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29484 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29486 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
29487 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
29488 | if ${ac_cv_lib_svld_dlopen+:} false; then :
29502 | char dlopen ();
29506 | return dlopen ();
29512 |   ac_cv_lib_svld_dlopen=yes
29514 |   ac_cv_lib_svld_dlopen=no
29520 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
29521 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
29522 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
29523 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
29562 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
29583 |   if test no = "$lt_cv_dlopen"; then
29584 |     enable_dlopen=no
29586 |     enable_dlopen=yes
29589 |   case $lt_cv_dlopen in
29590 |   dlopen)
29598 |     LIBS="$lt_cv_dlopen_libs $LIBS"
29600 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
29601 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
29602 | if ${lt_cv_dlopen_self+:} false; then :
29606 |   lt_cv_dlopen_self=cross
29661 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29688 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
29689 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
29690 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
29694 |     lt_cv_dlopen_self=no
29701 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
29702 | $as_echo "$lt_cv_dlopen_self" >&6; }
29704 |     if test yes = "$lt_cv_dlopen_self"; then
29706 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
29707 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
29708 | if ${lt_cv_dlopen_self_static+:} false; then :
29712 |   lt_cv_dlopen_self_static=cross
29767 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29794 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
29795 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
29796 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
29800 |     lt_cv_dlopen_self_static=no
29807 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
29808 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
29817 |   case $lt_cv_dlopen_self in
29818 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
29819 |   *) enable_dlopen_self=unknown ;;
29822 |   case $lt_cv_dlopen_self_static in
29823 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
29824 |   *) enable_dlopen_self_static=unknown ;;
34992 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
34993 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
34994 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
36243 | # Whether dlopen is supported.
36244 | dlopen_support=$enable_dlopen
36246 | # Whether dlopen of programs is supported.
36247 | dlopen_self=$enable_dlopen_self
36249 | # Whether dlopen of statically linked programs is supported.
36250 | dlopen_self_static=$enable_dlopen_self_static
36294 | # Compiler flag to allow reflexive dlopens.
36536 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/armci/autom4te.cache/output.2

```

{% raw %}
25698 |         enable_dlopen=no
29316 |   if test yes != "$enable_dlopen"; then
29317 |   enable_dlopen=unknown
29318 |   enable_dlopen_self=unknown
29319 |   enable_dlopen_self_static=unknown
29321 |   lt_cv_dlopen=no
29322 |   lt_cv_dlopen_libs=
29326 |     lt_cv_dlopen=load_add_on
29327 |     lt_cv_dlopen_libs=
29328 |     lt_cv_dlopen_self=yes
29332 |     lt_cv_dlopen=LoadLibrary
29333 |     lt_cv_dlopen_libs=
29337 |     lt_cv_dlopen=dlopen
29338 |     lt_cv_dlopen_libs=
29343 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29344 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29345 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29359 | char dlopen ();
29363 | return dlopen ();
29369 |   ac_cv_lib_dl_dlopen=yes
29371 |   ac_cv_lib_dl_dlopen=no
29377 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29378 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29379 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29380 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29383 |     lt_cv_dlopen=dyld
29384 |     lt_cv_dlopen_libs=
29385 |     lt_cv_dlopen_self=yes
29394 |     lt_cv_dlopen=dlopen
29395 |     lt_cv_dlopen_libs=
29396 |     lt_cv_dlopen_self=no
29402 |   lt_cv_dlopen=shl_load
29441 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
29443 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
29444 | if test "x$ac_cv_func_dlopen" = xyes; then :
29445 |   lt_cv_dlopen=dlopen
29447 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
29448 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
29449 | if ${ac_cv_lib_dl_dlopen+:} false; then :
29463 | char dlopen ();
29467 | return dlopen ();
29473 |   ac_cv_lib_dl_dlopen=yes
29475 |   ac_cv_lib_dl_dlopen=no
29481 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
29482 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
29483 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
29484 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
29486 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
29487 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
29488 | if ${ac_cv_lib_svld_dlopen+:} false; then :
29502 | char dlopen ();
29506 | return dlopen ();
29512 |   ac_cv_lib_svld_dlopen=yes
29514 |   ac_cv_lib_svld_dlopen=no
29520 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
29521 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
29522 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
29523 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
29562 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
29583 |   if test no = "$lt_cv_dlopen"; then
29584 |     enable_dlopen=no
29586 |     enable_dlopen=yes
29589 |   case $lt_cv_dlopen in
29590 |   dlopen)
29598 |     LIBS="$lt_cv_dlopen_libs $LIBS"
29600 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
29601 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
29602 | if ${lt_cv_dlopen_self+:} false; then :
29606 |   lt_cv_dlopen_self=cross
29661 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29688 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
29689 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
29690 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
29694 |     lt_cv_dlopen_self=no
29701 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
29702 | $as_echo "$lt_cv_dlopen_self" >&6; }
29704 |     if test yes = "$lt_cv_dlopen_self"; then
29706 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
29707 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
29708 | if ${lt_cv_dlopen_self_static+:} false; then :
29712 |   lt_cv_dlopen_self_static=cross
29767 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
29794 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
29795 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
29796 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
29800 |     lt_cv_dlopen_self_static=no
29807 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
29808 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
29817 |   case $lt_cv_dlopen_self in
29818 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
29819 |   *) enable_dlopen_self=unknown ;;
29822 |   case $lt_cv_dlopen_self_static in
29823 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
29824 |   *) enable_dlopen_self_static=unknown ;;
34992 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
34993 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
34994 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
36243 | # Whether dlopen is supported.
36244 | dlopen_support=$enable_dlopen
36246 | # Whether dlopen of programs is supported.
36247 | dlopen_self=$enable_dlopen_self
36249 | # Whether dlopen of statically linked programs is supported.
36250 | dlopen_self_static=$enable_dlopen_self_static
36294 | # Compiler flag to allow reflexive dlopens.
36536 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/armci/autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
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
533 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
1232 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
1543 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5838 | m4trace:configure.ac:267: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/tools/ga-5.6.5/armci/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
388 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
4129 | m4trace:m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
4130 | if test yes != "$enable_dlopen"; then
4131 |   enable_dlopen=unknown
4132 |   enable_dlopen_self=unknown
4133 |   enable_dlopen_self_static=unknown
4135 |   lt_cv_dlopen=no
4136 |   lt_cv_dlopen_libs=
4140 |     lt_cv_dlopen=load_add_on
4141 |     lt_cv_dlopen_libs=
4142 |     lt_cv_dlopen_self=yes
4146 |     lt_cv_dlopen=LoadLibrary
4147 |     lt_cv_dlopen_libs=
4151 |     lt_cv_dlopen=dlopen
4152 |     lt_cv_dlopen_libs=
4157 |     AC_CHECK_LIB([dl], [dlopen],
4158 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
4159 |     lt_cv_dlopen=dyld
4160 |     lt_cv_dlopen_libs=
4161 |     lt_cv_dlopen_self=yes
4168 |     lt_cv_dlopen=dlopen
4169 |     lt_cv_dlopen_libs=
4170 |     lt_cv_dlopen_self=no
4175 | 	  [lt_cv_dlopen=shl_load],
4177 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
4178 | 	[AC_CHECK_FUNC([dlopen],
4179 | 	      [lt_cv_dlopen=dlopen],
4180 | 	  [AC_CHECK_LIB([dl], [dlopen],
4181 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
4182 | 	    [AC_CHECK_LIB([svld], [dlopen],
4183 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
4185 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
4194 |   if test no = "$lt_cv_dlopen"; then
4195 |     enable_dlopen=no
4197 |     enable_dlopen=yes
4200 |   case $lt_cv_dlopen in
4201 |   dlopen)
4209 |     LIBS="$lt_cv_dlopen_libs $LIBS"
4211 |     AC_CACHE_CHECK([whether a program can dlopen itself],
4212 | 	  lt_cv_dlopen_self, [dnl
4213 | 	  _LT_TRY_DLOPEN_SELF(
4214 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
4215 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
4218 |     if test yes = "$lt_cv_dlopen_self"; then
4220 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
4221 | 	  lt_cv_dlopen_self_static, [dnl
4222 | 	  _LT_TRY_DLOPEN_SELF(
4223 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
4224 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
4234 |   case $lt_cv_dlopen_self in
4235 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
4236 |   *) enable_dlopen_self=unknown ;;
4239 |   case $lt_cv_dlopen_self_static in
4240 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
4241 |   *) enable_dlopen_self_static=unknown ;;
4244 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
4245 | 	 [Whether dlopen is supported])
4246 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
4247 | 	 [Whether dlopen of programs is supported])
4248 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
4249 | 	 [Whether dlopen of statically linked programs is supported])
4251 | m4trace:m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4252 | m4trace:m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
4254 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
4563 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
4566 | put the 'dlopen' option into LT_INIT's first parameter.])
4568 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
4570 | _LT_SET_OPTION([LT_INIT], [dlopen])
4573 | put the 'dlopen' option into LT_INIT's first parameter.])
4665 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
5838 | m4trace:configure.ac:267: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/tools/ga-5.6.5/armci/m4/libtool.m4

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
### src/tools/ga-5.6.5/armci/m4/ltoptions.m4

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
### src/tools/ga-5.6.5/armci/build-aux/ltmain.sh

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
### src/tools/ga-5.6.5/autom4te.cache/output.0

```

{% raw %}
30559 |         enable_dlopen=no
34201 |   if test yes != "$enable_dlopen"; then
34202 |   enable_dlopen=unknown
34203 |   enable_dlopen_self=unknown
34204 |   enable_dlopen_self_static=unknown
34206 |   lt_cv_dlopen=no
34207 |   lt_cv_dlopen_libs=
34211 |     lt_cv_dlopen=load_add_on
34212 |     lt_cv_dlopen_libs=
34213 |     lt_cv_dlopen_self=yes
34217 |     lt_cv_dlopen=LoadLibrary
34218 |     lt_cv_dlopen_libs=
34222 |     lt_cv_dlopen=dlopen
34223 |     lt_cv_dlopen_libs=
34228 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34229 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34230 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34244 | char dlopen ();
34256 | return dlopen ();
34262 |   ac_cv_lib_dl_dlopen=yes
34264 |   ac_cv_lib_dl_dlopen=no
34270 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34271 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34272 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34273 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34276 |     lt_cv_dlopen=dyld
34277 |     lt_cv_dlopen_libs=
34278 |     lt_cv_dlopen_self=yes
34287 |     lt_cv_dlopen=dlopen
34288 |     lt_cv_dlopen_libs=
34289 |     lt_cv_dlopen_self=no
34295 |   lt_cv_dlopen=shl_load
34342 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
34344 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
34345 | if test "x$ac_cv_func_dlopen" = xyes; then :
34346 |   lt_cv_dlopen=dlopen
34348 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34349 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34350 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34364 | char dlopen ();
34376 | return dlopen ();
34382 |   ac_cv_lib_dl_dlopen=yes
34384 |   ac_cv_lib_dl_dlopen=no
34390 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34391 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34392 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34393 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34395 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
34396 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
34397 | if ${ac_cv_lib_svld_dlopen+:} false; then :
34411 | char dlopen ();
34423 | return dlopen ();
34429 |   ac_cv_lib_svld_dlopen=yes
34431 |   ac_cv_lib_svld_dlopen=no
34437 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
34438 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
34439 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
34440 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
34487 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
34508 |   if test no = "$lt_cv_dlopen"; then
34509 |     enable_dlopen=no
34511 |     enable_dlopen=yes
34514 |   case $lt_cv_dlopen in
34515 |   dlopen)
34523 |     LIBS="$lt_cv_dlopen_libs $LIBS"
34525 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
34526 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
34527 | if ${lt_cv_dlopen_self+:} false; then :
34531 |   lt_cv_dlopen_self=cross
34586 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34613 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
34614 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
34615 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
34619 |     lt_cv_dlopen_self=no
34626 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
34627 | $as_echo "$lt_cv_dlopen_self" >&6; }
34629 |     if test yes = "$lt_cv_dlopen_self"; then
34631 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
34632 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
34633 | if ${lt_cv_dlopen_self_static+:} false; then :
34637 |   lt_cv_dlopen_self_static=cross
34692 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34719 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
34720 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
34721 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
34725 |     lt_cv_dlopen_self_static=no
34732 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
34733 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
34742 |   case $lt_cv_dlopen_self in
34743 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
34744 |   *) enable_dlopen_self=unknown ;;
34747 |   case $lt_cv_dlopen_self_static in
34748 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
34749 |   *) enable_dlopen_self_static=unknown ;;
42923 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
42924 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
42925 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
44265 | # Whether dlopen is supported.
44266 | dlopen_support=$enable_dlopen
44268 | # Whether dlopen of programs is supported.
44269 | dlopen_self=$enable_dlopen_self
44271 | # Whether dlopen of statically linked programs is supported.
44272 | dlopen_self_static=$enable_dlopen_self_static
44316 | # Compiler flag to allow reflexive dlopens.
44558 | # Compiler flag to allow reflexive dlopens.
44711 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/autom4te.cache/output.1

```

{% raw %}
30559 |         enable_dlopen=no
34201 |   if test yes != "$enable_dlopen"; then
34202 |   enable_dlopen=unknown
34203 |   enable_dlopen_self=unknown
34204 |   enable_dlopen_self_static=unknown
34206 |   lt_cv_dlopen=no
34207 |   lt_cv_dlopen_libs=
34211 |     lt_cv_dlopen=load_add_on
34212 |     lt_cv_dlopen_libs=
34213 |     lt_cv_dlopen_self=yes
34217 |     lt_cv_dlopen=LoadLibrary
34218 |     lt_cv_dlopen_libs=
34222 |     lt_cv_dlopen=dlopen
34223 |     lt_cv_dlopen_libs=
34228 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34229 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34230 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34244 | char dlopen ();
34256 | return dlopen ();
34262 |   ac_cv_lib_dl_dlopen=yes
34264 |   ac_cv_lib_dl_dlopen=no
34270 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34271 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34272 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34273 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34276 |     lt_cv_dlopen=dyld
34277 |     lt_cv_dlopen_libs=
34278 |     lt_cv_dlopen_self=yes
34287 |     lt_cv_dlopen=dlopen
34288 |     lt_cv_dlopen_libs=
34289 |     lt_cv_dlopen_self=no
34295 |   lt_cv_dlopen=shl_load
34342 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
34344 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
34345 | if test "x$ac_cv_func_dlopen" = xyes; then :
34346 |   lt_cv_dlopen=dlopen
34348 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34349 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34350 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34364 | char dlopen ();
34376 | return dlopen ();
34382 |   ac_cv_lib_dl_dlopen=yes
34384 |   ac_cv_lib_dl_dlopen=no
34390 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34391 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34392 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34393 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34395 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
34396 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
34397 | if ${ac_cv_lib_svld_dlopen+:} false; then :
34411 | char dlopen ();
34423 | return dlopen ();
34429 |   ac_cv_lib_svld_dlopen=yes
34431 |   ac_cv_lib_svld_dlopen=no
34437 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
34438 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
34439 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
34440 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
34487 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
34508 |   if test no = "$lt_cv_dlopen"; then
34509 |     enable_dlopen=no
34511 |     enable_dlopen=yes
34514 |   case $lt_cv_dlopen in
34515 |   dlopen)
34523 |     LIBS="$lt_cv_dlopen_libs $LIBS"
34525 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
34526 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
34527 | if ${lt_cv_dlopen_self+:} false; then :
34531 |   lt_cv_dlopen_self=cross
34586 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34613 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
34614 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
34615 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
34619 |     lt_cv_dlopen_self=no
34626 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
34627 | $as_echo "$lt_cv_dlopen_self" >&6; }
34629 |     if test yes = "$lt_cv_dlopen_self"; then
34631 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
34632 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
34633 | if ${lt_cv_dlopen_self_static+:} false; then :
34637 |   lt_cv_dlopen_self_static=cross
34692 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34719 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
34720 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
34721 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
34725 |     lt_cv_dlopen_self_static=no
34732 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
34733 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
34742 |   case $lt_cv_dlopen_self in
34743 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
34744 |   *) enable_dlopen_self=unknown ;;
34747 |   case $lt_cv_dlopen_self_static in
34748 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
34749 |   *) enable_dlopen_self_static=unknown ;;
42923 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
42924 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
42925 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
44265 | # Whether dlopen is supported.
44266 | dlopen_support=$enable_dlopen
44268 | # Whether dlopen of programs is supported.
44269 | dlopen_self=$enable_dlopen_self
44271 | # Whether dlopen of statically linked programs is supported.
44272 | dlopen_self_static=$enable_dlopen_self_static
44316 | # Compiler flag to allow reflexive dlopens.
44558 | # Compiler flag to allow reflexive dlopens.
44711 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/autom4te.cache/output.2

```

{% raw %}
30559 |         enable_dlopen=no
34201 |   if test yes != "$enable_dlopen"; then
34202 |   enable_dlopen=unknown
34203 |   enable_dlopen_self=unknown
34204 |   enable_dlopen_self_static=unknown
34206 |   lt_cv_dlopen=no
34207 |   lt_cv_dlopen_libs=
34211 |     lt_cv_dlopen=load_add_on
34212 |     lt_cv_dlopen_libs=
34213 |     lt_cv_dlopen_self=yes
34217 |     lt_cv_dlopen=LoadLibrary
34218 |     lt_cv_dlopen_libs=
34222 |     lt_cv_dlopen=dlopen
34223 |     lt_cv_dlopen_libs=
34228 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34229 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34230 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34244 | char dlopen ();
34256 | return dlopen ();
34262 |   ac_cv_lib_dl_dlopen=yes
34264 |   ac_cv_lib_dl_dlopen=no
34270 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34271 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34272 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34273 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34276 |     lt_cv_dlopen=dyld
34277 |     lt_cv_dlopen_libs=
34278 |     lt_cv_dlopen_self=yes
34287 |     lt_cv_dlopen=dlopen
34288 |     lt_cv_dlopen_libs=
34289 |     lt_cv_dlopen_self=no
34295 |   lt_cv_dlopen=shl_load
34342 |   lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld
34344 |   ac_fn_c_check_func "$LINENO" "dlopen" "ac_cv_func_dlopen"
34345 | if test "x$ac_cv_func_dlopen" = xyes; then :
34346 |   lt_cv_dlopen=dlopen
34348 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -ldl" >&5
34349 | $as_echo_n "checking for dlopen in -ldl... " >&6; }
34350 | if ${ac_cv_lib_dl_dlopen+:} false; then :
34364 | char dlopen ();
34376 | return dlopen ();
34382 |   ac_cv_lib_dl_dlopen=yes
34384 |   ac_cv_lib_dl_dlopen=no
34390 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_dl_dlopen" >&5
34391 | $as_echo "$ac_cv_lib_dl_dlopen" >&6; }
34392 | if test "x$ac_cv_lib_dl_dlopen" = xyes; then :
34393 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl
34395 |   { $as_echo "$as_me:${as_lineno-$LINENO}: checking for dlopen in -lsvld" >&5
34396 | $as_echo_n "checking for dlopen in -lsvld... " >&6; }
34397 | if ${ac_cv_lib_svld_dlopen+:} false; then :
34411 | char dlopen ();
34423 | return dlopen ();
34429 |   ac_cv_lib_svld_dlopen=yes
34431 |   ac_cv_lib_svld_dlopen=no
34437 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_cv_lib_svld_dlopen" >&5
34438 | $as_echo "$ac_cv_lib_svld_dlopen" >&6; }
34439 | if test "x$ac_cv_lib_svld_dlopen" = xyes; then :
34440 |   lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld
34487 |   lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld
34508 |   if test no = "$lt_cv_dlopen"; then
34509 |     enable_dlopen=no
34511 |     enable_dlopen=yes
34514 |   case $lt_cv_dlopen in
34515 |   dlopen)
34523 |     LIBS="$lt_cv_dlopen_libs $LIBS"
34525 |     { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a program can dlopen itself" >&5
34526 | $as_echo_n "checking whether a program can dlopen itself... " >&6; }
34527 | if ${lt_cv_dlopen_self+:} false; then :
34531 |   lt_cv_dlopen_self=cross
34586 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34613 |       x$lt_dlno_uscore) lt_cv_dlopen_self=yes ;;
34614 |       x$lt_dlneed_uscore) lt_cv_dlopen_self=yes ;;
34615 |       x$lt_dlunknown|x*) lt_cv_dlopen_self=no ;;
34619 |     lt_cv_dlopen_self=no
34626 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self" >&5
34627 | $as_echo "$lt_cv_dlopen_self" >&6; }
34629 |     if test yes = "$lt_cv_dlopen_self"; then
34631 |       { $as_echo "$as_me:${as_lineno-$LINENO}: checking whether a statically linked program can dlopen itself" >&5
34632 | $as_echo_n "checking whether a statically linked program can dlopen itself... " >&6; }
34633 | if ${lt_cv_dlopen_self_static+:} false; then :
34637 |   lt_cv_dlopen_self_static=cross
34692 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
34719 |       x$lt_dlno_uscore) lt_cv_dlopen_self_static=yes ;;
34720 |       x$lt_dlneed_uscore) lt_cv_dlopen_self_static=yes ;;
34721 |       x$lt_dlunknown|x*) lt_cv_dlopen_self_static=no ;;
34725 |     lt_cv_dlopen_self_static=no
34732 | { $as_echo "$as_me:${as_lineno-$LINENO}: result: $lt_cv_dlopen_self_static" >&5
34733 | $as_echo "$lt_cv_dlopen_self_static" >&6; }
34742 |   case $lt_cv_dlopen_self in
34743 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
34744 |   *) enable_dlopen_self=unknown ;;
34747 |   case $lt_cv_dlopen_self_static in
34748 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
34749 |   *) enable_dlopen_self_static=unknown ;;
42923 | enable_dlopen='`$ECHO "$enable_dlopen" | $SED "$delay_single_quote_subst"`'
42924 | enable_dlopen_self='`$ECHO "$enable_dlopen_self" | $SED "$delay_single_quote_subst"`'
42925 | enable_dlopen_self_static='`$ECHO "$enable_dlopen_self_static" | $SED "$delay_single_quote_subst"`'
44265 | # Whether dlopen is supported.
44266 | dlopen_support=$enable_dlopen
44268 | # Whether dlopen of programs is supported.
44269 | dlopen_self=$enable_dlopen_self
44271 | # Whether dlopen of statically linked programs is supported.
44272 | dlopen_self_static=$enable_dlopen_self_static
44316 | # Compiler flag to allow reflexive dlopens.
44558 | # Compiler flag to allow reflexive dlopens.
44711 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/tools/ga-5.6.5/autom4te.cache/traces.0

```

{% raw %}
411 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
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
533 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
534 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
536 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
1086 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
1130 | eval "LTDLOPEN=\"$libname_spec\""
1131 | AC_SUBST([LTDLOPEN])
1133 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
1232 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
1233 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
1543 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
1546 | put the 'dlopen' option into LT_INIT's first parameter.])
1548 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
1550 | _LT_SET_OPTION([LT_INIT], [dlopen])
1553 | put the 'dlopen' option into LT_INIT's first parameter.])
1645 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
7716 | m4trace:configure.ac:495: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/tools/ga-5.6.5/autom4te.cache/traces.2

```

{% raw %}
242 | AC_REQUIRE([LT_SYS_DLOPEN_DEPLIBS])dnl
286 | eval "LTDLOPEN=\"$libname_spec\""
287 | AC_SUBST([LTDLOPEN])
289 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:443: -1- AC_DEFUN([LT_SYS_DLOPEN_DEPLIBS], [AC_REQUIRE([AC_CANONICAL_HOST])dnl
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
388 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AU_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [m4_if($#, 0, [LT_SYS_DLOPEN_DEPLIBS], [LT_SYS_DLOPEN_DEPLIBS($@)])])
389 | m4trace:/people/d3n000/constance/deleteme/ga-5.6.5/autotools/share/aclocal/ltdl.m4:545: -1- AC_DEFUN([AC_LTDL_SYS_DLOPEN_DEPLIBS], [AC_DIAGNOSE([obsolete], [The macro `AC_LTDL_SYS_DLOPEN_DEPLIBS' is obsolete.
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
5541 | m4trace:m4/libtool.m4:1921: -1- AC_DEFUN([LT_SYS_DLOPEN_SELF], [m4_require([_LT_HEADER_DLFCN])dnl
5542 | if test yes != "$enable_dlopen"; then
5543 |   enable_dlopen=unknown
5544 |   enable_dlopen_self=unknown
5545 |   enable_dlopen_self_static=unknown
5547 |   lt_cv_dlopen=no
5548 |   lt_cv_dlopen_libs=
5552 |     lt_cv_dlopen=load_add_on
5553 |     lt_cv_dlopen_libs=
5554 |     lt_cv_dlopen_self=yes
5558 |     lt_cv_dlopen=LoadLibrary
5559 |     lt_cv_dlopen_libs=
5563 |     lt_cv_dlopen=dlopen
5564 |     lt_cv_dlopen_libs=
5569 |     AC_CHECK_LIB([dl], [dlopen],
5570 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
5571 |     lt_cv_dlopen=dyld
5572 |     lt_cv_dlopen_libs=
5573 |     lt_cv_dlopen_self=yes
5580 |     lt_cv_dlopen=dlopen
5581 |     lt_cv_dlopen_libs=
5582 |     lt_cv_dlopen_self=no
5587 | 	  [lt_cv_dlopen=shl_load],
5589 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
5590 | 	[AC_CHECK_FUNC([dlopen],
5591 | 	      [lt_cv_dlopen=dlopen],
5592 | 	  [AC_CHECK_LIB([dl], [dlopen],
5593 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
5594 | 	    [AC_CHECK_LIB([svld], [dlopen],
5595 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
5597 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
5606 |   if test no = "$lt_cv_dlopen"; then
5607 |     enable_dlopen=no
5609 |     enable_dlopen=yes
5612 |   case $lt_cv_dlopen in
5613 |   dlopen)
5621 |     LIBS="$lt_cv_dlopen_libs $LIBS"
5623 |     AC_CACHE_CHECK([whether a program can dlopen itself],
5624 | 	  lt_cv_dlopen_self, [dnl
5625 | 	  _LT_TRY_DLOPEN_SELF(
5626 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
5627 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
5630 |     if test yes = "$lt_cv_dlopen_self"; then
5632 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
5633 | 	  lt_cv_dlopen_self_static, [dnl
5634 | 	  _LT_TRY_DLOPEN_SELF(
5635 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
5636 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
5646 |   case $lt_cv_dlopen_self in
5647 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
5648 |   *) enable_dlopen_self=unknown ;;
5651 |   case $lt_cv_dlopen_self_static in
5652 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
5653 |   *) enable_dlopen_self_static=unknown ;;
5656 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
5657 | 	 [Whether dlopen is supported])
5658 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
5659 | 	 [Whether dlopen of programs is supported])
5660 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
5661 | 	 [Whether dlopen of statically linked programs is supported])
5663 | m4trace:m4/libtool.m4:2046: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
5664 | m4trace:m4/libtool.m4:2046: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN_SELF' is obsolete.
5666 | m4_if($#, 0, [LT_SYS_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF($@)])])
5975 | m4trace:m4/ltoptions.m4:113: -1- AU_DEFUN([AC_LIBTOOL_DLOPEN], [_LT_SET_OPTION([LT_INIT], [dlopen])
5978 | put the 'dlopen' option into LT_INIT's first parameter.])
5980 | m4trace:m4/ltoptions.m4:113: -1- AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_DIAGNOSE([obsolete], [The macro `AC_LIBTOOL_DLOPEN' is obsolete.
5982 | _LT_SET_OPTION([LT_INIT], [dlopen])
5985 | put the 'dlopen' option into LT_INIT's first parameter.])
6077 | m4trace:m4/lt~obsolete.m4:51: -1- AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF])
7716 | m4trace:configure.ac:495: -1- LT_SYS_DLOPEN_SELF
{% endraw %}

```
### src/tools/ga-5.6.5/m4/libtool.m4

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
### src/tools/ga-5.6.5/m4/ltoptions.m4

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
### src/tools/ga-5.6.5/build-aux/ltmain.sh

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