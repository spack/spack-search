---
name: "lighttpd"
layout: package
next_package: libxaw3d
previous_package: raft
languages: ['cpp', 'bash']
---
## 1.4.53
32 / 384 files match

 - [configure.ac](#configureac)
 - [ltmain.sh](#ltmainsh)
 - [src/mod_usertrack.c](#srcmod_usertrackc)
 - [src/mod_magnet.c](#srcmod_magnetc)
 - [src/plugin.h](#srcpluginh)
 - [src/mod_uploadprogress.c](#srcmod_uploadprogressc)
 - [src/mod_secdownload.c](#srcmod_secdownloadc)
 - [src/mod_vhostdb_mysql.c](#srcmod_vhostdb_mysqlc)
 - [src/mod_ssi.c](#srcmod_ssic)
 - [src/mod_geoip.c](#srcmod_geoipc)
 - [src/mod_alias.c](#srcmod_aliasc)
 - [src/mod_vhostdb_ldap.c](#srcmod_vhostdb_ldapc)
 - [src/mod_staticfile.c](#srcmod_staticfilec)
 - [src/mod_webdav.c](#srcmod_webdavc)
 - [src/mod_vhostdb_pgsql.c](#srcmod_vhostdb_pgsqlc)
 - [src/mod_setenv.c](#srcmod_setenvc)
 - [src/mod_trigger_b4_dl.c](#srcmod_trigger_b4_dlc)
 - [src/mod_flv_streaming.c](#srcmod_flv_streamingc)
 - [src/mod_expire.c](#srcmod_expirec)
 - [src/meson.build](#srcmesonbuild)
 - [src/mod_skeleton.c](#srcmod_skeletonc)
 - [src/mod_userdir.c](#srcmod_userdirc)
 - [src/mod_dirlisting.c](#srcmod_dirlistingc)
 - [src/mod_mysql_vhost.c](#srcmod_mysql_vhostc)
 - [src/mod_indexfile.c](#srcmod_indexfilec)
 - [src/plugin.c](#srcpluginc)
 - [src/mod_vhostdb_dbi.c](#srcmod_vhostdb_dbic)
 - [src/mod_extforward.c](#srcmod_extforwardc)
 - [src/CMakeLists.txt](#srccmakeliststxt)
 - [m4/libtool.m4](#m4libtoolm4)
 - [m4/ltoptions.m4](#m4ltoptionsm4)
 - [doc/outdated/plugins.txt](#docoutdatedpluginstxt)

### configure.ac

```

{% raw %}
88 | AC_LIBTOOL_DLOPEN
158 | dnl need dlopen/-ldl to load plugins (when not on windows)
161 | AC_SEARCH_LIBS([dlopen], [dl], [
{% endraw %}

```
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
### src/mod_usertrack.c

```cpp

{% raw %}
269 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_magnet.c

```cpp

{% raw %}
1054 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/plugin.h

```cpp

{% raw %}
66 | 	/* dlopen handle */
{% endraw %}

```
### src/mod_uploadprogress.c

```cpp

{% raw %}
396 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_secdownload.c

```cpp

{% raw %}
555 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_vhostdb_mysql.c

```cpp

{% raw %}
282 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_ssi.c

```cpp

{% raw %}
1347 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_geoip.c

```cpp

{% raw %}
289 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_alias.c

```cpp

{% raw %}
203 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_vhostdb_ldap.c

```cpp

{% raw %}
543 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_staticfile.c

```cpp

{% raw %}
205 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_webdav.c

```cpp

{% raw %}
2801 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_vhostdb_pgsql.c

```cpp

{% raw %}
259 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_setenv.c

```cpp

{% raw %}
294 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_trigger_b4_dl.c

```cpp

{% raw %}
588 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_flv_streaming.c

```cpp

{% raw %}
208 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_expire.c

```cpp

{% raw %}
408 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/meson.build

```

{% raw %}
210 | 		if not(compiler.has_function('dlopen', args: defs, dependencies: libdl, prefix: '#include <dlfcn.h>'))
211 | 			error('Couldn\'t find dlfcn.h or dlopen in lib dl')
{% endraw %}

```
### src/mod_skeleton.c

```cpp

{% raw %}
169 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_userdir.c

```cpp

{% raw %}
333 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_dirlisting.c

```cpp

{% raw %}
1200 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_mysql_vhost.c

```cpp

{% raw %}
365 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_indexfile.c

```cpp

{% raw %}
219 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/plugin.c

```cpp

{% raw %}
228 | 		if (NULL == (p->lib = dlopen(srv->tmp_buf->ptr, RTLD_NOW|RTLD_GLOBAL))) {
229 | 			log_error_write(srv, __FILE__, __LINE__, "sbs", "dlopen() failed for:",
{% endraw %}

```
### src/mod_vhostdb_dbi.c

```cpp

{% raw %}
318 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/mod_extforward.c

```cpp

{% raw %}
1165 | /* this function is called at dlopen() time and inits the callbacks */
{% endraw %}

```
### src/CMakeLists.txt

```

{% raw %}
592 | 	check_library_exists(dl dlopen "" HAVE_LIBDL)
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
### doc/outdated/plugins.txt

```

{% raw %}
92 | ``lib`` is the library handler from dlopen and ``data`` will be the storage
{% endraw %}

```