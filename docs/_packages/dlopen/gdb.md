---
name: "gdb"
layout: package
next_package: wt
previous_package: zabbix
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 7.10.1
63 / 10755 files match, 30 filtered matches.

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
4475 |   entry->relocstlsoff += l;
4476 | 
4477 |   /* If there's any TLSOFF relocation, mark the output file as not
4478 |      suitable for dlopening.  This mark will remain even if we relax
4479 |      all such relocations, but this is not a problem, since we'll only
4480 |      do so for executables, and we definitely don't want anyone
4481 |      dlopening executables.  */
4482 |   if (entry->relocstlsoff)
4483 |     dinfo->info->flags |= DF_STATIC_TLS;
5651 |     return TRUE;
5652 | 
5653 |   /* We can only relax when linking the main executable or a library
5654 |      that can't be dlopened.  */
5655 |   if (! info->executable && ! (info->flags & DF_STATIC_TLS))
5656 |     return TRUE;
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
213 | 
214 |   *has_plugin_p = 0;
215 | 
216 |   plugin_handle = dlopen (pname, RTLD_NOW);
217 |   if (!plugin_handle)
218 |     {
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
### gdb/breakpoint.c

```c

{% raw %}
13085 | momentary_bkpt_re_set (struct breakpoint *b)
13086 | {
13087 |   /* Keep temporary breakpoints, which can be encountered when we step
13088 |      over a dlopen call and solib_add is resetting the breakpoints.
13089 |      Otherwise these should have been blown away via the cleanup chain
13090 |      or by breakpoint_init_inferior when we rerun the executable.  */
{% endraw %}

```
### gdb/gdb-dlfcn.h

```c

{% raw %}
23 |    for that dynamic library.  Return NULL if the loading fails for any
24 |    reason.  */
25 | 
26 | void *gdb_dlopen (const char *filename);
27 | 
28 | /* Return the address of the symbol named SYMBOL inside the shared
{% endraw %}

```
### gdb/linux-thread-db.c

```c

{% raw %}
222 | 
223 | /* Add the current inferior to the list of processes using libpthread.
224 |    Return a pointer to the newly allocated object that was added to
225 |    THREAD_DB_LIST.  HANDLE is the handle returned by dlopen'ing
226 |    LIBTHREAD_DB_SO.  */
227 | 
263 | /* When PID has exited or has been detached, we no longer want to keep
264 |    track of it as using libpthread.  Call this function to discard
265 |    thread_db related info related to PID.  Note that this closes
266 |    LIBTHREAD_DB_SO's dlopen'ed handle.  */
267 | 
268 | static void
837 | 	return 0;
838 |     }
839 | 
840 |   handle = dlopen (library, RTLD_NOW);
841 |   if (handle == NULL)
842 |     {
843 |       if (libthread_db_debug)
844 | 	fprintf_unfiltered (gdb_stdlog, _("dlopen failed: %s.\n"), dlerror ());
845 |       return 0;
846 |     }
950 | 
951 | /* Handle $sdir in libthread-db-search-path.
952 |    Look for libthread_db in the system dirs, or wherever a plain
953 |    dlopen(file_without_path) will look.
954 |    The result is true for success.  */
955 | 
{% endraw %}

```
### gdb/jit.c

```c

{% raw %}
173 |   if (jit_debug)
174 |     fprintf_unfiltered (gdb_stdlog, _("Opening shared object %s.\n"),
175 |                         file_name);
176 |   so = gdb_dlopen (file_name);
177 |   old_cleanups = make_cleanup_dlclose (so);
178 | 
{% endraw %}

```
### gdb/ppc64-tdep.c

```c

{% raw %}
570 | 	 section.  Unfortunately, this function may be called at a time
571 | 	 where these relocations have not yet been performed -- this can
572 | 	 happen for example shortly after a library has been loaded with
573 | 	 dlopen, but ld.so has not yet applied the relocations.
574 | 
575 | 	 To cope with both the case where the relocation has been applied,
{% endraw %}

```
### gdb/sol-thread.c

```c

{% raw %}
1243 | 
1244 |   init_sol_thread_ops ();
1245 | 
1246 |   dlhandle = dlopen ("libthread_db.so.1", RTLD_NOW);
1247 |   if (!dlhandle)
1248 |     goto die;
{% endraw %}

```
### gdb/gdb-dlfcn.c

```c

{% raw %}
31 | #ifdef NO_SHARED_LIB
32 | 
33 | void *
34 | gdb_dlopen (const char *filename)
35 | {
36 |   gdb_assert_not_reached ("gdb_dlopen should not be called on this platform.");
37 | }
38 | 
64 | #else /* NO_SHARED_LIB */
65 | 
66 | void *
67 | gdb_dlopen (const char *filename)
68 | {
69 |   void *result;
70 | #ifdef HAVE_DLFCN_H
71 |   result = dlopen (filename, RTLD_NOW);
72 | #elif __MINGW32__
73 |   result = (void *) LoadLibrary (filename);
{% endraw %}

```
### gdb/ia64-libunwind-tdep.c

```c

{% raw %}
493 |   void *handle;
494 |   char *so_error = NULL;
495 | 
496 |   handle = dlopen (LIBUNWIND_SO, RTLD_NOW);
497 |   if (handle == NULL)
498 |     {
499 |       so_error = xstrdup (dlerror ());
500 | #ifdef LIBUNWIND_SO_7
501 |       handle = dlopen (LIBUNWIND_SO_7, RTLD_NOW);
502 | #endif /* LIBUNWIND_SO_7 */
503 |     }
{% endraw %}

```
### gdb/compile/compile-c-support.c

```c

{% raw %}
78 | 
79 |    /* gdb_dlopen will call error () on an error, so no need to check
80 |       value.  */
81 |   handle = gdb_dlopen (STRINGIFY (GCC_C_FE_LIBCC));
82 |   func = (gcc_c_fe_context_function *) gdb_dlsym (handle,
83 | 						  STRINGIFY (GCC_C_FE_CONTEXT));
{% endraw %}

```
### gdb/gdbserver/thread-db.c

```c

{% raw %}
704 |   if (debug_threads)
705 |     debug_printf ("Trying host libthread_db library: %s.\n",
706 | 		  library);
707 |   handle = dlopen (library, RTLD_NOW);
708 |   if (handle == NULL)
709 |     {
710 |       if (debug_threads)
711 | 	debug_printf ("dlopen failed: %s.\n", dlerror ());
712 |       return 0;
713 |     }
739 | 
740 | /* Handle $sdir in libthread-db-search-path.
741 |    Look for libthread_db in the system dirs, or wherever a plain
742 |    dlopen(file_without_path) will look.
743 |    The result is true for success.  */
744 | 
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
33 |     return;
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