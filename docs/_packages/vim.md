---
name: "vim"
layout: package
next_package: py-cyvcf2
previous_package: py-grpcio
languages: ['cpp']
---
## 8.1.0001
11 / 2766 files match

 - [src/os_unix.c](#srcos_unixc)
 - [src/config.h.in](#srcconfighin)
 - [src/configure.ac](#srcconfigureac)
 - [src/feature.h](#srcfeatureh)
 - [src/if_python.c](#srcif_pythonc)
 - [src/if_perl.xs](#srcif_perlxs)
 - [src/if_tcl.c](#srcif_tclc)
 - [src/if_ruby.c](#srcif_rubyc)
 - [src/if_python3.c](#srcif_python3c)
 - [src/if_lua.c](#srcif_luac)
 - [runtime/doc/version8.txt](#runtimedocversion8txt)

### src/os_unix.c

```cpp

{% raw %}
7271 | # if defined(USE_DLOPEN)
7286 | # if defined(USE_DLOPEN)
7287 |     /* First clear any error, it's not cleared by the dlopen() call. */
7290 |     hinstLib = dlopen((char *)libname, RTLD_LAZY
7318 | #  if defined(USE_DLOPEN)
7331 | # if defined(USE_DLOPEN)
7340 | # if defined(USE_DLOPEN)
7353 | # if defined(USE_DLOPEN)
7362 | # if defined(USE_DLOPEN)
7400 | # if defined(USE_DLOPEN)
{% endraw %}

```
### src/config.h.in

```

{% raw %}
326 | /* Define for linking via dlopen() or LoadLibrary() */
335 | /* Define for linking via dlopen() or LoadLibrary() */
344 | /* Define for linking via dlopen() or LoadLibrary() */
347 | /* Define for linking via dlopen() or LoadLibrary() */
359 | /* Define for linking via dlopen() or LoadLibrary() */
365 | /* Define for linking via dlopen() or LoadLibrary() */
419 | /* Define if we have dlopen() */
420 | #undef HAVE_DLOPEN
{% endraw %}

```
### src/configure.ac

```

{% raw %}
1589 | dnl with dlopen(), dlsym(), dlclose() 
1610 |       void* pylib = dlopen(python_instsoname, RTLD_LAZY|RTLD_LOCAL);
1656 |       void* pylib = dlopen(python_instsoname, RTLD_LAZY|RTLD_LOCAL);
4274 |   AC_MSG_CHECKING([for dlopen()])
4276 | 		extern void* dlopen();
4277 | 		dlopen();
4280 | 	      AC_DEFINE(HAVE_DLOPEN, 1, [ Define if we have dlopen() ]),
4282 | 	      AC_MSG_CHECKING([for dlopen() in -ldl])
4286 | 				extern void* dlopen();
4287 | 				dlopen();
4290 | 			  AC_DEFINE(HAVE_DLOPEN, 1, [ Define if we have dlopen() ]),
4293 |   dnl ReliantUNIX has dlopen() in libc but everything else in libdl
{% endraw %}

```
### src/feature.h

```cpp

{% raw %}
679 | /* Using dlopen() also requires dlsym() to be available. */
680 | #if defined(HAVE_DLOPEN) && defined(HAVE_DLSYM)
681 | # define USE_DLOPEN
684 | 	&& (defined(USE_DLOPEN) || defined(HAVE_SHL_LOAD))))
{% endraw %}

```
### src/if_python.c

```cpp

{% raw %}
132 | #   define load_dll(n) dlopen((n), RTLD_LAZY)
134 | #   define load_dll(n) dlopen((n), RTLD_LAZY|RTLD_GLOBAL)
{% endraw %}

```
### src/if_perl.xs

```

{% raw %}
164 | #  define load_dll(n) dlopen((n), RTLD_LAZY|RTLD_GLOBAL)
662 |  * 1. Get module handle using dlopen() or vimLoadLib().
{% endraw %}

```
### src/if_tcl.c

```cpp

{% raw %}
166 | #  define load_dll(n) dlopen((n), RTLD_LAZY|RTLD_GLOBAL)
{% endraw %}

```
### src/if_ruby.c

```cpp

{% raw %}
68 | # define load_dll(n) dlopen((n), RTLD_LAZY|RTLD_GLOBAL)
{% endraw %}

```
### src/if_python3.c

```cpp

{% raw %}
119 | #   define load_dll(n) dlopen((n), RTLD_LAZY)
121 | #   define load_dll(n) dlopen((n), RTLD_LAZY|RTLD_GLOBAL)
{% endraw %}

```
### src/if_lua.c

```cpp

{% raw %}
73 | # define load_dll(n) dlopen((n), RTLD_LAZY|RTLD_GLOBAL)
{% endraw %}

```
### runtime/doc/version8.txt

```

{% raw %}
7578 | Problem:    On OSX the default flag for dlopen() is different.
{% endraw %}

```