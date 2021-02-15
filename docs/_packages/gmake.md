---
name: "gmake"
layout: package
next_package: boost
previous_package: gawk
languages: ['cpp']
---
## 4.2.1
6 / 204 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [load.c](#loadc)
 - [config/lib-link.m4](#configlib-linkm4)
 - [w32/compat/posixfcn.c](#w32compatposixfcnc)
 - [w32/include/dlfcn.h](#w32includedlfcnh)

### config.h.in

```

{% raw %}
66 | /* Define to 1 if you have the declaration of `dlopen', and to 0 if you don't.
68 | #undef HAVE_DECL_DLOPEN
{% endraw %}

```
### configure.ac

```

{% raw %}
314 | AC_CHECK_DECLS([dlopen, dlsym, dlerror], [], [],
323 | AS_CASE([/$ac_cv_have_decl_dlopen/$ac_cv_have_decl_dlsym/$ac_cv_have_decl_dlerror/],
328 |   AC_SEARCH_LIBS([dlopen], [dl], [], [make_cv_load=])
496 |   echo "         supports the dlopen(), dlsym(), and dlerror() functions."
{% endraw %}

```
### load.c

```cpp

{% raw %}
55 |       global_dl = dlopen (NULL, RTLD_NOW|RTLD_GLOBAL);
75 |         dlp = dlopen (concat (2, "./", ldname), RTLD_LAZY|RTLD_GLOBAL);
79 |         dlp = dlopen (ldname, RTLD_LAZY|RTLD_GLOBAL);
{% endraw %}

```
### config/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### w32/compat/posixfcn.c

```cpp

{% raw %}
371 | dlopen (const char *file, int mode)
{% endraw %}

```
### w32/include/dlfcn.h

```cpp

{% raw %}
23 | extern void *dlopen (const char *, int);
{% endraw %}

```