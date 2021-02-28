---
name: "julia"
layout: package
next_package: mariadb
previous_package: amgx
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.5.2
31 / 1327 files match, 9 filtered matches.

 - [src/staticdata.c](#srcstaticdatac)
 - [src/sys.c](#srcsysc)
 - [src/dlload.c](#srcdlloadc)
 - [src/runtime_intrinsics.c](#srcruntime_intrinsicsc)
 - [src/init.c](#srcinitc)
 - [src/julia.h](#srcjuliah)
 - [src/flisp/print.c](#srcflispprintc)
 - [src/flisp/flisp.h](#srcflispflisph)
 - [src/flisp/cvalues.c](#srcflispcvaluesc)

### src/staticdata.c

```c

{% raw %}
211 |     int imaging_mode = jl_generating_output() && !jl_options.incremental;
212 |     // in --build mode only use sysimg data, not precompiled native code
213 |     if (!imaging_mode && jl_options.use_sysimage_native_code==JL_OPTIONS_USE_SYSIMAGE_NATIVE_CODE_YES) {
214 |         jl_dlsym(jl_sysimg_handle, "jl_sysimg_gvars_base", (void **)&sysimg_gvars_base, 1);
215 |         jl_dlsym(jl_sysimg_handle, "jl_sysimg_gvars_offsets", (void **)&sysimg_gvars_offsets, 1);
216 |         sysimg_gvars_offsets += 1;
217 |         assert(sysimg_fptrs.base);
218 |         uintptr_t *tls_getter_slot;
219 |         jl_dlsym(jl_sysimg_handle, "jl_get_ptls_states_slot", (void **)&tls_getter_slot, 1);
220 |         *tls_getter_slot = (uintptr_t)jl_get_ptls_states_getter();
221 |         size_t *tls_offset_idx;
222 |         jl_dlsym(jl_sysimg_handle, "jl_tls_offset", (void **)&tls_offset_idx, 1);
223 |         *tls_offset_idx = (uintptr_t)(jl_tls_offset == -1 ? 0 : jl_tls_offset);
224 | 
238 |         memset(&sysimg_fptrs, 0, sizeof(sysimg_fptrs));
239 |     }
240 |     const char *sysimg_data;
241 |     jl_dlsym(jl_sysimg_handle, "jl_system_image_data", (void **)&sysimg_data, 1);
242 |     size_t *plen;
243 |     jl_dlsym(jl_sysimg_handle, "jl_system_image_size", (void **)&plen, 1);
244 |     jl_restore_system_image_data(sysimg_data, *plen);
245 | }
1494 | JL_DLLEXPORT void jl_set_sysimg_so(void *handle)
1495 | {
1496 |     void* *jl_RTLD_DEFAULT_handle_pointer;
1497 |     int symbol_found = jl_dlsym(handle, "jl_RTLD_DEFAULT_handle_pointer", (void **)&jl_RTLD_DEFAULT_handle_pointer, 0);
1498 |     if (!symbol_found || (void*)&jl_RTLD_DEFAULT_handle != *jl_RTLD_DEFAULT_handle_pointer)
1499 |         jl_error("System image file failed consistency check: maybe opened the wrong version?");
{% endraw %}

```
### src/sys.c

```c

{% raw %}
378 | #elif defined(_OS_WINDOWS_)
379 |     //Try to get WIN7 API method
380 |     GAPC gapc;
381 |     if (jl_dlsym(jl_kernel32_handle, "GetActiveProcessorCount", (void **)&gapc, 0)) {
382 |         return gapc(ALL_PROCESSOR_GROUPS);
383 |     }
{% endraw %}

```
### src/dlload.c

```c

{% raw %}
237 |     return handle;
238 | }
239 | 
240 | JL_DLLEXPORT int jl_dlsym(void *handle, const char *symbol, void ** value, int throw_err)
241 | {
242 |     int symbol_found = 0;
275 | const char *jl_dlfind_win32(const char *f_name)
276 | {
277 |     void * dummy;
278 |     if (jl_dlsym(jl_exe_handle, f_name, &dummy, 0))
279 |         return JL_EXE_LIBNAME;
280 |     if (jl_dlsym(jl_dl_handle, f_name, &dummy, 0))
281 |         return JL_DL_LIBNAME;
282 |     if (jl_dlsym(jl_kernel32_handle, f_name, &dummy, 0))
283 |         return "kernel32";
284 |     if (jl_dlsym(jl_ntdll_handle, f_name, &dummy, 0))
285 |         return "ntdll";
286 |     if (jl_dlsym(jl_crtdll_handle, f_name, &dummy, 0))
287 | #if defined(_MSC_VER)
288 | #if _MSC_VER == 1800
293 | #else
294 |         return "msvcrt";
295 | #endif
296 |     if (jl_dlsym(jl_winsock_handle, f_name, &dummy, 0))
297 |         return "ws2_32";
298 |     // additional common libraries (libc?) could be added here, but in general,
{% endraw %}

```
### src/runtime_intrinsics.c

```c

{% raw %}
121 | #endif
122 | 
123 |     void *ptr;
124 |     jl_dlsym(jl_get_library(f_lib), f_name, &ptr, 1);
125 |     jl_value_t *jv = jl_gc_alloc_1w();
126 |     jl_set_typeof(jv, rt);
{% endraw %}

```
### src/init.c

```c

{% raw %}
667 |     needsSymRefreshModuleList = 0;
668 |     HMODULE jl_dbghelp = (HMODULE) jl_dlopen("dbghelp.dll", 0);
669 |     if (jl_dbghelp)
670 |         jl_dlsym(jl_dbghelp, "SymRefreshModuleList", (void **)&hSymRefreshModuleList, 1);
671 | #else
672 |     jl_exe_handle = jl_dlopen(NULL, JL_RTLD_NOW);
{% endraw %}

```
### src/julia.h

```c

{% raw %}
1636 | JL_DLLEXPORT jl_uv_libhandle jl_load_dynamic_library(const char *fname, unsigned flags, int throw_err);
1637 | JL_DLLEXPORT jl_uv_libhandle jl_dlopen(const char *filename, unsigned flags);
1638 | JL_DLLEXPORT int jl_dlclose(jl_uv_libhandle handle);
1639 | JL_DLLEXPORT int jl_dlsym(jl_uv_libhandle handle, const char *symbol, void ** value, int throw_err);
1640 | 
1641 | // compiler
{% endraw %}

```
### src/flisp/print.c

```c

{% raw %}
641 |             if (init == 0) {
642 | #if defined(RTLD_SELF)
643 |                 jl_static_print = (size_t (*)(ios_t*, void*))
644 |                     (uintptr_t)dlsym(RTLD_SELF, "jl_static_show");
645 | #elif defined(RTLD_DEFAULT)
646 |                 jl_static_print = (size_t (*)(ios_t*, void*))
647 |                     (uintptr_t)dlsym(RTLD_DEFAULT, "jl_static_show");
648 | #elif defined(_OS_WINDOWS_)
649 |                 HMODULE handle;
745 | 
746 |     if (cv_class(cv) == fl_ctx->builtintype) {
747 |         void *fptr = *(void**)data;
748 |         label = (value_t)ptrhash_get(&fl_ctx->reverse_dlsym_lookup_table, cv);
749 |         if (label == (value_t)HT_NOTFOUND) {
750 |             fl_ctx->HPOS += ios_printf(f, "#<builtin @0x%08zx>", (size_t)fptr);
{% endraw %}

```
### src/flisp/flisp.h

```c

{% raw %}
33 |     value_t binding;   // global value binding
34 |     struct _fltype_t *type;
35 |     uint32_t hash;
36 |     void *dlcache;     // dlsym address
37 |     // below fields are private
38 |     struct _symbol_t *left;
393 |     value_t arraysym, cfunctionsym, voidsym, pointersym;
394 | 
395 |     htable_t TypeTable;
396 |     htable_t reverse_dlsym_lookup_table;
397 | 
398 |     fltype_t *int8type, *uint8type;
{% endraw %}

```
### src/flisp/cvalues.c

```c

{% raw %}
788 | 
789 |     value_t sym = symbol(fl_ctx, name);
790 |     ((symbol_t*)ptr(sym))->dlcache = cv;
791 |     ptrhash_put(&fl_ctx->reverse_dlsym_lookup_table, cv, (void*)sym);
792 | 
793 |     return tagptr(cv, TAG_CVALUE);
837 |     fl_ctx->maxfinalizers = 0;
838 | 
839 |     htable_new(&fl_ctx->TypeTable, 256);
840 |     htable_new(&fl_ctx->reverse_dlsym_lookup_table, 256);
841 | 
842 |     fl_ctx->builtintype = define_opaque_type(fl_ctx->builtinsym, sizeof(builtin_t), NULL, NULL);
{% endraw %}

```