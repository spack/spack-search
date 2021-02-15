---
name: "grads"
layout: package
next_package: flac
previous_package: lzo
languages: ['html', 'cpp', 'bash']
---
## 2.2.1
8 / 515 files match

 - [configure.ac](#configureac)
 - [src/gafunc.c](#srcgafuncc)
 - [src/gxsubs.c](#srcgxsubsc)
 - [src/gradspy.c](#srcgradspyc)
 - [etc/ltmain.sh](#etcltmainsh)
 - [doc/plugins.html](#docpluginshtml)
 - [doc/udp.html](#docudphtml)
 - [doc/python.html](#docpythonhtml)

### configure.ac

```

{% raw %}
62 | LT_INIT([dlopen disable-static])
{% endraw %}

```
### src/gafunc.c

```cpp

{% raw %}
7214 |     handle = dlopen(upb->fname,RTLD_LAZY);
7216 |       snprintf (pout,1255,"Error: dlopen failed to get a handle on %s \n",upb->fname);
{% endraw %}

```
### src/gxsubs.c

```cpp

{% raw %}
150 |   phandle = dlopen (pname, RTLD_LAZY);
152 |     printf("GX Package Error: dlopen failed to get a handle on gxprint plug-in named \"%s\" \n",gxpopt); 
190 |   dhandle = dlopen (dname, RTLD_LAZY);
192 |     printf("GX Package Error: dlopen failed to get a a handle on gxdisplay plug-in named \"%s\" \n",gxdopt); 
{% endraw %}

```
### src/gradspy.c

```cpp

{% raw %}
245 |   handle = dlopen ("libgradspy.so",    RTLD_LAZY | RTLD_GLOBAL );  /* for linux */
246 | /*   handle = dlopen ("libgradspy.dylib", RTLD_LAZY | RTLD_GLOBAL );  /\* for mac   *\/ */
{% endraw %}

```
### etc/ltmain.sh

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
### doc/plugins.html

```html

{% raw %}
55 | the file named by the GAUDPT environment variable, and in a file named &quot;udpt&quot; in the GADDIR directory. If there are any syntax errors in either of these  files, it is not a fatal error -- GrADS will issue a warning message with information about where the error is and what is wrong with the record, then it will ignore the record and continue. After all the available information about plug-ins has been parsed, GrADS will initialize the graphics package, with the message <code>&quot;GX Package Initialization&quot;</code>. It is at this point that GrADS will try to open and load the graphics plug-ins. If there are any problems, GrADS will return the message <code>&quot;GX Package Error: Could not find a record for the printing plug-in&quot;</code> or <code>&quot;GX Package Error: Could not find a record for the display plug-in&quot;</code> followed by some helpful information about the name of the  plug-in it is looking for, and the names of the files it parsed. These errors mean that something is wrong with the <a href="udpt.html">User-Defined Plug-in Tables</a>. Remember that the records in the GAUDPT file take precedence over records in the default udpt in GADDIR. If GrADS returns the message <code>&quot;GX Package Error: dlopen failed&quot;</code> it means the error is related to the shared object file itself -- it may be missing, corrupted, or the permissions may be wrong. 
{% endraw %}

```
### doc/udp.html

```html

{% raw %}
50 | <p> User Defined Plug-ins are compiled as dynamic libraries or shared object files and are loaded by GrADS using the dlopen(), dlsym(), and dlclose() functions. Compiling these dynamic object files is a two-step process that requires a slightly different syntax than what is normally used to compile a stand-alone executable. Consider an example plug-in program called addthis.c:
{% endraw %}

```
### doc/python.html

```html

{% raw %}
21 | <p>1. Move to the directory where your GrADS source code is installed (e.g. $HOME/grads-2.2.1/src). Make sure that gradspy.c, gradspy.h, and setup.py are in that directory. Edit the gradspy.c file so that the dlopen command will point to the correct name of the libgradspy  file for your system (use the .so extension for linux, the .dylib extension for Mac OS X). The relevant code looks like this (you must comment out one of these):
22 | <p> <code> handle = dlopen (&quot;libgradspy.so&quot;,    RTLD_LAZY | RTLD_GLOBAL );  /* for linux */<br>
23 |   handle = dlopen (&quot;libgradspy.dylib&quot;, RTLD_LAZY | RTLD_GLOBAL );  /* for mac   */ 
{% endraw %}

```