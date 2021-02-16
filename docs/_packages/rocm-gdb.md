---
name: "rocm-gdb"
layout: package
next_package: osi
previous_package: scorep
languages: ['cpp', 'c']
---
## 3.8.0
115 / 33677 files match, 47 filtered matches.

 - [sim/bfin/gui.c](#simbfinguic)
 - [include/aout/sun4.h](#includeaoutsun4h)
 - [bfd/elf32-frv.c](#bfdelf32-frvc)
 - [bfd/elf64-ppc.c](#bfdelf64-ppcc)
 - [bfd/plugin.c](#bfdpluginc)
 - [intl/libgnuintl.h](#intllibgnuintlh)
 - [gold/layout.cc](#goldlayoutcc)
 - [gold/options.h](#goldoptionsh)
 - [gold/plugin.cc](#goldplugincc)
 - [gold/testsuite/ifuncmain3.c](#goldtestsuiteifuncmain3c)
 - [gdb/breakpoint.c](#gdbbreakpointc)
 - [gdb/linux-thread-db.c](#gdblinux-thread-dbc)
 - [gdb/jit.c](#gdbjitc)
 - [gdb/ppc64-tdep.c](#gdbppc64-tdepc)
 - [gdb/sol-thread.c](#gdbsol-threadc)
 - [gdb/ia64-libunwind-tdep.c](#gdbia64-libunwind-tdepc)
 - [gdb/compile/compile-c-support.c](#gdbcompilecompile-c-supportc)
 - [gdb/gdbserver/thread-db.c](#gdbgdbserverthread-dbc)
 - [gdb/testsuite/gdb.cp/infcall-dlopen.cc](#gdbtestsuitegdbcpinfcall-dlopencc)
 - [gdb/testsuite/gdb.base/info-shared.c](#gdbtestsuitegdbbaseinfo-sharedc)
 - [gdb/testsuite/gdb.base/catch-load.c](#gdbtestsuitegdbbasecatch-loadc)
 - [gdb/testsuite/gdb.base/solib-disc.c](#gdbtestsuitegdbbasesolib-discc)
 - [gdb/testsuite/gdb.base/print-file-var-main.c](#gdbtestsuitegdbbaseprint-file-var-mainc)
 - [gdb/testsuite/gdb.base/watchpoint-solib.c](#gdbtestsuitegdbbasewatchpoint-solibc)
 - [gdb/testsuite/gdb.base/solib-vanish-main.c](#gdbtestsuitegdbbasesolib-vanish-mainc)
 - [gdb/testsuite/gdb.base/jit-dlmain.c](#gdbtestsuitegdbbasejit-dlmainc)
 - [gdb/testsuite/gdb.base/break-probes.c](#gdbtestsuitegdbbasebreak-probesc)
 - [gdb/testsuite/gdb.base/unload.c](#gdbtestsuitegdbbaseunloadc)
 - [gdb/testsuite/gdb.base/corefile-buildid-shlib.c](#gdbtestsuitegdbbasecorefile-buildid-shlibc)
 - [gdb/testsuite/gdb.threads/dlopen-libpthread.c](#gdbtestsuitegdbthreadsdlopen-libpthreadc)
 - [gdb/testsuite/gdb.perf/solib.c](#gdbtestsuitegdbperfsolibc)
 - [gdb/testsuite/gdb.btrace/dlopen.c](#gdbtestsuitegdbbtracedlopenc)
 - [gdb/testsuite/gdb.trace/change-loc.c](#gdbtestsuitegdbtracechange-locc)
 - [gdb/testsuite/gdb.trace/pending.c](#gdbtestsuitegdbtracependingc)
 - [gdb/testsuite/gdb.mi/mi-pending.c](#gdbtestsuitegdbmimi-pendingc)
 - [gdb/testsuite/gdb.mi/mi-catch-load.c](#gdbtestsuitegdbmimi-catch-loadc)
 - [gdb/testsuite/gdb.mi/pending.c](#gdbtestsuitegdbmipendingc)
 - [gdb/gdbsupport/gdb-dlfcn.h](#gdbgdbsupportgdb-dlfcnh)
 - [gdb/gdbsupport/gdb-dlfcn.c](#gdbgdbsupportgdb-dlfcnc)
 - [ld/lexsup.c](#ldlexsupc)
 - [ld/plugin.c](#ldpluginc)
 - [ld/testsuite/ld-elf/dl1main.c](#ldtestsuiteld-elfdl1mainc)
 - [ld/testsuite/ld-elf/dl6dmain.c](#ldtestsuiteld-elfdl6dmainc)
 - [ld/testsuite/ld-elf/dl6bmain.c](#ldtestsuiteld-elfdl6bmainc)
 - [ld/testsuite/ld-elf/dl6amain.c](#ldtestsuiteld-elfdl6amainc)
 - [ld/testsuite/ld-elf/dl6cmain.c](#ldtestsuiteld-elfdl6cmainc)
 - [ld/testsuite/ld-elf/pr21964-2c.c](#ldtestsuiteld-elfpr21964-2cc)

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
4469 |      suitable for dlopening.  This mark will remain even if we relax
4472 |      dlopening executables.  */
5646 |      that can't be dlopened.  */
{% endraw %}

```
### bfd/elf64-ppc.c

```c

{% raw %}
7588 |      An app that "cleverly" uses dlopen to only load necessary
{% endraw %}

```
### bfd/plugin.c

```c

{% raw %}
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
243 |   plugin_handle = dlopen (pname, RTLD_NOW);
{% endraw %}

```
### intl/libgnuintl.h

```c

{% raw %}
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
{% endraw %}

```
### gold/layout.cc

```cpp

{% raw %}
5339 |   if (parameters->options().nodlopen())
{% endraw %}

```
### gold/options.h

```c

{% raw %}
1483 |   DEFINE_bool(nodlopen, options::DASH_Z, '\0', false,
1484 | 	      N_("Mark DSO not available to dlopen"),
{% endraw %}

```
### gold/plugin.cc

```cpp

{% raw %}
47 | dlopen(const char *file, int mode ATTRIBUTE_UNUSED)
198 |   this->handle_ = dlopen(this->filename_.c_str(), RTLD_NOW);
{% endraw %}

```
### gold/testsuite/ifuncmain3.c

```c

{% raw %}
45 |   void *h = dlopen ("ifuncmod3.so", RTLD_LAZY);
{% endraw %}

```
### gdb/breakpoint.c

```c

{% raw %}
12631 |      over a dlopen call and solib_add is resetting the breakpoints.
{% endraw %}

```
### gdb/linux-thread-db.c

```c

{% raw %}
222 |    THREAD_DB_LIST.  HANDLE is the handle returned by dlopen'ing
264 |    LIBTHREAD_DB_SO's dlopen'ed handle.  */
982 |   handle = dlopen (library, RTLD_NOW);
986 | 	fprintf_unfiltered (gdb_stdlog, _("dlopen failed: %s.\n"), dlerror ());
1081 |    dlopen(file_without_path) will look.
{% endraw %}

```
### gdb/jit.c

```c

{% raw %}
188 |   gdb_dlhandle_up so = gdb_dlopen (file_name);
{% endraw %}

```
### gdb/ppc64-tdep.c

```c

{% raw %}
572 | 	 dlopen, but ld.so has not yet applied the relocations.
{% endraw %}

```
### gdb/sol-thread.c

```c

{% raw %}
1153 |   dlhandle = dlopen ("libthread_db.so.1", RTLD_NOW);
{% endraw %}

```
### gdb/ia64-libunwind-tdep.c

```c

{% raw %}
512 |   handle = dlopen (LIBUNWIND_SO, RTLD_NOW);
517 |       handle = dlopen (LIBUNWIND_SO_7, RTLD_NOW);
{% endraw %}

```
### gdb/compile/compile-c-support.c

```c

{% raw %}
82 |   gdb_dlhandle_up handle = gdb_dlopen (fe_libcc);
{% endraw %}

```
### gdb/gdbserver/thread-db.c

```c

{% raw %}
608 |   handle = dlopen (library, RTLD_NOW);
612 | 	debug_printf ("dlopen failed: %s.\n", dlerror ());
642 |    dlopen(file_without_path) will look.
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
### gdb/testsuite/gdb.base/print-file-var-main.c

```c

{% raw %}
47 |     void *handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/watchpoint-solib.c

```c

{% raw %}
39 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-vanish-main.c

```c

{% raw %}
32 |   handle = dlopen (VANISH_LIB, RTLD_NOW);
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
### gdb/testsuite/gdb.base/corefile-buildid-shlib.c

```c

{% raw %}
40 |   handle = dlopen (the_shlib, RTLD_LAZY);
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
### gdb/testsuite/gdb.btrace/dlopen.c

```c

{% raw %}
28 |   dso = dlopen (DSO_NAME, RTLD_NOW | RTLD_GLOBAL);
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
### gdb/gdbsupport/gdb-dlfcn.h

```c

{% raw %}
37 | gdb_dlhandle_up gdb_dlopen (const char *filename);
{% endraw %}

```
### gdb/gdbsupport/gdb-dlfcn.c

```c

{% raw %}
34 | gdb_dlopen (const char *filename)
36 |   gdb_assert_not_reached ("gdb_dlopen should not be called on this platform.");
60 | gdb_dlopen (const char *filename)
64 |   result = dlopen (filename, RTLD_NOW);
{% endraw %}

```
### ld/lexsup.c

```c

{% raw %}
1808 |   -z nodlopen                 Mark DSO not available to dlopen\n"));
{% endraw %}

```
### ld/plugin.c

```c

{% raw %}
184 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
244 |   newplug->dlhandle = dlopen (plugin, RTLD_NOW);
{% endraw %}

```
### ld/testsuite/ld-elf/dl1main.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl1.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl1.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6dmain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6d.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6d.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6bmain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6b.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6b.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6amain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6a.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6a.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl6cmain.c

```c

{% raw %}
12 |   handle = dlopen("./tmpdir/libdl6c.so", RTLD_GLOBAL|RTLD_LAZY);
15 |       printf("dlopen ./tmpdir/libdl6c.so: %s\n", dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-2c.c

```c

{% raw %}
14 |   dl = dlopen("pr21964-2b.so", RTLD_LAZY);
{% endraw %}

```