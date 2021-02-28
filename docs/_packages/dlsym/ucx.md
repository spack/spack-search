---
name: "ucx"
layout: package
next_package: boost
previous_package: lua
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 1.4.0
7 / 590 files match, 4 filtered matches.

 - [src/ucm/util/reloc.c](#srcucmutilrelocc)
 - [src/ucs/debug/debug.c](#srcucsdebugdebugc)
 - [test/mpi/test_memhooks.c](#testmpitest_memhooksc)
 - [test/gtest/ucs/test_debug.cc](#testgtestucstest_debugcc)

### src/ucm/util/reloc.c

```c

{% raw %}
307 |     const char *error;
308 |     void *func_ptr;
309 | 
310 |     func_ptr = dlsym(RTLD_NEXT, symbol);
311 |     if (func_ptr == NULL) {
312 |         (void)dlerror();
313 |         func_ptr = dlsym(RTLD_DEFAULT, symbol);
314 |         if (func_ptr == replacement) {
315 |             error = dlerror();
{% endraw %}

```
### src/ucs/debug/debug.c

```c

{% raw %}
1019 | {
1020 |     void *func_ptr;
1021 | 
1022 |     func_ptr = dlsym(RTLD_NEXT, symbol);
1023 |     if (func_ptr == NULL) {
1024 |         func_ptr = dlsym(RTLD_DEFAULT, symbol);
1025 |     }
1026 |     return func_ptr;
{% endraw %}

```
### test/mpi/test_memhooks.c

```c

{% raw %}
27 |     do { \
28 |         char *error; \
29 |         dlerror(); /* clear existing errors */ \
30 |         func = dlsym(dl, func_name); \
31 |         if (((error = dlerror()) != NULL) || (func == NULL)) { \
32 |             error = error ? error : "not found"; \
{% endraw %}

```
### test/gtest/ucs/test_debug.cc

```cpp

{% raw %}
45 |     const char sym[] = "ucs_log_flush";
46 | 
47 |     ucs_debug_address_info info;
48 |     ucs_status_t status = ucs_debug_lookup_address(dlsym(RTLD_DEFAULT, sym), &info);
49 |     ASSERT_UCS_OK(status);
50 | 
{% endraw %}

```