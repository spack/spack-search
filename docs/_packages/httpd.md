---
name: "httpd"
layout: package
next_package: libxvmc
previous_package: kubernetes
languages: ['cpp', 'bash']
---
## 2.4.38
6 / 2704 files match

 - [README.platforms](#readmeplatforms)
 - [build/ltmain.sh](#buildltmainsh)
 - [docs/manual/dso.html.ja.utf8](#docsmanualdsohtmljautf8)
 - [docs/manual/dso.html.tr.utf8](#docsmanualdsohtmltrutf8)
 - [docs/manual/dso.html.fr.utf8](#docsmanualdsohtmlfrutf8)
 - [modules/core/mod_so.c](#modulescoremod_soc)

### README.platforms

```

{% raw %}
57 |    The dlopen() system call in HP-UX has problems when loading/unloading
59 |    of dlopen(). This is fixed in the Apache 2.0.44 release.
65 |       When using dlopen          : "cpprt0_stub.s -lcl -lCsup"
68 |       When using dlopen/shl_load : "cpprt0_stub.s -lcl -lunwind"
{% endraw %}

```
### build/ltmain.sh

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
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### docs/manual/dso.html.ja.utf8

```

{% raw %}
159 |     <code>dlopen()/dlsym()</code> による Unix ローダへの
192 |     ですので、実行プログラムは <code>dlopen()</code> を使って
294 |       <code>dlopen ()</code> を使ってコードを自分自身でロードするかの
{% endraw %}

```
### docs/manual/dso.html.tr.utf8

```

{% raw %}
162 |       arayüzü sağlayan <code>dlopen()/dlsym()</code> sistem çağrılarının elle
201 |       çalıştırılabilir program DSO’yu çalışma anında <code>dlopen()</code>
294 |         <code>dlopen()</code> vasıtasıyla yüklemektir.</li>
{% endraw %}

```
### docs/manual/dso.html.fr.utf8

```

{% raw %}
176 |     des appels système <code>dlopen()/dlsym()</code>.</p>
216 |     espace d'adressage à l'aide de l'appel système <code>dlopen()</code>.
321 |       chargez le code vous-même via <code>dlopen()</code>.</li>
{% endraw %}

```
### modules/core/mod_so.c

```cpp

{% raw %}
64 |  * vendors cc(1), ld(1) and dlopen(3) manpages to find out the appropriate
121 | #ifndef NO_DLOPEN
152 |         /* retry on error without path to use dlopen()'s search path */
398 | #else /* not NO_DLOPEN */
415 | #endif /* NO_DLOPEN */
419 | #ifndef NO_DLOPEN
{% endraw %}

```