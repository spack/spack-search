---
name: "flexiblas"
layout: package
next_package: foam-extend
previous_package: fipscheck
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.0.3
9 / 16005 files match, 7 filtered matches.

 - [src/hooks.c](#srchooksc)
 - [src/sh_utils.c](#srcsh_utilsc)
 - [src/helper.h](#srchelperh)
 - [src/flexiblas.c](#srcflexiblasc)
 - [src/tool/hookhandling.c](#srctoolhookhandlingc)
 - [libcscutils/contrib/lua/src/loadlib.c](#libcscutilscontribluasrcloadlibc)
 - [tools/lapack_checks/lapack-check.c](#toolslapack_checkslapack-checkc)

### src/hooks.c

```c

{% raw %}
100 | 
101 |             printf("%s\n", curfn);
102 | 
103 |             handle  = __flexiblas_dlopen(curfn, RTLD_LAZY | RTLD_LOCAL , NULL);
104 |             if ( !handle) continue;
105 | 
183 |             if ( stat(curfn, &st)) continue;
184 |             if ( ! ( S_ISREG(st.st_mode))) continue;
185 | 
186 |             handle  = __flexiblas_dlopen(curfn, RTLD_LAZY | RTLD_LOCAL , NULL);
187 |             if ( !handle) continue;
188 | 
213 |     flexiblas_hook_register_t *reg;
214 |     char *ret;
215 | 
216 |     handle  = __flexiblas_dlopen(path, RTLD_LAZY | RTLD_LOCAL , NULL);
217 |     if ( !handle) return NULL;
218 | 
{% endraw %}

```
### src/sh_utils.c

```c

{% raw %}
115 | 	}
116 | }
117 | 
118 | HIDDEN void * __flexiblas_dlopen( const char *libname, int flags, char ** sofile ){
119 | 	char *path = NULL;
120 | 	char *filepath = NULL;
204 | #endif
205 | 		if ( flags < 0 ) {
206 | 			dlerror();
207 | 			handle = dlopen(filepath, RTLD_LAZY | RTLD_LOCAL);
208 | 			if (!handle) {
209 | 				DPRINTF_ERROR(0, "Failed to load %s - error: %s \n", filepath, dlerror());
259 | #endif  */
260 | 		}
261 | 
262 | 		handle = dlopen(filepath, flags);
263 | #endif
264 | 
268 | #ifdef __WIN32__
269 | 			DPRINTF_ERROR(0, "Unable to load library: %s\r\n", filepath);
270 | #else
271 | 			DPRINTF_ERROR(0, "dlopen: %s\n", dlerror());
272 | #endif
273 | 		}
361 | 	if( found ) {
362 |         void *sym = NULL;
363 |         dlerror();
364 |         handle = dlopen(filepath, RTLD_LAZY | RTLD_LOCAL);
365 |         if (!handle) {
366 |             DPRINTF_ERROR(0, "Failed to load %s - error: %s \n", filepath, dlerror());
{% endraw %}

```
### src/helper.h

```c

{% raw %}
57 |     void flexiblas_print_warning(const char *prefix, const char *fmt, ... );
58 |     void flexiblas_print_info(const char *prefix, const char *fmt, ... );
59 | 
60 |     HIDDEN void * __flexiblas_dlopen( const char *libname, int flags, char **soname );
61 |     HIDDEN int __flexiblas_dl_symbol_exist( const char *libname, const char *symbol_name );
62 | 
{% endraw %}

```
### src/flexiblas.c

```c

{% raw %}
263 |         }
264 | 
265 |         DPRINTF(1,"Use default BLAS: %s - %s from %s\n", blas_name, clibrary, flexiblas_mgmt_location_to_string(loc) );
266 |         library = __flexiblas_dlopen(clibrary, DLOPEN_FLAGS_FROM_FILE , NULL);
267 |         strncpy(name, blas_name, FLEXIBLAS_MGMT_MAX_BUFFER_LEN);
268 | 
271 |          *  Try to open env_FLEXIBLAS directly and the get the value from the Hashtable
272 |          *-----------------------------------------------------------------------------*/
273 |         DPRINTF(1,"Trying to use the content of " ENV_FLEXIBLAS ": \"%s\" as shared library.\n", env_FLEXIBLAS);
274 |         library = __flexiblas_dlopen(env_FLEXIBLAS, DLOPEN_FLAGS_FROM_FILE, NULL);
275 |         strncpy(name, env_FLEXIBLAS, FLEXIBLAS_MGMT_MAX_BUFFER_LEN);
276 | 
308 |             }
309 | 
310 |             DPRINTF(1,"Trying to load  %s\n", clibrary );
311 |             library  = __flexiblas_dlopen(clibrary, DLOPEN_FLAGS_FROM_FILE , NULL);
312 |             if ( clibrary != NULL) free(clibrary);
313 |             free(tmp);
324 |             DPRINTF_ERROR(0, "Failed to get the BLAS backend (__FALLBACK__) from the configuration.\n");
325 |             library = NULL;
326 |         } else {
327 |             library = __flexiblas_dlopen(clibrary,DLOPEN_FLAGS_FROM_FILE , NULL);
328 |         }
329 |         free(clibrary);
401 |     }
402 | 
403 |     DPRINTF(2, " Try to load %s - %s\n", blas_name, clibrary);
404 |     library = __flexiblas_dlopen(clibrary, DLOPEN_FLAGS_FROM_FILE, (char **) NULL);
405 | 
406 |     if ( library == NULL ) {
494 |     void *library = NULL;
495 | 
496 |     DPRINTF(2, PRINT_PREFIX " Try to load %s \n", blas_sofile);
497 |     library = __flexiblas_dlopen(blas_sofile, DLOPEN_FLAGS_FROM_FILE, (char **) NULL);
498 | 
499 |     if ( library == NULL ) {
676 |             snprintf(blas_name,len, "%s%s", FALLBACK_NAME,SO_EXTENSION);
677 |             free(SO_EXTENSION);
678 | 
679 |             __flexiblas_blas_fallback = __flexiblas_dlopen(blas_name, RTLD_LAZY | RTLD_GLOBAL , NULL);
680 |             if ( __flexiblas_blas_fallback == NULL ) {
681 |                 DPRINTF_ERROR(0," Failed to load the BLAS fallback library.  Abort!\n");
695 |             snprintf(lapack_name,len, "%s%s", LAPACK_FALLBACK_NAME,SO_EXTENSION);
696 |             free(SO_EXTENSION);
697 | #ifdef LAPACK_DEEPBIND
698 |             __flexiblas_lapack_fallback = __flexiblas_dlopen(lapack_name, RTLD_LAZY | RTLD_DEEPBIND |  RTLD_GLOBAL , NULL);
699 | #else
700 |             __flexiblas_lapack_fallback = __flexiblas_dlopen(lapack_name, RTLD_LAZY | RTLD_GLOBAL , NULL);
701 | #endif
702 |             if ( __flexiblas_lapack_fallback == NULL ) {
781 |             void * handle = NULL;
782 | 
783 |             sofile = __flexiblas_hook_sofile(hook_load_list[i]);
784 |             handle  = __flexiblas_dlopen(sofile, RTLD_LAZY | RTLD_LOCAL , NULL);
785 |             DPRINTF(1,"Load hook: %s - %s\n", hook_load_list[i], sofile);
786 |             if ( ! handle ) {
{% endraw %}

```
### src/tool/hookhandling.c

```c

{% raw %}
174 |     }
175 | 
176 |     dlerror();
177 |     handle = __flexiblas_dlopen(sofile, RTLD_LAZY | RTLD_LOCAL, NULL);
178 |     if ( !handle) {
179 |         printf("Cannot open %s as shared library. (error = %s)\n", sofile, dlerror());
386 |          return -1;
387 |     }
388 | 
389 |     handle = __flexiblas_dlopen(sofile, RTLD_LAZY | RTLD_LOCAL, NULL);
390 |     if ( !handle) {
391 |         printf("Opening hook %s/%s failed.\n", hookname, sofile);
{% endraw %}

```
### libcscutils/contrib/lua/src/loadlib.c

```c

{% raw %}
123 | 
124 | 
125 | static void *lsys_load (lua_State *L, const char *path, int seeglb) {
126 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
127 |   if (lib == NULL) lua_pushstring(L, dlerror());
128 |   return lib;
{% endraw %}

```
### tools/lapack_checks/lapack-check.c

```c

{% raw %}
184 |         return -1;
185 |     }
186 | 
187 |     ptr = dlopen(argv[1], RTLD_LOCAL | RTLD_LAZY);
188 |     if ( ptr == NULL ) {
189 |         printf("Failed to open :%s\n", argv[1]);
{% endraw %}

```