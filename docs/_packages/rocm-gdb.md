---
name: "rocm-gdb"
layout: package
next_package: rocm-opencl
previous_package: rocksdb
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
77 |   if (sdl.handle)
78 |     return 0;
79 | 
80 |   sdl.handle = dlopen ("libSDL-1.2.so.0", RTLD_LAZY);
81 |   if (sdl.handle == NULL)
82 |     return -1;
{% endraw %}

```
### include/aout/sun4.h

```c

{% raw %}
87 | struct internal_sun4_dynamic_link
88 | {
89 |   /* Linked list of loaded objects.  This is filled in at runtime by
90 |      ld.so and probably by dlopen.  */
91 |   unsigned long ld_loaded;
92 | 
{% endraw %}

```
### bfd/elf32-frv.c

```c

{% raw %}
4466 |   entry->relocstlsoff += l;
4467 | 
4468 |   /* If there's any TLSOFF relocation, mark the output file as not
4469 |      suitable for dlopening.  This mark will remain even if we relax
4470 |      all such relocations, but this is not a problem, since we'll only
4471 |      do so for executables, and we definitely don't want anyone
4472 |      dlopening executables.  */
4473 |   if (entry->relocstlsoff)
4474 |     dinfo->info->flags |= DF_STATIC_TLS;
5643 |     return TRUE;
5644 | 
5645 |   /* We can only relax when linking the main executable or a library
5646 |      that can't be dlopened.  */
5647 |   if (! bfd_link_executable (info) && ! (info->flags & DF_STATIC_TLS))
5648 |     return TRUE;
{% endraw %}

```
### bfd/elf64-ppc.c

```c

{% raw %}
7585 |      work than the pthread implementation.  __pthread_condattr_destroy
7586 |      is one such symbol: the libpthread.so implementation is
7587 |      localentry:0 while the libc.so implementation is localentry:8.
7588 |      An app that "cleverly" uses dlopen to only load necessary
7589 |      libraries at runtime may omit loading libpthread.so when not
7590 |      running multi-threaded, which then results in the libc.so
{% endraw %}

```
### bfd/plugin.c

```c

{% raw %}
42 | #define RTLD_NOW 0      /* Dummy value.  */
43 | 
44 | static void *
45 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
46 | {
47 |   return LoadLibrary (file);
240 | 
241 |   *has_plugin_p = 0;
242 | 
243 |   plugin_handle = dlopen (pname, RTLD_NOW);
244 |   if (!plugin_handle)
245 |     {
{% endraw %}

```
### intl/libgnuintl.h

```c

{% raw %}
72 |      2. in the shared libraries specified on the link command line, in order,
73 |      3. in the dependencies of the shared libraries specified on the link
74 |         command line,
75 |      4. in the dlopen()ed shared libraries, in the order in which they were
76 |         dlopen()ed.
77 |    The definition in the C library would override the one in libintl.so if
78 |    either
{% endraw %}

```
### gold/layout.cc

```cpp

{% raw %}
5336 |     flags |= elfcpp::DF_1_NODEFLIB;
5337 |   if (parameters->options().nodelete())
5338 |     flags |= elfcpp::DF_1_NODELETE;
5339 |   if (parameters->options().nodlopen())
5340 |     flags |= elfcpp::DF_1_NOOPEN;
5341 |   if (parameters->options().nodump())
{% endraw %}

```
### gold/options.h

```c

{% raw %}
1480 |   DEFINE_bool(nodelete, options::DASH_Z, '\0', false,
1481 | 	      N_("Mark DSO non-deletable at runtime"),
1482 | 	      NULL);
1483 |   DEFINE_bool(nodlopen, options::DASH_Z, '\0', false,
1484 | 	      N_("Mark DSO not available to dlopen"),
1485 | 	      NULL);
1486 |   DEFINE_bool(nodump, options::DASH_Z, '\0', false,
{% endraw %}

```
### gold/plugin.cc

```cpp

{% raw %}
44 | 
45 | #define RTLD_NOW 0      /* Dummy value.  */
46 | static void *
47 | dlopen(const char *file, int mode ATTRIBUTE_UNUSED)
48 | {
49 |   return LoadLibrary(file);
195 | #ifdef ENABLE_PLUGINS
196 |   // Load the plugin library.
197 |   // FIXME: Look for the library in standard locations.
198 |   this->handle_ = dlopen(this->filename_.c_str(), RTLD_NOW);
199 |   if (this->handle_ == NULL)
200 |     {
{% endraw %}

```
### gold/testsuite/ifuncmain3.c

```c

{% raw %}
42 |   foo_p (*f) (void);
43 |   int *ret;
44 | 
45 |   void *h = dlopen ("ifuncmod3.so", RTLD_LAZY);
46 |   if (h == NULL)
47 |     {
{% endraw %}

```
### gdb/breakpoint.c

```c

{% raw %}
12628 | momentary_bkpt_re_set (struct breakpoint *b)
12629 | {
12630 |   /* Keep temporary breakpoints, which can be encountered when we step
12631 |      over a dlopen call and solib_add is resetting the breakpoints.
12632 |      Otherwise these should have been blown away via the cleanup chain
12633 |      or by breakpoint_init_inferior when we rerun the executable.  */
{% endraw %}

```
### gdb/linux-thread-db.c

```c

{% raw %}
219 | 
220 | /* Add the current inferior to the list of processes using libpthread.
221 |    Return a pointer to the newly allocated object that was added to
222 |    THREAD_DB_LIST.  HANDLE is the handle returned by dlopen'ing
223 |    LIBTHREAD_DB_SO.  */
224 | 
261 | /* When PID has exited or has been detached, we no longer want to keep
262 |    track of it as using libpthread.  Call this function to discard
263 |    thread_db related info related to PID.  Note that this closes
264 |    LIBTHREAD_DB_SO's dlopen'ed handle.  */
265 | 
266 | static void
979 | 	return false;
980 |     }
981 | 
982 |   handle = dlopen (library, RTLD_NOW);
983 |   if (handle == NULL)
984 |     {
985 |       if (libthread_db_debug)
986 | 	fprintf_unfiltered (gdb_stdlog, _("dlopen failed: %s.\n"), dlerror ());
987 |       return false;
988 |     }
1078 | 
1079 | /* Handle $sdir in libthread-db-search-path.
1080 |    Look for libthread_db in the system dirs, or wherever a plain
1081 |    dlopen(file_without_path) will look.
1082 |    The result is true for success.  */
1083 | 
{% endraw %}

```
### gdb/jit.c

```c

{% raw %}
185 |   if (jit_debug)
186 |     fprintf_unfiltered (gdb_stdlog, _("Opening shared object %s.\n"),
187 |                         file_name);
188 |   gdb_dlhandle_up so = gdb_dlopen (file_name);
189 | 
190 |   init_fn = (reader_init_fn_type *) gdb_dlsym (so, reader_init_fn_sym);
{% endraw %}

```
### gdb/ppc64-tdep.c

```c

{% raw %}
569 | 	 section.  Unfortunately, this function may be called at a time
570 | 	 where these relocations have not yet been performed -- this can
571 | 	 happen for example shortly after a library has been loaded with
572 | 	 dlopen, but ld.so has not yet applied the relocations.
573 | 
574 | 	 To cope with both the case where the relocation has been applied,
{% endraw %}

```
### gdb/sol-thread.c

```c

{% raw %}
1150 | {
1151 |   void *dlhandle;
1152 | 
1153 |   dlhandle = dlopen ("libthread_db.so.1", RTLD_NOW);
1154 |   if (!dlhandle)
1155 |     goto die;
{% endraw %}

```
### gdb/ia64-libunwind-tdep.c

```c

{% raw %}
509 |   void *handle;
510 |   char *so_error = NULL;
511 | 
512 |   handle = dlopen (LIBUNWIND_SO, RTLD_NOW);
513 |   if (handle == NULL)
514 |     {
515 |       so_error = xstrdup (dlerror ());
516 | #ifdef LIBUNWIND_SO_7
517 |       handle = dlopen (LIBUNWIND_SO_7, RTLD_NOW);
518 | #endif /* LIBUNWIND_SO_7 */
519 |     }
{% endraw %}

```
### gdb/compile/compile-c-support.c

```c

{% raw %}
79 | 
80 |   /* gdb_dlopen will call error () on an error, so no need to check
81 |      value.  */
82 |   gdb_dlhandle_up handle = gdb_dlopen (fe_libcc);
83 |   func = (FUNCTYPE *) gdb_dlsym (handle, fe_context);
84 | 
{% endraw %}

```
### gdb/gdbserver/thread-db.c

```c

{% raw %}
605 |   if (debug_threads)
606 |     debug_printf ("Trying host libthread_db library: %s.\n",
607 | 		  library);
608 |   handle = dlopen (library, RTLD_NOW);
609 |   if (handle == NULL)
610 |     {
611 |       if (debug_threads)
612 | 	debug_printf ("dlopen failed: %s.\n", dlerror ());
613 |       return 0;
614 |     }
639 | 
640 | /* Handle $sdir in libthread-db-search-path.
641 |    Look for libthread_db in the system dirs, or wherever a plain
642 |    dlopen(file_without_path) will look.
643 |    The result is true for success.  */
644 | 
{% endraw %}

```
### gdb/testsuite/gdb.cp/infcall-dlopen.cc

```cpp

{% raw %}
20 | static int
21 | openlib (const char *filename)
22 | {
23 |   void *h = dlopen (filename, RTLD_LAZY);
24 | 
25 |   if (filename == NULL)
{% endraw %}

```
### gdb/testsuite/gdb.base/info-shared.c

```c

{% raw %}
27 |   void *handle1, *handle2;
28 |   void (*func)(int);
29 | 
30 |   handle1 = dlopen (SHLIB1_NAME, RTLD_LAZY);
31 |   assert (handle1 != NULL);
32 |   stop ();
33 | 
34 |   handle2 = dlopen (SHLIB2_NAME, RTLD_LAZY);
35 |   assert (handle2 != NULL);
36 |   stop ();
{% endraw %}

```
### gdb/testsuite/gdb.base/catch-load.c

```c

{% raw %}
32 | {
33 |   void *h;
34 | 
35 |   h = dlopen (libname, RTLD_LAZY);
36 | 
37 |   dlclose (h);
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-disc.c

```c

{% raw %}
32 |   void *handle;
33 |   void (*func) (void);
34 | 
35 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
36 |   if (!handle)
37 |     {
{% endraw %}

```
### gdb/testsuite/gdb.base/print-file-var-main.c

```c

{% raw %}
44 | 
45 | #ifdef SHLIB_NAME
46 |   {
47 |     void *handle = dlopen (SHLIB_NAME, RTLD_LAZY);
48 |     int (*getver2) (void);
49 | 
{% endraw %}

```
### gdb/testsuite/gdb.base/watchpoint-solib.c

```c

{% raw %}
36 |   void *handle;
37 |   void (*foo) (int);
38 | 
39 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
40 |   
41 |   if (!handle)
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-vanish-main.c

```c

{% raw %}
29 |   char *dest = VANISH_LIB ".renamed";
30 | 
31 |   /* Open library.  */
32 |   handle = dlopen (VANISH_LIB, RTLD_NOW);
33 |   if (!handle)
34 |     {
{% endraw %}

```
### gdb/testsuite/gdb.base/jit-dlmain.c

```c

{% raw %}
7 |   void *h;
8 |   int (*p_main) (int, char **);
9 | 
10 |   h = NULL;  /* break here before-dlopen  */
11 |   h = dlopen (jit_libname, RTLD_LAZY);
12 |   if (h == NULL) return 1;
13 | 
14 |   p_main = dlsym (h, "jit_dl_main");
15 |   if (p_main == NULL) return 2;
16 | 
17 |   h = h;  /* break here after-dlopen */
18 |   return (*p_main) (argc, argv);
19 | }
{% endraw %}

```
### gdb/testsuite/gdb.base/break-probes.c

```c

{% raw %}
19 | int
20 | main (void)
21 | {
22 |   void *handle = dlopen (SHLIB_NAME, RTLD_LAZY);
23 | 
24 |   assert (handle != NULL);
{% endraw %}

```
### gdb/testsuite/gdb.base/unload.c

```c

{% raw %}
39 |   int y;
40 |   const char *msg;
41 | 
42 |   handle = dlopen (SHLIB_NAME, RTLD_LAZY);
43 |   
44 |   if (!handle)
66 | 
67 |   /* The second library should share the same memory address.  */
68 | 
69 |   handle = dlopen (SHLIB_NAME2, RTLD_LAZY);
70 |   
71 |   if (!handle)
{% endraw %}

```
### gdb/testsuite/gdb.base/corefile-buildid-shlib.c

```c

{% raw %}
37 |   int (*func) (void);
38 |   int result;
39 | 
40 |   handle = dlopen (the_shlib, RTLD_LAZY);
41 |   if (!handle)
42 |     {
{% endraw %}

```
### gdb/testsuite/gdb.threads/dlopen-libpthread.c

```c

{% raw %}
33 |   void (*fp) (void (*) (void));
34 | 
35 |   assert (filename != NULL);
36 |   h = dlopen (filename, RTLD_LAZY);
37 |   assert (h != NULL);
38 | 
{% endraw %}

```
### gdb/testsuite/gdb.perf/solib.c

```c

{% raw %}
44 |   for (i = 0; i < number; i++)
45 |     {
46 |       sprintf (libname, "solib-lib%d", i);
47 |       handles[i] = dlopen (libname, RTLD_LAZY);
48 |       if (handles[i] == NULL)
49 | 	{
50 | 	  printf ("ERROR on dlopen %s\n", libname);
51 | 	  exit (-1);
52 | 	}
{% endraw %}

```
### gdb/testsuite/gdb.btrace/dlopen.c

```c

{% raw %}
25 |   int (*fun) (void);
26 |   int answer;
27 | 
28 |   dso = dlopen (DSO_NAME, RTLD_NOW | RTLD_GLOBAL);
29 |   assert (dso != NULL);
30 | 
{% endraw %}

```
### gdb/testsuite/gdb.trace/change-loc.c

```c

{% raw %}
35 | 
36 |   marker ();
37 | 
38 |   h = dlopen (libname, RTLD_LAZY);
39 |   if (h == NULL) return 1;
40 | 
{% endraw %}

```
### gdb/testsuite/gdb.trace/pending.c

```c

{% raw %}
34 | 
35 |   marker ();
36 | 
37 |   h = dlopen (libname, RTLD_LAZY);
38 |   if (h == NULL) return 1;
39 | 
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-pending.c

```c

{% raw %}
28 |   void *h;
29 |   int (*p_func) ();
30 | 
31 |   h = dlopen (libname, RTLD_LAZY);  /* set breakpoint here */
32 |   if (h == NULL)
33 |     return NULL;
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-catch-load.c

```c

{% raw %}
31 | {
32 |   void *h;
33 | 
34 |   h = dlopen (libname, RTLD_LAZY);
35 | 
36 |   dlclose (h);
{% endraw %}

```
### gdb/testsuite/gdb.mi/pending.c

```c

{% raw %}
35 | 
36 |   marker ();
37 | 
38 |   h = dlopen (libname, RTLD_LAZY);
39 |   if (h == NULL) return 1;
40 | 
{% endraw %}

```
### gdb/gdbsupport/gdb-dlfcn.h

```c

{% raw %}
34 |    for that dynamic library.  Return NULL if the loading fails for any
35 |    reason.  */
36 | 
37 | gdb_dlhandle_up gdb_dlopen (const char *filename);
38 | 
39 | /* Return the address of the symbol named SYMBOL inside the shared
{% endraw %}

```
### gdb/gdbsupport/gdb-dlfcn.c

```c

{% raw %}
31 | #ifdef NO_SHARED_LIB
32 | 
33 | gdb_dlhandle_up
34 | gdb_dlopen (const char *filename)
35 | {
36 |   gdb_assert_not_reached ("gdb_dlopen should not be called on this platform.");
37 | }
38 | 
57 | #else /* NO_SHARED_LIB */
58 | 
59 | gdb_dlhandle_up
60 | gdb_dlopen (const char *filename)
61 | {
62 |   void *result;
63 | #ifdef HAVE_DLFCN_H
64 |   result = dlopen (filename, RTLD_NOW);
65 | #elif __MINGW32__
66 |   result = (void *) LoadLibrary (filename);
{% endraw %}

```
### ld/lexsup.c

```c

{% raw %}
1805 |   fprintf (file, _("\
1806 |   -z nodelete                 Mark DSO non-deletable at runtime\n"));
1807 |   fprintf (file, _("\
1808 |   -z nodlopen                 Mark DSO not available to dlopen\n"));
1809 |   fprintf (file, _("\
1810 |   -z nodump                   Mark DSO not available to dldump\n"));
{% endraw %}

```
### ld/plugin.c

```c

{% raw %}
181 | #define RTLD_NOW 0	/* Dummy value.  */
182 | 
183 | static void *
184 | dlopen (const char *file, int mode ATTRIBUTE_UNUSED)
185 | {
186 |   return LoadLibrary (file);
241 |   newplug = xmalloc (sizeof *newplug);
242 |   memset (newplug, 0, sizeof *newplug);
243 |   newplug->name = plugin;
244 |   newplug->dlhandle = dlopen (plugin, RTLD_NOW);
245 |   if (!newplug->dlhandle)
246 |     einfo (_("%F%P: %s: error loading plugin: %s\n"), plugin, dlerror ());
{% endraw %}

```
### ld/testsuite/ld-elf/dl1main.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl1.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl1.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6dmain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6d.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6d.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6bmain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6b.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6b.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6amain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6a.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6a.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6cmain.c

```c

{% raw %}
9 |   void *handle;
10 |   void (*fcn) (void);
11 | 
12 |   handle = dlopen("./tmpdir/libdl6c.so", RTLD_GLOBAL|RTLD_LAZY);
13 |   if (!handle)
14 |     {
15 |       printf("dlopen ./tmpdir/libdl6c.so: %s\n", dlerror ());
16 |       return 1;
17 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-2c.c

```c

{% raw %}
11 |   if (foo1 () != 0)
12 |     return 1;
13 | 
14 |   dl = dlopen("pr21964-2b.so", RTLD_LAZY);
15 |   if (!dl)
16 |     return 2;
{% endraw %}

```