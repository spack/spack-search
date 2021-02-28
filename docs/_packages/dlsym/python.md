---
name: "python"
layout: package
next_package: bazel
previous_package: sandbox
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.6.12
9 / 4070 files match, 5 filtered matches.

 - [Python/dynload_shlib.c](#pythondynload_shlibc)
 - [Modules/_ctypes/_ctypes.c](#modules_ctypes_ctypesc)
 - [Modules/_ctypes/callproc.c](#modules_ctypescallprocc)
 - [Modules/_ctypes/darwin/dlfcn.h](#modules_ctypesdarwindlfcnh)
 - [Modules/_ctypes/darwin/dlfcn_simple.c](#modules_ctypesdarwindlfcn_simplec)

### Python/dynload_shlib.c

```c

{% raw %}
78 |         for (i = 0; i < nhandles; i++) {
79 |             if (status.st_dev == handles[i].dev &&
80 |                 status.st_ino == handles[i].ino) {
81 |                 p = (dl_funcptr) dlsym(handles[i].handle,
82 |                                        funcname);
83 |                 return p;
122 |     }
123 |     if (fp != NULL && nhandles < 128)
124 |         handles[nhandles++].handle = handle;
125 |     p = (dl_funcptr) dlsym(handle, funcname);
126 |     return p;
127 | }
{% endraw %}

```
### Modules/_ctypes/_ctypes.c

```c

{% raw %}
675 |         return NULL;
676 |     }
677 | #else
678 |     address = (void *)ctypes_dlsym(handle, name);
679 |     if (!address) {
680 | #ifdef __CYGWIN__
3395 |         return NULL;
3396 |     }
3397 | #else
3398 |     address = (PPROC)ctypes_dlsym(handle, name);
3399 |     if (!address) {
3400 | #ifdef __CYGWIN__
{% endraw %}

```
### Modules/_ctypes/callproc.c

```c

{% raw %}
1407 |     void *handle;
1408 |     void *ptr;
1409 | 
1410 |     if (!PyArg_ParseTuple(args, "O&s:dlsym",
1411 |                           &_parse_voidp, &handle, &name))
1412 |         return NULL;
1413 |     ptr = ctypes_dlsym((void*)handle, name);
1414 |     if (!ptr) {
1415 |         PyErr_SetString(PyExc_OSError,
1826 |     {"dlopen", py_dl_open, METH_VARARGS,
1827 |      "dlopen(name, flag={RTLD_GLOBAL|RTLD_LOCAL}) open a shared library"},
1828 |     {"dlclose", py_dl_close, METH_VARARGS, "dlclose a library"},
1829 |     {"dlsym", py_dl_sym, METH_VARARGS, "find symbol in shared library"},
1830 | #endif
1831 |     {"alignment", align_func, METH_O, alignment_doc},
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn.h

```c

{% raw %}
53 | #warning CTYPES_DARWIN_DLFCN
54 | #define CTYPES_DARWIN_DLFCN
55 | extern void * (*ctypes_dlopen)(const char *path, int mode);
56 | extern void * (*ctypes_dlsym)(void * handle, const char *symbol);
57 | extern const char * (*ctypes_dlerror)(void);
58 | extern int (*ctypes_dlclose)(void * handle);
59 | extern int (*ctypes_dladdr)(const void *, Dl_info *);
60 | #else
61 | extern void * dlopen(const char *path, int mode);
62 | extern void * dlsym(void * handle, const char *symbol);
63 | extern const char * dlerror(void);
64 | extern int dlclose(void * handle);
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn_simple.c

```c

{% raw %}
50 | #if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
51 | #define DARWIN_HAS_DLOPEN
52 | extern void * dlopen(const char *path, int mode) __attribute__((weak_import));
53 | extern void * dlsym(void * handle, const char *symbol) __attribute__((weak_import));
54 | extern const char * dlerror(void) __attribute__((weak_import));
55 | extern int dlclose(void * handle) __attribute__((weak_import));
65 | #endif
66 | 
67 | void * (*ctypes_dlopen)(const char *path, int mode);
68 | void * (*ctypes_dlsym)(void * handle, const char *symbol);
69 | const char * (*ctypes_dlerror)(void);
70 | int (*ctypes_dlclose)(void * handle);
73 | #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_3
74 | /* Mac OS X 10.3+ has dlopen, so strip all this dead code to avoid warnings */
75 | 
76 | static void *dlsymIntern(void *handle, const char *symbol);
77 | 
78 | static const char *error(int setget, const char *str, ...);
144 | }
145 | 
146 | /* dlsymIntern is used by dlsym to find the symbol */
147 | static void *dlsymIntern(void *handle, const char *symbol)
148 | {
149 |     NSSymbol nssym = 0;
210 | 
211 | 
212 | /* dlsym, prepend the underscore and call dlsymIntern */
213 | static void *darwin_dlsym(void *handle, const char *symbol)
214 | {
215 |     static char undersym[257];          /* Saves calls to malloc(3) */
220 |     if (sym_len < 256)
221 |     {
222 |         snprintf(undersym, 256, "_%s", symbol);
223 |         value = dlsymIntern(handle, undersym);
224 |     }
225 |     else
228 |         if (malloc_sym)
229 |         {
230 |             sprintf(malloc_sym, "_%s", symbol);
231 |             value = dlsymIntern(handle, malloc_sym);
232 |             free(malloc_sym);
233 |         }
252 | #endif
253 | void ctypes_dlfcn_init(void) {
254 |     if (dlopen != NULL) {
255 |         ctypes_dlsym = dlsym;
256 |         ctypes_dlopen = dlopen;
257 |         ctypes_dlerror = dlerror;
259 |         ctypes_dladdr = dladdr;
260 |     } else {
261 | #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_3
262 |         ctypes_dlsym = darwin_dlsym;
263 |         ctypes_dlopen = darwin_dlopen;
264 |         ctypes_dlerror = darwin_dlerror;
{% endraw %}

```