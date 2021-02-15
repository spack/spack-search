---
name: "verrou"
layout: package
next_package: xcb-util-cursor
previous_package: py-chainer
languages: ['cpp']
---
## 2.0.0
21 / 5652 files match

 - [valgrind-3.13.0/glibc-2.2.supp](#valgrind-3130glibc-22supp)
 - [valgrind-3.13.0/glibc-2.3.supp](#valgrind-3130glibc-23supp)
 - [valgrind-3.13.0/darwin12.supp](#valgrind-3130darwin12supp)
 - [valgrind-3.13.0/mpi/libmpiwrap.c](#valgrind-3130mpilibmpiwrapc)
 - [valgrind-3.13.0/perf/tinycc.c](#valgrind-3130perftinyccc)
 - [valgrind-3.13.0/cachegrind/tests/dlclose.c](#valgrind-3130cachegrindtestsdlclosec)
 - [valgrind-3.13.0/callgrind/global.h](#valgrind-3130callgrindglobalh)
 - [valgrind-3.13.0/exp-sgcheck/tests/preen_invars_so.c](#valgrind-3130exp-sgchecktestspreen_invars_soc)
 - [valgrind-3.13.0/exp-sgcheck/tests/preen_invars.c](#valgrind-3130exp-sgchecktestspreen_invarsc)
 - [valgrind-3.13.0/drd/drd_pthread_intercepts.c](#valgrind-3130drddrd_pthread_interceptsc)
 - [valgrind-3.13.0/drd/tests/dlopen_lib.c](#valgrind-3130drdtestsdlopen_libc)
 - [valgrind-3.13.0/drd/tests/dlopen.vgtest](#valgrind-3130drdtestsdlopenvgtest)
 - [valgrind-3.13.0/drd/tests/Makefile.am](#valgrind-3130drdtestsmakefileam)
 - [valgrind-3.13.0/drd/tests/dlopen_main.c](#valgrind-3130drdtestsdlopen_mainc)
 - [valgrind-3.13.0/drd/tests/Makefile.in](#valgrind-3130drdtestsmakefilein)
 - [valgrind-3.13.0/docs/index.ps](#valgrind-3130docsindexps)
 - [valgrind-3.13.0/docs/xml/manual-core-adv.xml](#valgrind-3130docsxmlmanual-core-advxml)
 - [valgrind-3.13.0/docs/internals/3_12_BUGSTATUS.txt](#valgrind-3130docsinternals3_12_bugstatustxt)
 - [valgrind-3.13.0/docs/internals/segments-seginfos.txt](#valgrind-3130docsinternalssegments-seginfostxt)
 - [valgrind-3.13.0/docs/internals/3_11_BUGSTATUS.txt](#valgrind-3130docsinternals3_11_bugstatustxt)
 - [valgrind-3.13.0/none/tests/solaris/mmap_noreserve.c](#valgrind-3130nonetestssolarismmap_noreservec)

### valgrind-3.13.0/glibc-2.2.supp

```

{% raw %}
33 |    strlen/__GI__dl_open/dlopen_doit
37 |    fun:dlopen_doit
{% endraw %}

```
### valgrind-3.13.0/glibc-2.3.supp

```

{% raw %}
32 |    strlen/__GI__dl_open/dlopen_doit
36 |    fun:dlopen_doit
{% endraw %}

```
### valgrind-3.13.0/darwin12.supp

```

{% raw %}
311 |    fun:dlopen
319 |    fun:dlopen
{% endraw %}

```
### valgrind-3.13.0/mpi/libmpiwrap.c

```cpp

{% raw %}
929 | /* Hook so it's visible from outside (can be handy to dlopen/dlsym
{% endraw %}

```
### valgrind-3.13.0/perf/tinycc.c

```cpp

{% raw %}
1360 | 					   by rld on dlopen() calls.  */
6584 | void *dlopen(const char *filename, int flag)
21009 |                     //h = dlopen(filename, RTLD_GLOBAL | RTLD_LAZY);
21010 | 		    // jrs: remove need for dlopen
{% endraw %}

```
### valgrind-3.13.0/cachegrind/tests/dlclose.c

```cpp

{% raw %}
18 |    handle = dlopen ("./myprint.so", RTLD_LAZY);
{% endraw %}

```
### valgrind-3.13.0/callgrind/global.h

```cpp

{% raw %}
431 | /* If an object is dlopened multiple times, we hope that <name> is unique;
432 |  * <start> and <offset> can change with each dlopen, and <start> is
{% endraw %}

```
### valgrind-3.13.0/exp-sgcheck/tests/preen_invars_so.c

```cpp

{% raw %}
2 |    which is dlopened by preen_invar.c.  That then accesses the global
{% endraw %}

```
### valgrind-3.13.0/exp-sgcheck/tests/preen_invars.c

```cpp

{% raw %}
12 |   void* hdl = dlopen("./preen_invars_so.so", RTLD_NOW);
{% endraw %}

```
### valgrind-3.13.0/drd/drd_pthread_intercepts.c

```cpp

{% raw %}
241 |  * dlopen() has loaded the shared library with DRD client intercepts because
{% endraw %}

```
### valgrind-3.13.0/drd/tests/dlopen_lib.c

```cpp

{% raw %}
3 | #include "dlopen_lib.h"
{% endraw %}

```
### valgrind-3.13.0/drd/tests/dlopen.vgtest

```

{% raw %}
0 | prereq: test -e dlopen_main && ./supported_libpthread
2 | prog: dlopen_main ./dlopen_lib.so
{% endraw %}

```
### valgrind-3.13.0/drd/tests/Makefile.am

```

{% raw %}
22 | 	dlopen_lib.h
106 | 	dlopen.stderr.exp			    \
107 | 	dlopen.stdout.exp			    \
108 | 	dlopen.vgtest				    \
367 |   dlopen_main         \
368 |   dlopen_lib.so       \
463 | dlopen_main_LDADD           = -ldl
464 | dlopen_lib_so_SOURCES       = dlopen_lib.c
465 | dlopen_lib_so_CFLAGS        = -fPIC
466 | dlopen_lib_so_LDFLAGS       = -shared -fPIC
{% endraw %}

```
### valgrind-3.13.0/drd/tests/dlopen_main.c

```cpp

{% raw %}
3 | #include "dlopen_lib.h"
12 |   handle = dlopen(lib, RTLD_NOW);
{% endraw %}

```
### valgrind-3.13.0/drd/tests/Makefile.in

```

{% raw %}
128 | 	dlopen_main$(EXEEXT) dlopen_lib.so$(EXEEXT) fp_race$(EXEEXT) \
297 | am_dlopen_lib_so_OBJECTS = dlopen_lib_so-dlopen_lib.$(OBJEXT)
298 | dlopen_lib_so_OBJECTS = $(am_dlopen_lib_so_OBJECTS)
299 | dlopen_lib_so_LDADD = $(LDADD)
300 | dlopen_lib_so_DEPENDENCIES =
301 | dlopen_lib_so_LINK = $(CCLD) $(dlopen_lib_so_CFLAGS) $(CFLAGS) \
302 | 	$(dlopen_lib_so_LDFLAGS) $(LDFLAGS) -o $@
303 | dlopen_main_SOURCES = dlopen_main.c
304 | dlopen_main_OBJECTS = dlopen_main.$(OBJEXT)
305 | dlopen_main_DEPENDENCIES =
591 | 	custom_alloc.c $(dlopen_lib_so_SOURCES) dlopen_main.c \
616 | 	$(dlopen_lib_so_SOURCES) dlopen_main.c fp_race.c \
1050 | 	dlopen_lib.h
1134 | 	dlopen.stderr.exp			    \
1135 | 	dlopen.stdout.exp			    \
1136 | 	dlopen.vgtest				    \
1385 | dlopen_main_LDADD = -ldl
1386 | dlopen_lib_so_SOURCES = dlopen_lib.c
1387 | dlopen_lib_so_CFLAGS = -fPIC
1388 | dlopen_lib_so_LDFLAGS = -shared -fPIC
1549 | dlopen_lib.so$(EXEEXT): $(dlopen_lib_so_OBJECTS) $(dlopen_lib_so_DEPENDENCIES) $(EXTRA_dlopen_lib_so_DEPENDENCIES) 
1550 | 	@rm -f dlopen_lib.so$(EXEEXT)
1551 | 	$(AM_V_CCLD)$(dlopen_lib_so_LINK) $(dlopen_lib_so_OBJECTS) $(dlopen_lib_so_LDADD) $(LIBS)
1553 | dlopen_main$(EXEEXT): $(dlopen_main_OBJECTS) $(dlopen_main_DEPENDENCIES) $(EXTRA_dlopen_main_DEPENDENCIES) 
1554 | 	@rm -f dlopen_main$(EXEEXT)
1555 | 	$(AM_V_CCLD)$(LINK) $(dlopen_main_OBJECTS) $(dlopen_main_LDADD) $(LIBS)
1780 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen_lib_so-dlopen_lib.Po@am__quote@
1781 | @AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/dlopen_main.Po@am__quote@
1849 | dlopen_lib_so-dlopen_lib.o: dlopen_lib.c
1850 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -MT dlopen_lib_so-dlopen_lib.o -MD -MP -MF $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo -c -o dlopen_lib_so-dlopen_lib.o `test -f 'dlopen_lib.c' || echo '$(srcdir)/'`dlopen_lib.c
1851 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo $(DEPDIR)/dlopen_lib_so-dlopen_lib.Po
1852 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen_lib.c' object='dlopen_lib_so-dlopen_lib.o' libtool=no @AMDEPBACKSLASH@
1854 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -c -o dlopen_lib_so-dlopen_lib.o `test -f 'dlopen_lib.c' || echo '$(srcdir)/'`dlopen_lib.c
1856 | dlopen_lib_so-dlopen_lib.obj: dlopen_lib.c
1857 | @am__fastdepCC_TRUE@	$(AM_V_CC)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -MT dlopen_lib_so-dlopen_lib.obj -MD -MP -MF $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo -c -o dlopen_lib_so-dlopen_lib.obj `if test -f 'dlopen_lib.c'; then $(CYGPATH_W) 'dlopen_lib.c'; else $(CYGPATH_W) '$(srcdir)/dlopen_lib.c'; fi`
1858 | @am__fastdepCC_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/dlopen_lib_so-dlopen_lib.Tpo $(DEPDIR)/dlopen_lib_so-dlopen_lib.Po
1859 | @AMDEP_TRUE@@am__fastdepCC_FALSE@	$(AM_V_CC)source='dlopen_lib.c' object='dlopen_lib_so-dlopen_lib.obj' libtool=no @AMDEPBACKSLASH@
1861 | @am__fastdepCC_FALSE@	$(AM_V_CC@am__nodep@)$(CC) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(dlopen_lib_so_CFLAGS) $(CFLAGS) -c -o dlopen_lib_so-dlopen_lib.obj `if test -f 'dlopen_lib.c'; then $(CYGPATH_W) 'dlopen_lib.c'; else $(CYGPATH_W) '$(srcdir)/dlopen_lib.c'; fi`
{% endraw %}

```
### valgrind-3.13.0/docs/index.ps

```

{% raw %}
520042 | (dlopen')
520336 | (dlopened)
520644 | (dlopens)
521876 | (dlopen')
{% endraw %}

```
### valgrind-3.13.0/docs/xml/manual-core-adv.xml

```

{% raw %}
1758 | appear and disappear (are dlopen'd and dlclose'd) on the fly.
1761 | <para>For example, suppose a process has dlopened (an ELF object with
1766 | <para>After a while it dlopens <filename>wrappers.so</filename>,
1783 | eventually dlopen'd again, the wrapper will become active again.</para>
{% endraw %}

```
### valgrind-3.13.0/docs/internals/3_12_BUGSTATUS.txt

```

{% raw %}
195 | 358980  32 byte leak reported when code uses dlopen and links against pthread
199 | 361504  dlopen()/dlclose() and shared object usage check
474 | 358980  32 byte leak reported when code uses dlopen and links against pthread
{% endraw %}

```
### valgrind-3.13.0/docs/internals/segments-seginfos.txt

```

{% raw %}
109 | (well, dlopen() does try for mutual exclusion) and that any "holes" between
{% endraw %}

```
### valgrind-3.13.0/docs/internals/3_11_BUGSTATUS.txt

```

{% raw %}
108 | 358980  32 byte leak reported when code uses dlopen and links against pthread
109 | 361504  dlopen()/dlclose() and shared object usage check [wishlist]
{% endraw %}

```
### valgrind-3.13.0/none/tests/solaris/mmap_noreserve.c

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