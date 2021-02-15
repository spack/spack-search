---
name: "sdl2"
layout: package
next_package: prrte
previous_package: pcre2
languages: ['cmake', 'cpp', 'bash']
---
## 2.0.5
16 / 1065 files match

 - [Android.mk](#androidmk)
 - [Makefile.wiz](#makefilewiz)
 - [Makefile.pandora](#makefilepandora)
 - [configure.in](#configurein)
 - [CMakeLists.txt](#cmakeliststxt)
 - [Xcode-iOS/SDL/SDL.xcodeproj/project.pbxproj](#xcode-iossdlsdlxcodeprojprojectpbxproj)
 - [build-scripts/ltmain.sh](#build-scriptsltmainsh)
 - [src/video/x11/SDL_x11opengl.c](#srcvideox11sdl_x11openglc)
 - [src/video/directfb/SDL_DirectFB_opengl.c](#srcvideodirectfbsdl_directfb_openglc)
 - [src/loadso/dlopen/SDL_sysloadso.c](#srcloadsodlopensdl_sysloadsoc)
 - [src/dynapi/SDL_dynapi.c](#srcdynapisdl_dynapic)
 - [Xcode/SDL/SDL.xcodeproj/project.pbxproj](#xcodesdlsdlxcodeprojprojectpbxproj)
 - [acinclude/libtool.m4](#acincludelibtoolm4)
 - [acinclude/ltoptions.m4](#acincludeltoptionsm4)
 - [debian/sdl2-config.1](#debiansdl2-config1)
 - [cmake/sdlchecks.cmake](#cmakesdlcheckscmake)

### Android.mk

```

{% raw %}
33 | 	$(wildcard $(LOCAL_PATH)/src/loadso/dlopen/*.c) \
{% endraw %}

```
### Makefile.wiz

```

{% raw %}
17 | 	./src/audio/dummy/*.c ./src/loadso/dlopen/*.c ./src/audio/dsp/*.c \
{% endraw %}

```
### Makefile.pandora

```

{% raw %}
17 | 	./src/audio/dummy/*.c ./src/loadso/dlopen/*.c ./src/audio/dsp/*.c \
{% endraw %}

```
### configure.in

```

{% raw %}
2672 | CheckDLOPEN()
2674 |     AC_ARG_ENABLE(sdl-dlopen,
2675 | AC_HELP_STRING([--enable-sdl-dlopen], [use dlopen for shared object loading [[default=yes]]]),
2676 |                   , enable_sdl_dlopen=yes)
2677 |     if test x$enable_sdl_dlopen = xyes; then
2678 |         AC_MSG_CHECKING(for dlopen)
2679 |         have_dlopen=no
2683 |          void *handle = dlopen("", RTLD_NOW);
2686 |         have_dlopen=yes
2688 |         AC_MSG_RESULT($have_dlopen)
2690 |         if test x$have_dlopen = xyes; then
2691 |             AC_CHECK_LIB(c, dlopen, EXTRA_LDFLAGS="$EXTRA_LDFLAGS",
2692 |                AC_CHECK_LIB(dl, dlopen, EXTRA_LDFLAGS="$EXTRA_LDFLAGS -ldl",
2693 |                   AC_CHECK_LIB(ltdl, dlopen, EXTRA_LDFLAGS="$EXTRA_LDFLAGS -lltdl")))
2694 |             AC_DEFINE(SDL_LOADSO_DLOPEN, 1, [ ])
2695 |             SOURCES="$SOURCES $srcdir/src/loadso/dlopen/*.c"
2956 |         CheckDLOPEN
3285 |         CheckDLOPEN
3355 |         CheckDLOPEN
3454 |         CheckDLOPEN
{% endraw %}

```
### CMakeLists.txt

```

{% raw %}
236 |   set(SDL_DLOPEN_ENABLED_BY_DEFAULT OFF)
245 |     File Loadso CPUinfo Filesystem Dlopen)
276 | set_option(SDL_DLOPEN          "Use dlopen for shared object loading" ${SDL_DLOPEN_ENABLED_BY_DEFAULT})
685 | # TODO: in configure.in, the test for LOADSO and SDL_DLOPEN is a bit weird:
687 | # If however on Unix or APPLE dlopen() is detected via CheckDLOPEN(),
707 | if(SDL_DLOPEN)
710 |     CheckDLOPEN()
{% endraw %}

```
### Xcode-iOS/SDL/SDL.xcodeproj/project.pbxproj

```

{% raw %}
778 | 				FD8BD8180E27E25900B52CD5 /* dlopen */,
784 | 		FD8BD8180E27E25900B52CD5 /* dlopen */ = {
789 | 			path = dlopen;
{% endraw %}

```
### build-scripts/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6152 |       if test "$pass" = dlopen; then
6371 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6372 | 	      # If there is no dlopen support or we're linking statically,
6402 | 	dlopen=
6432 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6478 | 	# This library was specified with -dlopen.
6479 | 	if test "$pass" = dlopen; then
6481 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6484 | 	     test "$dlopen_support" != yes ||
6486 | 	    # If there is no dlname, no dlopen support or we're linking
6495 | 	fi # $pass = dlopen
6551 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6553 | 	      # We recover the dlopen module name by 'saving' the la file
6577 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6706 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6707 | 	  dlopenmodule=""
6710 | 	      dlopenmodule="$dlpremoduletest"
6714 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6811 | 		    # if the lib is a (non-dlopened) module then we can not
6815 | 		      if test "X$dlopenmodule" != "X$lib"; then
6967 | 	      echo "*** a static module, that should work as long as the dlopening application"
6968 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7112 |       if test "$pass" != dlopen; then
7211 | 	func_warning "\`-dlopen' is ignored for archives"
7278 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7954 | 	    echo "*** a static module, that should work as long as the dlopening"
7955 | 	    echo "*** application is linked with the -dlopen flag."
7973 | 	    echo "*** or is declared to -dlopen it."
8584 | 	func_warning "\`-dlopen' is ignored for objects"
8702 |         && test "$dlopen_support" = unknown \
8703 | 	&& test "$dlopen_self" = unknown \
8704 | 	&& test "$dlopen_self_static" = unknown && \
8705 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9386 | # The name that we can dlopen(3).
9415 | # Files to dlopen/dlpreopen
9416 | dlopen='$dlfiles'
{% endraw %}

```
### src/video/x11/SDL_x11opengl.c

```cpp

{% raw %}
131 | #define OPENGL_REQUIRES_DLOPEN
132 | #if defined(OPENGL_REQUIRES_DLOPEN) && defined(SDL_LOADSO_DLOPEN)
134 | #define GL_LoadObject(X)    dlopen(X, (RTLD_NOW|RTLD_GLOBAL))
165 | #if defined(OPENGL_REQUIRES_DLOPEN) && defined(SDL_LOADSO_DLOPEN)
{% endraw %}

```
### src/video/directfb/SDL_DirectFB_opengl.c

```cpp

{% raw %}
48 | #define OPENGL_REQUIRS_DLOPEN
49 | #if defined(OPENGL_REQUIRS_DLOPEN) && defined(SDL_LOADSO_DLOPEN)
51 | #define GL_LoadObject(X)    dlopen(X, (RTLD_NOW|RTLD_GLOBAL))
{% endraw %}

```
### src/loadso/dlopen/SDL_sysloadso.c

```cpp

{% raw %}
22 | #ifdef SDL_LOADSO_DLOPEN
49 |     handle = dlopen(sofile, RTLD_NOW|RTLD_LOCAL);
85 | #endif /* SDL_LOADSO_DLOPEN */
{% endraw %}

```
### src/dynapi/SDL_dynapi.c

```cpp

{% raw %}
236 |     void *lib = dlopen(fname, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### Xcode/SDL/SDL.xcodeproj/project.pbxproj

```

{% raw %}
1444 | 				04BDFE3212E6671700899322 /* dlopen */,
1450 | 		04BDFE3212E6671700899322 /* dlopen */ = {
1455 | 			path = dlopen;
{% endraw %}

```
### acinclude/libtool.m4

```

{% raw %}
1746 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1749 | m4_defun([_LT_TRY_DLOPEN_SELF],
1807 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1840 | ])# _LT_TRY_DLOPEN_SELF
1843 | # LT_SYS_DLOPEN_SELF
1845 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1847 | if test "x$enable_dlopen" != xyes; then
1848 |   enable_dlopen=unknown
1849 |   enable_dlopen_self=unknown
1850 |   enable_dlopen_self_static=unknown
1852 |   lt_cv_dlopen=no
1853 |   lt_cv_dlopen_libs=
1857 |     lt_cv_dlopen="load_add_on"
1858 |     lt_cv_dlopen_libs=
1859 |     lt_cv_dlopen_self=yes
1863 |     lt_cv_dlopen="LoadLibrary"
1864 |     lt_cv_dlopen_libs=
1868 |     lt_cv_dlopen="dlopen"
1869 |     lt_cv_dlopen_libs=
1874 |     AC_CHECK_LIB([dl], [dlopen],
1875 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1876 |     lt_cv_dlopen="dyld"
1877 |     lt_cv_dlopen_libs=
1878 |     lt_cv_dlopen_self=yes
1884 | 	  [lt_cv_dlopen="shl_load"],
1886 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1887 | 	[AC_CHECK_FUNC([dlopen],
1888 | 	      [lt_cv_dlopen="dlopen"],
1889 | 	  [AC_CHECK_LIB([dl], [dlopen],
1890 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1891 | 	    [AC_CHECK_LIB([svld], [dlopen],
1892 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1894 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1903 |   if test "x$lt_cv_dlopen" != xno; then
1904 |     enable_dlopen=yes
1906 |     enable_dlopen=no
1909 |   case $lt_cv_dlopen in
1910 |   dlopen)
1918 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1920 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1921 | 	  lt_cv_dlopen_self, [dnl
1922 | 	  _LT_TRY_DLOPEN_SELF(
1923 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1924 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1927 |     if test "x$lt_cv_dlopen_self" = xyes; then
1929 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1930 | 	  lt_cv_dlopen_self_static, [dnl
1931 | 	  _LT_TRY_DLOPEN_SELF(
1932 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1933 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1943 |   case $lt_cv_dlopen_self in
1944 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1945 |   *) enable_dlopen_self=unknown ;;
1948 |   case $lt_cv_dlopen_self_static in
1949 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1950 |   *) enable_dlopen_self_static=unknown ;;
1953 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1954 | 	 [Whether dlopen is supported])
1955 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1956 | 	 [Whether dlopen of programs is supported])
1957 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1958 | 	 [Whether dlopen of statically linked programs is supported])
1959 | ])# LT_SYS_DLOPEN_SELF
1962 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1964 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5671 |     [Compiler flag to allow reflexive dlopens])
5784 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### acinclude/ltoptions.m4

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
### debian/sdl2-config.1

```

{% raw %}
44 | .IR dlopen (3).
{% endraw %}

```
### cmake/sdlchecks.cmake

```cmake

{% raw %}
31 | macro(CheckDLOPEN)
32 |   check_function_exists(dlopen HAVE_DLOPEN)
33 |   if(NOT HAVE_DLOPEN)
35 |       check_library_exists("${_LIBNAME}" "dlopen" "" DLOPEN_LIB)
36 |       if(DLOPEN_LIB)
39 |         set(HAVE_DLOPEN TRUE)
45 |   if(HAVE_DLOPEN)
52 |          void *handle = dlopen(\"\", RTLD_NOW);
54 |        }" HAVE_DLOPEN)
58 |   if (HAVE_DLOPEN)
59 |     set(SDL_LOADSO_DLOPEN 1)
60 |     set(HAVE_SDL_DLOPEN TRUE)
61 |     file(GLOB DLOPEN_SOURCES ${SDL2_SOURCE_DIR}/src/loadso/dlopen/*.c)
62 |     set(SOURCE_FILES ${SOURCE_FILES} ${DLOPEN_SOURCES})
102 | # - HAVE_DLOPEN opt
115 |         if(NOT HAVE_DLOPEN)
134 | # - HAVE_DLOPEN opt
145 |         if(NOT HAVE_DLOPEN)
164 | # - HAVE_DLOPEN opt
175 |         if(NOT HAVE_DLOPEN)
194 | # - HAVE_DLOPEN opt
209 |         if(NOT HAVE_DLOPEN)
229 | # - HAVE_DLOPEN opt
241 |         if(NOT HAVE_DLOPEN)
260 | # - HAVE_DLOPEN opt
272 |         if(NOT HAVE_DLOPEN)
291 | # - HAVE_DLOPEN opt
302 |         if(NOT HAVE_DLOPEN)
321 | # - HAVE_DLOPEN opt
372 |         if(NOT HAVE_DLOPEN)
506 | # - HAVE_DLOPEN opt
525 |                 if(NOT HAVE_DLOPEN)
567 | # - HAVE_DLOPEN opt
644 |         if(NOT HAVE_DLOPEN)
688 | # - HAVE_DLOPEN opt
700 |         if(NOT HAVE_DLOPEN)
{% endraw %}

```