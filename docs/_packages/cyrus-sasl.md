---
name: "cyrus-sasl"
layout: package
next_package: googletest
previous_package: libquo
languages: ['html', 'cpp', 'bash']
---
## 2.1.26
16 / 529 files match

 - [configure.in](#configurein)
 - [config/libtool.m4](#configlibtoolm4)
 - [config/ltmain.sh](#configltmainsh)
 - [lib/windlopen.c](#libwindlopenc)
 - [lib/Makefile.am](#libmakefileam)
 - [lib/dlopen.c](#libdlopenc)
 - [lib/saslint.h](#libsaslinth)
 - [dlcompat-20010505/dlfcn.h](#dlcompat-20010505dlfcnh)
 - [dlcompat-20010505/dlopen.c](#dlcompat-20010505dlopenc)
 - [mac/mac_lib/mac_monolithic_dlopen.c](#macmac_libmac_monolithic_dlopenc)
 - [mac/mac_lib/mac_dyn_dlopen.c](#macmac_libmac_dyn_dlopenc)
 - [contrib/stripplus_canonuser.patch](#contribstripplus_canonuserpatch)
 - [contrib/cyrus-sasl-1.5.24-ltdl.patches](#contribcyrus-sasl-1524-ltdlpatches)
 - [saslauthd/config/ltmain.sh](#saslauthdconfigltmainsh)
 - [doc/plugprog.html](#docplugproghtml)
 - [doc/macosx.html](#docmacosxhtml)

### configure.in

```

{% raw %}
121 | AC_ARG_ENABLE(staticdlopen, [  --enable-staticdlopen   try dynamic plugins when we are a static libsasl [[no]] ],
122 |                 enable_staticdlopen=$enableval,
123 |                 enable_staticdlopen=no)
125 | if test "$enable_staticdlopen" = yes; then
126 |   AC_DEFINE(TRY_DLOPEN_WHEN_STATIC,[],[Should we try to dlopen() plugins while statically compiled?])
217 | AC_CHECK_LIB(dl, dlopen, SASL_DL_LIB="-ldl", SASL_DL_LIB="")
247 |   if test $ac_cv_lib_dl_dlopen = yes ; then
255 | main() { void *self, *ptr1, *ptr2; self=dlopen(NULL,RTLD_LAZY);
941 | 	AC_DEFINE(DO_DLOPEN,[],[Should we build a shared plugin (via dlopen) library?])
{% endraw %}

```
### config/libtool.m4

```

{% raw %}
80 | ifdef([AC_PROVIDE_AC_LIBTOOL_DLOPEN],
81 | [libtool_flags="$libtool_flags --enable-dlopen"])
133 | # AC_LIBTOOL_DLOPEN - enable checks for dlopen support
134 | AC_DEFUN([AC_LIBTOOL_DLOPEN], [AC_BEFORE([$0],[AC_LIBTOOL_SETUP])])
{% endraw %}

```
### config/ltmain.sh

```bash

{% raw %}
194 |   -dlopen)
195 |     prevopt="-dlopen"
260 |   # Only execute mode is allowed to have -dlopen flags.
262 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
876 | 	    dlopen_self=$dlopen_self_static
880 | 	    dlopen_self=$dlopen_self_static
929 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1020 |       -dlopen)
1196 | 	  if test "$build_libtool_libs" = yes && test "$dlopen" = yes; then
1300 | 	# This library was specified with -dlopen.
1303 | 	  if test -z "$dlname" || test "$dlopen" != yes || test "$build_libtool_libs" = no; then
1304 | 	    # If there is no dlname, no dlopen support or we're linking statically,
1561 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
1631 | 	$echo "$modename: warning: \`-dlopen' is ignored for libtool libraries" 1>&2
2037 | 	    echo "*** a static module, that should work as long as the dlopening"
2038 | 	    echo "*** application is linked with the -dlopen flag."
2056 | 	    echo "*** or is declared to -dlopen it."
2226 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
2396 | 	if test "$dlopen" = unknown && test "$dlopen_self" = unknown &&
2397 | 	   test "$dlopen_self_static" = unknown; then
2398 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
3136 | # The name that we can dlopen(3).
3653 |     # Handle -dlopen flags immediately.
3682 | 	# Skip this library if it cannot be dlopened.
3707 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
3942 |   -dlopen FILE      add the directory containing FILE to the library path
3944 | This mode sets the library path environment variable according to \`-dlopen'
3993 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
4002 |   -module           build a library that can dlopened
{% endraw %}

```
### lib/windlopen.c

```cpp

{% raw %}
0 | /* windlopen.c--Windows dynamic loader interface
2 |  * $Id: windlopen.c,v 1.17 2009/01/25 20:20:57 mel Exp $
{% endraw %}

```
### lib/Makefile.am

```

{% raw %}
49 | EXTRA_DIST = windlopen.c staticopen.h NTMakefile
57 | common_sources = auxprop.c canonusr.c checkpw.c client.c common.c config.c external.c md5.c saslutil.c server.c seterror.c dlopen.c ../plugins/plugin_common.c
{% endraw %}

```
### lib/dlopen.c

```cpp

{% raw %}
0 | /* dlopen.c--Unix dlopen() dynamic loader interface
3 |  * $Id: dlopen.c,v 1.52 2009/04/11 10:21:43 mel Exp $
63 | #ifdef DO_DLOPEN
101 | dlopen(char *fname, int mode)
175 | #endif /* DO_DLOPEN */
180 | #ifdef DO_DLOPEN
225 | #endif /* DO_DLOPEN */
228 | #ifdef DO_DLOPEN
348 | #endif /* DO_DLOPEN */
355 | #ifdef DO_DLOPEN
374 |     if (!(library = dlopen(file, flag))) {
376 | 		  "unable to dlopen %s: %s", file, dlerror());
389 | #endif /* DO_DLOPEN */
399 | #ifdef DO_DLOPEN
455 |  * we support dlopen()
457 |  *      OR we are staticly compiled and TRY_DLOPEN_WHEN_STATIC is defined
459 | #if defined(DO_DLOPEN) && (defined(PIC) || (!defined(PIC) && defined(TRY_DLOPEN_WHEN_STATIC)))
540 | #endif /* defined(DO_DLOPEN) && (!defined(PIC) || (defined(PIC) && defined(TRY_DLOPEN_WHEN_STATIC))) */
548 | #ifdef DO_DLOPEN
559 | #endif /* DO_DLOPEN */
{% endraw %}

```
### lib/saslint.h

```cpp

{% raw %}
351 |  * dlopen.c and staticopen.c
{% endraw %}

```
### dlcompat-20010505/dlfcn.h

```cpp

{% raw %}
33 | extern void * dlopen(
{% endraw %}

```
### dlcompat-20010505/dlopen.c

```cpp

{% raw %}
58 |  * The structure of a dlopen() handle.
60 | struct dlopen_handle {
63 |     int dlopen_mode;	/* current dlopen mode for this handle */
64 |     int dlopen_count;	/* number of times dlopen() called on this handle */
66 |     struct dlopen_handle *prev;
67 |     struct dlopen_handle *next;
69 | static struct dlopen_handle *dlopen_handles = NULL;
70 | static const struct dlopen_handle main_program_handle = {NULL};
77 |  * the functionality need to implement the dlopen() interfaces.
180 |  * dlopen() the MacOS X version of the FreeBSD dlopen() interface.
183 | dlopen(
193 |     struct dlopen_handle *p;
199 |         DEBUG_PRINT2("libdl: dlopen(%s,0x%x) -> ", path, (unsigned int)mode);
240 | 	    p = dlopen_handles;
244 | 		    if((p->dlopen_mode & RTLD_UNSHARED) == RTLD_UNSHARED)
252 | 		    if((p->dlopen_mode & RTLD_LOCAL) == RTLD_LOCAL &&
256 | 			    p->dlopen_mode &= ~RTLD_LOCAL;
257 | 			    p->dlopen_mode |= RTLD_GLOBAL;
258 | 			    p->dlopen_count++;
269 | 		    p->dlopen_count++;
327 | 	    dlerror_pointer = "NSLinkModule() failed for dlopen()";
345 | 	p = malloc(sizeof(struct dlopen_handle));
347 | 	    dlerror_pointer = "can't allocate memory for the dlopen handle";
356 | 	    p->dlopen_mode = RTLD_GLOBAL;
358 | 	    p->dlopen_mode = RTLD_LOCAL;
359 | 	p->dlopen_mode |= (mode & RTLD_UNSHARED) |
362 | 	p->dlopen_count = 1;
365 | 	p->next = dlopen_handles;
366 | 	if(dlopen_handles != NULL)
367 | 	    dlopen_handles->prev = p;
368 | 	dlopen_handles = p;
382 |  * dlsym() the MacOS X version of the FreeBSD dlopen() interface.
389 |     struct dlopen_handle *dlopen_handle, *p;
395 | 	dlopen_handle = (struct dlopen_handle *)handle;
400 | 	if(dlopen_handle == (struct dlopen_handle *)&main_program_handle){
418 | 	p = dlopen_handles;
420 | 	    if(dlopen_handle == p){
443 |  * dlerror() the MacOS X version of the FreeBSD dlopen() interface.
457 |  * dlclose() the MacOS X version of the FreeBSD dlopen() interface.
463 |     struct dlopen_handle *p, *q;
471 | 	q = (struct dlopen_handle *)handle;
472 | 	p = dlopen_handles;
475 | 		/* if the dlopen() count is not zero we are done */
476 | 		p->dlopen_count--;
477 | 		if(p->dlopen_count != 0){
491 | 		if(p->dlopen_mode & RTLD_NODELETE)
493 | 		if(p->dlopen_mode & RTLD_LAZY_UNDEF)
504 | 		if(dlopen_handles == p)
505 | 		    dlopen_handles = p->next;
{% endraw %}

```
### mac/mac_lib/mac_monolithic_dlopen.c

```cpp

{% raw %}
39 | /* $Id: mac_monolithic_dlopen.c,v 1.3 2003/02/13 19:55:59 rjs3 Exp $ */
{% endraw %}

```
### mac/mac_lib/mac_dyn_dlopen.c

```cpp

{% raw %}
2 |  * $Id: mac_dyn_dlopen.c,v 1.3 2003/02/13 19:55:59 rjs3 Exp $
{% endraw %}

```
### contrib/stripplus_canonuser.patch

```

{% raw %}
8 |  	AC_DEFINE(DO_DLOPEN,[],[Should we build a shared plugin (via dlopen) library?])
{% endraw %}

```
### contrib/cyrus-sasl-1.5.24-ltdl.patches

```

{% raw %}
22 | +AC_LIBTOOL_DLOPEN
66 |  EXTRA_DIST = saslint.h windlopen.c
121 | diff -x ltcf-c.sh -x ltconfig -x ltmain.sh -x libltdl -x config.guess -x config.sub -x configure -x aclocal.m4 -x Makefile.in -uNr cyrus-sasl-1.5.24.orig/lib/dlopen.c cyrus-sasl-1.5.24.new/lib/dlopen.c
122 | --- cyrus-sasl-1.5.24.orig/lib/dlopen.c	Thu Mar  9 21:53:47 2000
123 | +++ cyrus-sasl-1.5.24.new/lib/dlopen.c	Tue Jul 17 12:45:35 2001
143 | -dlopen(char *fname, int mode)
249 | -	if (!(library = dlopen(tmp, flag))) {
250 | +	if (!(library = lt_dlopen(tmp))) {
252 | -		      "unable to dlopen %s: %s", tmp, dlerror());
253 | +		      "unable to lt_dlopen %s: %s", tmp, lt_dlerror());
324 | -  void *library; /* this a pointer to shared library returned by dlopen 
325 | +  lt_dlhandle library; /* this a pointer to shared library returned by dlopen 
{% endraw %}

```
### saslauthd/config/ltmain.sh

```bash

{% raw %}
194 |   -dlopen)
195 |     prevopt="-dlopen"
260 |   # Only execute mode is allowed to have -dlopen flags.
262 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
876 | 	    dlopen_self=$dlopen_self_static
880 | 	    dlopen_self=$dlopen_self_static
929 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1020 |       -dlopen)
1196 | 	  if test "$build_libtool_libs" = yes && test "$dlopen" = yes; then
1300 | 	# This library was specified with -dlopen.
1303 | 	  if test -z "$dlname" || test "$dlopen" != yes || test "$build_libtool_libs" = no; then
1304 | 	    # If there is no dlname, no dlopen support or we're linking statically,
1561 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
1631 | 	$echo "$modename: warning: \`-dlopen' is ignored for libtool libraries" 1>&2
2036 | 	    echo "*** a static module, that should work as long as the dlopening"
2037 | 	    echo "*** application is linked with the -dlopen flag."
2055 | 	    echo "*** or is declared to -dlopen it."
2220 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
2390 | 	if test "$dlopen" = unknown && test "$dlopen_self" = unknown &&
2391 | 	   test "$dlopen_self_static" = unknown; then
2392 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
3130 | # The name that we can dlopen(3).
3647 |     # Handle -dlopen flags immediately.
3676 | 	# Skip this library if it cannot be dlopened.
3701 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
3936 |   -dlopen FILE      add the directory containing FILE to the library path
3938 | This mode sets the library path environment variable according to \`-dlopen'
3987 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
3996 |   -module           build a library that can dlopened
{% endraw %}

```
### doc/plugprog.html

```html

{% raw %}
61 |        the ability to dlopen a shared library.  Thus, all plugins should
64 |        get the appropriate name to dlopen), but they can have an extention
{% endraw %}

```
### doc/macosx.html

```html

{% raw %}
116 |   <li>Symbols which are dlopened have an underscore prefixed. (This
{% endraw %}

```