---
name: "pulseaudio"
layout: package
next_package: kahip
previous_package: cbtf-lanl
languages: ['cpp', 'bash']
---
## 13.0
60 / 892 files match

 - [configure.ac](#configureac)
 - [meson.build](#mesonbuild)
 - [src/Makefile.am](#srcmakefileam)
 - [src/Makefile.in](#srcmakefilein)
 - [src/daemon/ltdl-bind-now.c](#srcdaemonltdl-bind-nowc)
 - [src/pulsecore/module.c](#srcpulsecoremodulec)
 - [src/pulsecore/modinfo.c](#srcpulsecoremodinfoc)
 - [src/modules/ladspa.h](#srcmodulesladspah)
 - [src/modules/module-ladspa-sink.c](#srcmodulesmodule-ladspa-sinkc)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [po/cs.po](#pocspo)
 - [po/zh_CN.po](#pozh_cnpo)
 - [po/hu.po](#pohupo)
 - [po/sr@latin.po](#posr@latinpo)
 - [po/uk.po](#poukpo)
 - [po/ml.po](#pomlpo)
 - [po/nn.po](#ponnpo)
 - [po/hr.po](#pohrpo)
 - [po/el.po](#poelpo)
 - [po/ko.po](#pokopo)
 - [po/sk.po](#poskpo)
 - [po/sr.po](#posrpo)
 - [po/es.po](#poespo)
 - [po/or.po](#poorpo)
 - [po/pl.po](#poplpo)
 - [po/pt.po](#poptpo)
 - [po/ru.po](#porupo)
 - [po/kn.po](#poknpo)
 - [po/zh_TW.po](#pozh_twpo)
 - [po/ca.po](#pocapo)
 - [po/nl.po](#ponlpo)
 - [po/gu.po](#pogupo)
 - [po/sv.po](#posvpo)
 - [po/gl.po](#poglpo)
 - [po/lt.po](#poltpo)
 - [po/de_CH.po](#pode_chpo)
 - [po/oc.po](#poocpo)
 - [po/fi.po](#pofipo)
 - [po/as.po](#poaspo)
 - [po/he.po](#pohepo)
 - [po/pulseaudio.pot](#populseaudiopot)
 - [po/hi.po](#pohipo)
 - [po/it.po](#poitpo)
 - [po/tr.po](#potrpo)
 - [po/pt_BR.po](#popt_brpo)
 - [po/ja.po](#pojapo)
 - [po/te.po](#potepo)
 - [po/bn_IN.po](#pobn_inpo)
 - [po/pa.po](#popapo)
 - [po/mr.po](#pomrpo)
 - [po/af.po](#poafpo)
 - [po/fr.po](#pofrpo)
 - [po/id.po](#poidpo)
 - [po/be.po](#pobepo)
 - [po/ta.po](#potapo)
 - [po/de.po](#podepo)
 - [po/da.po](#podapo)
 - [build-aux/ltmain.sh](#build-auxltmainsh)

### configure.ac

```

{% raw %}
387 | LT_INIT([dlopen win32-dll disable-static])
519 | AC_SEARCH_LIBS([dlopen], [dl])
1513 |     AS_HELP_STRING([--enable-force-preopen],[Preopen modules, even when dlopen() is supported.]))
{% endraw %}

```
### meson.build

```

{% raw %}
498 | # FIXME: can meson support libtool -dlopen/-dlpreopen things?
{% endraw %}

```
### src/Makefile.am

```

{% raw %}
180 | pulseaudio_LDFLAGS = $(AM_LDFLAGS) $(BINLDFLAGS) $(IMMEDIATE_LDFLAGS) -ffast-math -dlopen force $(foreach f,$(PREOPEN_LIBS),-dlopen $(f))
{% endraw %}

```
### src/Makefile.in

```

{% raw %}
4067 | @FORCE_PREOPEN_FALSE@	$(IMMEDIATE_LDFLAGS) -ffast-math -dlopen \
4068 | @FORCE_PREOPEN_FALSE@	force $(foreach f,$(PREOPEN_LIBS),-dlopen \
{% endraw %}

```
### src/daemon/ltdl-bind-now.c

```cpp

{% raw %}
73 |     if (!(m = dlopen(fname, PA_BIND_NOW))) {
114 |     const lt_dlvtable *dlopen_loader;
124 |     if (!(dlopen_loader = lt_dlloader_find((char*) "lt_dlopen"))) {
125 |         pa_log_warn(_("Failed to find original lt_dlopen loader."));
134 |     memcpy(bindnow_loader, dlopen_loader, sizeof(*bindnow_loader));
{% endraw %}

```
### src/pulsecore/module.c

```cpp

{% raw %}
137 |     if (!(m->dl = lt_dlopenext(name))) {
{% endraw %}

```
### src/pulsecore/modinfo.c

```cpp

{% raw %}
76 |     if (!(dl = lt_dlopenext(name))) {
{% endraw %}

```
### src/modules/ladspa.h

```cpp

{% raw %}
65 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### src/modules/module-ladspa-sink.c

```cpp

{% raw %}
1080 |     m->dl = lt_dlopenext(plugin);
{% endraw %}

```
### m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6141 |     [Compiler flag to allow reflexive dlopens])
6254 |   LT_SYS_DLOPEN_SELF
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
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### po/cs.po

```

{% raw %}
375 | msgid "Failed to find original lt_dlopen loader."
376 | msgstr "Nezdařilo se nalézt původní zaváděcí program lt_dlopen."
{% endraw %}

```
### po/zh_CN.po

```

{% raw %}
353 | msgid "Failed to find original lt_dlopen loader."
354 | msgstr "查找原始 lt_dlopen 加载器失败。"
{% endraw %}

```
### po/hu.po

```

{% raw %}
390 | msgid "Failed to find original lt_dlopen loader."
391 | msgstr "Nem található az eredeti „lt_dlopen” betöltő."
{% endraw %}

```
### po/sr@latin.po

```

{% raw %}
119 | msgid "Failed to find original lt_dlopen loader."
120 | msgstr "Neuspešna pretraga za originalnim lt_dlopen učitavačem."
{% endraw %}

```
### po/uk.po

```

{% raw %}
389 | msgid "Failed to find original lt_dlopen loader."
391 | "Спроба знайти початковий інструмент завантаження lt_dlopen зазнала невдачі."
{% endraw %}

```
### po/ml.po

```

{% raw %}
107 | msgid "Failed to find original lt_dlopen loader."
108 | msgstr "യഥാര്‍ത്ഥ lt_dlopen ലോഡര്‍ ലഭ്യമാക്കുന്നതില്‍ പരാജയപ്പെട്ടു."
{% endraw %}

```
### po/nn.po

```

{% raw %}
344 | msgid "Failed to find original lt_dlopen loader."
345 | msgstr "Fann ikkje opphavleg lt_dlopen-lastar."
{% endraw %}

```
### po/hr.po

```

{% raw %}
387 | msgid "Failed to find original lt_dlopen loader."
388 | msgstr "Neuspjelo traženje izvornog lt_dlopen učitača."
{% endraw %}

```
### po/el.po

```

{% raw %}
459 | msgid "Failed to find original lt_dlopen loader."
460 | msgstr "Αποτυχία εύρεσης αρχικού φορτωτή lt_dlopen."
{% endraw %}

```
### po/ko.po

```

{% raw %}
96 | msgid "Failed to find original lt_dlopen loader."
97 | msgstr "기존 lt_dlopen 로더를 찾는데 실패했습니다."
{% endraw %}

```
### po/sk.po

```

{% raw %}
297 | msgid "Failed to find original lt_dlopen loader."
{% endraw %}

```
### po/sr.po

```

{% raw %}
119 | msgid "Failed to find original lt_dlopen loader."
120 | msgstr "Неуспешна претрага за оригиналним lt_dlopen учитавачем."
{% endraw %}

```
### po/es.po

```

{% raw %}
121 | msgid "Failed to find original lt_dlopen loader."
122 | msgstr "Falló al buscar cargador el cargador lt_dlopen original."
{% endraw %}

```
### po/or.po

```

{% raw %}
133 | msgid "Failed to find original lt_dlopen loader."
134 | msgstr "ପ୍ରକୃତ lt_dlopen ଧାରକକୁ ଖୋଜି ପାଇବାରେ ବିଫଳ।"
{% endraw %}

```
### po/pl.po

```

{% raw %}
378 | msgid "Failed to find original lt_dlopen loader."
380 | "Odnalezienie pierwotnego programu wczytującego lt_dlopen się nie powiodło."
{% endraw %}

```
### po/pt.po

```

{% raw %}
117 | msgid "Failed to find original lt_dlopen loader."
118 | msgstr "Não foi possível encontrar o carregador \"lt_dlopen\"."
{% endraw %}

```
### po/ru.po

```

{% raw %}
393 | msgid "Failed to find original lt_dlopen loader."
394 | msgstr "Не удалось найти исходный загрузчик lt_dlopen."
{% endraw %}

```
### po/kn.po

```

{% raw %}
114 | msgid "Failed to find original lt_dlopen loader."
115 | msgstr "ಮೂಲ lt_dlopen loader ಅನ್ನು ಲೋಡ್ ಮಾಡುವಲ್ಲಿ ವಿಫಲಗೊಂಡಿದೆ."
{% endraw %}

```
### po/zh_TW.po

```

{% raw %}
359 | msgid "Failed to find original lt_dlopen loader."
360 | msgstr "找不到 original lt_dlopen loader。"
{% endraw %}

```
### po/ca.po

```

{% raw %}
132 | msgid "Failed to find original lt_dlopen loader."
133 | msgstr "No s'ha trobat el carregador lt_dlopen original."
{% endraw %}

```
### po/nl.po

```

{% raw %}
118 | msgid "Failed to find original lt_dlopen loader."
119 | msgstr "Kon de originele lt_dlopen lader niet vinden."
{% endraw %}

```
### po/gu.po

```

{% raw %}
116 | msgid "Failed to find original lt_dlopen loader."
117 | msgstr "મૂળ lt_dlopen લોડરને શોધવામાં નિષ્ફળ."
{% endraw %}

```
### po/sv.po

```

{% raw %}
389 | msgid "Failed to find original lt_dlopen loader."
390 | msgstr "Misslyckades med att hitta original-lt_dlopen loader."
{% endraw %}

```
### po/gl.po

```

{% raw %}
391 | msgid "Failed to find original lt_dlopen loader."
392 | msgstr "Produciuse un fallo ao buscar o cargador llt_dlopen orixinal."
{% endraw %}

```
### po/lt.po

```

{% raw %}
391 | msgid "Failed to find original lt_dlopen loader."
392 | msgstr "Nepavyko rasti pradinio lt_dlopen įkėliklio."
{% endraw %}

```
### po/de_CH.po

```

{% raw %}
116 | msgid "Failed to find original lt_dlopen loader."
117 | msgstr "Ursprünglicher dlopen-Loader konnte nicht gefunden werden."
121 | msgstr "Neuer dlopen-Loader konnte nicht gefunden werden."
{% endraw %}

```
### po/oc.po

```

{% raw %}
307 | msgid "Failed to find original lt_dlopen loader."
308 | msgstr "Fracàs al moment de la recèrca del cargador lt_dlopen original."
{% endraw %}

```
### po/fi.po

```

{% raw %}
117 | msgid "Failed to find original lt_dlopen loader."
118 | msgstr "Alkuperäisen lt_dlopen-lataimen löytäminen epäonnistui."
{% endraw %}

```
### po/as.po

```

{% raw %}
114 | msgid "Failed to find original lt_dlopen loader."
115 | msgstr "প্ৰাথমিক lt_dlopen loader পোৱা ন'গ'ল ।"
{% endraw %}

```
### po/he.po

```

{% raw %}
95 | msgid "Failed to find original lt_dlopen loader."
{% endraw %}

```
### po/pulseaudio.pot

```

{% raw %}
295 | msgid "Failed to find original lt_dlopen loader."
{% endraw %}

```
### po/hi.po

```

{% raw %}
122 | msgid "Failed to find original lt_dlopen loader."
123 | msgstr "मौलिक ltdlopen लोडर ढूँढ़ने में विफल (_d)."
{% endraw %}

```
### po/it.po

```

{% raw %}
404 | msgid "Failed to find original lt_dlopen loader."
405 | msgstr "Ricerca del loader lt_dlopen originale non riuscita."
{% endraw %}

```
### po/tr.po

```

{% raw %}
458 | msgid "Failed to find original lt_dlopen loader."
459 | msgstr "Orjinal lt_dlopen yükleyicisi bulunamadı."
{% endraw %}

```
### po/pt_BR.po

```

{% raw %}
349 | msgid "Failed to find original lt_dlopen loader."
350 | msgstr "Falha ao localizar o carregador original lt_dlopen."
{% endraw %}

```
### po/ja.po

```

{% raw %}
121 | msgid "Failed to find original lt_dlopen loader."
122 | msgstr "オリジナルの lt_dlopen ローダーを見つけるのに失敗しました。"
{% endraw %}

```
### po/te.po

```

{% raw %}
120 | msgid "Failed to find original lt_dlopen loader."
121 | msgstr "వాస్తవ lt_dlopen లోడర్ కనుగొనుటలో విఫలమైంది."
{% endraw %}

```
### po/bn_IN.po

```

{% raw %}
115 | msgid "Failed to find original lt_dlopen loader."
116 | msgstr "মূল lt_dlopen লোডার সনাক্ত করতে ব্যর্থ।"
{% endraw %}

```
### po/pa.po

```

{% raw %}
113 | msgid "Failed to find original lt_dlopen loader."
114 | msgstr "ਅਸਲੀ lt_dlopen ਲੋਡਰ ਲੱਭਣ ਵਿੱਚ ਫੇਲ੍ਹ ਹੋਇਆ।"
{% endraw %}

```
### po/mr.po

```

{% raw %}
114 | msgid "Failed to find original lt_dlopen loader."
115 | msgstr "मूळ lt_dlopen दाखलकर्ता शोधण्यास अपयशी."
{% endraw %}

```
### po/af.po

```

{% raw %}
294 | msgid "Failed to find original lt_dlopen loader."
{% endraw %}

```
### po/fr.po

```

{% raw %}
387 | msgid "Failed to find original lt_dlopen loader."
388 | msgstr "Échec lors de la recherche du chargeur lt_dlopen original."
{% endraw %}

```
### po/id.po

```

{% raw %}
381 | msgid "Failed to find original lt_dlopen loader."
382 | msgstr "Gagal menemukan pemuat lt_dlopen asli."
{% endraw %}

```
### po/be.po

```

{% raw %}
378 | msgid "Failed to find original lt_dlopen loader."
379 | msgstr "Не атрымалася знайсці арыгінальны lt_dlopen-загрузчык."
{% endraw %}

```
### po/ta.po

```

{% raw %}
140 | msgid "Failed to find original lt_dlopen loader."
141 | msgstr "அசல் lt_dlopen ஏற்றியை காண முடியவில்லை."
{% endraw %}

```
### po/de.po

```

{% raw %}
392 | msgid "Failed to find original lt_dlopen loader."
393 | msgstr "Ursprünglicher lt_dlopen-Lader konnte nicht gefunden werden."
397 | msgstr "Neuer dlopen-Loader konnte nicht zugewiesen werden."
{% endraw %}

```
### po/da.po

```

{% raw %}
373 | msgid "Failed to find original lt_dlopen loader."
374 | msgstr "Kunne ikke finde oprindelige lt_dlopen-indlæser."
{% endraw %}

```
### build-aux/ltmain.sh

```bash

{% raw %}
2335 |     opt_dlopen=
2408 |         --dlopen|-dlopen)
2409 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2532 |       # Only execute mode is allowed to have -dlopen flags.
2533 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2534 |         func_error "unrecognized option '-dlopen'"
3760 |   -dlopen FILE      add the directory containing FILE to the library path
3762 | This mode sets the library path environment variable according to '-dlopen'
3817 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3826 |   -module           build a library that can dlopened
3934 |     # Handle -dlopen flags immediately.
3935 |     for file in $opt_dlopen; do
3954 | 	# Skip this library if it cannot be dlopened.
3981 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6674 | 	    dlopen_self=$dlopen_self_static
6680 | 	    dlopen_self=$dlopen_self_static
6686 | 	    dlopen_self=$dlopen_self_static
6744 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6834 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7001 |       -dlopen)
7439 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7507 | 	  # This library was specified with -dlopen.
7627 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7638 | 	passes="conv scan dlopen dlpreopen link"
7664 | 	dlopen) libs=$dlfiles ;;
7695 |       if test dlopen = "$pass"; then
7915 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7916 | 	      # If there is no dlopen support or we're linking statically,
7944 | 	dlopen=
7974 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
8020 | 	# This library was specified with -dlopen.
8021 | 	if test dlopen = "$pass"; then
8023 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
8025 | 	     test yes != "$dlopen_support" ||
8028 | 	    # If there is no dlname, no dlopen support or we're linking
8037 | 	fi # $pass = dlopen
8093 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8095 | 	      # We recover the dlopen module name by 'saving' the la file
8119 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8248 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8249 | 	  dlopenmodule=
8252 | 	      dlopenmodule=$dlpremoduletest
8256 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8353 | 		    # if the lib is a (non-dlopened) module then we cannot
8357 | 		      if test "X$dlopenmodule" != "X$lib"; then
8509 | 	      echo "*** a static module, that should work as long as the dlopening application"
8510 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8654 |       if test dlopen != "$pass"; then
8784 | 	func_warning "'-dlopen' is ignored for archives"
8851 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9548 | 	    echo "*** a static module, that should work as long as the dlopening"
9549 | 	    echo "*** application is linked with the -dlopen flag."
9567 | 	    echo "*** or is declared to -dlopen it."
10179 | 	func_warning "'-dlopen' is ignored for objects"
10299 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10300 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10981 | # The name that we can dlopen(3).
11010 | # Files to dlopen/dlpreopen
11011 | dlopen='$dlfiles'
{% endraw %}

```