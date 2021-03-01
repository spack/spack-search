---
name: "pnmpi"
layout: package
next_package: pocl
previous_package: pmix
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.7
3 / 294 files match, 3 filtered matches.

 - [src/pnmpi/core.h](#srcpnmpicoreh)
 - [src/pnmpi/core.c](#srcpnmpicorec)
 - [externals/adept-utils/cutils/test.c](#externalsadept-utilscutilstestc)

### src/pnmpi/core.h

```c

{% raw %}
181 |  */
182 | #ifdef RTLD_NEXT
183 | #define RTLDNEXT_RETRIEVAL(r_type, routine) \
184 |   r_type __tmp_function_ptr = (r_type)dlsym(RTLD_NEXT, routine);
185 | #define RTLDNEXT_CHECK(stack) pnmpi_function_ptrs.stack[i] != __tmp_function_ptr
186 | #else
{% endraw %}

```
### src/pnmpi/core.c

```c

{% raw %}
183 | PNMPI_INTERNAL
184 | void *find_symbol(const module_def_p module, const char *symbol_name)
185 | {
186 |   void *symbol = dlsym(module->handle, symbol_name);
187 | 
188 | #ifdef HAVE_ADEPT_UTILS
{% endraw %}

```
### externals/adept-utils/cutils/test.c

```c

{% raw %}
4 | 
5 | #define printsymbol(symbol) \
6 |   { \
7 |     void *mysym = dlsym(RTLD_NEXT, #symbol); \
8 |     struct link_map *map = get_module_for_address(mysym); \
9 |     printf("module for " #symbol "(%#tx): %#tx(%s)\n", mysym, map->l_addr, map->l_name); \
16 | 
17 |   printsymbol(printf);
18 |   printsymbol(malloc);
19 |   printsymbol(dlsym);
20 | 
21 | 
{% endraw %}

```