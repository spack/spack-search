---
name: "nettle"
layout: package
next_package: magics
previous_package: lcms
languages: ['cpp']
---
## 3.4.1
5 / 637 files match

 - [config.h.in](#confighin)
 - [configure.ac](#configureac)
 - [fat-setup.h](#fat-setuph)
 - [testsuite/dlopen-test.c](#testsuitedlopen-testc)
 - [testsuite/Makefile.in](#testsuitemakefilein)

### config.h.in

```

{% raw %}
38 | /* Define to 1 if you have dlopen (with -ldl). */
{% endraw %}

```
### configure.ac

```

{% raw %}
194 | AC_CHECK_LIB([dl], [dlopen],
196 | 			[Define to 1 if you have dlopen (with -ldl).])])
663 |     # -lhogweed -lgmp -lnettle are still required). Also makes dlopen
834 | IF_DLOPEN_TEST='#'
838 |   if test "x$ac_cv_lib_dl_dlopen" = xyes ; then
839 |     IF_DLOPEN_TEST=''
878 | AC_SUBST(IF_DLOPEN_TEST)
{% endraw %}

```
### fat-setup.h

```cpp

{% raw %}
83 |    platform-specific feature. To trigger problems, simply try dlopen
{% endraw %}

```
### testsuite/dlopen-test.c

```cpp

{% raw %}
11 |   void *handle = dlopen ("../libnettle.so", RTLD_NOW);
15 |       fprintf (stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### testsuite/Makefile.in

```

{% raw %}
64 | TS_ALL = $(TARGETS) $(TS_SH) @IF_DLOPEN_TEST@ dlopen-test$(EXEEXT)
70 | SOURCES = $(TS_SOURCES) $(EXTRA_SOURCES) testutils.c dlopen-test.c
99 | dlopen-test$(EXEEXT): dlopen-test.$(OBJEXT) testutils.$(OBJEXT)
100 | 	$(LINK) dlopen-test.$(OBJEXT) -ldl -o dlopen-test$(EXEEXT)
155 | 	-rm -f $(TARGETS) $(EXTRA_TARGETS) dlopen-test$(EXEEXT) \
{% endraw %}

```