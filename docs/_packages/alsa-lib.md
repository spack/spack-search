---
name: "alsa-lib"
layout: package
next_package: libpulsar
previous_package: samrai
languages: ['cpp', 'bash']
---
## 1.2.3.2
22 / 388 files match

 - [ltmain.sh](#ltmainsh)
 - [src/dlmisc.c](#srcdlmiscc)
 - [src/Versions.in](#srcversionsin)
 - [src/conf.c](#srcconfc)
 - [src/seq/seq.c](#srcseqseqc)
 - [src/hwdep/hwdep.c](#srchwdephwdepc)
 - [src/mixer/simple_abst.c](#srcmixersimple_abstc)
 - [src/pcm/pcm_hooks.c](#srcpcmpcm_hooksc)
 - [src/pcm/pcm_meter.c](#srcpcmpcm_meterc)
 - [src/pcm/pcm_ladspa.c](#srcpcmpcm_ladspac)
 - [src/pcm/ladspa.h](#srcpcmladspah)
 - [src/timer/timer_query.c](#srctimertimer_queryc)
 - [src/timer/timer.c](#srctimertimerc)
 - [include/global.h](#includeglobalh)
 - [include/local.h](#includelocalh)
 - [utils/alsa.m4](#utilsalsam4)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [modules/mixer/simple/sbase.h](#modulesmixersimplesbaseh)
 - [modules/mixer/simple/ac97.c](#modulesmixersimpleac97c)
 - [modules/mixer/simple/hda.c](#modulesmixersimplehdac)
 - [modules/mixer/simple/sbasedl.c](#modulesmixersimplesbasedlc)

### ltmain.sh

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
7345 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7413 | 	  # This library was specified with -dlopen.
7533 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7544 | 	passes="conv scan dlopen dlpreopen link"
7570 | 	dlopen) libs=$dlfiles ;;
7598 |       if test dlopen = "$pass"; then
7818 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7819 | 	      # If there is no dlopen support or we're linking statically,
7847 | 	dlopen=
7877 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7923 | 	# This library was specified with -dlopen.
7924 | 	if test dlopen = "$pass"; then
7926 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7928 | 	     test yes != "$dlopen_support" ||
7931 | 	    # If there is no dlname, no dlopen support or we're linking
7940 | 	fi # $pass = dlopen
7996 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7998 | 	      # We recover the dlopen module name by 'saving' the la file
8022 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8151 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8152 | 	  dlopenmodule=
8155 | 	      dlopenmodule=$dlpremoduletest
8159 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8256 | 		    # if the lib is a (non-dlopened) module then we cannot
8260 | 		      if test "X$dlopenmodule" != "X$lib"; then
8412 | 	      echo "*** a static module, that should work as long as the dlopening application"
8413 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8557 |       if test dlopen != "$pass"; then
8687 | 	func_warning "'-dlopen' is ignored for archives"
8754 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9448 | 	    echo "*** a static module, that should work as long as the dlopening"
9449 | 	    echo "*** application is linked with the -dlopen flag."
9467 | 	    echo "*** or is declared to -dlopen it."
10079 | 	func_warning "'-dlopen' is ignored for objects"
10199 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10200 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10881 | # The name that we can dlopen(3).
10910 | # Files to dlopen/dlpreopen
10911 | dlopen='$dlfiles'
{% endraw %}

```
### src/dlmisc.c

```cpp

{% raw %}
105 |  * \brief Opens a dynamic library - ALSA wrapper for \c dlopen.
106 |  * \param name name of the library, similar to \c dlopen.
107 |  * \param mode mode flags, similar to \c dlopen.
116 | EXPORT_SYMBOL void *INTERNAL(snd_dlopen)(const char *name, int mode, char *errbuf, size_t errbuflen)
118 | void *snd_dlopen(const char *name, int mode, char *errbuf, size_t errbuflen)
130 | 			if (dladdr(snd_dlopen, &dlinfo) > 0)
139 | 	 * Handle the plugin dir not being on the default dlopen search
150 | 			handle = dlopen(filename, mode);
161 | 		handle = dlopen(name, mode);
174 | void *INTERNAL(snd_dlopen_old)(const char *name, int mode)
176 |   return INTERNAL(snd_dlopen)(name, mode, NULL, 0);
180 | use_symbol_version(__snd_dlopen_old, snd_dlopen, ALSA_0.9);
181 | use_default_symbol_version(__snd_dlopen, snd_dlopen, ALSA_1.1.6);
339 | 	dlobj = INTERNAL(snd_dlopen)(lib, RTLD_NOW,
{% endraw %}

```
### src/Versions.in

```

{% raw %}
134 |     @SYMBOL_PREFIX@snd_dlopen;
{% endraw %}

```
### src/conf.c

```cpp

{% raw %}
3718 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
4721 | 		h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/seq/seq.c

```cpp

{% raw %}
901 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/hwdep/hwdep.c

```cpp

{% raw %}
118 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/mixer/simple_abst.c

```cpp

{% raw %}
82 | 	h = INTERNAL(snd_dlopen)(xlib, RTLD_NOW, errbuf, sizeof(errbuf));
129 | 	h = INTERNAL(snd_dlopen)(xlib, RTLD_NOW|RTLD_GLOBAL, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/pcm/pcm_hooks.c

```cpp

{% raw %}
426 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/pcm/pcm_meter.c

```cpp

{% raw %}
672 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/pcm/pcm_ladspa.c

```cpp

{% raw %}
1093 | 	handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/pcm/ladspa.h

```cpp

{% raw %}
66 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### src/timer/timer_query.c

```cpp

{% raw %}
110 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/timer/timer.c

```cpp

{% raw %}
152 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### include/global.h

```cpp

{% raw %}
100 | void *snd_dlopen(const char *file, int mode, char *errbuf, size_t errbuflen);
{% endraw %}

```
### include/local.h

```cpp

{% raw %}
373 | void *INTERNAL(snd_dlopen)(const char *name, int mode, char *errbuf, size_t errbuflen);
{% endraw %}

```
### utils/alsa.m4

```

{% raw %}
55 | AC_CHECK_LIB(c, dlopen, LIBDL="", [AC_CHECK_LIB(dl, dlopen, LIBDL="-ldl")])
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
6125 |     [Compiler flag to allow reflexive dlopens])
6238 |   LT_SYS_DLOPEN_SELF
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
### modules/mixer/simple/sbase.h

```cpp

{% raw %}
107 | int mixer_simple_basic_dlopen(snd_mixer_class_t *class,
{% endraw %}

```
### modules/mixer/simple/ac97.c

```cpp

{% raw %}
78 | 	err = mixer_simple_basic_dlopen(class, &ops);
{% endraw %}

```
### modules/mixer/simple/hda.c

```cpp

{% raw %}
79 | 	err = mixer_simple_basic_dlopen(class, &ops);
{% endraw %}

```
### modules/mixer/simple/sbasedl.c

```cpp

{% raw %}
1 |  *  Mixer Interface - simple abstact module - base library (dlopen function)
37 | int mixer_simple_basic_dlopen(snd_mixer_class_t *class,
65 | 	h = snd_dlopen(xlib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```