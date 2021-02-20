---
name: "python"
layout: package
next_package: q-e-sirius
previous_package: pythia8
languages: ['python', 'c']
---
## 3.6.12
24 / 4070 files match, 9 filtered matches.

 - [Lib/test/test_sys.py](#libtesttest_syspy)
 - [Lib/ctypes/__init__.py](#libctypes__init__py)
 - [Python/dynload_shlib.c](#pythondynload_shlibc)
 - [Python/sysmodule.c](#pythonsysmodulec)
 - [Python/pystate.c](#pythonpystatec)
 - [Include/pystate.h](#includepystateh)
 - [Modules/_ctypes/callproc.c](#modules_ctypescallprocc)
 - [Modules/_ctypes/darwin/dlfcn.h](#modules_ctypesdarwindlfcnh)
 - [Modules/_ctypes/darwin/dlfcn_simple.c](#modules_ctypesdarwindlfcn_simplec)

### Lib/test/test_sys.py

```python

{% raw %}
312 |     def test_call_tracing(self):
313 |         self.assertRaises(TypeError, sys.call_tracing, type, 2)
314 | 
315 |     @unittest.skipUnless(hasattr(sys, "setdlopenflags"),
316 |                          'test needs sys.setdlopenflags()')
317 |     def test_dlopenflags(self):
318 |         self.assertTrue(hasattr(sys, "getdlopenflags"))
319 |         self.assertRaises(TypeError, sys.getdlopenflags, 42)
320 |         oldflags = sys.getdlopenflags()
321 |         self.assertRaises(TypeError, sys.setdlopenflags)
322 |         sys.setdlopenflags(oldflags+1)
323 |         self.assertEqual(sys.getdlopenflags(), oldflags+1)
324 |         sys.setdlopenflags(oldflags)
325 | 
326 |     @test.support.refcount_test
{% endraw %}

```
### Lib/ctypes/__init__.py

```python

{% raw %}
103 |         return CFunctionType
104 | 
105 | if _os.name == "nt":
106 |     from _ctypes import LoadLibrary as _dlopen
107 |     from _ctypes import FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL
108 | 
129 |         WINFUNCTYPE.__doc__ = CFUNCTYPE.__doc__.replace("CFUNCTYPE", "WINFUNCTYPE")
130 | 
131 | elif _os.name == "posix":
132 |     from _ctypes import dlopen as _dlopen
133 | 
134 | from _ctypes import sizeof, byref, addressof, alignment, resize
344 |         self._FuncPtr = _FuncPtr
345 | 
346 |         if handle is None:
347 |             self._handle = _dlopen(self._name, mode)
348 |         else:
349 |             self._handle = handle
{% endraw %}

```
### Python/dynload_shlib.c

```c

{% raw %}
59 |     void *handle;
60 |     char funcname[258];
61 |     char pathbuf[260];
62 |     int dlopenflags=0;
63 | 
64 |     if (strchr(pathname, '/') == NULL) {
89 |         }
90 |     }
91 | 
92 |     dlopenflags = PyThreadState_GET()->interp->dlopenflags;
93 | 
94 |     handle = dlopen(pathname, dlopenflags);
95 | 
96 |     if (handle == NULL) {
99 |         PyObject *error_ob;
100 |         const char *error = dlerror();
101 |         if (error == NULL)
102 |             error = "unknown dlopen() error";
103 |         error_ob = PyUnicode_FromString(error);
104 |         if (error_ob == NULL)
{% endraw %}

```
### Python/sysmodule.c

```c

{% raw %}
1022 | 
1023 | #ifdef HAVE_DLOPEN
1024 | static PyObject *
1025 | sys_setdlopenflags(PyObject *self, PyObject *args)
1026 | {
1027 |     int new_val;
1028 |     PyThreadState *tstate = PyThreadState_GET();
1029 |     if (!PyArg_ParseTuple(args, "i:setdlopenflags", &new_val))
1030 |         return NULL;
1031 |     if (!tstate)
1032 |         return NULL;
1033 |     tstate->interp->dlopenflags = new_val;
1034 |     Py_INCREF(Py_None);
1035 |     return Py_None;
1036 | }
1037 | 
1038 | PyDoc_STRVAR(setdlopenflags_doc,
1039 | "setdlopenflags(n) -> None\n\
1040 | \n\
1041 | Set the flags used by the interpreter for dlopen calls, such as when the\n\
1042 | interpreter loads extension modules.  Among other things, this will enable\n\
1043 | a lazy resolving of symbols when importing a module, if called as\n\
1044 | sys.setdlopenflags(0).  To share symbols across extension modules, call as\n\
1045 | sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag modules\n\
1046 | can be found in the os module (RTLD_xxx constants, e.g. os.RTLD_LAZY).");
1047 | 
1048 | static PyObject *
1049 | sys_getdlopenflags(PyObject *self, PyObject *args)
1050 | {
1051 |     PyThreadState *tstate = PyThreadState_GET();
1052 |     if (!tstate)
1053 |         return NULL;
1054 |     return PyLong_FromLong(tstate->interp->dlopenflags);
1055 | }
1056 | 
1057 | PyDoc_STRVAR(getdlopenflags_doc,
1058 | "getdlopenflags() -> int\n\
1059 | \n\
1060 | Return the current value of the flags that are used for dlopen calls.\n\
1061 | The flag constants are defined in the os module.");
1062 | 
1364 |     {"getdefaultencoding", (PyCFunction)sys_getdefaultencoding,
1365 |      METH_NOARGS, getdefaultencoding_doc},
1366 | #ifdef HAVE_DLOPEN
1367 |     {"getdlopenflags", (PyCFunction)sys_getdlopenflags, METH_NOARGS,
1368 |      getdlopenflags_doc},
1369 | #endif
1370 |     {"getallocatedblocks", (PyCFunction)sys_getallocatedblocks, METH_NOARGS,
1413 |      getswitchinterval_doc},
1414 | #endif
1415 | #ifdef HAVE_DLOPEN
1416 |     {"setdlopenflags", sys_setdlopenflags, METH_VARARGS,
1417 |      setdlopenflags_doc},
1418 | #endif
1419 |     {"setprofile",      sys_setprofile, METH_O, setprofile_doc},
1641 | excepthook() -- print an exception and its traceback to sys.stderr\n\
1642 | exc_info() -- return thread-safe information about the current exception\n\
1643 | exit() -- exit the interpreter by raising SystemExit\n\
1644 | getdlopenflags() -- returns flags to be used for dlopen() calls\n\
1645 | getprofile() -- get the global profiling function\n\
1646 | getrefcount() -- return the reference count for an object (plus one :-)\n\
1648 | getsizeof() -- return the size of an object in bytes\n\
1649 | gettrace() -- get the global debug tracing function\n\
1650 | setcheckinterval() -- control how often the interpreter checks for events\n\
1651 | setdlopenflags() -- set the flags to be used for dlopen() calls\n\
1652 | setprofile() -- set the global profiling function\n\
1653 | setrecursionlimit() -- set the max recursion depth for the interpreter\n\
{% endraw %}

```
### Python/pystate.c

```c

{% raw %}
102 |         coextra->interp = interp;
103 | #ifdef HAVE_DLOPEN
104 | #if HAVE_DECL_RTLD_NOW
105 |         interp->dlopenflags = RTLD_NOW;
106 | #else
107 |         interp->dlopenflags = RTLD_LAZY;
108 | #endif
109 | #endif
{% endraw %}

```
### Include/pystate.h

```c

{% raw %}
40 |     int fscodec_initialized;
41 | 
42 | #ifdef HAVE_DLOPEN
43 |     int dlopenflags;
44 | #endif
45 | 
{% endraw %}

```
### Modules/_ctypes/callproc.c

```c

{% raw %}
1359 |     /* cygwin doesn't define RTLD_LOCAL */
1360 |     int mode = RTLD_NOW;
1361 | #endif
1362 |     if (!PyArg_ParseTuple(args, "O|i:dlopen", &name, &mode))
1363 |         return NULL;
1364 |     mode |= RTLD_NOW;
1373 |         name_str = NULL;
1374 |         name2 = NULL;
1375 |     }
1376 |     handle = ctypes_dlopen(name_str, mode);
1377 |     Py_XDECREF(name2);
1378 |     if (!handle) {
1379 |         char *errmsg = ctypes_dlerror();
1380 |         if (!errmsg)
1381 |             errmsg = "dlopen() error";
1382 |         PyErr_SetString(PyExc_OSError,
1383 |                                errmsg);
1823 |     {"FreeLibrary", free_library, METH_VARARGS, free_library_doc},
1824 |     {"_check_HRESULT", check_hresult, METH_VARARGS},
1825 | #else
1826 |     {"dlopen", py_dl_open, METH_VARARGS,
1827 |      "dlopen(name, flag={RTLD_GLOBAL|RTLD_LOCAL}) open a shared library"},
1828 |     {"dlclose", py_dl_close, METH_VARARGS, "dlclose a library"},
1829 |     {"dlsym", py_dl_sym, METH_VARARGS, "find symbol in shared library"},
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn.h

```c

{% raw %}
52 | #if MAC_OS_X_VERSION_MIN_REQUIRED <= MAC_OS_X_VERSION_10_2
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
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn_simple.c

```c

{% raw %}
49 | 
50 | #if MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_3
51 | #define DARWIN_HAS_DLOPEN
52 | extern void * dlopen(const char *path, int mode) __attribute__((weak_import));
53 | extern void * dlsym(void * handle, const char *symbol) __attribute__((weak_import));
54 | extern const char * dlerror(void) __attribute__((weak_import));
64 | #define dladdr darwin_dladdr
65 | #endif
66 | 
67 | void * (*ctypes_dlopen)(const char *path, int mode);
68 | void * (*ctypes_dlsym)(void * handle, const char *symbol);
69 | const char * (*ctypes_dlerror)(void);
105 | }
106 | 
107 | /* darwin_dlopen */
108 | static void *darwin_dlopen(const char *path, int mode)
109 | {
110 |     void *module = 0;
251 | static
252 | #endif
253 | void ctypes_dlfcn_init(void) {
254 |     if (dlopen != NULL) {
255 |         ctypes_dlsym = dlsym;
256 |         ctypes_dlopen = dlopen;
257 |         ctypes_dlerror = dlerror;
258 |         ctypes_dlclose = dlclose;
260 |     } else {
261 | #if MAC_OS_X_VERSION_MIN_REQUIRED < MAC_OS_X_VERSION_10_3
262 |         ctypes_dlsym = darwin_dlsym;
263 |         ctypes_dlopen = darwin_dlopen;
264 |         ctypes_dlerror = darwin_dlerror;
265 |         ctypes_dlclose = darwin_dlclose;
{% endraw %}

```