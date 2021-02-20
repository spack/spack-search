---
name: "timemory"
layout: package
next_package: tpm2-tss
previous_package: thepeg
languages: ['c']
---
## master
29 / 2657 files match, 10 filtered matches.

 - [external/gotcha/src/gotcha_dl.h](#externalgotchasrcgotcha_dlh)
 - [external/gotcha/src/gotcha_dl.c](#externalgotchasrcgotcha_dlc)
 - [external/gotcha/src/gotcha.c](#externalgotchasrcgotchac)
 - [external/gotcha/test/dlopen/test_dlopen.c](#externalgotchatestdlopentest_dlopenc)
 - [external/gotcha/test/multi_agent_dlopen/dlsym.c](#externalgotchatestmulti_agent_dlopendlsymc)
 - [external/gotcha/test/multi_agent_dlopen/monitor.c](#externalgotchatestmulti_agent_dlopenmonitorc)
 - [external/gotcha/test/multi_agent_dlopen/main.c](#externalgotchatestmulti_agent_dlopenmainc)
 - [external/caliper/ext/gotcha/src/gotcha_dl.h](#externalcaliperextgotchasrcgotcha_dlh)
 - [external/caliper/ext/gotcha/src/gotcha_dl.c](#externalcaliperextgotchasrcgotcha_dlc)
 - [external/caliper/ext/gotcha/src/gotcha.c](#externalcaliperextgotchasrcgotchac)

### external/gotcha/src/gotcha_dl.h

```c

{% raw %}
7 | extern void update_all_library_gots(hash_table_t *bindings);
8 | extern int prepare_symbol(struct internal_binding_t *binding);
9 | 
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
11 | extern gotcha_wrappee_handle_t orig_dlsym_handle;
12 | 
{% endraw %}

```
### external/gotcha/src/gotcha_dl.c

```c

{% raw %}
6 | 
7 | void* _dl_sym(void* handle, const char* name, void* where);
8 | 
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
10 | gotcha_wrappee_handle_t orig_dlsym_handle;
11 | 
14 |    int result;
15 |    struct internal_binding_t *binding = (struct internal_binding_t *) data;
16 | 
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
18 |                 binding->user_binding->name, binding->associated_binding_table->tool->tool_name);
19 |    
25 |    
26 |    result = prepare_symbol(binding);
27 |    if (result == -1) {
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
29 |       return 0;
30 |    }
33 |    return 0;
34 | }
35 | 
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
38 |    void *handle;
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
41 | 
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
43 |    foreach_hash_entry(&notfound_binding_table, NULL, per_binding);
44 | 
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
46 |    update_all_library_gots(&function_hash_table);
47 |   
69 | }
70 | 
71 | struct gotcha_binding_t dl_binds[] = {
72 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
73 |   {"dlsym", dlsym_wrapper, &orig_dlsym_handle}
74 | };     
{% endraw %}

```
### external/gotcha/src/gotcha.c

```c

{% raw %}
314 |         debug_printf(2, "Symbol %s needs lookup operation\n", binding->user_binding->name);
315 |         int presult = prepare_symbol(binding);
316 |         if (presult == -1) {
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
318 |                         binding->user_binding->name);
319 |            addto_hashtable(&notfound_binding_table, (hash_key_t) binding->user_binding->name, (hash_data_t) binding);
{% endraw %}

```
### external/gotcha/test/dlopen/test_dlopen.c

```c

{% raw %}
56 |    int had_error = 0;
57 |    int result;
58 | 
59 |    result = gotcha_wrap(funcs, 2, "dlopen_test");
60 |    if(result != GOTCHA_FUNCTION_NOT_FOUND){
61 |      fprintf(stderr, "GOTCHA should have failed to find a function, but found it\n");
62 |      return -1;
63 |    }
64 | 
65 |    libnum = dlopen(LIB_NAME, RTLD_NOW);
66 |    if (!libnum) {
67 |       fprintf(stderr, "ERROR: Test failed to dlopen libnum.so\n");
68 |       return -1;
69 |    }
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/dlsym.c

```c

{% raw %}
13 | #define MYNAME  "libsym.so"
14 | 
15 | typedef void * dlsym_fcn_t(void *, const char *);
16 | typedef void * dlopen_mode_fcn_t(const char *, int);
17 | 
18 | dlsym_fcn_t __libc_dlsym;
19 | dlopen_mode_fcn_t __libc_dlopen_mode;
20 | 
21 | void *
23 | {
24 |     fprintf(stderr, "%s:  enter dlsym:  sym = %s\n", MYNAME, symbol);
25 | 
26 |     void * dl_handle = __libc_dlopen_mode("libdl.so", RTLD_LAZY);
27 | 
28 |     if (dl_handle == NULL) {
29 | 	err(1, "__libc_dlopen_mode failed");
30 |     }
31 | 
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/monitor.c

```c

{% raw %}
13 | 
14 | #define MYNAME  "libmon.so"
15 | 
16 | typedef void *dlopen_fcn_t(const char *, int);
17 | 
18 | gotcha_wrappee_handle_t reel_dlopen_handle;
19 | 
20 | void *
21 | wrap_dlopen(const char *file, int flag)
22 | {
23 |     typeof(&wrap_dlopen) reel_dlopen = gotcha_get_wrappee(reel_dlopen_handle);
24 |     fprintf(stderr, "ENTER WRAP: %p\n", reel_dlopen);
25 |     fprintf(stderr, "%s:  enter dlopen:  file = %s\n", MYNAME, file);
26 | 
27 |     void *ans = reel_dlopen ? (reel_dlopen)(file, flag) : NULL;
28 |     if(!ans){
29 |       fprintf(stderr, "Real dlopen not found\n");
30 |     }
31 |     fprintf(stderr, "%s:  exit  dlopen:  handle = %p\n", MYNAME, ans);
32 | 
33 |     return ans;
34 | }
35 | void* opaque;
36 | struct gotcha_binding_t binds[] = {
37 |   { "dlopen", wrap_dlopen, &reel_dlopen_handle}
38 | };
39 | void fix_things(){
40 |   reel_dlopen_handle = NULL;
41 |   gotcha_wrap(binds, 1, "silly");
42 |   typeof(&wrap_dlopen) reel_dlopen = gotcha_get_wrappee(reel_dlopen_handle);
43 |   fprintf(stderr, "IMMEDIATE WRITE: %p\n", reel_dlopen);
44 | }
45 | __attribute__((constructor)) void startup_fix_things(){
{% endraw %}

```
### external/gotcha/test/multi_agent_dlopen/main.c

```c

{% raw %}
20 | 
21 |     fprintf(stderr, "%s:  val = %.6f\n", MYNAME, val);
22 | 
23 |     void *handle = dlopen("libm.so", RTLD_NOW);
24 |     if (handle == NULL) {
25 | 	err(1, "dlopen failed");
26 |     }
27 | 
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha_dl.h

```c

{% raw %}
7 | extern void update_all_library_gots(hash_table_t *bindings);
8 | extern int prepare_symbol(struct internal_binding_t *binding);
9 | 
10 | extern gotcha_wrappee_handle_t orig_dlopen_handle;
11 | extern gotcha_wrappee_handle_t orig_dlsym_handle;
12 | 
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha_dl.c

```c

{% raw %}
6 | 
7 | void* _dl_sym(void* handle, const char* name, void* where);
8 | 
9 | gotcha_wrappee_handle_t orig_dlopen_handle;
10 | gotcha_wrappee_handle_t orig_dlsym_handle;
11 | 
14 |    int result;
15 |    struct internal_binding_t *binding = (struct internal_binding_t *) data;
16 | 
17 |    debug_printf(3, "Trying to re-bind %s from tool %s after dlopen\n",
18 |                 binding->user_binding->name, binding->associated_binding_table->tool->tool_name);
19 |    
25 |    
26 |    result = prepare_symbol(binding);
27 |    if (result == -1) {
28 |       debug_printf(3, "Still could not prepare binding %s after dlopen\n", binding->user_binding->name);
29 |       return 0;
30 |    }
33 |    return 0;
34 | }
35 | 
36 | static void* dlopen_wrapper(const char* filename, int flags) {
37 |    typeof(&dlopen_wrapper) orig_dlopen = gotcha_get_wrappee(orig_dlopen_handle);
38 |    void *handle;
39 |    debug_printf(1, "User called dlopen(%s, 0x%x)\n", filename, (unsigned int) flags);
40 |    handle = orig_dlopen(filename,flags);
41 | 
42 |    debug_printf(2, "Searching new dlopened libraries for previously-not-found exports\n");
43 |    foreach_hash_entry(&notfound_binding_table, NULL, per_binding);
44 | 
45 |    debug_printf(2, "Updating GOT entries for new dlopened libraries\n");
46 |    update_all_library_gots(&function_hash_table);
47 |   
65 | }
66 | 
67 | struct gotcha_binding_t dl_binds[] = {
68 |   {"dlopen", dlopen_wrapper, &orig_dlopen_handle},
69 |   {"dlsym", dlsym_wrapper, &orig_dlsym_handle}
70 | };     
{% endraw %}

```
### external/caliper/ext/gotcha/src/gotcha.c

```c

{% raw %}
314 |         debug_printf(2, "Symbol %s needs lookup operation\n", binding->user_binding->name);
315 |         int presult = prepare_symbol(binding);
316 |         if (presult == -1) {
317 |            debug_printf(2, "Stashing %s in notfound_binding table to re-lookup on dlopens\n",
318 |                         binding->user_binding->name);
319 |            addto_hashtable(&notfound_binding_table, (hash_key_t) binding->user_binding->name, (hash_data_t) binding);
{% endraw %}

```