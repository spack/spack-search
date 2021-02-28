---
name: "hashcat"
layout: package
next_package: libfuse
previous_package: gettext
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.0.0
2 / 1181 files match, 2 filtered matches.

 - [src/dynloader.c](#srcdynloaderc)
 - [include/dynloader.h](#includedynloaderh)

### src/dynloader.c

```c

{% raw %}
17 |   return FreeLibrary (hLibModule);
18 | }
19 | 
20 | FARPROC hc_dlsym (HMODULE hModule, LPCSTR lpProcName)
21 | {
22 |   return GetProcAddress (hModule, lpProcName);
34 |   return dlclose (handle);
35 | }
36 | 
37 | void *hc_dlsym (void *module, const char *symbol)
38 | {
39 |   return dlsym (module, symbol);
40 | }
41 | 
{% endraw %}

```
### include/dynloader.h

```c

{% raw %}
19 | #ifdef _WIN
20 | HMODULE hc_dlopen  (LPCSTR lpLibFileName);
21 | BOOL    hc_dlclose (HMODULE hLibModule);
22 | FARPROC hc_dlsym   (HMODULE hModule, LPCSTR lpProcName);
23 | #else
24 | void *hc_dlopen  (const char *fileName, int flag);
25 | int   hc_dlclose (void *handle);
26 | void *hc_dlsym   (void *module, const char *symbol);
27 | #endif
28 | 
29 | #define HC_LOAD_FUNC2(ptr,name,type,var,libname,noerr) \
30 |   ptr->name = (type) hc_dlsym (ptr->var, #name); \
31 |   if (noerr != -1) { \
32 |     if (!ptr->name) { \
42 |   }
43 | 
44 | #define HC_LOAD_FUNC(ptr,name,type,libname,noerr) \
45 |   ptr->name = (type) hc_dlsym (ptr->lib, #name); \
46 |   if (noerr != -1) { \
47 |     if (!ptr->name) { \
{% endraw %}

```