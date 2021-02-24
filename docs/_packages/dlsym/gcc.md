---
name: "gcc"
layout: package
next_package: None
previous_package: cdo
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 6.1.0
49 / 94447 files match, 27 filtered matches.

 - [gcc/plugin.c](#gccpluginc)
 - [gcc/jit/jit-result.c](#gccjitjit-resultc)
 - [gcc/testsuite/c-c++-common/tsan/tsan_barrier.h](#gcctestsuitec-c++-commontsantsan_barrierh)
 - [gcc/testsuite/g++.dg/tsan/tsan_barrier.h](#gcctestsuiteg++dgtsantsan_barrierh)
 - [gcc/testsuite/jit.dg/verify-dynamic-library.c](#gcctestsuitejitdgverify-dynamic-libraryc)
 - [libjava/prims.cc](#libjavaprimscc)
 - [libjava/classpath/native/jni/midi-dssi/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.c](#libjavaclasspathnativejnimidi-dssignu_javax_sound_midi_dssi_dssimidideviceproviderc)
 - [libjava/classpath/tools/toolwrapper.c](#libjavaclasspathtoolstoolwrapperc)
 - [libjava/libltdl/ltdl.h](#libjavalibltdlltdlh)
 - [libjava/libltdl/ltdl.c](#libjavalibltdlltdlc)
 - [libjava/java/lang/natRuntime.cc](#libjavajavalangnatruntimecc)
 - [libjava/java/net/natVMURLConnection.cc](#libjavajavanetnatvmurlconnectioncc)
 - [libstdc++-v3/testsuite/ext/mt_allocator/22309_thread.cc](#libstdc++-v3testsuiteextmt_allocator22309_threadcc)
 - [libstdc++-v3/testsuite/18_support/bad_exception/23591_thread-1.c](#libstdc++-v3testsuite18_supportbad_exception23591_thread-1c)
 - [boehm-gc/dyn_load.c](#boehm-gcdyn_loadc)
 - [libvtv/testsuite/other-tests/dlopen.cc](#libvtvtestsuiteother-testsdlopencc)
 - [libvtv/testsuite/other-tests/dlopen_mt.cc](#libvtvtestsuiteother-testsdlopen_mtcc)
 - [libsanitizer/asan/asan_linux.cc](#libsanitizerasanasan_linuxcc)
 - [libsanitizer/asan/asan_malloc_linux.cc](#libsanitizerasanasan_malloc_linuxcc)
 - [libsanitizer/sanitizer_common/sanitizer_unwind_linux_libcdep.cc](#libsanitizersanitizer_commonsanitizer_unwind_linux_libcdepcc)
 - [libsanitizer/sanitizer_common/sanitizer_linux_libcdep.cc](#libsanitizersanitizer_commonsanitizer_linux_libcdepcc)
 - [libsanitizer/lsan/lsan_interceptors.cc](#libsanitizerlsanlsan_interceptorscc)
 - [libgcc/config/darwin-crt3.c](#libgccconfigdarwin-crt3c)
 - [lto-plugin/lto-symtab.c](#lto-pluginlto-symtabc)
 - [libgomp/target.c](#libgomptargetc)
 - [libgomp/plugin/plugin-hsa.c](#libgomppluginplugin-hsac)
 - [libgomp/testsuite/libgomp.c/affinity-1.c](#libgomptestsuitelibgompcaffinity-1c)

### gcc/plugin.c

```c

{% raw %}
584 |   dlerror ();
585 | 
586 |   /* Check the plugin license.  */
587 |   if (dlsym (dl_handle, str_license) == NULL)
588 |     fatal_error (input_location,
589 | 		 "plugin %s is not licensed under a GPL-compatible license\n"
590 | 		 "%s", plugin->full_name, dlerror ());
591 | 
592 |   PTR_UNION_AS_VOID_PTR (plugin_init_union) =
593 |       dlsym (dl_handle, str_plugin_init_func_name);
594 |   plugin_init = PTR_UNION_AS_CAST_PTR (plugin_init_union);
595 | 
{% endraw %}

```
### gcc/jit/jit-result.c

```c

{% raw %}
59 | }
60 | 
61 | /* Attempt to locate the given function by name within the
62 |    playback::result, using dlsym.
63 | 
64 |    Implements the post-error-checking part of
76 |   /* Clear any existing error.  */
77 |   dlerror ();
78 | 
79 |   code = dlsym (m_dso_handle, funcname);
80 | 
81 |   if ((error = dlerror()) != NULL)  {
86 | }
87 | 
88 | /* Attempt to locate the given global by name within the
89 |    playback::result, using dlsym.
90 | 
91 |    Implements the post-error-checking part of
103 |   /* Clear any existing error.  */
104 |   dlerror ();
105 | 
106 |   global = dlsym (m_dso_handle, name);
107 | 
108 |   if ((error = dlerror()) != NULL)  {
{% endraw %}

```
### gcc/testsuite/c-c++-common/tsan/tsan_barrier.h

```c

{% raw %}
8 | {
9 |   void *h = dlopen ("libpthread.so.0", RTLD_LAZY);
10 |   barrier_wait = (__typeof (pthread_barrier_wait) *)
11 | 	 	 dlsym (h, "pthread_barrier_wait");
12 |   pthread_barrier_init (barrier, NULL, count);
13 | }
{% endraw %}

```
### gcc/testsuite/g++.dg/tsan/tsan_barrier.h

```c

{% raw %}
8 | {
9 |   void *h = dlopen ("libpthread.so.0", RTLD_LAZY);
10 |   barrier_wait = (__typeof (pthread_barrier_wait) *)
11 | 	 	 dlsym (h, "pthread_barrier_wait");
12 |   pthread_barrier_init (barrier, NULL, count);
13 | }
{% endraw %}

```
### gcc/testsuite/jit.dg/verify-dynamic-library.c

```c

{% raw %}
27 | 
28 |   if ((error = dlerror()) != NULL)
29 |     {
30 |       fprintf (stderr, "dlsym failed: %s\n", error);
31 |       exit (2);
32 |     }
{% endraw %}

```
### libjava/prims.cc

```cpp

{% raw %}
1408 |   if (lib)
1409 |     {
1410 |       jvmti_agentonload 
1411 |         = (jvmti_agent_onload_func *) lt_dlsym (lib, "Agent_OnLoad");
1412 |  
1413 |       if (!jvmti_agentonload)
1422 |       else
1423 |         {
1424 |           jvmti_agentonunload
1425 |             = (jvmti_agent_onunload_func *) lt_dlsym (lib, "Agent_OnUnload");
1426 | 	   
1427 |           return 0;
{% endraw %}

```
### libjava/classpath/native/jni/midi-dssi/gnu_javax_sound_midi_dssi_DSSIMidiDeviceProvider.c

```c

{% raw %}
66 |   if (handle == 0)
67 |     goto done;
68 |   
69 |   fn = (DSSI_Descriptor_Function) dlsym(handle, "dssi_descriptor");
70 |   
71 |   if (fn == 0)
{% endraw %}

```
### libjava/classpath/tools/toolwrapper.c

```c

{% raw %}
177 |       fprintf (stderr, TOOLNAME ": failed to open " LIBJVM "\n");
178 |       goto destroy;
179 |     }
180 |   libjvm_create = (createVM*) lt_dlsym (libjvm_handle, "JNI_CreateJavaVM");
181 |   if (!libjvm_create)
182 |     {
{% endraw %}

```
### libjava/libltdl/ltdl.h

```c

{% raw %}
169 | /* Portable libltdl versions of the system dlopen() API. */
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
172 | LT_SCOPE	lt_ptr	    lt_dlsym		LT_PARAMS((lt_dlhandle handle,
173 | 						     const char *name));
174 | LT_SCOPE	const char *lt_dlerror		LT_PARAMS((void));
220 | typedef struct {
221 |   const char *name;
222 |   lt_ptr      address;
223 | } lt_dlsymlist;
224 | 
225 | LT_SCOPE	int	lt_dlpreload	LT_PARAMS((const lt_dlsymlist *preloaded));
226 | LT_SCOPE	int	lt_dlpreload_default
227 | 				LT_PARAMS((const lt_dlsymlist *preloaded));
228 | 
229 | #define LTDL_SET_PRELOADED_SYMBOLS() 		LT_STMT_START{	\
230 | 	extern const lt_dlsymlist lt_preloaded_symbols[];		\
231 | 	lt_dlpreload_default(lt_preloaded_symbols);			\
232 | 						}LT_STMT_END
{% endraw %}

```
### libjava/libltdl/ltdl.c

```c

{% raw %}
1142 |      lt_module module;
1143 |      const char *symbol;
1144 | {
1145 |   lt_ptr address = dlsym (module, symbol);
1146 | 
1147 |   if (!address)
1940 | 
1941 | /* emulate dynamic linking using preloaded_symbols */
1942 | 
1943 | typedef struct lt_dlsymlists_t
1944 | {
1945 |   struct lt_dlsymlists_t       *next;
1946 |   const lt_dlsymlist	       *syms;
1947 | } lt_dlsymlists_t;
1948 | 
1949 | static	const lt_dlsymlist     *default_preloaded_symbols	= 0;
1950 | static	lt_dlsymlists_t	       *preloaded_symbols		= 0;
1951 | 
1952 | static int
1971 | static int
1972 | presym_free_symlists ()
1973 | {
1974 |   lt_dlsymlists_t *lists;
1975 | 
1976 |   LT_DLMUTEX_LOCK ();
1978 |   lists = preloaded_symbols;
1979 |   while (lists)
1980 |     {
1981 |       lt_dlsymlists_t	*tmp = lists;
1982 | 
1983 |       lists = lists->next;
2000 | 
2001 | static int
2002 | presym_add_symlist (preloaded)
2003 |      const lt_dlsymlist *preloaded;
2004 | {
2005 |   lt_dlsymlists_t *tmp;
2006 |   lt_dlsymlists_t *lists;
2007 |   int		   errors   = 0;
2008 | 
2018 |       lists = lists->next;
2019 |     }
2020 | 
2021 |   tmp = LT_EMALLOC (lt_dlsymlists_t, 1);
2022 |   if (tmp)
2023 |     {
2024 |       memset (tmp, 0, sizeof(lt_dlsymlists_t));
2025 |       tmp->syms = preloaded;
2026 |       tmp->next = preloaded_symbols;
2041 |      lt_user_data loader_data;
2042 |      const char *filename;
2043 | {
2044 |   lt_dlsymlists_t *lists;
2045 |   lt_module	   module = (lt_module) 0;
2046 | 
2064 | 
2065 |   while (lists)
2066 |     {
2067 |       const lt_dlsymlist *syms = lists->syms;
2068 | 
2069 |       while (syms->name)
2102 |      lt_module module;
2103 |      const char *symbol;
2104 | {
2105 |   lt_dlsymlist *syms = (lt_dlsymlist*) module;
2106 | 
2107 |   ++syms;
2255 | 
2256 | int
2257 | lt_dlpreload (preloaded)
2258 |      const lt_dlsymlist *preloaded;
2259 | {
2260 |   int errors = 0;
2280 | 
2281 | int
2282 | lt_dlpreload_default (preloaded)
2283 |      const lt_dlsymlist *preloaded;
2284 | {
2285 |   LT_DLMUTEX_LOCK ();
3847 | }
3848 | 
3849 | lt_ptr
3850 | lt_dlsym (handle, symbol)
3851 |      lt_dlhandle handle;
3852 |      const char *symbol;
{% endraw %}

```
### libjava/java/lang/natRuntime.cc

```cpp

{% raw %}
54 | 
55 | /* FIXME: we don't always need this.  The next libtool will let us use
56 |    AC_LTDL_PREOPEN to see if we do.  */
57 | extern const lt_dlsymlist lt_preloaded_symbols[1] = { { 0, 0 } };
58 | 
59 | struct lookup_data
66 | find_symbol (lt_dlhandle handle, lt_ptr data)
67 | {
68 |   lookup_data *ld = (lookup_data *) data;
69 |   ld->result = lt_dlsym (handle, ld->symname);
70 |   return ld->result != NULL;
71 | }
192 |   const char **name = onload_names;
193 |   while (*name != NULL)
194 |     {
195 |       onload = lt_dlsym (h, *name);
196 |       if (onload != NULL)
197 | 	break;
{% endraw %}

```
### libjava/java/net/natVMURLConnection.cc

```cpp

{% raw %}
35 |   if (!handle)
36 |     return;
37 | 
38 |   p_magic_open = (typeof (p_magic_open))lt_dlsym(handle, "magic_open");
39 |   if (p_magic_open == NULL)
40 |     return;
41 |   p_magic_buffer = (typeof (p_magic_buffer))lt_dlsym(handle, "magic_buffer");
42 |   if (p_magic_buffer == NULL)
43 |     return;
44 |   p_magic_close = (typeof (p_magic_close))lt_dlsym(handle, "magic_close");
45 |   if (p_magic_close == NULL)
46 |     return;
47 |   p_magic_load = (typeof (p_magic_load))lt_dlsym(handle, "magic_load");
48 |   if (p_magic_load == NULL)
49 |     return;
{% endraw %}

```
### libstdc++-v3/testsuite/ext/mt_allocator/22309_thread.cc

```cpp

{% raw %}
42 | }
43 | 
44 | void
45 | check_dlsym(void*& h)
46 | {
47 |   dlerror();
48 | 
49 |   typedef void (*function_type) (void);
50 |   function_type fn;
51 |   fn = reinterpret_cast<function_type>(dlsym(h, "try_allocation"));
52 | 
53 |   try 
82 | {
83 |   void* h;
84 |   check_dlopen(h);
85 |   check_dlsym(h);
86 |   check_dlclose(h);
87 |   return 0;
{% endraw %}

```
### libstdc++-v3/testsuite/18_support/bad_exception/23591_thread-1.c

```c

{% raw %}
36 |       printf("dlopen failed: %s\n", strerror(errno));
37 |       return 0;
38 |     }
39 |   cb = (function_type) dlsym(lib, "try_throw_exception");
40 |   if (!cb)
41 |     {
42 |       printf("dlsym failed: %s\n", strerror(errno));
43 |       return 0;
44 |     }
{% endraw %}

```
### boehm-gc/dyn_load.c

```c

{% raw %}
167 | 	/* at program startup.						*/
168 | 	if( dynStructureAddr == 0 ) {
169 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
170 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
171 | 		}
172 | #   else
{% endraw %}

```
### libvtv/testsuite/other-tests/dlopen.cc

```cpp

{% raw %}
24 |       fprintf(stderr, "dlopen %s error: %s\n", so_name, dlerror());
25 |       exit(1);
26 |     }
27 |   voidfn so_entry = (voidfn)dlsym(dlhandle, "so_entry_0");
28 |   if (!so_entry)
29 |     {
30 |       fprintf(stderr, "dlopen %s dlsym error: %s\n", so_name, dlerror());
31 |       exit(2);
32 |     }
{% endraw %}

```
### libvtv/testsuite/other-tests/dlopen_mt.cc

```cpp

{% raw %}
35 |     }
36 |   char so_entry [sizeof("so_entry_xxx")];
37 |   sprintf(so_entry, "so_entry_%d", so_num);
38 |   voidfn so_entry_fn = (voidfn)dlsym(dlhandle, so_entry);
39 |   if (!so_entry_fn)
40 |     {
41 |       fprintf(stderr, "so:%s dlsym error: %s\n", so_name, dlerror());
42 |       exit(2);
43 |     }
{% endraw %}

```
### libsanitizer/asan/asan_linux.cc

```cpp

{% raw %}
168 | #endif
169 | 
170 | void *AsanDlSymNext(const char *sym) {
171 |   return dlsym(RTLD_NEXT, sym);
172 | }
173 | 
{% endraw %}

```
### libsanitizer/asan/asan_malloc_linux.cc

```cpp

{% raw %}
42 |   if (UNLIKELY(!asan_inited)) {
43 |     // Hack: dlsym calls calloc before REAL(calloc) is retrieved from dlsym.
44 |     const uptr kCallocPoolSize = 1024;
45 |     static uptr calloc_memory_for_dlsym[kCallocPoolSize];
46 |     static uptr allocated;
47 |     uptr size_in_words = ((nmemb * size) + kWordSize - 1) / kWordSize;
48 |     void *mem = (void*)&calloc_memory_for_dlsym[allocated];
49 |     allocated += size_in_words;
50 |     CHECK(allocated < kCallocPoolSize);
{% endraw %}

```
### libsanitizer/sanitizer_common/sanitizer_unwind_linux_libcdep.cc

```cpp

{% raw %}
53 |     return;
54 |   }
55 |   acquire_my_map_info_list =
56 |       (acquire_my_map_info_list_func)(uptr)dlsym(p, "acquire_my_map_info_list");
57 |   release_my_map_info_list =
58 |       (release_my_map_info_list_func)(uptr)dlsym(p, "release_my_map_info_list");
59 |   unwind_backtrace_signal_arch = (unwind_backtrace_signal_arch_func)(uptr)dlsym(
60 |       p, "unwind_backtrace_signal_arch");
61 |   if (!acquire_my_map_info_list || !release_my_map_info_list ||
{% endraw %}

```
### libsanitizer/sanitizer_common/sanitizer_linux_libcdep.cc

```cpp

{% raw %}
121 | 
122 | #if !SANITIZER_GO
123 | bool SetEnv(const char *name, const char *value) {
124 |   void *f = dlsym(RTLD_NEXT, "setenv");
125 |   if (!f)
126 |     return false;
187 |   const size_t kStackAlign = 16;
188 |   typedef void (*get_tls_func)(size_t*, size_t*) DL_INTERNAL_FUNCTION;
189 |   get_tls_func get_tls;
190 |   void *get_tls_static_info_ptr = dlsym(RTLD_NEXT, "_dl_get_tls_static_info");
191 |   CHECK_EQ(sizeof(get_tls), sizeof(get_tls_static_info_ptr));
192 |   internal_memcpy(&get_tls, &get_tls_static_info_ptr,
{% endraw %}

```
### libsanitizer/lsan/lsan_interceptors.cc

```cpp

{% raw %}
60 |   if (lsan_init_is_running) {
61 |     // Hack: dlsym calls calloc before REAL(calloc) is retrieved from dlsym.
62 |     const uptr kCallocPoolSize = 1024;
63 |     static uptr calloc_memory_for_dlsym[kCallocPoolSize];
64 |     static uptr allocated;
65 |     uptr size_in_words = ((nmemb * size) + kWordSize - 1) / kWordSize;
66 |     void *mem = (void*)&calloc_memory_for_dlsym[allocated];
67 |     allocated += size_in_words;
68 |     CHECK(allocated < kCallocPoolSize);
{% endraw %}

```
### libgcc/config/darwin-crt3.c

```c

{% raw %}
285 | 	{
286 | 	  int chk_result;
287 | 
288 | 	  r->cxa_atexit_f = (cxa_atexit_p)dlsym (handle, "__cxa_atexit");
289 | 	  r->cxa_finalize_f = (cxa_finalize_p)dlsym (handle, "__cxa_finalize");
290 | 	  if (! r->cxa_atexit_f || ! r->cxa_finalize_f)
291 | 	    goto error;
297 | 	    r->atexit_status = atexit_status_broken;
298 | 	  else
299 | 	    {
300 | 	      r->atexit_f = (atexit_p)dlsym (handle, "atexit");
301 | 	      if (! r->atexit_f)
302 | 		goto error;
{% endraw %}

```
### lto-plugin/lto-symtab.c

```c

{% raw %}
139 |   plugin_handle = dlopen (name, RTLD_LAZY);
140 | 
141 |   assert (plugin_handle != NULL);
142 |   onload = dlsym (plugin_handle, "onload");
143 |   assert (onload);
144 |   onload (tv);
{% endraw %}

```
### libgomp/target.c

```c

{% raw %}
2357 |      their handlers.  None of the symbols can legitimately be NULL,
2358 |      so we don't need to check dlerror all the time.  */
2359 | #define DLSYM(f)							\
2360 |   if (!(device->f##_func = dlsym (plugin_handle, "GOMP_OFFLOAD_" #f)))	\
2361 |     goto dl_fail
2362 |   /* Similar, but missing functions are not an error.  Return false if
2363 |      failed, true otherwise.  */
2364 | #define DLSYM_OPT(f, n)							\
2365 |   ((device->f##_func = dlsym (plugin_handle, "GOMP_OFFLOAD_" #n))	\
2366 |    || (last_missing = #n, 0))
2367 | 
{% endraw %}

```
### libgomp/plugin/plugin-hsa.c

```c

{% raw %}
687 |   struct brig_library_info *library = NULL;
688 | 
689 |   void *f = dlopen (file_name, RTLD_NOW);
690 |   void *start = dlsym (f, "__brig_start");
691 |   void *end = dlsym (f, "__brig_end");
692 | 
693 |   if (start == NULL || end == NULL)
{% endraw %}

```
### libgomp/testsuite/libgomp.c/affinity-1.c

```c

{% raw %}
80 |   if (orig_getaffinity_np == NULL)
81 |     {
82 |       orig_getaffinity_np = (int (*) (pthread_t, size_t, cpu_set_t *))
83 | 			    dlsym (RTLD_NEXT, "pthread_getaffinity_np");
84 |       if (orig_getaffinity_np == NULL)
85 | 	exit (0);
{% endraw %}

```