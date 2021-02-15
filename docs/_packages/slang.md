---
name: "slang"
layout: package
next_package: stacks
previous_package: tix
languages: ['cpp']
---
## 2.3.2
3 / 528 files match

 - [changes.txt](#changestxt)
 - [src/slimport.c](#srcslimportc)
 - [autoconf/aclocal.m4](#autoconfaclocalm4)

### changes.txt

```

{% raw %}
2706 | 10. src/slimport.c: Better handling of dlopen errors as suggested by
2817 |     required for dlopen. In addition, molesen at zeunastaerker.de sent
{% endraw %}

```
### src/slimport.c

```cpp

{% raw %}
41 | # define dlopen(a, b) LoadLibrary(a)
230 | 	handle = (VOID_STAR) dlopen (file, RTLD_NOW | RTLD_GLOBAL);
232 | 	handle = (VOID_STAR) dlopen (file, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### autoconf/aclocal.m4

```

{% raw %}
576 | dnl# AH_TEMPLATE([HAVE_DLOPEN],1,[Define if you have dlopen])
580 |   AC_CHECK_LIB(dl,dlopen,[
582 |     AC_DEFINE(HAVE_DLOPEN,1,[Define if you have dlopen])
584 |     AC_CHECK_FUNC(dlopen,AC_DEFINE(HAVE_DLOPEN,[Define if you have dlopen]))
585 |     if test "$ac_cv_func_dlopen" != yes
{% endraw %}

```