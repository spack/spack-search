---
name: "gdb"
layout: package
next_package: wt
previous_package: zabbix
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.10.1
26 / 10755 files match, 23 filtered matches.

 - [sim/bfin/gui.c](#simbfinguic)
 - [bfd/plugin.c](#bfdpluginc)
 - [gdb/gdb-dlfcn.h](#gdbgdb-dlfcnh)
 - [gdb/linux-thread-db.c](#gdblinux-thread-dbc)
 - [gdb/jit.c](#gdbjitc)
 - [gdb/sol-thread.c](#gdbsol-threadc)
 - [gdb/gdb-dlfcn.c](#gdbgdb-dlfcnc)
 - [gdb/ia64-libunwind-tdep.c](#gdbia64-libunwind-tdepc)
 - [gdb/compile/compile-c-support.c](#gdbcompilecompile-c-supportc)
 - [gdb/gdbserver/thread-db.c](#gdbgdbserverthread-dbc)
 - [gdb/gdbserver/tracepoint.c](#gdbgdbservertracepointc)
 - [gdb/contrib/expect-read1.c](#gdbcontribexpect-read1c)
 - [gdb/testsuite/lib/read1.c](#gdbtestsuitelibread1c)
 - [gdb/testsuite/gdb.base/info-shared.c](#gdbtestsuitegdbbaseinfo-sharedc)
 - [gdb/testsuite/gdb.base/solib-disc.c](#gdbtestsuitegdbbasesolib-discc)
 - [gdb/testsuite/gdb.base/watchpoint-solib.c](#gdbtestsuitegdbbasewatchpoint-solibc)
 - [gdb/testsuite/gdb.base/jit-dlmain.c](#gdbtestsuitegdbbasejit-dlmainc)
 - [gdb/testsuite/gdb.base/unload.c](#gdbtestsuitegdbbaseunloadc)
 - [gdb/testsuite/gdb.threads/dlopen-libpthread.c](#gdbtestsuitegdbthreadsdlopen-libpthreadc)
 - [gdb/testsuite/gdb.trace/change-loc.c](#gdbtestsuitegdbtracechange-locc)
 - [gdb/testsuite/gdb.trace/pending.c](#gdbtestsuitegdbtracependingc)
 - [gdb/testsuite/gdb.mi/mi-pending.c](#gdbtestsuitegdbmimi-pendingc)
 - [gdb/testsuite/gdb.mi/pending.c](#gdbtestsuitegdbmipendingc)

### sim/bfin/gui.c

```c

{% raw %}
84 |   funcs = (void *) &sdl.Init;
85 |   for (i = 0; i < ARRAY_SIZE (sdl_syms); ++i)
86 |     {
87 |       funcs[i] = dlsym (sdl.handle, sdl_syms[i]);
88 |       if (funcs[i] == NULL)
89 | 	{
{% endraw %}

```
### bfd/plugin.c

```c

{% raw %}
48 | }
49 | 
50 | static void *
51 | dlsym (void *handle, const char *name)
52 | {
53 |   return GetProcAddress (handle, name);
220 |       return 0;
221 |     }
222 | 
223 |   onload = dlsym (plugin_handle, "onload");
224 |   if (!onload)
225 |     goto err;
{% endraw %}

```
### gdb/gdb-dlfcn.h

```c

{% raw %}
29 |    library whose handle is HANDLE.  Return NULL when the symbol could
30 |    not be found.  */
31 | 
32 | void *gdb_dlsym (void *handle, const char *symbol);
33 | 
34 | /* Install a cleanup routine which closes the handle HANDLE.  */
{% endraw %}

```
### gdb/linux-thread-db.c

```c

{% raw %}
465 | }
466 | 
467 | static void *
468 | verbose_dlsym (void *handle, const char *name)
469 | {
470 |   void *sym = dlsym (handle, name);
471 |   if (sym == NULL)
472 |     warning (_("Symbol \"%s\" not found in libthread_db: %s"),
676 |   /* Initialize pointers to the dynamic library functions we will use.
677 |      Essential functions first.  */
678 | 
679 |   info->td_init_p = verbose_dlsym (info->handle, "td_init");
680 |   if (info->td_init_p == NULL)
681 |     return 0;
688 |       return 0;
689 |     }
690 | 
691 |   info->td_ta_new_p = verbose_dlsym (info->handle, "td_ta_new");
692 |   if (info->td_ta_new_p == NULL)
693 |     return 0;
719 |       return 0;
720 |     }
721 | 
722 |   info->td_ta_map_lwp2thr_p = verbose_dlsym (info->handle,
723 | 					     "td_ta_map_lwp2thr");
724 |   if (info->td_ta_map_lwp2thr_p == NULL)
725 |     return 0;
726 | 
727 |   info->td_ta_thr_iter_p = verbose_dlsym (info->handle, "td_ta_thr_iter");
728 |   if (info->td_ta_thr_iter_p == NULL)
729 |     return 0;
730 | 
731 |   info->td_thr_get_info_p = verbose_dlsym (info->handle, "td_thr_get_info");
732 |   if (info->td_thr_get_info_p == NULL)
733 |     return 0;
734 | 
735 |   /* These are not essential.  */
736 |   info->td_ta_event_addr_p = dlsym (info->handle, "td_ta_event_addr");
737 |   info->td_ta_set_event_p = dlsym (info->handle, "td_ta_set_event");
738 |   info->td_ta_clear_event_p = dlsym (info->handle, "td_ta_clear_event");
739 |   info->td_ta_event_getmsg_p = dlsym (info->handle, "td_ta_event_getmsg");
740 |   info->td_thr_event_enable_p = dlsym (info->handle, "td_thr_event_enable");
741 |   info->td_thr_tls_get_addr_p = dlsym (info->handle, "td_thr_tls_get_addr");
742 |   info->td_thr_tlsbase_p = dlsym (info->handle, "td_thr_tlsbase");
743 | 
744 |   /* It's best to avoid td_ta_thr_iter if possible.  That walks data
849 |     {
850 |       void *td_init;
851 | 
852 |       td_init = dlsym (handle, "td_init");
853 |       if (td_init != NULL)
854 |         {
{% endraw %}

```
### gdb/jit.c

```c

{% raw %}
176 |   so = gdb_dlopen (file_name);
177 |   old_cleanups = make_cleanup_dlclose (so);
178 | 
179 |   init_fn = gdb_dlsym (so, reader_init_fn_sym);
180 |   if (!init_fn)
181 |     error (_("Could not locate initialization function: %s."),
182 |           reader_init_fn_sym);
183 | 
184 |   if (gdb_dlsym (so, "plugin_is_GPL_compatible") == NULL)
185 |     error (_("Reader not GPL compatible."));
186 | 
{% endraw %}

```
### gdb/sol-thread.c

```c

{% raw %}
1248 |     goto die;
1249 | 
1250 | #define resolve(X) \
1251 |   if (!(p_##X = dlsym (dlhandle, #X))) \
1252 |     goto die;
1253 | 
{% endraw %}

```
### gdb/gdb-dlfcn.c

```c

{% raw %}
37 | }
38 | 
39 | void *
40 | gdb_dlsym (void *handle, const char *symbol)
41 | {
42 |   gdb_assert_not_reached ("gdb_dlsym should not be called on this platform.");
43 | }
44 | 
96 | }
97 | 
98 | void *
99 | gdb_dlsym (void *handle, const char *symbol)
100 | {
101 | #ifdef HAVE_DLFCN_H
102 |   return dlsym (handle, symbol);
103 | #elif __MINGW32__
104 |   return (void *) GetProcAddress (handle, symbol);
{% endraw %}

```
### gdb/ia64-libunwind-tdep.c

```c

{% raw %}
516 | 
517 |   /* Initialize pointers to the dynamic library functions we will use.  */
518 | 
519 |   unw_get_reg_p = dlsym (handle, get_reg_name);
520 |   if (unw_get_reg_p == NULL)
521 |     return 0;
522 | 
523 |   unw_get_fpreg_p = dlsym (handle, get_fpreg_name);
524 |   if (unw_get_fpreg_p == NULL)
525 |     return 0;
526 | 
527 |   unw_get_saveloc_p = dlsym (handle, get_saveloc_name);
528 |   if (unw_get_saveloc_p == NULL)
529 |     return 0;
530 | 
531 |   unw_is_signal_frame_p = dlsym (handle, is_signal_frame_name);
532 |   if (unw_is_signal_frame_p == NULL)
533 |     return 0;
534 | 
535 |   unw_step_p = dlsym (handle, step_name);
536 |   if (unw_step_p == NULL)
537 |     return 0;
538 | 
539 |   unw_init_remote_p = dlsym (handle, init_remote_name);
540 |   if (unw_init_remote_p == NULL)
541 |     return 0;
542 | 
543 |   unw_create_addr_space_p = dlsym (handle, create_addr_space_name);
544 |   if (unw_create_addr_space_p == NULL)
545 |     return 0;
546 | 
547 |   unw_destroy_addr_space_p = dlsym (handle, destroy_addr_space_name);
548 |   if (unw_destroy_addr_space_p == NULL)
549 |     return 0;
550 | 
551 |   unw_search_unwind_table_p = dlsym (handle, search_unwind_table_name);
552 |   if (unw_search_unwind_table_p == NULL)
553 |     return 0;
554 | 
555 |   unw_find_dyn_list_p = dlsym (handle, find_dyn_list_name);
556 |   if (unw_find_dyn_list_p == NULL)
557 |     return 0;
{% endraw %}

```
### gdb/compile/compile-c-support.c

```c

{% raw %}
79 |    /* gdb_dlopen will call error () on an error, so no need to check
80 |       value.  */
81 |   handle = gdb_dlopen (STRINGIFY (GCC_C_FE_LIBCC));
82 |   func = (gcc_c_fe_context_function *) gdb_dlsym (handle,
83 | 						  STRINGIFY (GCC_C_FE_CONTEXT));
84 | 
{% endraw %}

```
### gdb/gdbserver/thread-db.c

```c

{% raw %}
633 |       if ((a) == NULL)						\
634 | 	{							\
635 | 	  if (debug_threads)					\
636 | 	    debug_printf ("dlsym: %s\n", dlerror ());		\
637 | 	  if (required)						\
638 | 	    {							\
644 |     }								\
645 |   while (0)
646 | 
647 |   CHK (1, tdb->td_ta_new_p = dlsym (handle, "td_ta_new"));
648 | 
649 |   /* Attempt to open a connection to the thread library.  */
657 |       return 0;
658 |     }
659 | 
660 |   CHK (1, tdb->td_ta_map_lwp2thr_p = dlsym (handle, "td_ta_map_lwp2thr"));
661 |   CHK (1, tdb->td_thr_get_info_p = dlsym (handle, "td_thr_get_info"));
662 |   CHK (1, tdb->td_ta_thr_iter_p = dlsym (handle, "td_ta_thr_iter"));
663 |   CHK (1, tdb->td_symbol_list_p = dlsym (handle, "td_symbol_list"));
664 | 
665 |   /* This is required only when thread_db_use_events is on.  */
666 |   CHK (thread_db_use_events,
667 |        tdb->td_thr_event_enable_p = dlsym (handle, "td_thr_event_enable"));
668 | 
669 |   /* These are not essential.  */
670 |   CHK (0, tdb->td_ta_event_addr_p = dlsym (handle, "td_ta_event_addr"));
671 |   CHK (0, tdb->td_ta_set_event_p = dlsym (handle, "td_ta_set_event"));
672 |   CHK (0, tdb->td_ta_event_getmsg_p = dlsym (handle, "td_ta_event_getmsg"));
673 |   CHK (0, tdb->td_thr_tls_get_addr_p = dlsym (handle, "td_thr_tls_get_addr"));
674 |   CHK (0, tdb->td_thr_tlsbase_p = dlsym (handle, "td_thr_tlsbase"));
675 | 
676 | #undef CHK
717 |     {
718 |       void *td_init;
719 | 
720 |       td_init = dlsym (handle, "td_init");
721 |       if (td_init != NULL)
722 | 	{
913 | 				       td_thr_events_t *event);
914 | 
915 | #ifndef USE_LIBTHREAD_DB_DIRECTLY
916 |       td_ta_clear_event_p = dlsym (thread_db->handle, "td_ta_clear_event");
917 | #else
918 |       td_ta_clear_event_p = &td_ta_clear_event;
976 |       td_err_e (*td_ta_delete_p) (td_thragent_t *);
977 | 
978 | #ifndef USE_LIBTHREAD_DB_DIRECTLY
979 |       td_ta_delete_p = dlsym (thread_db->handle, "td_ta_delete");
980 | #else
981 |       td_ta_delete_p = &td_ta_delete;
{% endraw %}

```
### gdb/gdbserver/tracepoint.c

```c

{% raw %}
6588 |   do								\
6589 |     {								\
6590 |       if (ust_ops.SYM == NULL)					\
6591 | 	ust_ops.SYM = (typeof (&SYM)) dlsym (RTLD_DEFAULT, #SYM);	\
6592 |       if (ust_ops.SYM == NULL)					\
6593 | 	return 0;						\
6598 | /* Get pointers to all libust.so functions we care about.  */
6599 | 
6600 | static int
6601 | dlsym_ust (void)
6602 | {
6603 |   GET_UST_SYM (serialize_to_text);
7121 | static void
7122 | gdb_ust_init (void)
7123 | {
7124 |   if (!dlsym_ust ())
7125 |     return;
7126 | 
{% endraw %}

```
### gdb/contrib/expect-read1.c

```c

{% raw %}
29 |   if (read2 == NULL)
30 |     {
31 |       unsetenv ("LD_PRELOAD");
32 |       read2 = dlsym (RTLD_NEXT, "read");
33 |     }
34 | 
{% endraw %}

```
### gdb/testsuite/lib/read1.c

```c

{% raw %}
31 |   if (read2 == NULL)
32 |     {
33 |       unsetenv ("LD_PRELOAD");
34 |       read2 = dlsym (RTLD_NEXT, "read");
35 |     }
36 |   if (count > 1 && isatty (fd) >= 1)
{% endraw %}

```
### gdb/testsuite/gdb.base/info-shared.c

```c

{% raw %}
35 |   assert (handle2 != NULL);
36 |   stop ();
37 | 
38 |   func = (void (*)(int)) dlsym (handle1, "foo");
39 |   func (1);
40 | 
41 |   func = (void (*)(int)) dlsym (handle2, "bar");
42 |   func (2);
43 | 
{% endraw %}

```
### gdb/testsuite/gdb.base/solib-disc.c

```c

{% raw %}
39 |       exit (1);
40 |     }
41 | 
42 |   func = (void (*)(void)) dlsym (handle, "shrfunc");
43 |   if (!func)
44 |     {
{% endraw %}

```
### gdb/testsuite/gdb.base/watchpoint-solib.c

```c

{% raw %}
48 |       exit (1);
49 |     }
50 | 
51 |   foo = (void (*)(int))dlsym (handle, "foo");
52 | 
53 |   if (!foo)
{% endraw %}

```
### gdb/testsuite/gdb.base/jit-dlmain.c

```c

{% raw %}
11 |   h = dlopen (jit_libname, RTLD_LAZY);
12 |   if (h == NULL) return 1;
13 | 
14 |   p_main = dlsym (h, "jit_dl_main");
15 |   if (p_main == NULL) return 2;
16 | 
{% endraw %}

```
### gdb/testsuite/gdb.base/unload.c

```c

{% raw %}
47 |       exit (1);
48 |     }
49 | 
50 |   unloadshr = (int (*) (int)) dlsym (handle, "shrfunc1");
51 | 
52 |   if (!unloadshr)
74 |       exit (1);
75 |     }
76 | 
77 |   unloadshr = (int (*)(int)) dlsym (handle, "shrfunc2");
78 | 
79 |   if (!unloadshr)
{% endraw %}

```
### gdb/testsuite/gdb.threads/dlopen-libpthread.c

```c

{% raw %}
36 |   h = dlopen (filename, RTLD_LAZY);
37 |   assert (h != NULL);
38 | 
39 |   fp = dlsym (h, "f");
40 |   assert (fp != NULL);
41 | 
{% endraw %}

```
### gdb/testsuite/gdb.trace/change-loc.c

```c

{% raw %}
38 |   h = dlopen (libname, RTLD_LAZY);
39 |   if (h == NULL) return 1;
40 | 
41 |   p_func = dlsym (h, "func2");
42 |   if (p_func == NULL) return 2;
43 | 
{% endraw %}

```
### gdb/testsuite/gdb.trace/pending.c

```c

{% raw %}
37 |   h = dlopen (libname, RTLD_LAZY);
38 |   if (h == NULL) return 1;
39 | 
40 |   p_func = dlsym (h, "pendfunc2");
41 |   if (p_func == NULL) return 2;
42 | 
{% endraw %}

```
### gdb/testsuite/gdb.mi/mi-pending.c

```c

{% raw %}
32 |   if (h == NULL)
33 |     return;
34 | 
35 |   p_func = dlsym (h, "pendfunc3");
36 |   if (p_func == NULL)
37 |     return;
{% endraw %}

```
### gdb/testsuite/gdb.mi/pending.c

```c

{% raw %}
38 |   h = dlopen (libname, RTLD_LAZY);
39 |   if (h == NULL) return 1;
40 | 
41 |   p_func = dlsym (h, "pendfunc2");
42 |   if (p_func == NULL) return 2;
43 | 
{% endraw %}

```