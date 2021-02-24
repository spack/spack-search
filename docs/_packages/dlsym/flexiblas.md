---
name: "flexiblas"
layout: package
next_package: imlib2
previous_package: openloops
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.0.3
12 / 16005 files match, 12 filtered matches.

 - [src/xerbla.c](#srcxerblac)
 - [src/flexiblas_api_standalone.c](#srcflexiblas_api_standalonec)
 - [src/hooks.c](#srchooksc)
 - [src/sh_utils.c](#srcsh_utilsc)
 - [src/flexiblas.c](#srcflexiblasc)
 - [src/hook_loader.c](#srchook_loaderc)
 - [src/set_num_threads.c](#srcset_num_threadsc)
 - [src/wrap_cblas.c](#srcwrap_cblasc)
 - [src/loader.c](#srcloaderc)
 - [src/tool/hookhandling.c](#srctoolhookhandlingc)
 - [libcscutils/contrib/lua/src/loadlib.c](#libcscutilscontribluasrcloadlibc)
 - [tools/lapack_checks/lapack-check.c](#toolslapack_checkslapack-checkc)

### src/xerbla.c

```c

{% raw %}
99 | 	/* Check if the user supplied a XERBLA function  */
100 | 	{
101 |         int user_xerbla = 0;
102 | 		void *xerbla_symbol1 = dlsym(backend->library_handle,"xerbla_");
103 | 		void *xerbla_symbol2 = dlsym(RTLD_DEFAULT,"xerbla_");
104 | 		void *internal = (void*) &flexiblas_internal_xerbla;
105 | 		DPRINTF(1, "Available XERBLA ( backend: 0x%lx, user defined: 0x%lx, FlexiBLAS: 0x%lx )\n",
138 | 	/* Check if the user supplied a XERBLA function  */
139 | 	{
140 |         int user_xerbla = 0;
141 | 		void *xerbla_symbol1 = dlsym(backend->library_handle,"cblas_xerbla");
142 | 		void *xerbla_symbol2 = dlsym(RTLD_DEFAULT,"cblas_xerbla");
143 | 		void *internal = (void*) &flexiblas_internal_xerbla;
144 | 		DPRINTF(1, "Available CBLAS_XERBLA ( backend: 0x%lx, user defined: 0x%lx, FlexiBLAS: 0x%lx )\n",
{% endraw %}

```
### src/flexiblas_api_standalone.c

```c

{% raw %}
61 | int flexiblas_avail()
62 | {
63 |     int (*fnptr) ();
64 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_avail");
65 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_avail");
66 |     void *ptr_self = &flexiblas_avail;
67 | 
83 | 
84 | int flexiblas_get_color_output() {
85 |     int (*fnptr)();
86 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_get_color_output");
87 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_get_color_output");
88 |     void *ptr_self = &flexiblas_get_color_output;
89 | 
103 | 
104 | void flexiblas_set_color_output(int s) {
105 |     void (*fnptr)(int);
106 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_set_color_output");
107 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_set_color_output");
108 |     void *ptr_self = &flexiblas_get_color_output;
109 | 
125 | void flexiblas_get_version(int *major, int *minor, int *patch)
126 | {
127 |     void (*fnptr) (int *, int*, int *);
128 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_get_version");
129 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_get_version");
130 |     void *ptr_self = &flexiblas_get_version;
131 | 
152 | void flexiblas_print_loaded_backends(FILE *fp)
153 | {
154 |     void (*fnptr) (FILE *);
155 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_print_loaded_backends");
156 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_print_loaded_backends");
157 |     void *ptr_self = &flexiblas_print_loaded_backends;
158 | 
177 | void flexiblas_print_avail_backends(FILE *fp)
178 | {
179 |     void (*fnptr) (FILE *);
180 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_print_avail_backends");
181 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_print_avail_backends");
182 |     void *ptr_self = &flexiblas_print_avail_backends;
183 | 
202 | void flexiblas_print_current_backend(FILE* fp)
203 | {
204 |     void (*fnptr) (FILE *);
205 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_print_current_backend");
206 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_print_current_backend");
207 |     void *ptr_self = &flexiblas_print_current_backend;
208 | 
228 | ssize_t flexiblas_list(char *name, const size_t len, const ssize_t pos)
229 | {
230 |     ssize_t (*fnptr) (char *, size_t, ssize_t);
231 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_list");
232 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_list");
233 |     void *ptr_self = &flexiblas_list;
234 | 
251 | ssize_t flexiblas_list_loaded(char *name, size_t len, ssize_t pos)
252 | {
253 |     ssize_t (*fnptr) (char *, size_t, ssize_t);
254 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_list_loaded");
255 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_list_loaded");
256 |     void *ptr_self = &flexiblas_list_loaded;
257 | 
275 | int flexiblas_load_backend(const char * name )
276 | {
277 |     int (*fnptr) (const char *);
278 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_load_backend");
279 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_load_backend");
280 |     void *ptr_self = &flexiblas_load_backend;
281 | 
298 | int flexiblas_load_backend_library(const char *libname)
299 | {
300 |     int (*fnptr) (const char *);
301 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_load_backend_library");
302 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_load_backend_library");
303 |     void *ptr_self = &flexiblas_load_backend_library;
304 | 
322 | int flexiblas_switch(int id)
323 | {
324 |     int (*fnptr) (int);
325 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_switch");
326 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_switch");
327 |     void *ptr_self = &flexiblas_switch;
328 | 
346 | int flexiblas_current_backend(char *name, size_t len)
347 | {
348 |     int (*fnptr) (char *, size_t);
349 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_current_backend");
350 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_current_backend");
351 |     void *ptr_self = &flexiblas_current_backend;
352 | 
371 | void flexiblas_set_num_threads(int num)
372 | {
373 |     int (*fnptr) (int);
374 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_set_num_threads");
375 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_set_num_threads");
376 |     void *ptr_self = &flexiblas_set_num_threads;
377 | 
443 | int flexiblas_get_num_threads()
444 | {
445 |     int (*fnptr) ();
446 |     void *ptr_next    = dlsym(RTLD_NEXT, "flexiblas_get_num_threads");
447 |     void *ptr_default = dlsym(RTLD_DEFAULT, "flexiblas_get_num_threads");
448 |     void *ptr_self = &flexiblas_get_num_threads;
449 | 
{% endraw %}

```
### src/hooks.c

```c

{% raw %}
103 |             handle  = __flexiblas_dlopen(curfn, RTLD_LAZY | RTLD_LOCAL , NULL);
104 |             if ( !handle) continue;
105 | 
106 |             reg = dlsym(handle,"flexiblas_register");
107 |             if ( !reg ) {
108 |                 DPRINTF(0, "%s is not a hook\n");
116 |             printf("-> Descr:    %s\n", reg->desc);
117 |             printf("-> Authors:  %s\n", reg->authors);
118 | 
119 |             opts = dlsym(handle, "flexiblas_options");
120 |             if ( !opts) {
121 |                 dlclose(handle);
187 |             if ( !handle) continue;
188 | 
189 | 
190 |             reg = dlsym(handle,"flexiblas_register");
191 |             if ( !reg ) {
192 |                 DPRINTF(1, "%s is not a hook\n", dir_entry->d_name);
216 |     handle  = __flexiblas_dlopen(path, RTLD_LAZY | RTLD_LOCAL , NULL);
217 |     if ( !handle) return NULL;
218 | 
219 |     reg = dlsym(handle, "flexiblas_register");
220 |     if ( !reg ) return NULL;
221 | 
{% endraw %}

```
### src/sh_utils.c

```c

{% raw %}
211 | 				return NULL;
212 | 			}
213 | 
214 | 			ld_flags_sym_global = dlsym(handle, "flexiblas_ld_global");
215 | 			if ( ld_flags_sym_global == NULL) {
216 | 				ld_flags_global = 0;
218 | 				ld_flags_global = *((int32_t*) ld_flags_sym_global);
219 | 			}
220 | 
221 | 			ld_flags_sym_lazy = dlsym(handle, "flexiblas_ld_lazy");
222 | 			if ( ld_flags_sym_lazy == NULL) {
223 | 				ld_flags_lazy = 0;
225 | 				ld_flags_lazy = *((int32_t*) ld_flags_sym_lazy);
226 | 			}
227 | #ifdef __linux__
228 | 			ld_flags_sym_deep = dlsym(handle, "flexiblas_ld_deep");
229 | 			if ( ld_flags_sym_deep == NULL) {
230 | 				ld_flags_deep = 0;
367 |             if ( filepath) free(filepath);
368 |             return 0;
369 |         }
370 |         sym = dlsym(handle, symbol_name);
371 |         dlclose(handle);
372 |        	if ( filepath) free(filepath);
{% endraw %}

```
### src/flexiblas.c

```c

{% raw %}
202 |     backend->init_function = (flexiblas_init_function_t) GetProcAddress(library, FLEXIBLAS_INIT_FUNCTION_NAME);
203 |     backend->exit_function = (flexiblas_exit_function_t) GetProcAddress(library, FLEXIBLAS_EXIT_FUNCTION_NAME);
204 | #else
205 |     backend->info_function = (flexiblas_info_function_t) dlsym(library, FLEXIBLAS_INFO_FUNCTION_NAME);
206 |     backend->init_function = (flexiblas_init_function_t) dlsym(library, FLEXIBLAS_INIT_FUNCTION_NAME);
207 |     backend->exit_function = (flexiblas_exit_function_t) dlsym(library, FLEXIBLAS_EXIT_FUNCTION_NAME);
208 | #endif
209 | 
735 |         __flexiblas_hooks->hooks_loaded = 0;
736 |         __flexiblas_hooks->initialized  = 0;
737 | 
738 |         dlsym((void *) 0, "flexiblas_verbosity");
739 | 
740 |         int hooks_to_load = 0;
791 | 
792 | 
793 |             __flexiblas_hooks->handles[k] = handle;
794 |             __flexiblas_hooks->hook_init[k] = (flexiblas_init_function_t) dlsym(handle, FLEXIBLAS_HOOK_INIT_FUNCTION_NAME);
795 |             __flexiblas_hooks->hook_exit[k] = (flexiblas_exit_function_t) dlsym(handle, FLEXIBLAS_HOOK_EXIT_FUNCTION_NAME);
796 | 
797 |             __flexiblas_load_blas_hooks(__flexiblas_hooks, handle);
{% endraw %}

```
### src/hook_loader.c

```c

{% raw %}
72 | 			fprintf(stderr, "%s ", fname);
73 | 		}
74 | 
75 | 		ptr_hsymbol = dlsym(handle, fname);
76 | 
77 |         if (ptr_hsymbol!=NULL) {
{% endraw %}

```
### src/set_num_threads.c

```c

{% raw %}
204 |         if ( i != 1 ) {
205 |             snprintf(fn2_name, 130, "%s_", fn_name);
206 |         }
207 |     	ptr  = dlsym(backend->library_handle, fn_name);
208 |         ptr2  = dlsym(backend->library_handle, fn2_name);
209 | 
210 |         if (ptr != NULL || ptr2 != NULL)
252 |         if ( i != 1 )
253 |             snprintf(fn2_name, 130, "%s_", fn_name);
254 | 
255 |        	ptr  = dlsym(backend->library_handle, fn_name);
256 |         ptr2  = dlsym(backend->library_handle, fn2_name);
257 | 
258 |         if (ptr != NULL || ptr2 != NULL)
{% endraw %}

```
### src/wrap_cblas.c

```c

{% raw %}
61 | 
62 | HIDDEN int __flexiblas_load_cblas(flexiblas_backend_t *backend)
63 | {
64 |     void * cblas_in_blis = dlsym(backend->library_handle, "bli_info_get_enable_cblas");
65 |     if ( cblas_in_blis ) {
66 |         DPRINTF_WARN(1, "The desired BLAS library is BLIS. We do not load their CBLAS wrapper since it might alter the behavior of your programs.");
{% endraw %}

```
### src/loader.c

```c

{% raw %}
63 | 
64 | 	snprintf(cname, 39, "cblas_%s", name);
65 | 	DPRINTF(3, "Look up: %18s", cname);
66 |     ptr_csymbol = dlsym(handle, cname);
67 | 
68 | 	fn -> cblas_real = ptr_csymbol;
115 | #ifdef __WIN32__
116 | 		ptr_fsymbol = GetProcAddress(handle, fname);
117 | #else
118 | 		ptr_fsymbol = dlsym(handle, fname);
119 | #endif
120 | 		if (ptr_fsymbol!=NULL) {
{% endraw %}

```
### src/tool/hookhandling.c

```c

{% raw %}
181 |         goto fin;
182 |     }
183 | 
184 |     flexiblas_hook_register_t *reg = (flexiblas_hook_register_t *) dlsym(handle, "flexiblas_register");
185 | 
186 |     printf("Name:          %s\n", reg->name);
190 | 
191 |     int cnt = 0;
192 |     int nopts = 0;
193 |     flexiblas_option_t *opts = (flexiblas_option_t *) dlsym(handle, "flexiblas_options");
194 |     if ( opts == NULL)
195 |         nopts = 0;
391 |         printf("Opening hook %s/%s failed.\n", hookname, sofile);
392 |         return -1;
393 |     }
394 |     reg = (flexiblas_hook_register_t *) dlsym(handle, "flexiblas_register");
395 |     opts = (flexiblas_option_t *) dlsym(handle, "flexiblas_options");
396 | 
397 |     if ( reg == NULL) {
{% endraw %}

```
### libcscutils/contrib/lua/src/loadlib.c

```c

{% raw %}
130 | 
131 | 
132 | static lua_CFunction lsys_sym (lua_State *L, void *lib, const char *sym) {
133 |   lua_CFunction f = cast_func(dlsym(lib, sym));
134 |   if (f == NULL) lua_pushstring(L, dlerror());
135 |   return f;
{% endraw %}

```
### tools/lapack_checks/lapack-check.c

```c

{% raw %}
149 |     {
150 |         void *sym1, *sym2;
151 |         snprintf(name, 128, "%s_", list[i]);
152 |         sym1 = dlsym ( lib, list[i] );
153 |         sym2 = dlsym ( lib, name );
154 |         if ( sym1 == NULL && sym2 == NULL) {
155 |             if ( ! is_in_list(ignore_list, list[i]) ) {
{% endraw %}

```