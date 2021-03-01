---
name: "openmpi"
layout: package
next_package: openssl
previous_package: openmc
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.7.5
70 / 7011 files match, 26 filtered matches.

 - [ompi/mca/btl/usnic/test/ompi_btl_usnic_run_tests.c](#ompimcabtlusnictestompi_btl_usnic_run_testsc)
 - [ompi/mca/common/cuda/common_cuda.c](#ompimcacommoncudacommon_cudac)
 - [ompi/mpi/java/c/mpi_MPI.c](#ompimpijavacmpi_mpic)
 - [ompi/debuggers/dlopen_test.c](#ompidebuggersdlopen_testc)
 - [ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c](#ompicontribvtvtvtlibvt_mallocwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_libwrap.c](#ompicontribvtvtvtlibvt_libwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_iowrap.c](#ompicontribvtvtvtlibvt_iowrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c](#ompicontribvtvtvtlibvt_plugin_cntrc)
 - [ompi/tools/ompi_info/param.c](#ompitoolsompi_infoparamc)
 - [oshmem/tools/oshmem_info/param.c](#oshmemtoolsoshmem_infoparamc)
 - [orte/tools/orte-info/param.c](#ortetoolsorte-infoparamc)
 - [opal/mca/base/base.h](#opalmcabasebaseh)
 - [opal/mca/base/mca_base_open.c](#opalmcabasemca_base_openc)
 - [opal/mca/base/mca_base_component_find.c](#opalmcabasemca_base_component_findc)
 - [opal/mca/hwloc/hwloc172/hwloc/src/components.c](#opalmcahwlochwloc172hwlocsrccomponentsc)
 - [opal/mca/memory/linux/hooks.c](#opalmcamemorylinuxhooksc)
 - [opal/mca/memory/linux/memory_linux_ptmalloc2.c](#opalmcamemorylinuxmemory_linux_ptmalloc2c)
 - [opal/util/lt_interface.h](#opalutillt_interfaceh)
 - [opal/util/lt_interface.c](#opalutillt_interfacec)
 - [opal/libltdl/ltdl.h](#opallibltdlltdlh)
 - [opal/libltdl/ltdl.c](#opallibltdlltdlc)
 - [opal/libltdl/loaders/preopen.c](#opallibltdlloaderspreopenc)
 - [opal/libltdl/loaders/dlopen.c](#opallibltdlloadersdlopenc)
 - [opal/libltdl/libltdl/lt__private.h](#opallibltdllibltdllt__privateh)
 - [opal/libltdl/libltdl/lt_error.h](#opallibltdllibltdllt_errorh)
 - [test/support/components.c](#testsupportcomponentsc)

### ompi/mca/btl/usnic/test/ompi_btl_usnic_run_tests.c

```c

{% raw %}
38 |     char *to;
39 |     int path_len;
40 | 
41 |     mpi_handle = dlopen("libmpi.so", RTLD_NOW|RTLD_GLOBAL);
42 |     if (mpi_handle == NULL) {
43 |         fprintf(stderr, "mpi_handle=NULL dlerror()=%s\n", dlerror());
74 |     to = stpcpy(to, "/openmpi/");
75 |     to = stpcpy(to, MCA_BTL_USNIC_SO);
76 | 
77 |     usnic_handle = dlopen(path, RTLD_NOW|RTLD_LOCAL);
78 |     if (usnic_handle == NULL) {
79 |         fprintf(stderr, "usnic_handle=%p dlerror()=%s\n", (void *)usnic_handle, dlerror());
{% endraw %}

```
### ompi/mca/common/cuda/common_cuda.c

```c

{% raw %}
330 | 
331 |     if (0 != (retval = opal_lt_dlinit())) {
332 |         if (OPAL_ERR_NOT_SUPPORTED == retval) {
333 |             opal_show_help("help-mpi-common-cuda.txt", "dlopen disabled", true);
334 |         } else {
335 |             opal_show_help("help-mpi-common-cuda.txt", "unknown ltdl error", true,
382 |             i = 0;
383 |             while (cudalibs[i] != NULL) {
384 |                 const char *str;
385 |                 libcuda_handle = opal_lt_dlopenadvise(cudalibs[i], advise);
386 |                 if (NULL == libcuda_handle) {
387 |                     str = opal_lt_dlerror();
417 |             i = 0;
418 |             while (cudalibs[i] != NULL) {
419 |                 const char *str;
420 |                 libcuda_handle = opal_lt_dlopen(cudalibs[i]);
421 |                 if (NULL == libcuda_handle) {
422 |                     str = opal_lt_dlerror();
446 | 
447 |     if (true != stage_one_init_passed) {
448 |         errmsg = opal_argv_join(errmsgs, '\n');
449 |         opal_show_help("help-mpi-common-cuda.txt", "dlopen failed", true,
450 |                        errmsg);
451 |     }
{% endraw %}

```
### ompi/mpi/java/c/mpi_MPI.c

```c

{% raw %}
88 |  */
89 | JNIEXPORT jboolean JNICALL Java_mpi_MPI_loadGlobalLibraries(JNIEnv *env, jclass obj)
90 | {
91 |     if (NULL == (mpilibhandle = dlopen("libmpi." OPAL_DYN_LIB_SUFFIX,
92 |                                        RTLD_NOW | RTLD_GLOBAL))) {
93 |         return JNI_FALSE;
{% endraw %}

```
### ompi/debuggers/dlopen_test.c

```c

{% raw %}
50 |         exit(77);
51 |     }
52 |     /* We know the .la file is there, so read it, looking for the
53 |        dlopen value.  If the dlopen value is '' (i.e., empty), then
54 |        there's nothing to dlopen (i.e., OMPI was built with
55 |        --enable-static --disable-shared, so return 77 to skip this
56 |        test.  This is horrible, but I can't think of a better way to
72 |     }
73 |     fclose(fp);
74 |     if (!happy) {
75 |         fprintf(stderr, "No test file to dlopen (perhaps --enable-static?); skipping\n");
76 |         exit(77);
77 |     }
82 |         return 1;
83 |     }
84 | 
85 |     printf("Trying to lt_dlopen file with dladvise_local: %s\n", filename);
86 | 
87 | #if OPAL_HAVE_LTDL_ADVISE
91 |         fprintf(stderr, "lt_dladvise failed to initialize properly\n");
92 |         return 1;
93 |     }
94 |     dlhandle = lt_dlopenadvise(filename, dladvise);
95 |     lt_dladvise_destroy(&dladvise);
96 | #else
97 |     dlhandle = lt_dlopenext(filename);
98 | #endif
99 |     if (NULL != dlhandle) {
112 |         fprintf(stderr, "lt_dladvise failed to initialize properly\n");
113 |         return 1;
114 |     }
115 |     dlhandle = lt_dlopenadvise(filename, dladvise);
116 |     lt_dladvise_destroy(&dladvise);
117 | #else
118 |     dlhandle = lt_dlopenext(filename);
119 | #endif
120 |     if (NULL != dlhandle) {
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c

```c

{% raw %}
89 |   "LIBC-MALLOC", /* func_group */
90 | 
91 |   /* Do not search the actual function pointers in an external LIBC, because
92 |      dlopen calls malloc which would result in an infinite recursion when
93 |      determining the actual function pointer of malloc. Using RTLD_NEXT
94 |      instead. */
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_libwrap.c

```c

{% raw %}
156 | #endif /* VT_MT || VT_HYB || VT_JAVA */
157 | 
158 |     (void)dlerror();
159 |     libc_handle = dlopen(SHLIBC_PATHNAME,
160 |                          RTLD_LAZY | RTLD_LOCAL
161 | #ifdef _AIX
170 | #ifdef VT_IOWRAP
171 |       /* do not use vt_error_msg() here to prevent possible recursive calls to
172 |          this function */
173 |       printf("VampirTrace: FATAL: dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n",
174 |              dlerror());
175 |       exit(EXIT_FAILURE);
176 | #else /* VT_IOWRAP */
177 |       vt_error_msg("dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n", dlerror());
178 | #endif /* VT_IOWRAP */
179 |     }
259 |       for( i = 0; i < (*lw)->attr->shlibs_num; i++ )
260 |       {
261 |         (void)dlerror();
262 |         (*lw)->handlev[i] = dlopen((*lw)->attr->shlibs[i],
263 |                                    RTLD_LAZY | RTLD_LOCAL
264 | #ifdef _AIX
269 |         {
270 |           error = 1;
271 |           snprintf(error_msg, sizeof(error_msg) - 1,
272 |                    "dlopen(\"%s\") failed: %s",
273 |                    (*lw)->attr->shlibs[i], dlerror());
274 |           break;
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_iowrap.c

```c

{% raw %}
117 | 
118 |     if( iolib_pathname != NULL ) {
119 |       (void)dlerror();
120 |       iolib_handle = dlopen( iolib_pathname,
121 |                              RTLD_LAZY | RTLD_LOCAL
122 | #ifdef _AIX
124 | #endif /* _AIX */
125 |                            );
126 |       if( !iolib_handle ) {
127 |         printf("VampirTrace: FATAL: dlopen(\"%s\") error: %s\n", iolib_pathname, dlerror());
128 |         exit(EXIT_FAILURE);
129 |       }
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c

```c

{% raw %}
209 |     sprintf(buffer, "lib%s.so", current_plugin);
210 | 
211 |     /* now dlopen it */
212 |     handle = dlopen(buffer, RTLD_NOW);
213 | 
214 |     /* if it is not valid */
{% endraw %}

```
### ompi/tools/ompi_info/param.c

```c

{% raw %}
589 |     opal_info_out("MPI parameter check", "option:mpi-param-check", paramcheck);
590 |     opal_info_out("Memory profiling support", "option:mem-profile", memprofile);
591 |     opal_info_out("Memory debugging support", "option:mem-debug", memdebug);
592 |     opal_info_out("libltdl support", "option:dlopen", want_libltdl);
593 |     opal_info_out("Heterogeneous support", "options:heterogeneous", heterogeneous);
594 | #if OMPI_RTE_ORTE
{% endraw %}

```
### oshmem/tools/oshmem_info/param.c

```c

{% raw %}
558 |     opal_info_out("MPI parameter check", "option:mpi-param-check", paramcheck);
559 |     opal_info_out("Memory profiling support", "option:mem-profile", memprofile);
560 |     opal_info_out("Memory debugging support", "option:mem-debug", memdebug);
561 |     opal_info_out("libltdl support", "option:dlopen", want_libltdl);
562 |     opal_info_out("Heterogeneous support", "options:heterogeneous", heterogeneous);
563 | #if OMPI_RTE_ORTE
{% endraw %}

```
### orte/tools/orte-info/param.c

```c

{% raw %}
425 |     orte_info_out("Internal debug support", "option:debug", debug);
426 |     orte_info_out("Memory profiling support", "option:mem-profile", memprofile);
427 |     orte_info_out("Memory debugging support", "option:mem-debug", memdebug);
428 |     orte_info_out("libltdl support", "option:dlopen", want_libltdl);
429 |     orte_info_out("Heterogeneous support", "options:heterogeneous", heterogeneous);
430 |     orte_info_out("orterun default --prefix", "orterun:prefix_by_default", 
{% endraw %}

```
### opal/mca/base/base.h

```c

{% raw %}
65 |  */
66 | OPAL_DECLSPEC extern char *mca_base_component_path;
67 | OPAL_DECLSPEC extern bool mca_base_component_show_load_errors;
68 | OPAL_DECLSPEC extern bool mca_base_component_disable_dlopen;
69 | OPAL_DECLSPEC extern char *mca_base_system_default_path;
70 | OPAL_DECLSPEC extern char *mca_base_user_default_path;
{% endraw %}

```
### opal/mca/base/mca_base_open.c

```c

{% raw %}
45 | char *mca_base_system_default_path = NULL;
46 | char *mca_base_user_default_path = NULL;
47 | bool mca_base_component_show_load_errors = true;
48 | bool mca_base_component_disable_dlopen = false;
49 | 
50 | static char *mca_base_verbose = NULL;
109 |     (void) mca_base_var_register_synonym(var_id, "opal", "mca", NULL, "component_show_load_errors",
110 |                                          MCA_BASE_VAR_SYN_FLAG_DEPRECATED);
111 | 
112 |     mca_base_component_disable_dlopen = false;
113 |     var_id = mca_base_var_register("opal", "mca", "base", "component_disable_dlopen",
114 |                                    "Whether to attempt to disable opening dynamic components or not",
115 |                                    MCA_BASE_VAR_TYPE_BOOL, NULL, 0, 0,
116 |                                    OPAL_INFO_LVL_9,
117 |                                    MCA_BASE_VAR_SCOPE_READONLY,
118 |                                    &mca_base_component_disable_dlopen);
119 |     (void) mca_base_var_register_synonym(var_id, "opal", "mca", NULL, "component_disable_dlopen",
120 |                                          MCA_BASE_VAR_SYN_FLAG_DEPRECATED);
121 | 
{% endraw %}

```
### opal/mca/base/mca_base_component_find.c

```c

{% raw %}
199 | 
200 | #if OPAL_WANT_LIBLTDL
201 |     /* Find any available dynamic components in the specified directory */
202 |     if (open_dso_components && !mca_base_component_disable_dlopen) {
203 |         find_dyn_components(directory, type,
204 |                             (const char**)requested_component_names,
573 |   /* Now try to load the component */
574 | 
575 | #if OPAL_HAVE_LTDL_ADVISE
576 |   component_handle = lt_dlopenadvise(target_file->filename, opal_mca_dladvise);
577 | #else
578 |   component_handle = lt_dlopenext(target_file->filename);
579 | #endif
580 |   if (NULL == component_handle) {
{% endraw %}

```
### opal/mca/hwloc/hwloc172/hwloc/src/components.c

```c

{% raw %}
83 |     basename++;
84 | 
85 |   /* dlopen and get the component structure */
86 |   handle = lt_dlopenext(filename);
87 |   if (!handle) {
88 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### opal/mca/memory/linux/hooks.c

```c

{% raw %}
860 | /* OMPI change: add a dummy function here that will be called by the
861 |    linux component open() function.  This dummy function is
862 |    necessary for when OMPI is built as --disable-shared
863 |    --enable-static --disable-dlopen, because we won't use
864 |    -Wl,--export-dynamic when building OMPI.  So we need to ensure that
865 |    not only that all the symbols in this file end up in libopen-pal.a,
{% endraw %}

```
### opal/mca/memory/linux/memory_linux_ptmalloc2.c

```c

{% raw %}
33 | /* Need to call a function in hooks.c to ensure that all those symbols
34 |    get pulled in at link time (e.g., when building libmpi.a, so that
35 |    those symbols end up in the final executable -- especially if we
36 |    use --disable-dlopen and therefore -Wl,--export-dynamic isn't used
37 |    when we build OMPI). */
38 | extern void opal_memory_linux_hook_pull(bool *want_hooks);
{% endraw %}

```
### opal/util/lt_interface.h

```c

{% raw %}
62 | OPAL_DECLSPEC int opal_lt_dladvise_preload(opal_lt_dladvise *advise);
63 | 
64 | /* Portable libltdl versions of the system dlopen() API. */
65 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename);
66 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename);
67 | OPAL_DECLSPEC void *opal_lt_dlsym(opal_lt_dlhandle handle, const char *name);
68 | OPAL_DECLSPEC const char *opal_lt_dlerror(void);
69 | OPAL_DECLSPEC int opal_lt_dlclose(opal_lt_dlhandle handle);
70 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenadvise(const char *filename,
71 |                                                     opal_lt_dladvise advise);
72 | 
{% endraw %}

```
### opal/util/lt_interface.c

```c

{% raw %}
163 | }
164 | 
165 | /* Portable libltdl versions of the system dlopen() API. */
166 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename) {
167 | #if OPAL_WANT_LIBLTDL
168 |     opal_lt_dlhandle handle;
170 |     if (NULL == handle) {
171 |         return NULL;
172 |     }
173 |     handle->dlhandle = lt_dlopen(filename);
174 |     if (NULL == handle->dlhandle) {
175 |         free(handle);
181 | #endif /* OPAL_WANT_LIBLTDL */
182 | }
183 | 
184 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename) {
185 | #if OPAL_WANT_LIBLTDL
186 |     opal_lt_dlhandle handle;
188 |     if (NULL == handle) {
189 |         return NULL;
190 |     }
191 |     handle->dlhandle = lt_dlopenext(filename);
192 |     if (NULL == handle->dlhandle) {
193 |         free(handle);
225 | #endif
226 | }
227 | 
228 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenadvise(const char *filename,
229 |                                                     opal_lt_dladvise advise) {
230 | #if OPAL_WANT_LIBLTDL && OPAL_HAVE_LTDL_ADVISE
233 |     if (NULL == handle) {
234 |         return NULL;
235 |     }
236 |     handle->dlhandle = lt_dlopenadvise(filename, advise->dladvise);
237 |     if (NULL == handle->dlhandle) {
238 |         free(handle);
{% endraw %}

```
### opal/libltdl/ltdl.h

```c

{% raw %}
73 | LT_SCOPE int	    lt_dladvise_preload	 (lt_dladvise *advise);
74 | 
75 | /* Portable libltdl versions of the system dlopen() API. */
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
79 | 					 lt_dladvise advise);
80 | LT_SCOPE void *	    lt_dlsym		(lt_dlhandle handle, const char *name);
130 | typedef	struct {
131 |   char *	filename;	/* file name */
132 |   char *	name;		/* module name */
133 |   int		ref_count;	/* number of times lt_dlopened minus
134 | 				   number of times lt_dlclosed. */
135 |   unsigned int	is_resident:1;	/* module can't be unloaded. */
{% endraw %}

```
### opal/libltdl/ltdl.c

```c

{% raw %}
129 | static  int     has_library_ext       (const char *filename);
130 | static	int	load_deplibs	      (lt_dlhandle handle,  char *deplibs);
131 | static	int	trim		      (char **dest, const char *str);
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
133 | 				       const char *filename, const char *ext,
134 | 				       lt_dladvise advise);
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
136 | 				       const char *filename,
137 | 				       lt_dladvise padvise,
172 | #ifdef HAVE_LIBDLLOADER
173 | /* This function is called to initialise each preloaded module loader,
174 |    and hook it into the list of loaders to be used when attempting to
175 |    dlopen an application module.  */
176 | static int
177 | loader_init_callback (lt_dlhandle handle)
239 |       errors += loader_init (get_vtable, 0);
240 | 
241 |       /* Now open all the preloaded module loaders, so the application
242 | 	 can use _them_ to lt_dlopen its own modules.  */
243 | #ifdef HAVE_LIBDLLOADER
244 |       if (!errors)
364 |    If the library is not successfully loaded, return non-zero.  Otherwise,
365 |    the dlhandle is stored at the address given in PHANDLE.  */
366 | static int
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
368 | 	       lt_dladvise advise, const lt_dlvtable *vtable)
369 | {
372 |   int		errors		= 0;
373 | 
374 | #ifdef LT_DEBUG_LOADERS
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
376 | 	   filename ? filename : "(null)",
377 | 	   vtable ? vtable->name : "(ALL)");
382 |   /* check whether the module was already opened */
383 |   for (;handle; handle = handle->next)
384 |     {
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
386 | 	  || (handle->info.filename && filename
387 | 	      && streq (handle->info.filename, filename)))
482 | 
483 | 
484 | static int
485 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
486 | 		      const char *dirname, const char *dlname,
487 | 		      lt_dladvise advise)
518 |      shuffled.  Otherwise, attempt to open FILENAME as a module.  */
519 |   if (prefix)
520 |     {
521 |       error += tryall_dlopen_module (handle, (const char *) 0,
522 | 				     prefix, filename, advise);
523 |     }
524 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
525 |     {
526 |       ++error;
536 | 	     lt_dladvise advise)
537 | {
538 |   /* Try to open the old library first; if it was dlpreopened,
539 |      we want the preopened version of it, even if a dlopenable
540 |      module is available.  */
541 |   if (old_name && tryall_dlopen (handle, old_name,
542 | 			  advise, lt_dlloader_find ("lt_preopen") ) == 0)
543 |     {
550 |       /* try to open the installed module */
551 |       if (installed && libdir)
552 | 	{
553 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
554 | 				    libdir, dlname, advise) == 0)
555 | 	    return 0;
558 |       /* try to open the not-installed module */
559 |       if (!installed)
560 | 	{
561 | 	  if (tryall_dlopen_module (handle, dir, objdir,
562 | 				    dlname, advise) == 0)
563 | 	    return 0;
565 | 
566 |       /* maybe it was moved to another directory */
567 |       {
568 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
569 | 					    dir, dlname, advise) == 0))
570 | 	    return 0;
783 | 
784 |   /* Try to dlopen the file, but do not continue searching in any
785 |      case.  */
786 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
787 |     *phandle = 0;
788 | 
942 | 
943 |       for (i = 0; i < depcount; ++i)
944 | 	{
945 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
946 | 	  if (cur->deplibs[j])
947 | 	    {
1148 | 
1149 | /* Try to open FILENAME as a module. */
1150 | static int
1151 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1152 | 	    lt_dladvise advise)
1153 | {
1165 |   assert (*phandle == 0);
1166 | 
1167 | #ifdef LT_DEBUG_LOADERS
1168 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1169 | 	   filename ? filename : "(null)",
1170 | 	   ext ? ext : "(null)");
1184 |       /* lt_dlclose()ing yourself is very bad!  Disallow it.  */
1185 |       newhandle->info.is_resident = 1;
1186 | 
1187 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1188 | 	{
1189 | 	  FREE (*phandle);
1303 | 	      sprintf (archive_name, "%s.%s", name, libext);
1304 | 	    }
1305 | 
1306 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1307 | 	    {
1308 | 	      goto register_handle;
1470 | #endif
1471 | 		   )))
1472 | 	{
1473 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1474 | 	    {
1475 | 	      newhandle = NULL;
1613 | 
1614 | /* Libtool-1.5.x interface for loading a new module named FILENAME.  */
1615 | lt_dlhandle
1616 | lt_dlopen (const char *filename)
1617 | {
1618 |   return lt_dlopenadvise (filename, NULL);
1619 | }
1620 | 
1624 |    and if a file is still not found try again with MODULE_EXT appended
1625 |    instead.  */
1626 | lt_dlhandle
1627 | lt_dlopenext (const char *filename)
1628 | {
1629 |   lt_dlhandle	handle	= 0;
1630 |   lt_dladvise	advise;
1631 | 
1632 |   if (!lt_dladvise_init (&advise) && !lt_dladvise_ext (&advise))
1633 |     handle = lt_dlopenadvise (filename, advise);
1634 | 
1635 |   lt_dladvise_destroy (&advise);
1638 | 
1639 | 
1640 | lt_dlhandle
1641 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1642 | {
1643 |   lt_dlhandle	handle	= 0;
1660 |     {
1661 |       /* Just incase we missed a code path in try_dlopen() that reports
1662 | 	 an error, but forgot to reset handle... */
1663 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1664 | 	return 0;
1665 | 
1669 |     {
1670 | 
1671 |       /* First try appending ARCHIVE_EXT.  */
1672 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1673 | 
1674 |       /* If we found FILENAME, stop searching -- whether we were able to
1682 | #if defined(LT_MODULE_EXT)
1683 |       /* Try appending SHLIB_EXT.   */
1684 |       LT__SETERRORSTR (saved_error);
1685 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1686 | 
1687 |       /* As before, if the file was found but loading failed, return now
1693 | #if defined(LT_SHARED_EXT)
1694 |       /* Try appending SHARED_EXT.   */
1695 |       LT__SETERRORSTR (saved_error);
1696 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1697 | 
1698 |       /* As before, if the file was found but loading failed, return now
1888 | 
1889 | /* Call FUNC for each unique extensionless file in SEARCH_PATH, along
1890 |    with DATA.  The filenames passed to FUNC would be suitable for
1891 |    passing to lt_dlopenext.  The extensions are stripped so that
1892 |    individual modules do not generate several entries (e.g. libfoo.la,
1893 |    libfoo.so, libfoo.so.1, libfoo.so.1.0.0).  If SEARCH_PATH is NULL,
1894 |    then the same directories that lt_dlopen would search are examined.  */
1895 | int
1896 | lt_dlforeachfile (const char *search_path,
{% endraw %}

```
### opal/libltdl/loaders/preopen.c

```c

{% raw %}
189 |      use the preopen functionality in libltdl at all -- so we never
190 |      need to see errors from this module.  Additionally, this module
191 |      is usually invoked last in the sequence when trying to
192 |      lt_dlopenadvise() a DSO -- so if there was a real error when
193 |      opening that DSO (e.g., a symbol not found), setting the
194 |      FILE_NOT_FOUND error here will mask the real error.
367 | 	      if ((symbol->address == 0)
368 | 		  && (strneq (symbol->name, "@PROGRAM@")))
369 | 		{
370 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
371 | 		  if (handle == 0)
372 | 		    {
{% endraw %}

```
### opal/libltdl/loaders/dlopen.c

```c

{% raw %}
66 | 
67 |   if (vtable && !vtable->name)
68 |     {
69 |       vtable->name		= "lt_dlopen";
70 | #if defined(DLSYM_USCORE)
71 |       vtable->sym_prefix	= "_";
190 | #endif
191 |     }
192 | 
193 |   module = dlopen (filename, module_flags);
194 | 
195 |   if (!module)
{% endraw %}

```
### opal/libltdl/libltdl/lt__private.h

```c

{% raw %}
108 | 
109 | struct lt__handle {
110 |   lt_dlhandle		next;
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
112 |   lt_dlinfo		info;		/* user visible fields */
113 |   int			depcount;	/* number of dependencies */
{% endraw %}

```
### opal/libltdl/libltdl/lt_error.h

```c

{% raw %}
42 |    expilicitely initialize the string terminator. */
43 | #define lt_dlerror_table						\
44 |     LT_ERROR(UNKNOWN,		    "unknown error\0")			\
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
46 |     LT_ERROR(INVALID_LOADER,	    "invalid loader\0")			\
47 |     LT_ERROR(INIT_LOADER,	    "loader initialization failed\0")	\
{% endraw %}

```
### test/support/components.c

```c

{% raw %}
31 | /*
32 |  * Local functions
33 |  */
34 | static bool try_dlopen(const char *dir, const char *fw, const char *comp,
35 |                        test_component_handle_t *comp_handle,
36 |                        test_component_sym_t *comp_symbol);
57 | 
58 |     /* Try to open */
59 | 
60 |     if (try_dlopen(".", framework, component, comp_handle, &sym) ||
61 |         try_dlopen(dir_concat(BUILDDIR, "src/mca"), framework, 
62 |                    component, comp_handle, &sym) ||
63 |         try_dlopen(dir_concat(SRCDIR, "src/mca"), framework, 
64 |                    component, comp_handle, &sym)) {
65 | 
124 | }
125 | 
126 | 
127 | static bool try_dlopen(const char *dir, const char *fw, const char *comp,
128 |                        test_component_handle_t *comp_handle,
129 |                        test_component_sym_t *comp_symbol)
144 | 
145 |     /* First, look for the component symbol statically */
146 | 
147 |     comp_handle->tch_handle = lt_dlopen(NULL);
148 |     if (NULL != comp_handle->tch_handle) {
149 |         comp_symbol->tcs_variable = 
162 |     if ('\0' != file_name[BUFSIZ - 1]) {
163 |         return false;
164 |     }
165 |     comp_handle->tch_handle = lt_dlopenext(file_name);
166 |     if (NULL != comp_handle->tch_handle) {
167 |         comp_symbol->tcs_variable = 
{% endraw %}

```