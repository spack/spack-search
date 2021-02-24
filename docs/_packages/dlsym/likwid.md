---
name: "likwid"
layout: package
next_package: laszip
previous_package: apr
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.0.2
10 / 1422 files match, 7 filtered matches.

 - [src/pthread-overload/pthread-overload.c](#srcpthread-overloadpthread-overloadc)
 - [ext/GOTCHA/src/gotcha_dl.h](#extgotchasrcgotcha_dlh)
 - [ext/GOTCHA/src/gotcha_dl.c](#extgotchasrcgotcha_dlc)
 - [ext/hwloc/include/hwloc/plugins.h](#exthwlocincludehwlocpluginsh)
 - [ext/hwloc/hwloc/components.c](#exthwlochwloccomponentsc)
 - [ext/lua/src/loadlib.c](#extluasrcloadlibc)
 - [bench/src/ptt2asm.c](#benchsrcptt2asmc)

### src/pthread-overload/pthread-overload.c

```c

{% raw %}
241 |     }
242 | 
243 |     dlerror();    /* Clear any existing error */
244 |     rptc = dlsym(handle, "pthread_create");
245 | 
246 |     if ((error = dlerror()) != NULL)
{% endraw %}

```
### ext/GOTCHA/src/gotcha_dl.h

```c

{% raw %}
8 | extern int prepare_symbol(struct internal_binding_t *binding);
9 | 
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
11 | extern gotcha_wrappee_handle_t orig_dlsym_handle;
12 | 
13 | extern struct gotcha_binding_t dl_binds[];
{% endraw %}

```
### ext/GOTCHA/src/gotcha_dl.c

```c

{% raw %}
7 | void* _dl_sym(void* handle, const char* name, void* where);
8 | 
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
10 | gotcha_wrappee_handle_t orig_dlsym_handle;
11 | 
12 | static int per_binding(hash_key_t key, hash_data_t data, void *opaque KNOWN_UNUSED)
48 |    return handle;
49 | }
50 | 
51 | static void* dlsym_wrapper(void* handle, const char* symbol_name){
52 |   typeof(&dlsym_wrapper) orig_dlsym = gotcha_get_wrappee(orig_dlsym_handle);
53 |   struct internal_binding_t *binding;
54 |   int result;
59 |   
60 |   result = lookup_hashtable(&function_hash_table, (hash_key_t) symbol_name, (hash_data_t *) &binding);
61 |   if (result == -1)
62 |      return orig_dlsym(handle, symbol_name);
63 |   else
64 |      return binding->user_binding->wrapper_pointer;
66 | 
67 | struct gotcha_binding_t dl_binds[] = {
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
69 |   {"dlsym", dlsym_wrapper, &orig_dlsym_handle}
70 | };     
71 | void handle_libdl(){
{% endraw %}

```
### ext/hwloc/include/hwloc/plugins.h

```c

{% raw %}
423 |   if (!handle)
424 |     /* cannot check, assume things will work */
425 |     return 0;
426 |   sym = lt_dlsym(handle, symbol);
427 |   lt_dlclose(handle);
428 |   if (!sym) {
{% endraw %}

```
### ext/hwloc/hwloc/components.c

```c

{% raw %}
107 | {
108 |   char componentsymbolname[strlen(basename)+10+1];
109 |   sprintf(componentsymbolname, "%s_component", basename);
110 |   component = lt_dlsym(handle, componentsymbolname);
111 |   if (!component) {
112 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### ext/lua/src/loadlib.c

```c

{% raw %}
160 | 
161 | 
162 | static lua_CFunction lsys_sym (lua_State *L, void *lib, const char *sym) {
163 |   lua_CFunction f = cast_func(dlsym(lib, sym));
164 |   if (f == NULL) lua_pushstring(L, dlerror());
165 |   return f;
{% endraw %}

```
### bench/src/ptt2asm.c

```c

{% raw %}
555 | {
556 |     void* handle;
557 |     char *error;
558 |     void* (*owndlsym)(void*, const char*) = dlsym;
559 | 
560 |     dlerror();
564 |         return -1;
565 |     }
566 |     dlerror();
567 |     testcase->kernel = owndlsym(testcase->dlhandle, testcase->name);
568 |     if ((error = dlerror()) != NULL)  {
569 |         dlclose(testcase->dlhandle);
{% endraw %}

```