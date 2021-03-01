---
name: "clamav"
layout: package
next_package: clinfo
previous_package: chrony
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.101.2
38 / 6766 files match, 16 filtered matches.

 - [libclamav/others.c](#libclamavothersc)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/loaders/dyld.c](#libltdlloadersdyldc)
 - [libltdl/loaders/loadlibrary.c](#libltdlloadersloadlibraryc)
 - [libltdl/loaders/shl_load.c](#libltdlloadersshl_loadc)
 - [libltdl/loaders/load_add_on.c](#libltdlloadersload_add_onc)
 - [libltdl/loaders/dld_link.c](#libltdlloadersdld_linkc)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)
 - [win32/compat/ltdl.h](#win32compatltdlh)
 - [win32/compat/ltdl.c](#win32compatltdlc)
 - [win32/3rdparty/libxml2/os400/wrappers.h](#win323rdpartylibxml2os400wrappersh)
 - [win32/3rdparty/libxml2/os400/wrappers.c](#win323rdpartylibxml2os400wrappersc)
 - [win32/3rdparty/libxml2/os400/dlfcn/dlfcn.h](#win323rdpartylibxml2os400dlfcndlfcnh)
 - [win32/3rdparty/libxml2/os400/dlfcn/dlfcn.c](#win323rdpartylibxml2os400dlfcndlfcnc)

### libclamav/others.c

```c

{% raw %}
100 | 
101 | #if 0
102 | #define lt_preload_symbols lt_libclamav_LTX_preloaded_symbols
103 | extern const lt_dlsymlist lt_preload_symbols[];
104 | #endif
105 | 
182 |     if (!rhandle)
183 | 	return;
184 | 
185 |     if (!(cli_unrar_open = (cl_unrar_error_t(*)(const char *, void **, char **, uint32_t *, uint8_t))lt_dlsym(rhandle, "libclamunrar_iface_LTX_unrar_open")) ||
186 | 		!(cli_unrar_peek_file_header = (cl_unrar_error_t(*)(void *, unrar_metadata_t *))lt_dlsym(rhandle, "libclamunrar_iface_LTX_unrar_peek_file_header")) ||
187 | 		!(cli_unrar_extract_file = (cl_unrar_error_t(*)(void*, const char*, char*))lt_dlsym(rhandle, "libclamunrar_iface_LTX_unrar_extract_file")) ||
188 | 		!(cli_unrar_skip_file = (cl_unrar_error_t(*)(void *))lt_dlsym(rhandle, "libclamunrar_iface_LTX_unrar_skip_file")) ||
189 | 		!(cli_unrar_close = (void(*)(void *))lt_dlsym(rhandle, "libclamunrar_iface_LTX_unrar_close"))
190 | 	) {
191 | 	/* ideally we should never land here, we'd better warn so */
{% endraw %}

```
### libltdl/ltdl.h

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
### libltdl/ltdl.c

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
2009 | }
2010 | 
2011 | void *
2012 | lt_dlsym (lt_dlhandle place, const char *symbol)
2013 | {
2014 |   size_t lensym;
{% endraw %}

```
### libltdl/loaders/dyld.c

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
### libltdl/loaders/loadlibrary.c

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
### libltdl/loaders/shl_load.c

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
### libltdl/loaders/load_add_on.c

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
### libltdl/loaders/dld_link.c

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
### libltdl/loaders/preopen.c

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
207 | static void *
208 | vm_sym (lt_user_data loader_data LT__UNUSED, lt_module module, const char *name)
209 | {
210 |   lt_dlsymlist	       *symbol = (lt_dlsymlist*) module;
211 | 
212 |   if (symbol[1].name && STREQ (symbol[1].name, "@INIT@"))
257 | 
258 | /* Add a new symbol list to the global chain.  */
259 | static int
260 | add_symlist (const lt_dlsymlist *symlist)
261 | {
262 |   symlist_chain *lists;
301 | 
302 | /* Save a default symbol list for later.  */
303 | int
304 | lt_dlpreload_default (const lt_dlsymlist *preloaded)
305 | {
306 |   default_preloaded_symbols = preloaded;
311 | /* Add a symbol list to the global chain, or with a NULL argument,
312 |    revert to just the default list.  */
313 | int
314 | lt_dlpreload (const lt_dlsymlist *preloaded)
315 | {
316 |   int errors = 0;
350 |       if ((originator && STREQ (list->symlist->name, originator))
351 |           || (!originator && STREQ (list->symlist->name, "@PROGRAM@")))
352 | 	{
353 | 	  const lt_dlsymlist *symbol;
354 | 	  unsigned int idx = 0;
355 | 
{% endraw %}

```
### libltdl/loaders/dlopen.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dlopen_LTX_get_vtable
39 | 
263 | static void *
264 | vm_sym (lt_user_data loader_data LT__UNUSED, lt_module module, const char *name)
265 | {
266 |   void *address = dlsym (module, name);
267 | 
268 |   if (!address)
{% endraw %}

```
### win32/compat/ltdl.h

```c

{% raw %}
29 | 
30 | int lt_dlinit(void);
31 | lt_dlhandle lt_dlopen(const char *filename);
32 | void *lt_dlsym(lt_dlhandle handle, const char *name);
33 | const char *lt_dlerror(void);
34 | int lt_dlclose (lt_dlhandle handle);
{% endraw %}

```
### win32/compat/ltdl.c

```c

{% raw %}
33 | 	return h;
34 | }
35 | 
36 | void *lt_dlsym(lt_dlhandle handle, const char *name) {
37 | 	void *f = GetProcAddress(handle, name);
38 | 	if(!f) lasterr = GetLastError();
{% endraw %}

```
### win32/3rdparty/libxml2/os400/wrappers.h

```c

{% raw %}
38 |                 _lx_inet_ntop(int af,
39 |                         const void * src, char * dst, socklen_t size);
40 | extern void *   _lx_dlopen(const char * filename, int flag);
41 | extern void *   _lx_dlsym(void * handle, const char * symbol);
42 | extern char *   _lx_dlerror(void);
43 | 
{% endraw %}

```
### win32/3rdparty/libxml2/os400/wrappers.c

```c

{% raw %}
80 | 
81 | 
82 | void *
83 | _lx_dlsym(void * handle, const char * symbol)
84 | 
85 | {
86 |         xmlDictPtr d = NULL;
87 |         void * result;
88 | 
89 |         result = dlsym(handle, xmlTranscodeResult(symbol, NULL, &d, NULL));
90 |         xmlZapDict(&d);
91 |         return result;
{% endraw %}

```
### win32/3rdparty/libxml2/os400/dlfcn/dlfcn.h

```c

{% raw %}
24 | **/
25 | 
26 | extern void *           dlopen(const char * filename, int flag);
27 | extern void *           dlsym(void * handle, const char * symbol);
28 | extern const char *     dlerror(void);
29 | extern int              dlclose(void * handle);
{% endraw %}

```
### win32/3rdparty/libxml2/os400/dlfcn/dlfcn.c

```c

{% raw %}
982 | 
983 | 
984 | void *
985 | dlsym(void * handle, const char * symbol)
986 | 
987 | {
1034 |                 if (--(dlip->actcount))
1035 |                         return 0;
1036 | 
1037 |                 if (_fini = dlsym(handle, "_fini"))
1038 |                         (*_fini)();
1039 |                 }
1129 |         ***     Bump activation counter.
1130 |         **/
1131 | 
1132 |         if (!(dlip->actcount++) && (_init = dlsym(dlip, "_init")))
1133 |                 (*_init)();
1134 | 
{% endraw %}

```