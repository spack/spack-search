---
name: "python"
layout: package
next_package: freeipmi
previous_package: etcd
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
{% endraw %}

```
### Lib/ctypes/__init__.py

```python

{% raw %}
106 |     from _ctypes import LoadLibrary as _dlopen
132 |     from _ctypes import dlopen as _dlopen
347 |             self._handle = _dlopen(self._name, mode)
{% endraw %}

```
### Python/dynload_shlib.c

```c

{% raw %}
62 |     int dlopenflags=0;
92 |     dlopenflags = PyThreadState_GET()->interp->dlopenflags;
94 |     handle = dlopen(pathname, dlopenflags);
102 |             error = "unknown dlopen() error";
{% endraw %}

```
### Python/sysmodule.c

```c

{% raw %}
1025 | sys_setdlopenflags(PyObject *self, PyObject *args)
1029 |     if (!PyArg_ParseTuple(args, "i:setdlopenflags", &new_val))
1033 |     tstate->interp->dlopenflags = new_val;
1038 | PyDoc_STRVAR(setdlopenflags_doc,
1039 | "setdlopenflags(n) -> None\n\
1041 | Set the flags used by the interpreter for dlopen calls, such as when the\n\
1044 | sys.setdlopenflags(0).  To share symbols across extension modules, call as\n\
1045 | sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag modules\n\
1049 | sys_getdlopenflags(PyObject *self, PyObject *args)
1054 |     return PyLong_FromLong(tstate->interp->dlopenflags);
1057 | PyDoc_STRVAR(getdlopenflags_doc,
1058 | "getdlopenflags() -> int\n\
1060 | Return the current value of the flags that are used for dlopen calls.\n\
1367 |     {"getdlopenflags", (PyCFunction)sys_getdlopenflags, METH_NOARGS,
1368 |      getdlopenflags_doc},
1416 |     {"setdlopenflags", sys_setdlopenflags, METH_VARARGS,
1417 |      setdlopenflags_doc},
1644 | getdlopenflags() -- returns flags to be used for dlopen() calls\n\
1651 | setdlopenflags() -- set the flags to be used for dlopen() calls\n\
{% endraw %}

```
### Python/pystate.c

```c

{% raw %}
105 |         interp->dlopenflags = RTLD_NOW;
107 |         interp->dlopenflags = RTLD_LAZY;
{% endraw %}

```
### Include/pystate.h

```c

{% raw %}
43 |     int dlopenflags;
{% endraw %}

```
### Modules/_ctypes/callproc.c

```c

{% raw %}
1362 |     if (!PyArg_ParseTuple(args, "O|i:dlopen", &name, &mode))
1376 |     handle = ctypes_dlopen(name_str, mode);
1381 |             errmsg = "dlopen() error";
1826 |     {"dlopen", py_dl_open, METH_VARARGS,
1827 |      "dlopen(name, flag={RTLD_GLOBAL|RTLD_LOCAL}) open a shared library"},
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn.h

```c

{% raw %}
55 | extern void * (*ctypes_dlopen)(const char *path, int mode);
61 | extern void * dlopen(const char *path, int mode);
{% endraw %}

```
### Modules/_ctypes/darwin/dlfcn_simple.c

```c

{% raw %}
52 | extern void * dlopen(const char *path, int mode) __attribute__((weak_import));
67 | void * (*ctypes_dlopen)(const char *path, int mode);
108 | static void *darwin_dlopen(const char *path, int mode)
254 |     if (dlopen != NULL) {
256 |         ctypes_dlopen = dlopen;
263 |         ctypes_dlopen = darwin_dlopen;
{% endraw %}

```