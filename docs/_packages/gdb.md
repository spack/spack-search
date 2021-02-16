---
name: "gdb"
layout: package
next_package: dcmtk
previous_package: photos
languages: ['cpp', 'c']
---
## 7.10.1
63 / 10755 files match

 - [sim/bfin/gui.c](#simbfinguic)
 - [include/aout/sun4.h](#includeaoutsun4h)
 - [bfd/elf32-frv.c](#bfdelf32-frvc)
 - [bfd/plugin.c](#bfdpluginc)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [gdb/breakpoint.c](#gdbbreakpointc)
 - [gdb/gdb-dlfcn.h](#gdbgdb-dlfcnh)
 - [gdb/linux-thread-db.c](#gdblinux-thread-dbc)
 - [gdb/jit.c](#gdbjitc)
 - [gdb/ppc64-tdep.c](#gdbppc64-tdepc)
 - [gdb/sol-thread.c](#gdbsol-threadc)
 - [gdb/gdb-dlfcn.c](#gdbgdb-dlfcnc)
 - [gdb/ia64-libunwind-tdep.c](#gdbia64-libunwind-tdepc)
 - [gdb/compile/compile-c-support.c](#gdbcompilecompile-c-supportc)
 - [gdb/gdbserver/thread-db.c](#gdbgdbserverthread-dbc)
 - [gdb/testsuite/gdb.cp/infcall-dlopen.cc](#gdbtestsuitegdbcpinfcall-dlopencc)
 - [gdb/testsuite/gdb.base/info-shared.c](#gdbtestsuitegdbbaseinfo-sharedc)
 - [gdb/testsuite/gdb.base/catch-load.c](#gdbtestsuitegdbbasecatch-loadc)
 - [gdb/testsuite/gdb.base/solib-disc.c](#gdbtestsuitegdbbasesolib-discc)
 - [gdb/testsuite/gdb.base/watchpoint-solib.c](#gdbtestsuitegdbbasewatchpoint-solibc)
 - [gdb/testsuite/gdb.base/jit-dlmain.c](#gdbtestsuitegdbbasejit-dlmainc)
 - [gdb/testsuite/gdb.base/break-probes.c](#gdbtestsuitegdbbasebreak-probesc)
 - [gdb/testsuite/gdb.base/unload.c](#gdbtestsuitegdbbaseunloadc)
 - [gdb/testsuite/gdb.threads/dlopen-libpthread.c](#gdbtestsuitegdbthreadsdlopen-libpthreadc)
 - [gdb/testsuite/gdb.perf/solib.c](#gdbtestsuitegdbperfsolibc)
 - [gdb/testsuite/gdb.trace/change-loc.c](#gdbtestsuitegdbtracechange-locc)
 - [gdb/testsuite/gdb.trace/pending.c](#gdbtestsuitegdbtracependingc)
 - [gdb/testsuite/gdb.mi/mi-pending.c](#gdbtestsuitegdbmimi-pendingc)
 - [gdb/testsuite/gdb.mi/mi-catch-load.c](#gdbtestsuitegdbmimi-catch-loadc)
 - [gdb/testsuite/gdb.mi/pending.c](#gdbtestsuitegdbmipendingc)

### sim/bfin/gui.c

```c

{% raw %}
80 |   sdl.handle = dlopen ("libSDL-1.2.so.0", RTLD_LAZY);
{% endraw %}

```
### include/aout/sun4.h

```c

{% raw %}
90 |      ld.so and probably by dlopen.  */
{% endraw %}

```
### bfd/elf32-frv.c

```c

{% raw %}
4478 |      suitable for dlopening.  This mark will remain even if we relax
4481 |      dlopening executables.  */
5654 |      that can't be dlopened.  */
{% endraw %}

```
### bfd/plugin.c

```c

{% raw %}
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
216 |   plugin_handle = dlopen (pname, RTLD_NOW);
{% endraw %}

```
### intl/libgnuintl.h

```c

{% raw %}
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
{% endraw %}

```
### gdb/breakpoint.c

```c

{% raw %}
13088 |      over a dlopen call and solib_add is resetting the breakpoints.
{% endraw %}

```
### gdb/gdb-dlfcn.h

```c

{% raw %}
26 | void *gdb_dlopen (const char *filename);
{% endraw %}

```
### gdb/linux-thread-db.c

```c

{% raw %}
225 |    THREAD_DB_LIST.  HANDLE is the handle returned by dlopen'ing
266 |    LIBTHREAD_DB_SO's dlopen'ed handle.  */
840 |   handle = dlopen (library, RTLD_NOW);
844 | 	fprintf_unfiltered (gdb_stdlog, _("dlopen failed: %s.\n"), dlerror ());
953 |    dlopen(file_without_path) will look.
{% endraw %}

```
### gdb/jit.c

```c

{% raw %}
176 |   so = gdb_dlopen (file_name);
{% endraw %}

```
### gdb/ppc64-tdep.c

```c

{% raw %}
573 | 	 dlopen, but ld.so has not yet applied the relocations.
{% endraw %}

```
### gdb/sol-thread.c

```c

{% raw %}
1246 |   dlhandle = dlopen ("libthread_db.so.1", RTLD_NOW);
{% endraw %}

```
### gdb/gdb-dlfcn.c

```c

{% raw %}
34 | gdb_dlopen (const char *filename)
36 |   gdb_assert_not_reached ("gdb_dlopen should not be called on this platform.");
67 | gdb_dlopen (const char *filename)
71 |   result = dlopen (filename, RTLD_NOW);
{% endraw %}

```
### gdb/ia64-libunwind-tdep.c

```c

{% raw %}
496 |   handle = dlopen (LIBUNWIND_SO, RTLD_NOW);
501 |       handle = dlopen (LIBUNWIND_SO_7, RTLD_NOW);
{% endraw %}

```
### gdb/compile/compile-c-support.c

```c

{% raw %}
81 |   handle = gdb_dlopen (STRINGIFY (GCC_C_FE_LIBCC));
{% endraw %}

```
### gdb/gdbserver/thread-db.c

```c

{% raw %}
707 |   handle = dlopen (library, RTLD_NOW);
711 | 	debug_printf ("dlopen failed: %s.\n", dlerror ());
742 |    dlopen(file_without_path) will look.
{% endraw %}

```
### gdb/testsuite/gdb.cp/infcall-dlopen.cc

```cpp

{% raw %}
23 |   void *h = dlopen (filename, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/info-shared.c

```c

{% raw %}
30 |   handle1 = dlopen (SHLIB1_NAME, RTLD_LAZY);
34 |   handle2 = dlopen (SHLIB2_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/catch-load.c

```c

{% raw %}
35 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-disc.c

```c

{% raw %}
35 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/watchpoint-solib.c

```c

{% raw %}
39 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/jit-dlmain.c

```c

{% raw %}
10 |   h = NULL;  /* break here before-dlopen  */
11 |   h = dlopen (jit_libname, RTLD_LAZY);
17 |   h = h;  /* break here after-dlopen */
{% endraw %}

```
### gdb/testsuite/gdb.base/break-probes.c

```c

{% raw %}
22 |   void *handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/unload.c

```c

{% raw %}
42 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
69 |   handle = dlopen (SHLIB_NAME2, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.threads/dlopen-libpthread.c

```c

{% raw %}
36 |   h = dlopen (filename, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.perf/solib.c

```c

{% raw %}
47 |       handles[i] = dlopen (libname, RTLD_LAZY);
50 | 	  printf ("ERROR on dlopen %s\n", libname);
{% endraw %}

```
### gdb/testsuite/gdb.trace/change-loc.c

```c

{% raw %}
38 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.trace/pending.c

```c

{% raw %}
37 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-pending.c

```c

{% raw %}
31 |   h = dlopen (libname, RTLD_LAZY);  /* set breakpoint here */
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-catch-load.c

```c

{% raw %}
34 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.mi/pending.c

```c

{% raw %}
38 |   h = dlopen (libname, RTLD_LAZY);
{% endraw %}

```