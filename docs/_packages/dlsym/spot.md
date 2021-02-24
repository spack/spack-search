---
name: "spot"
layout: package
next_package: geopm
previous_package: libxslt
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 1.2.6
20 / 4036 files match, 10 filtered matches.

 - [iface/dve2/dve2.cc](#ifacedve2dve2cc)
 - [ltdl/ltdl.h](#ltdlltdlh)
 - [ltdl/ltdl.c](#ltdlltdlc)
 - [ltdl/loaders/dyld.c](#ltdlloadersdyldc)
 - [ltdl/loaders/loadlibrary.c](#ltdlloadersloadlibraryc)
 - [ltdl/loaders/shl_load.c](#ltdlloadersshl_loadc)
 - [ltdl/loaders/load_add_on.c](#ltdlloadersload_add_onc)
 - [ltdl/loaders/dld_link.c](#ltdlloadersdld_linkc)
 - [ltdl/loaders/preopen.c](#ltdlloaderspreopenc)
 - [ltdl/loaders/dlopen.c](#ltdlloadersdlopenc)

### iface/dve2/dve2.cc

```cpp

{% raw %}
1030 |     d->handle = h;
1031 | 
1032 |     d->get_initial_state = (void (*)(void*))
1033 |       lt_dlsym(h, "get_initial_state");
1034 |     d->have_property = (int (*)())
1035 |       lt_dlsym(h, "have_property");
1036 |     d->get_successors = (int (*)(void*, int*, TransitionCB, void*))
1037 |       lt_dlsym(h, "get_successors");
1038 |     d->get_state_variable_count = (int (*)())
1039 |       lt_dlsym(h, "get_state_variable_count");
1040 |     d->get_state_variable_name = (const char* (*)(int))
1041 |       lt_dlsym(h, "get_state_variable_name");
1042 |     d->get_state_variable_type = (int (*)(int))
1043 |       lt_dlsym(h, "get_state_variable_type");
1044 |     d->get_state_variable_type_count = (int (*)())
1045 |       lt_dlsym(h, "get_state_variable_type_count");
1046 |     d->get_state_variable_type_name = (const char* (*)(int))
1047 |       lt_dlsym(h, "get_state_variable_type_name");
1048 |     d->get_state_variable_type_value_count = (int (*)(int))
1049 |       lt_dlsym(h, "get_state_variable_type_value_count");
1050 |     d->get_state_variable_type_value = (const char* (*)(int, int))
1051 |       lt_dlsym(h, "get_state_variable_type_value");
1052 |     d->get_transition_count = (int (*)())
1053 |       lt_dlsym(h, "get_transition_count");
1054 | 
1055 |     if (!(d->get_initial_state
{% endraw %}

```
### ltdl/ltdl.h

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
### ltdl/ltdl.c

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
### ltdl/loaders/dyld.c

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
### ltdl/loaders/loadlibrary.c

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
### ltdl/loaders/shl_load.c

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
### ltdl/loaders/load_add_on.c

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
### ltdl/loaders/dld_link.c

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
### ltdl/loaders/preopen.c

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
208 | vm_sym (lt_user_data LT__UNUSED loader_data, lt_module module, const char *name)
209 | {
210 |   lt_dlsymlist	       *symbol = (lt_dlsymlist*) module;
211 | 
212 |   symbol +=2;			/* Skip header (originator then libname). */
252 | 
253 | /* Add a new symbol list to the global chain.  */
254 | static int
255 | add_symlist (const lt_dlsymlist *symlist)
256 | {
257 |   symlist_chain *lists;
289 | 
290 | /* Save a default symbol list for later.  */
291 | int
292 | lt_dlpreload_default (const lt_dlsymlist *preloaded)
293 | {
294 |   default_preloaded_symbols = preloaded;
299 | /* Add a symbol list to the global chain, or with a NULL argument,
300 |    revert to just the default list.  */
301 | int
302 | lt_dlpreload (const lt_dlsymlist *preloaded)
303 | {
304 |   int errors = 0;
338 |       if ((originator && streq (list->symlist->name, originator))
339 |           || (!originator && streq (list->symlist->name, "@PROGRAM@")))
340 | 	{
341 | 	  const lt_dlsymlist *symbol;
342 | 	  unsigned int idx = 0;
343 | 
{% endraw %}

```
### ltdl/loaders/dlopen.c

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