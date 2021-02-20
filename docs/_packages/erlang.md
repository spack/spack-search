---
name: "erlang"
layout: package
next_package: ermod
previous_package: energyplus
languages: ['c']
---
## 22.0
15 / 10600 files match, 5 filtered matches.

 - [erts/emulator/sys/unix/erl_unix_sys_ddll.c](#ertsemulatorsysunixerl_unix_sys_ddllc)
 - [erts/emulator/test/nif_SUITE_data/nif_api_2_4/erl_nif_api_funcs.h](#ertsemulatortestnif_suite_datanif_api_2_4erl_nif_api_funcsh)
 - [erts/emulator/beam/erl_nif.c](#ertsemulatorbeamerl_nifc)
 - [erts/emulator/beam/erl_nif_api_funcs.h](#ertsemulatorbeamerl_nif_api_funcsh)
 - [lib/crypto/c_src/crypto.c](#libcryptoc_srccryptoc)

### erts/emulator/sys/unix/erl_unix_sys_ddll.c

```c

{% raw %}
91 |      * dlerror(); otherwise, dlerror() might dump core. At least
92 |      * some versions of linuxthread suffer from this bug.
93 |      */
94 |     void *handle = dlopen("/nonexistinglib", RTLD_NOW);
95 |     if (handle)
96 | 	dlclose(handle);
127 |     int ret = ERL_DE_NO_ERROR;
128 |     char *str;
129 |     dlerror();
130 |     if ((*handle = dlopen(dlname, RTLD_NOW)) == NULL) {
131 | 	str = dlerror();
132 | 
{% endraw %}

```
### erts/emulator/test/nif_SUITE_data/nif_api_2_4/erl_nif_api_funcs.h

```c

{% raw %}
137 | ERL_NIF_API_FUNC_DECL(int,enif_is_exception,(ErlNifEnv*, ERL_NIF_TERM term));
138 | ERL_NIF_API_FUNC_DECL(int,enif_make_reverse_list,(ErlNifEnv*, ERL_NIF_TERM term, ERL_NIF_TERM *list));
139 | ERL_NIF_API_FUNC_DECL(int,enif_is_number,(ErlNifEnv*, ERL_NIF_TERM term));
140 | ERL_NIF_API_FUNC_DECL(void*,enif_dlopen,(const char* lib, void (*err_handler)(void*,const char*), void* err_arg));
141 | ERL_NIF_API_FUNC_DECL(void*,enif_dlsym,(void* handle, const char* symbol, void (*err_handler)(void*,const char*), void* err_arg));
142 | ERL_NIF_API_FUNC_DECL(int,enif_consume_timeslice,(ErlNifEnv*, int percent));
{% endraw %}

```
### erts/emulator/beam/erl_nif.c

```c

{% raw %}
74 |  */
75 | struct erl_module_nif {
76 |     void* priv_data;
77 |     void* handle;             /* "dlopen" */
78 |     struct enif_entry_t entry;
79 |     erts_refc_t rt_cnt;       /* number of resource types */
2764 | }
2765 | 
2766 | 
2767 | void* enif_dlopen(const char* lib,
2768 | 		  void (*err_handler)(void*,const char*), void* err_arg)
2769 | {
{% endraw %}

```
### erts/emulator/beam/erl_nif_api_funcs.h

```c

{% raw %}
138 | ERL_NIF_API_FUNC_DECL(int,enif_is_exception,(ErlNifEnv*, ERL_NIF_TERM term));
139 | ERL_NIF_API_FUNC_DECL(int,enif_make_reverse_list,(ErlNifEnv*, ERL_NIF_TERM term, ERL_NIF_TERM *list));
140 | ERL_NIF_API_FUNC_DECL(int,enif_is_number,(ErlNifEnv*, ERL_NIF_TERM term));
141 | ERL_NIF_API_FUNC_DECL(void*,enif_dlopen,(const char* lib, void (*err_handler)(void*,const char*), void* err_arg));
142 | ERL_NIF_API_FUNC_DECL(void*,enif_dlsym,(void* handle, const char* symbol, void (*err_handler)(void*,const char*), void* err_arg));
143 | ERL_NIF_API_FUNC_DECL(int,enif_consume_timeslice,(ErlNifEnv*, int percent));
{% endraw %}

```
### lib/crypto/c_src/crypto.c

```c

{% raw %}
207 | #ifdef HAVE_DYNAMIC_CRYPTO_LIB
208 |     if (!change_basename(&lib_bin, lib_buf, sizeof(lib_buf), crypto_callback_name))
209 |         return __LINE__;
210 |     if ((handle = enif_dlopen(lib_buf, &error_handler, NULL)) == NULL)
211 |         return __LINE__;
212 |     if ((funcp = (get_crypto_callbacks_t*) enif_dlsym(handle, "get_crypto_callbacks",
{% endraw %}

```