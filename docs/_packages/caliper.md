---
name: "caliper"
layout: package
next_package: cardioid
previous_package: cairo
languages: ['c']
---
## master
4 / 597 files match, 3 filtered matches.

 - [ext/gotcha/src/gotcha_dl.h](#extgotchasrcgotcha_dlh)
 - [ext/gotcha/src/gotcha_dl.c](#extgotchasrcgotcha_dlc)
 - [ext/gotcha/src/gotcha.c](#extgotchasrcgotchac)

### ext/gotcha/src/gotcha_dl.h

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
### ext/gotcha/src/gotcha_dl.c

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
### ext/gotcha/src/gotcha.c

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