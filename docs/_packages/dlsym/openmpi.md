---
name: "openmpi"
layout: package
next_package: openssl
previous_package: openloops
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.7.5
48 / 7011 files match, 26 filtered matches.

 - [ompi/mca/btl/usnic/btl_usnic_ext.h](#ompimcabtlusnicbtl_usnic_exth)
 - [ompi/mca/common/cuda/common_cuda.c](#ompimcacommoncudacommon_cudac)
 - [ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c](#ompicontribvtvtvtlibvt_mallocwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_execwrap.c](#ompicontribvtvtvtlibvt_execwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_iowrap.h](#ompicontribvtvtvtlibvt_iowraph)
 - [ompi/contrib/vt/vt/vtlib/vt_libwrap.c](#ompicontribvtvtvtlibvt_libwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_comp_gnu.c](#ompicontribvtvtvtlibvt_comp_gnuc)
 - [ompi/contrib/vt/vt/vtlib/vt_iowrap.c](#ompicontribvtvtvtlibvt_iowrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c](#ompicontribvtvtvtlibvt_plugin_cntrc)
 - [opal/mca/base/mca_base_component_find.c](#opalmcabasemca_base_component_findc)
 - [opal/mca/crs/self/crs_self_module.c](#opalmcacrsselfcrs_self_modulec)
 - [opal/mca/hwloc/hwloc172/hwloc/src/components.c](#opalmcahwlochwloc172hwlocsrccomponentsc)
 - [opal/mca/memory/malloc_solaris/memory_malloc_solaris_component.c](#opalmcamemorymalloc_solarismemory_malloc_solaris_componentc)
 - [opal/mca/memory/linux/memory_linux_munmap.c](#opalmcamemorylinuxmemory_linux_munmapc)
 - [opal/util/lt_interface.h](#opalutillt_interfaceh)
 - [opal/util/lt_interface.c](#opalutillt_interfacec)
 - [opal/libltdl/ltdl.h](#opallibltdlltdlh)
 - [opal/libltdl/ltdl.c](#opallibltdlltdlc)
 - [opal/libltdl/loaders/dyld.c](#opallibltdlloadersdyldc)
 - [opal/libltdl/loaders/loadlibrary.c](#opallibltdlloadersloadlibraryc)
 - [opal/libltdl/loaders/shl_load.c](#opallibltdlloadersshl_loadc)
 - [opal/libltdl/loaders/load_add_on.c](#opallibltdlloadersload_add_onc)
 - [opal/libltdl/loaders/dld_link.c](#opallibltdlloadersdld_linkc)
 - [opal/libltdl/loaders/preopen.c](#opallibltdlloaderspreopenc)
 - [opal/libltdl/loaders/dlopen.c](#opallibltdlloadersdlopenc)
 - [test/support/components.c](#testsupportcomponentsc)

### ompi/mca/btl/usnic/btl_usnic_ext.h

```c

{% raw %}
15 | 
16 | #include "opal_stdint.h"
17 | 
18 | typedef void *(*ompi_btl_usnic_dlsym_fn_t)(const char *name);
19 | 
20 | typedef struct {
21 |     int lookup_version;
22 |     uint64_t magic;
23 |     ompi_btl_usnic_dlsym_fn_t lookup;
24 | } ompi_btl_usnic_query_port_table_t;
25 | 
{% endraw %}

```
### ompi/mca/common/cuda/common_cuda.c

```c

{% raw %}
53 | do {                                                                                 \
54 |     *(void **)(&cuFunc.funcName) = opal_lt_dlsym(libhandle, STRINGIFY(funcName));    \
55 |     if (NULL == cuFunc.funcName) {                                                   \
56 |         opal_show_help("help-mpi-common-cuda.txt", "dlsym failed", true,             \
57 |                        STRINGIFY(funcName), opal_lt_dlerror());                      \
58 |         return 1;                                                                    \
59 |     } else {                                                                         \
60 |         opal_output_verbose(15, mca_common_cuda_output,                              \
61 |                             "CUDA: successful dlsym of %s",                          \
62 |                             STRINGIFY(funcName));                                    \
63 |     }                                                                                \
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c

```c

{% raw %}
246 | 
247 |   /* once, get the actual function pointer
248 | 
249 |      NOTE: The dlsym function which is used to determine the actual function
250 |      pointer of calloc uses itself this function, which would ends up in an
251 |      infinite recursion.
252 |      In order to make it work we have to perform a quite dirty hack found on
253 |      http://blog.bigpixel.ro/2010/09/interposing-calloc-on-linux:
254 |      While we are trying to get the actual function pointer, we're returning
255 |      NULL for the memory which needs to be allocated by dlsym, in hope that
256 |      dlsym can handle this situation.
257 |      If this workaround causes any problems, just undefine the MALLOCWRAP_CALLOC
258 |      macro above to disable the calloc wrapper function completely. */
265 |     {
266 |       /* before trying to get the actual function pointer of calloc, set
267 |          an indicator in order to return NULL from the next calloc called from
268 |          dlsym */
269 |       getting_func_ptr = 1;
270 |       VTLibwrap_func_init(mallocwrap_lw, VT_LIBWRAP_FUNC_NAME, NULL, 0,
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_execwrap.c

```c

{% raw %}
153 |   /* get pointer to global environ variable of external LIBC */
154 |   void* libc_handle = vt_libwrap_get_libc_handle();
155 |   vt_libassert(libc_handle);
156 |   execwrap_libc_environ = (char***)dlsym(libc_handle, "environ");
157 |   vt_libassert(execwrap_libc_environ);
158 | #endif /* EXECWRAP_EXEC_AND_FORK && HAVE_DECL_ENVIRON */
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_iowrap.h

```c

{% raw %}
333 | #define VT_IOWRAP_INIT_FUNC(FUNC_NAME) \
334 | { \
335 | 	if (!iofunctions[FUNC_IDX(FUNC_NAME)].lib_func.p) { \
336 | 		vt_cntl_msg(DBG_INIT, "init_func: dlsym(" stringify(FUNC_NAME) ") --> "); \
337 | 		(void)dlerror(); \
338 | 		iofunctions[FUNC_IDX(FUNC_NAME)].lib_func.p = \
339 | 			dlsym( iolib_handle, stringify(FUNC_NAME) ); \
340 | 		vt_cntl_msg(DBG_INIT, "%p", iofunctions[FUNC_IDX(FUNC_NAME)].lib_func.p); \
341 | 		if (!iofunctions[FUNC_IDX(FUNC_NAME)].lib_func.p) \
480 | 		get_iolib_handle(); \
481 | 		(void)dlerror(); \
482 | 		iofunctions[FUNC_IDX(VT_IOWRAP_THISFUNCNAME)].lib_func.p = \
483 | 			dlsym( iolib_handle, stringify(VT_IOWRAP_THISFUNCNAME) ); \
484 | 		if (!iofunctions[FUNC_IDX(VT_IOWRAP_THISFUNCNAME)].lib_func.p) \
485 | 			symload_fail( stringify(VT_IOWRAP_THISFUNCNAME), dlerror() ); \
498 |                 get_iolib_handle(); \
499 |                 (void)dlerror(); \
500 | 		iofunctions[FUNC_IDX(VT_IOWRAP_THISFUNCNAME)].lib_func.p = \
501 | 			dlsym( iolib_handle, stringify(VT_IOWRAP_THISFUNCNAME) ); \
502 | 		if (!iofunctions[FUNC_IDX(VT_IOWRAP_THISFUNCNAME)].lib_func.p) \
503 | 			symload_fail( stringify(VT_IOWRAP_THISFUNCNAME), dlerror() ); \
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_libwrap.c

```c

{% raw %}
100 |     (defined(HAVE_DECL__ERRNO) && HAVE_DECL__ERRNO)
101 |     *(void**)(&libc_errno) = dlsym(libc_handle, libc_errno_sym);
102 | #else /* HAVE_DECL___ERRNO_LOCATION || HAVE_DECL__ERRNO */
103 |     libc_errno = (int*)dlsym(libc_handle, libc_errno_sym);
104 | #endif /* HAVE_DECL___ERRNO_LOCATION || HAVE_DECL__ERRNO */
105 |     if( libc_errno == NULL )
107 | #ifdef VT_IOWRAP
108 |       /* do not use vt_error_msg() here to prevent possible recursive calls to
109 |          this function */
110 |       printf("VampirTrace: FATAL: dlsym(\"%s\") failed: %s\n",
111 |              libc_errno_sym, dlerror());
112 |       exit(EXIT_FAILURE);
113 | #else /* VT_IOWRAP */
114 |       vt_error_msg("dlsym(\"%s\") failed: %s\n", libc_errno_sym, dlerror());
115 | #endif /* VT_IOWRAP */
116 |     }
362 |   if( funcptr && !(*funcptr) )
363 |   {
364 |     /* array for dlsym error messages */
365 |     char dlsym_errors[MAX_HANDLES][256];
366 | 
367 |     /* search all handles for function */
374 |       /* function not found ? */
375 |       if( !(*funcptr) )
376 |       {
377 |         char* dlsym_error_msg = dlerror();
378 | 
379 |         /* store dlsym error message, if available */
380 |         if( dlsym_error_msg )
381 |         {
382 |           strncpy(dlsym_errors[i], dlsym_error_msg, sizeof(dlsym_errors[i])-1);
383 |         }
384 | #if defined(HAVE_DECL_RTLD_NEXT) && HAVE_DECL_RTLD_NEXT
385 |         /* usually the dlsym error message for RTLD_NEXT may empty */
386 |         else if( i == lw->handlen - 1 )
387 |         {
388 |           snprintf(dlsym_errors[i], sizeof(dlsym_errors[i])-1,
389 |                    "RTLD_NEXT: symbol not found: %s", func);
390 |         }
391 | #endif /* HAVE_DECL_RTLD_NEXT */
392 |         else
393 |         {
394 |           strncpy(dlsym_errors[i], "unknown error", sizeof(dlsym_errors[i])-1);
395 |         }
396 |       }
400 |        function not found */
401 |     if( !(*funcptr) )
402 |     {
403 |       char* dlsym_errors_merged;
404 | 
405 |       dlsym_errors_merged =
406 |         (char*)calloc(lw->handlen * sizeof(dlsym_errors[0]), sizeof(char));
407 |       if( dlsym_errors_merged == NULL )
408 |         vt_error();
409 | 
410 |       for( i = 0; i < lw->handlen; i++ )
411 |       {
412 |         if( i > 0 )
413 |           strncat(dlsym_errors_merged, "\n", 255 - strlen(dlsym_errors_merged));
414 |         strncat(dlsym_errors_merged, dlsym_errors[i],
415 |                 255 - strlen(dlsym_errors_merged));
416 |       }
417 |       vt_error_msg("dlsym(\"%s\") failed:\n%s", func, dlsym_errors_merged);
418 |     }
419 |   }
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_comp_gnu.c

```c

{% raw %}
33 | #if (defined(HAVE_DL) && HAVE_DL) && (defined(HAVE_DECL_RTLD_DEFAULT) && HAVE_DECL_RTLD_DEFAULT)
34 | # include <dlfcn.h>
35 | # define GET_SO_FUNC_ADDR(func) \
36 |   GET_IA64_FUNC_ADDR(dlsym(RTLD_DEFAULT, (func)))
37 | #else /* HAVE_DL && HAVE_DECL_RTLD_DEFAULT */
38 | # define GET_SO_FUNC_ADDR(func) 0
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_iowrap.c

```c

{% raw %}
105 |  */
106 | static void symload_fail(const char *str, const char *errstr)
107 | {
108 |   printf("VampirTrace: FATAL: dlsym() error for symbol %s: %s\n",
109 | 	 str, errstr);
110 |   exit(EXIT_FAILURE);
161 | 		} lib_func;
162 | 		get_iolib_handle();
163 | 		(void)dlerror();
164 | 		lib_func.p = dlsym( iolib_handle, "fprintf" );
165 | 		libc_fprintf = (int (*)(FILE *, const char *, ...))lib_func.f;
166 | 		if( !libc_fprintf )
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c

```c

{% raw %}
219 |     }
220 | 
221 |     /* now get the info */
222 |     get_info.vp = dlsym(handle, "get_info");
223 |     if ((dl_lib_error = dlerror()) != NULL) {
224 |       vt_error_msg("Error getting info from plugin: %s\n", dl_lib_error);
{% endraw %}

```
### opal/mca/base/mca_base_component_find.c

```c

{% raw %}
630 |     return OPAL_ERR_OUT_OF_RESOURCE;
631 |   }
632 | 
633 |   component_struct = (mca_base_component_t*)lt_dlsym(component_handle, struct_name);
634 |   if (NULL == component_struct) {
635 |       /* Apparently lt_dlerror() sometimes returns NULL! */
{% endraw %}

```
### opal/mca/crs/self/crs_self_module.c

```c

{% raw %}
94 |                    opal_crs_self_destruct);
95 | 
96 | 
97 | typedef void (*opal_crs_self_dlsym_dummy_fn_t)(void);
98 | 
99 | /************************************
100 |  * Locally Global vars & functions :)
101 |  ************************************/
102 | static int crs_self_find_function(char *prefix, char *suffix,
103 |                                   opal_crs_self_dlsym_dummy_fn_t *fn_ptr);
104 | 
105 | static int self_update_snapshot_metadata(opal_crs_self_snapshot_t *snapshot);
165 | static int opal_crs_self_extract_callbacks(void)
166 | {
167 |     bool callback_matched = true;
168 |     opal_crs_self_dlsym_dummy_fn_t loc_fn;
169 | 
170 |     /*
550 |  * Local functions
551 |  ******************/
552 | static int crs_self_find_function(char *prefix, char *suffix,
553 |                                   opal_crs_self_dlsym_dummy_fn_t *fn_ptr) {
554 |     char *func_to_find = NULL;
555 | 
{% endraw %}

```
### opal/mca/hwloc/hwloc172/hwloc/src/components.c

```c

{% raw %}
91 |   }
92 |   componentsymbolname = malloc(6+strlen(basename)+10+1);
93 |   sprintf(componentsymbolname, "%s_component", basename);
94 |   component = lt_dlsym(handle, componentsymbolname);
95 |   if (!component) {
96 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### opal/mca/memory/malloc_solaris/memory_malloc_solaris_component.c

```c

{% raw %}
124 |             void *munmap_p;
125 |         } tmp;
126 | 
127 |         tmp.munmap_p = dlsym(RTLD_NEXT, "munmap");
128 |         realmunmap = tmp.munmap_fp;
129 |     }
{% endraw %}

```
### opal/mca/memory/linux/memory_linux_munmap.c

```c

{% raw %}
56 | /* three ways to call munmap.  Prefered is to just call syscall, so
57 |    that we can intercept both munmap and __munmap.  If that isn't
58 |    possible, try calling __munmap from munmap and let __munmap go.  If
59 |    that doesn't work, try dlsym */
60 | int opal_memory_linux_free_ptmalloc2_munmap(void *start, size_t length, 
61 |                                             int from_alloc)
80 |             void *munmap_p;
81 |         } tmp;
82 | 
83 |         tmp.munmap_p = dlsym(RTLD_NEXT, "munmap");
84 |         realmunmap = tmp.munmap_fp;
85 |     }
{% endraw %}

```
### opal/util/lt_interface.h

```c

{% raw %}
64 | /* Portable libltdl versions of the system dlopen() API. */
65 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename);
66 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename);
67 | OPAL_DECLSPEC void *opal_lt_dlsym(opal_lt_dlhandle handle, const char *name);
68 | OPAL_DECLSPEC const char *opal_lt_dlerror(void);
69 | OPAL_DECLSPEC int opal_lt_dlclose(opal_lt_dlhandle handle);
{% endraw %}

```
### opal/util/lt_interface.c

```c

{% raw %}
199 | #endif  /* OPAL_WANT_LIBLTDL */
200 | }
201 | 
202 | OPAL_DECLSPEC void *opal_lt_dlsym(opal_lt_dlhandle handle, const char *name) {
203 | #if OPAL_WANT_LIBLTDL
204 |     return lt_dlsym(handle->dlhandle, name);
205 | #else /* OPAL_WANT_LIBLTDL */
206 |     return NULL;
{% endraw %}

```
### opal/libltdl/ltdl.h

```c

{% raw %}
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
79 | 					 lt_dladvise advise);
80 | LT_SCOPE void *	    lt_dlsym		(lt_dlhandle handle, const char *name);
81 | LT_SCOPE const char *lt_dlerror		(void);
82 | LT_SCOPE int	    lt_dlclose		(lt_dlhandle handle);
91 | typedef struct {
92 |   const char *name;
93 |   void       *address;
94 | } lt_dlsymlist;
95 | 
96 | typedef int lt_dlpreload_callback_func (lt_dlhandle handle);
97 | 
98 | LT_SCOPE int	lt_dlpreload	     (const lt_dlsymlist *preloaded);
99 | LT_SCOPE int	lt_dlpreload_default (const lt_dlsymlist *preloaded);
100 | LT_SCOPE int	lt_dlpreload_open    (const char *originator,
101 | 				      lt_dlpreload_callback_func *func);
102 | 
103 | #define lt_preloaded_symbols	lt__PROGRAM__LTX_preloaded_symbols
104 | /* Ensure C linkage.  */
105 | extern LT_DLSYM_CONST lt_dlsymlist lt__PROGRAM__LTX_preloaded_symbols[];
106 | 
107 | #define LTDL_SET_PRELOADED_SYMBOLS() \
{% endraw %}

```
### opal/libltdl/ltdl.c

```c

{% raw %}
176 | static int
177 | loader_init_callback (lt_dlhandle handle)
178 | {
179 |   lt_get_vtable *vtable_func = (lt_get_vtable *) lt_dlsym (handle, "get_vtable");
180 |   return loader_init (vtable_func, 0);
181 | }
217 | LT_SCOPE const lt_dlvtable *	get_vtable (lt_user_data data);
218 | LT_END_C_DECLS
219 | #ifdef HAVE_LIBDLLOADER
220 | extern LT_DLSYM_CONST lt_dlsymlist preloaded_symbols[];
221 | #endif
222 | 
2002 | }
2003 | 
2004 | void *
2005 | lt_dlsym (lt_dlhandle place, const char *symbol)
2006 | {
2007 |   size_t lensym;
{% endraw %}

```
### opal/libltdl/loaders/dyld.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dyld_LTX_get_vtable
39 | 
{% endraw %}

```
### opal/libltdl/loaders/loadlibrary.c

```c

{% raw %}
38 | /* Use the preprocessor to rename non-static symbols to avoid namespace
39 |    collisions when the loader code is statically linked into libltdl.
40 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
41 |    be fetched from the preloaded symbol list by lt_dlsym():  */
42 | #define get_vtable	loadlibrary_LTX_get_vtable
43 | 
{% endraw %}

```
### opal/libltdl/loaders/shl_load.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	shl_load_LTX_get_vtable
39 | 
{% endraw %}

```
### opal/libltdl/loaders/load_add_on.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	load_add_on_LTX_get_vtable
39 | 
{% endraw %}

```
### opal/libltdl/loaders/dld_link.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dld_link_LTX_get_vtable
39 | 
{% endraw %}

```
### opal/libltdl/loaders/preopen.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	preopen_LTX_get_vtable
39 | 
96 | typedef struct symlist_chain
97 | {
98 |   struct symlist_chain *next;
99 |   const lt_dlsymlist   *symlist;
100 | } symlist_chain;
101 | 
102 | 
103 | static int add_symlist   (const lt_dlsymlist *symlist);
104 | static int free_symlists (void);
105 | 
107 | static symlist_chain	       *preloaded_symlists		= 0;
108 | 
109 | /* A symbol list preloaded before lt_init() was called.  */
110 | static const	lt_dlsymlist   *default_preloaded_symbols	= 0;
111 | 
112 | 
164 | 
165 |   for (lists = preloaded_symlists; lists; lists = lists->next)
166 |     {
167 |       const lt_dlsymlist *symbol;
168 |       for (symbol= lists->symlist; symbol->name; ++symbol)
169 | 	{
174 | 		 In this case we pretend that we never saw the module and
175 | 	         hope that some other loader will be able to load the module
176 | 	         and have access to its symbols */
177 | 	      const lt_dlsymlist *next_symbol = symbol +1;
178 | 	      if (next_symbol->address && next_symbol->name)
179 | 		{
224 | static void *
225 | vm_sym (lt_user_data LT__UNUSED loader_data, lt_module module, const char *name)
226 | {
227 |   lt_dlsymlist	       *symbol = (lt_dlsymlist*) module;
228 | 
229 |   symbol +=2;			/* Skip header (originator then libname). */
269 | 
270 | /* Add a new symbol list to the global chain.  */
271 | static int
272 | add_symlist (const lt_dlsymlist *symlist)
273 | {
274 |   symlist_chain *lists;
306 | 
307 | /* Save a default symbol list for later.  */
308 | int
309 | lt_dlpreload_default (const lt_dlsymlist *preloaded)
310 | {
311 |   default_preloaded_symbols = preloaded;
316 | /* Add a symbol list to the global chain, or with a NULL argument,
317 |    revert to just the default list.  */
318 | int
319 | lt_dlpreload (const lt_dlsymlist *preloaded)
320 | {
321 |   int errors = 0;
355 |       if ((originator && streq (list->symlist->name, originator))
356 |           || (!originator && streq (list->symlist->name, "@PROGRAM@")))
357 | 	{
358 | 	  const lt_dlsymlist *symbol;
359 | 	  unsigned int idx = 0;
360 | 
{% endraw %}

```
### opal/libltdl/loaders/dlopen.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dlopen_LTX_get_vtable
39 | 
223 | static void *
224 | vm_sym (lt_user_data LT__UNUSED loader_data, lt_module module, const char *name)
225 | {
226 |   void *address = dlsym (module, name);
227 | 
228 |   if (!address)
{% endraw %}

```
### test/support/components.c

```c

{% raw %}
90 | {
91 |     /* Use a union to avoid pesky compilers that complain [rightfully,
92 |        unfortunately] about converting (void*) to a function pointer
93 |        -- need to wait until the ltdl library has a lt_dlsymfunc()
94 |        function for a real fix... */
95 | 
102 |         return OPAL_ERR_BAD_PARAM;
103 |     }
104 | 
105 |     value.vvalue = lt_dlsym(handle->tch_handle, name);
106 |     sym->tcs_function = value.fvalue;
107 |     return OPAL_SUCCESS;
147 |     comp_handle->tch_handle = lt_dlopen(NULL);
148 |     if (NULL != comp_handle->tch_handle) {
149 |         comp_symbol->tcs_variable = 
150 |             lt_dlsym(comp_handle->tch_handle, component_name);
151 |         if (NULL != comp_symbol->tcs_variable) {
152 |             return true;
165 |     comp_handle->tch_handle = lt_dlopenext(file_name);
166 |     if (NULL != comp_handle->tch_handle) {
167 |         comp_symbol->tcs_variable = 
168 |             lt_dlsym(comp_handle->tch_handle, component_name);
169 |         if (NULL != comp_symbol->tcs_variable) {
170 |             return true;
{% endraw %}

```