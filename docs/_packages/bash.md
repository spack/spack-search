---
name: "bash"
layout: package
next_package: ompss
previous_package: py-importlib-resources
languages: ['cpp']
---
## 4.3
10 / 953 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [aclocal.m4](#aclocalm4)
 - [cross-build/cygwin32.cache](#cross-buildcygwin32cache)
 - [cross-build/opennt.cache](#cross-buildopenntcache)
 - [lib/intl/libgnuintl.h.in](#libintllibgnuintlhin)
 - [examples/loadables/Makefile.in](#examplesloadablesmakefilein)
 - [CWRU/misc/hpux10-dlfcn.h](#cwrumischpux10-dlfcnh)
 - [doc/rose94.ps](#docrose94ps)
 - [builtins/enable.def](#builtinsenabledef)

### config.h.in

```

{% raw %}
563 | /* Define if you have the dlopen function.  */
564 | #undef HAVE_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
854 | AC_CHECK_LIB(dl, dlopen)
855 | AC_CHECK_FUNCS(dlopen dlclose dlsym)
1131 | if test "$ac_cv_func_dlopen" = "yes" && test -f ${srcdir}/support/shobj-conf
{% endraw %}

```
### aclocal.m4

```

{% raw %}
3306 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### cross-build/cygwin32.cache

```

{% raw %}
33 | ac_cv_func_dlopen=${ac_cv_func_dlopen='yes'}
149 | ac_cv_lib_dl_dlopen=${ac_cv_lib_dl_dlopen='no'}
{% endraw %}

```
### cross-build/opennt.cache

```

{% raw %}
23 | ac_cv_func_dlopen=${ac_cv_func_dlopen=no}
101 | ac_cv_lib_dl_dlopen=${ac_cv_lib_dl_dlopen=no}
{% endraw %}

```
### lib/intl/libgnuintl.h.in

```

{% raw %}
77 |      4. in the dlopen()ed shared libraries, in the order in which they were
78 |         dlopen()ed.
83 |      * libintl.so is a dependency of a dlopen()ed shared library but not
{% endraw %}

```
### examples/loadables/Makefile.in

```

{% raw %}
99 | 	@echo "loading of shared objects using the dlopen(3) interface,"
{% endraw %}

```
### CWRU/misc/hpux10-dlfcn.h

```cpp

{% raw %}
3 |  * Not needed for later versions; HPUX 11.x has dlopen() and friends.
6 |  * with stub entries for dlopen, dlclose, dlsym, and dlerror:
8 |  *	int dlopen() { return(0);}
54 | #define dlopen(file,mode) (void *)shl_load((file), (mode), 0L)
{% endraw %}

```
### doc/rose94.ps

```

{% raw %}
1377 | 549.6 R F2(dlopen)2.848 E F0 .349(\(3\) library function, bash-2.0 will allo)B
{% endraw %}

```
### builtins/enable.def

```

{% raw %}
84 | #if defined (HAVE_DLOPEN) && defined (HAVE_DLSYM)
106 | #if defined (HAVE_DLOPEN) && defined (HAVE_DLSYM)
131 | #if defined (HAVE_DLOPEN) && defined (HAVE_DLSYM)
174 | #if defined (HAVE_DLOPEN) && defined (HAVE_DLSYM)
277 | #if defined (HAVE_DLOPEN) && defined (HAVE_DLSYM)
304 |   handle = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
306 |   handle = dlopen (filename, RTLD_LAZY);
{% endraw %}

```