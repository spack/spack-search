---
name: "erlang"
layout: package
next_package: parsec
previous_package: varnish-cache
languages: ['c']
---
## 22.0
15 / 10600 files match

 - [erts/emulator/sys/unix/erl_unix_sys_ddll.c](#ertsemulatorsysunixerl_unix_sys_ddllc)
 - [erts/emulator/test/nif_SUITE_data/nif_api_2_4/erl_nif_api_funcs.h](#ertsemulatortestnif_suite_datanif_api_2_4erl_nif_api_funcsh)
 - [erts/emulator/beam/erl_nif.c](#ertsemulatorbeamerl_nifc)
 - [erts/emulator/beam/erl_nif_api_funcs.h](#ertsemulatorbeamerl_nif_api_funcsh)
 - [lib/crypto/c_src/crypto.c](#libcryptoc_srccryptoc)

### erts/emulator/sys/unix/erl_unix_sys_ddll.c

```c

{% raw %}
94 |     void *handle = dlopen("/nonexistinglib", RTLD_NOW);
130 |     if ((*handle = dlopen(dlname, RTLD_NOW)) == NULL) {
{% endraw %}

```
### erts/emulator/test/nif_SUITE_data/nif_api_2_4/erl_nif_api_funcs.h

```c

{% raw %}
140 | ERL_NIF_API_FUNC_DECL(void*,enif_dlopen,(const char* lib, void (*err_handler)(void*,const char*), void* err_arg));
{% endraw %}

```
### erts/emulator/beam/erl_nif.c

```c

{% raw %}
77 |     void* handle;             /* "dlopen" */
2767 | void* enif_dlopen(const char* lib,
{% endraw %}

```
### erts/emulator/beam/erl_nif_api_funcs.h

```c

{% raw %}
141 | ERL_NIF_API_FUNC_DECL(void*,enif_dlopen,(const char* lib, void (*err_handler)(void*,const char*), void* err_arg));
{% endraw %}

```
### lib/crypto/c_src/crypto.c

```c

{% raw %}
210 |     if ((handle = enif_dlopen(lib_buf, &error_handler, NULL)) == NULL)
{% endraw %}

```