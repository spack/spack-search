---
name: "valgrind"
layout: package
next_package: libpciaccess
previous_package: libidn2
languages: ['cpp']
---
## 3.14.0
26 / 5760 files match

 - [glibc-2.2.supp](#glibc-22supp)
 - [glibc-2.3.supp](#glibc-23supp)
 - [darwin12.supp](#darwin12supp)
 - [mpi/libmpiwrap.c](#mpilibmpiwrapc)
 - [perf/tinycc.c](#perftinyccc)
 - [cachegrind/tests/dlclose.c](#cachegrindtestsdlclosec)
 - [memcheck/tests/linux/dlclose_leak_so.c](#memchecktestslinuxdlclose_leak_soc)
 - [memcheck/tests/linux/dlclose_leak.c](#memchecktestslinuxdlclose_leakc)
 - [memcheck/tests/linux/Makefile.am](#memchecktestslinuxmakefileam)
 - [memcheck/tests/linux/Makefile.in](#memchecktestslinuxmakefilein)
 - [callgrind/global.h](#callgrindglobalh)
 - [exp-sgcheck/tests/preen_invars_so.c](#exp-sgchecktestspreen_invars_soc)
 - [exp-sgcheck/tests/preen_invars.c](#exp-sgchecktestspreen_invarsc)
 - [drd/drd_pthread_intercepts.c](#drddrd_pthread_interceptsc)
 - [drd/tests/dlopen_lib.c](#drdtestsdlopen_libc)
 - [drd/tests/dlopen.vgtest](#drdtestsdlopenvgtest)
 - [drd/tests/Makefile.am](#drdtestsmakefileam)
 - [drd/tests/dlopen_main.c](#drdtestsdlopen_mainc)
 - [drd/tests/Makefile.in](#drdtestsmakefilein)
 - [docs/index.ps](#docsindexps)
 - [docs/xml/manual-core-adv.xml](#docsxmlmanual-core-advxml)
 - [docs/internals/3_12_BUGSTATUS.txt](#docsinternals3_12_bugstatustxt)
 - [docs/internals/3_13_BUGSTATUS.txt](#docsinternals3_13_bugstatustxt)
 - [docs/internals/segments-seginfos.txt](#docsinternalssegments-seginfostxt)
 - [docs/internals/3_11_BUGSTATUS.txt](#docsinternals3_11_bugstatustxt)
 - [none/tests/solaris/mmap_noreserve.c](#nonetestssolarismmap_noreservec)

### glibc-2.2.supp

```

{% raw %}
33 |    strlen/__GI__dl_open/dlopen_doit
37 |    fun:dlopen_doit
{% endraw %}

```
### glibc-2.3.supp

```

{% raw %}
32 |    strlen/__GI__dl_open/dlopen_doit
36 |    fun:dlopen_doit
{% endraw %}

```
### darwin12.supp

```

{% raw %}
311 |    fun:dlopen
319 |    fun:dlopen
{% endraw %}

```
### mpi/libmpiwrap.c

```cpp

{% raw %}
929 | /* Hook so it's visible from outside (can be handy to dlopen/dlsym
{% endraw %}

```
### perf/tinycc.c

```cpp

{% raw %}
1360 | 					   by rld on dlopen() calls.  */
6584 | void *dlopen(const char *filename, int flag)
21009 |                     //h = dlopen(filename, RTLD_GLOBAL | RTLD_LAZY);
21010 | 		    // jrs: remove need for dlopen
{% endraw %}

```
### cachegrind/tests/dlclose.c

```cpp

{% raw %}
18 |    handle = dlopen ("./myprint.so", RTLD_LAZY);
{% endraw %}

```
### memcheck/tests/linux/dlclose_leak_so.c

```cpp

{% raw %}
5 |  * errors reported while the dlopen'ed object is loaded work. */
{% endraw %}

```
### memcheck/tests/linux/dlclose_leak.c

```cpp

{% raw %}
0 | /*  Test reporting of memory leaks in objects that have been dlopen'ed.
17 |         void* handle = dlopen("./dlclose_leak_so.so", RTLD_NOW);
19 |             printf("FAILURE to dlopen dlclose_leak_so.so\n");
{% endraw %}

```
### memcheck/tests/linux/Makefile.am

```

{% raw %}
66 | # in order to properly test a 'fully dynamic' use of dlopen/dlclose
{% endraw %}

```
### memcheck/tests/linux/Makefile.in

```

{% raw %}
680 | # in order to properly test a 'fully dynamic' use of dlopen/dlclose
{% endraw %}

```
### callgrind/global.h

```cpp

{% raw %}
431 | /* If an object is dlopened multiple times, we hope that <name> is unique;
432 |  * <start> and <offset> can change with each dlopen, and <start> is
{% endraw %}

```
### exp-sgcheck/tests/preen_invars_so.c

```cpp

{% raw %}
2 |    which is dlopened by preen_invar.c.  That then accesses the global
{% endraw %}

```
### exp-sgcheck/tests/preen_invars.c

```cpp

{% raw %}
12 |   void* hdl = dlopen("./preen_invars_so.so", RTLD_NOW);
{% endraw %}

```
### drd/drd_pthread_intercepts.c

```cpp

{% raw %}
241 |  * dlopen() has loaded the shared library with DRD client intercepts because
{% endraw %}

```
### drd/tests/dlopen_lib.c

```cpp

{% raw %}
3 | #include "dlopen_lib.h"
{% endraw %}

```
### drd/tests/dlopen.vgtest

```

{% raw %}
0 | prereq: test -e dlopen_main && ./supported_libpthread
2 | prog: dlopen_main ./dlopen_lib.so
{% endraw %}

```
### drd/tests/Makefile.am

```

{% raw %}
22 | 	dlopen_lib.h
108 | 	dlopen.stderr.exp			    \
109 | 	dlopen.stdout.exp			    \
110 | 	dlopen.vgtest				    \
370 |   dlopen_main         \
371 |   dlopen_lib.so       \
474 | dlopen_main_LDADD           = -ldl
475 | dlopen_lib_so_SOURCES       = dlopen_lib.c
476 | dlopen_lib_so_CFLAGS        = -fPIC
477 | dlopen_lib_so_LDFLAGS       = -shared -fPIC
{% endraw %}

```
### drd/tests/dlopen_main.c

```cpp

{% raw %}
3 | #include "dlopen_lib.h"
12 |   handle = dlopen(lib, RTLD_NOW);
{% endraw %}

```
### drd/tests/Makefile.in

```

{% raw %}
131 | 	dlopen_main$(EXEEXT) dlopen_lib.so$(EXEEXT) fp_race$(EXEEXT) \
310 | am_dlopen_lib_so_OBJECTS = dlopen_lib_so-dlopen_lib.$(OBJEXT)
311 | dlopen_lib_so_OBJECTS = $(am_dlopen_lib_so_OBJECTS)
312 | dlopen_lib_so_LDADD = $(LDADD)
313 | dlopen_lib_so_DEPENDENCIES =
314 | dlopen_lib_so_LINK = $(CCLD) $(dlopen_lib_so_CFLAGS) $(CFLAGS) \
315 | 	$(dlopen_lib_so_LDFLAGS) $(LDFLAGS) -o $@
316 | dlopen_main_SOURCES = dlopen_main.c
317 | dlopen_main_OBJECTS = dlopen_main.$(OBJEXT)
318 | dlopen_main_DEPENDENCIES =
605 | 	$(dlopen_lib_so_SOURCES) dlopen_main.c fp_race.c \
631 | 	$(dlopen_lib_so_SOURCES) dlopen_main.c fp_race.c \
1068 | 	dlopen_lib.h
1154 | 	dlopen.stderr.exp			    \
1155 | 	dlopen.stdout.exp			    \
1156 | 	dlopen.vgtest				    \
1407 | dlopen_main_LDADD = -ldl
1408 | dlopen_lib_so_SOURCES = dlopen_lib.c
1409 | dlopen_lib_so_CFLAGS = -fPIC
1410 | dlopen_lib_so_LDFLAGS = -shared -fPIC
1574 | dlopen_lib.so$(EXEEXT): $(dlopen_lib_so_OBJECTS) $(dlopen_lib_so_DEPENDENCIES) $(EXTRA_dlopen_lib_so_DEPENDENCIES) 
1575 | 	@rm -f dlopen_lib.so$(EXEEXT)
1576 | 	$(AM_V_CCLD)$(dlopen_lib_so_LINK) $(dlopen_lib_so_OBJECTS) $(dlopen_lib_so_LDADD) $(LIBS)
1578 | dlopen_main$(EXEEXT): $(dlopen_main_OBJECTS) $(dlopen_main_DEPENDENCIES) $(EXTRA_dlopen_main_DEPENDENCIES) 
1579 | 	@rm -f dlopen_main$(EXEEXT)
1580 | 	$(AM_V_CCLD)$(LINK) $(dlopen_main_OBJECTS) $(dlopen_main_LDADD) $(LIBS)
1806 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen_lib_so-dlopen_lib.Po@am__quote@
1807 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen_main.Po@am__quote@
1875 | dlopen_lib_so-dlopen_lib.o: dlopen_lib.c
1876 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -MT dlopen_lib_so-dlopen_lib.o -MD -MP -MF $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo -c -o dlopen_lib_so-dlopen_lib.o `test -f 'dlopen_lib.c' || echo '$(srcdir)/'`dlopen_lib.c
1877 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo $(DEPDIR)/dlopen_lib_so-dlopen_lib.Po
1878 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen_lib.c' object='dlopen_lib_so-dlopen_lib.o' libtool=no @AMDEPBACKSLASH@
1880 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -c -o dlopen_lib_so-dlopen_lib.o `test -f 'dlopen_lib.c' || echo '$(srcdir)/'`dlopen_lib.c
1882 | dlopen_lib_so-dlopen_lib.obj: dlopen_lib.c
1883 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -MT dlopen_lib_so-dlopen_lib.obj -MD -MP -MF $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo -c -o dlopen_lib_so-dlopen_lib.obj `if test -f 'dlopen_lib.c'; then $(CYGPATH_W) 'dlopen_lib.c'; else $(CYGPATH_W) '$(srcdir)/dlopen_lib.c'; fi`
1884 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo $(DEPDIR)/dlopen_lib_so-dlopen_lib.Po
1885 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen_lib.c' object='dlopen_lib_so-dlopen_lib.obj' libtool=no @AMDEPBACKSLASH@
1887 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -c -o dlopen_lib_so-dlopen_lib.obj `if test -f 'dlopen_lib.c'; then $(CYGPATH_W) 'dlopen_lib.c'; else $(CYGPATH_W) '$(srcdir)/dlopen_lib.c'; fi`
{% endraw %}

```
### docs/index.ps

```

{% raw %}
527817 | (dlopen')
528111 | (dlopened)
528419 | (dlopens)
529651 | (dlopen')
{% endraw %}

```
### docs/xml/manual-core-adv.xml

```

{% raw %}
1758 | appear and disappear (are dlopen'd and dlclose'd) on the fly.
1761 | <para>For example, suppose a process has dlopened (an ELF object with
1766 | <para>After a while it dlopens <filename>wrappers.so</filename>,
1783 | eventually dlopen'd again, the wrapper will become active again.</para>
{% endraw %}

```
### docs/internals/3_12_BUGSTATUS.txt

```

{% raw %}
195 | 358980  32 byte leak reported when code uses dlopen and links against pthread
199 | 361504  dlopen()/dlclose() and shared object usage check
474 | 358980  32 byte leak reported when code uses dlopen and links against pthread
{% endraw %}

```
### docs/internals/3_13_BUGSTATUS.txt

```

{% raw %}
395 | 358980  32 byte leak reported when code uses dlopen and links against pthread
399 | 361504  dlopen()/dlclose() and shared object usage check
864 | 358980  32 byte leak reported when code uses dlopen and links against pthread
{% endraw %}

```
### docs/internals/segments-seginfos.txt

```

{% raw %}
109 | (well, dlopen() does try for mutual exclusion) and that any "holes" between
{% endraw %}

```
### docs/internals/3_11_BUGSTATUS.txt

```

{% raw %}
108 | 358980  32 byte leak reported when code uses dlopen and links against pthread
109 | 361504  dlopen()/dlclose() and shared object usage check [wishlist]
{% endraw %}

```
### none/tests/solaris/mmap_noreserve.c

```cpp

{% raw %}
26 | static void *do_dlopen(const char *pathname)
29 |    void *handle = dlopen(pathname, mode);
31 |       fprintf(stderr, "dlopen failed for %s: %s",
42 |    do_dlopen("libm.so");
46 |    do_dlopen("liby.so");
52 |    do_dlopen("libz.so");
67 |       do_dlopen("libw.so");
{% endraw %}

```