---
name: "erlang"
layout: package
next_package: lua
previous_package: mono
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 22.0
32 / 10600 files match, 7 filtered matches.

 - [erts/emulator/sys/common/erl_mtrace_sys_wrap.c](#ertsemulatorsyscommonerl_mtrace_sys_wrapc)
 - [erts/emulator/sys/unix/erl_unix_sys_ddll.c](#ertsemulatorsysunixerl_unix_sys_ddllc)
 - [erts/emulator/test/nif_SUITE_data/nif_api_2_4/erl_nif_api_funcs.h](#ertsemulatortestnif_suite_datanif_api_2_4erl_nif_api_funcsh)
 - [erts/emulator/hipe/hipe_x86_signal.c](#ertsemulatorhipehipe_x86_signalc)
 - [erts/emulator/beam/erl_nif.c](#ertsemulatorbeamerl_nifc)
 - [erts/emulator/beam/erl_nif_api_funcs.h](#ertsemulatorbeamerl_nif_api_funcsh)
 - [lib/crypto/c_src/crypto.c](#libcryptoc_srccryptoc)

### erts/emulator/sys/common/erl_mtrace_sys_wrap.c

```c

{% raw %}
148 | #define INIT_XBRK_SYM(SYM)			\
149 | do {						\
150 |     if (!real_ ## SYM) {			\
151 | 	real_ ## SYM = dlsym(RTLD_NEXT, #SYM);	\
152 | 	if (!real_ ## SYM) {			\
153 | 	    errno = ENOMEM;			\
{% endraw %}

```
### erts/emulator/sys/unix/erl_unix_sys_ddll.c

```c

{% raw %}
165 |     char *e;
166 |     int ret;
167 |     dlerror();
168 |     sym = dlsym(handle, func_name);
169 |     if ((e = dlerror()) != NULL) {
170 | 	ret = ERL_DE_DYNAMIC_ERROR_OFFSET - find_errcode(e, err);
{% endraw %}

```
### erts/emulator/test/nif_SUITE_data/nif_api_2_4/erl_nif_api_funcs.h

```c

{% raw %}
138 | ERL_NIF_API_FUNC_DECL(int,enif_make_reverse_list,(ErlNifEnv*, ERL_NIF_TERM term, ERL_NIF_TERM *list));
139 | ERL_NIF_API_FUNC_DECL(int,enif_is_number,(ErlNifEnv*, ERL_NIF_TERM term));
140 | ERL_NIF_API_FUNC_DECL(void*,enif_dlopen,(const char* lib, void (*err_handler)(void*,const char*), void* err_arg));
141 | ERL_NIF_API_FUNC_DECL(void*,enif_dlsym,(void* handle, const char* symbol, void (*err_handler)(void*,const char*), void* err_arg));
142 | ERL_NIF_API_FUNC_DECL(int,enif_consume_timeslice,(ErlNifEnv*, int percent));
143 | 
{% endraw %}

```
### erts/emulator/hipe/hipe_x86_signal.c

```c

{% raw %}
182 | static int (*next_sigaction)(int, const struct sigaction*, struct sigaction*);
183 | static void do_init(void)
184 | {
185 |     next_sigaction = dlsym(RTLD_NEXT, NEXT_SIGACTION);
186 |     if (next_sigaction != 0)
187 | 	return;
188 |     perror("dlsym");
189 |     abort();
190 | }
{% endraw %}

```
### erts/emulator/beam/erl_nif.c

```c

{% raw %}
2785 |     return handle;
2786 | }
2787 | 
2788 | void* enif_dlsym(void* handle, const char* symbol,
2789 | 		 void (*err_handler)(void*,const char*), void* err_arg)
2790 | {
{% endraw %}

```
### erts/emulator/beam/erl_nif_api_funcs.h

```c

{% raw %}
139 | ERL_NIF_API_FUNC_DECL(int,enif_make_reverse_list,(ErlNifEnv*, ERL_NIF_TERM term, ERL_NIF_TERM *list));
140 | ERL_NIF_API_FUNC_DECL(int,enif_is_number,(ErlNifEnv*, ERL_NIF_TERM term));
141 | ERL_NIF_API_FUNC_DECL(void*,enif_dlopen,(const char* lib, void (*err_handler)(void*,const char*), void* err_arg));
142 | ERL_NIF_API_FUNC_DECL(void*,enif_dlsym,(void* handle, const char* symbol, void (*err_handler)(void*,const char*), void* err_arg));
143 | ERL_NIF_API_FUNC_DECL(int,enif_consume_timeslice,(ErlNifEnv*, int percent));
144 | ERL_NIF_API_FUNC_DECL(int, enif_is_map, (ErlNifEnv* env, ERL_NIF_TERM term));
{% endraw %}

```
### lib/crypto/c_src/crypto.c

```c

{% raw %}
209 |         return __LINE__;
210 |     if ((handle = enif_dlopen(lib_buf, &error_handler, NULL)) == NULL)
211 |         return __LINE__;
212 |     if ((funcp = (get_crypto_callbacks_t*) enif_dlsym(handle, "get_crypto_callbacks",
213 |                                                        &error_handler, NULL)) == NULL)
214 |         return __LINE__;
{% endraw %}

```