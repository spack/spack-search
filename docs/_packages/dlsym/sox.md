---
name: "sox"
layout: package
next_package: libpam
previous_package: pmdk
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 14.4.2
8 / 361 files match, 6 filtered matches.

 - [src/formats.c](#srcformatsc)
 - [src/win32-ltdl.h](#srcwin32-ltdlh)
 - [src/ladspa.c](#srcladspac)
 - [src/util.c](#srcutilc)
 - [src/win32-ltdl.c](#srcwin32-ltdlc)
 - [src/sox_i.h](#srcsox_ih)

### src/formats.c

```c

{% raw %}
1202 |           "lsx_%.*s_format_fn", (int)(end - start), start);
1203 |       if (ret > 0 && ret < (int)MAX_NAME_LEN) {
1204 |         union {sox_format_fn_t fn; lt_ptr ptr;} ltptr;
1205 |         ltptr.ptr = lt_dlsym(lth, fnname);
1206 |         lsx_debug("opening format plugin `%s': library %p, entry point %p\n",
1207 |             fnname, (void *)lth, ltptr.ptr);
{% endraw %}

```
### src/win32-ltdl.h

```c

{% raw %}
52 |   const char *szFileName);
53 | 
54 | lt_ptr
55 | lt_dlsym(
56 |   lt_dlhandle hModule,
57 |   const char *szSymbolName);
{% endraw %}

```
### src/ladspa.c

```c

{% raw %}
136 |   }
137 | 
138 |   /* Get descriptor function */
139 |   if ((ltptr.ptr = lt_dlsym(l_st->lth, "ladspa_descriptor")) == NULL) {
140 |     lsx_fail("could not find ladspa_descriptor");
141 |     return SOX_EOF;
{% endraw %}

```
### src/util.c

```c

{% raw %}
185 |         for (i = 0; func_infos[i].name; i++)
186 |         {
187 |           union {lsx_dlptr fn; lt_ptr ptr;} func;
188 |           func.ptr = lt_dlsym(dl, func_infos[i].name);
189 |           selected_funcs[i] = func.fn ? func.fn : func_infos[i].stub_func;
190 |           if (!selected_funcs[i])
{% endraw %}

```
### src/win32-ltdl.c

```c

{% raw %}
355 | }
356 | 
357 | lt_ptr
358 | lt_dlsym(
359 |     lt_dlhandle hModule,
360 |     const char *szSymbolName)
{% endraw %}

```
### src/sox_i.h

```c

{% raw %}
395 | 
396 |   /* LSX_DLENTRY_DYNAMIC: For use in creating an ENTRIES macro. func need
397 |      not be available at link time (and if present, the link time version will
398 |      not be used). func will be loaded via dlsym. If this function is not
399 |      found in the shared library, the shared library will not be used. */
400 | #define LSX_DLENTRY_DYNAMIC(f,x, ret, func, args) f(x, ret, func, args, NULL, NULL, func)
401 | 
402 |   /* LSX_DLENTRY_STUB: For use in creating an ENTRIES macro. func need not
403 |      be available at link time (and if present, the link time version will not
404 |      be used). If using DL_LAME, the func may be loaded via dlopen/dlsym, but
405 |      if not found, the shared library will still be used if all of the
406 |      non-stub functions are found. If the function is not found via dlsym (or
407 |      if we are not loading any shared libraries), the stub will be used. This
408 |      assumes that the name of the stub function is the name of the function +
{% endraw %}

```