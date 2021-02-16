---
name: "py-cffi"
layout: package
next_package: py-chainer
previous_package: py-billiard
languages: ['python', 'c']
---
## 1.13.0
30 / 183 files match, 23 filtered matches.

 - [demo/manual2.py](#demomanual2py)
 - [demo/readdir.py](#demoreaddirpy)
 - [demo/cffi-cocoa.py](#democffi-cocoapy)
 - [testing/cffi1/test_verify1.py](#testingcffi1test_verify1py)
 - [testing/cffi1/test_dlopen_unicode_literals.py](#testingcffi1test_dlopen_unicode_literalspy)
 - [testing/cffi1/test_re_python.py](#testingcffi1test_re_pythonpy)
 - [testing/cffi0/test_parsing.py](#testingcffi0test_parsingpy)
 - [testing/cffi0/test_unicode_literals.py](#testingcffi0test_unicode_literalspy)
 - [testing/cffi0/test_function.py](#testingcffi0test_functionpy)
 - [testing/cffi0/backend_tests.py](#testingcffi0backend_testspy)
 - [testing/cffi0/test_ffi_backend.py](#testingcffi0test_ffi_backendpy)
 - [testing/cffi0/test_ownlib.py](#testingcffi0test_ownlibpy)
 - [testing/cffi0/test_verify.py](#testingcffi0test_verifypy)
 - [cffi/api.py](#cffiapipy)
 - [cffi/vengine_cpy.py](#cffivengine_cpypy)
 - [cffi/verifier.py](#cffiverifierpy)
 - [c/ffi_obj.c](#cffi_objc)
 - [c/_cffi_backend.c](#c_cffi_backendc)
 - [c/lib_obj.c](#clib_objc)
 - [c/test_c.py](#ctest_cpy)
 - [c/cffi1_module.c](#ccffi1_modulec)
 - [c/cdlopen.c](#ccdlopenc)
 - [c/misc_win32.h](#cmisc_win32h)

### demo/manual2.py

```python

{% raw %}
14 | lib = ffi.dlopen(None)
{% endraw %}

```
### demo/readdir.py

```python

{% raw %}
8 | lib = ffi.dlopen(None)
{% endraw %}

```
### demo/cffi-cocoa.py

```python

{% raw %}
50 | objc = ffi.dlopen('objc')
51 | appkit = ffi.dlopen('AppKit')
{% endraw %}

```
### testing/cffi1/test_verify1.py

```python

{% raw %}
2095 |     lib = ffi.dlopen("Kernel32.dll")
2103 | def test_verify_dlopen_flags():
2104 |     if not hasattr(sys, 'setdlopenflags'):
2105 |         py.test.skip("requires sys.setdlopenflags()")
2110 |     old = sys.getdlopenflags()
2113 |         ffi1.cdef("int foo_verify_dlopen_flags_1;")
2114 |         sys.setdlopenflags(ffi1.RTLD_GLOBAL | ffi1.RTLD_NOW)
2115 |         lib1 = ffi1.verify("int foo_verify_dlopen_flags_1;")
2117 |         sys.setdlopenflags(old)
2122 |         extern int foo_verify_dlopen_flags_1;
2123 |         static int *getptr(void) { return &foo_verify_dlopen_flags_1; }
2126 |     assert ffi1.addressof(lib1, 'foo_verify_dlopen_flags_1') == p
{% endraw %}

```
### testing/cffi1/test_dlopen_unicode_literals.py

```python

{% raw %}
5 | with open(os.path.join(os.path.dirname(__file__), 'test_dlopen.py')) as f:
{% endraw %}

```
### testing/cffi1/test_re_python.py

```python

{% raw %}
98 |     lib = ffi.dlopen(extmod)
105 |     lib = ffi.dlopen(extmod, 0)
109 | def test_dlopen_none():
117 |             py.test.skip("dlopen(None) cannot work on Windows with Python 3")
118 |     lib = ffi.dlopen(name)
124 |     lib = ffi.dlopen(extmod)
137 |     lib = ffi.dlopen(extmod)
177 |     lib = ffi.dlopen(extmod)     # <- a random unrelated library would be fine
187 |     lib = ffi.dlopen(extmod)
197 |     lib = ffi.dlopen(extmod)
203 |     lib = ffi.dlopen(extmod)
215 |     lib = ffi.dlopen(extmod)
{% endraw %}

```
### testing/cffi0/test_parsing.py

```python

{% raw %}
2 | from .backend_tests import needs_dlopen_none
86 |     m = ffi.dlopen(lib_m)
94 |     needs_dlopen_none()
95 |     C = ffi.dlopen(None)
103 |     needs_dlopen_none()
104 |     C = ffi.dlopen(None)
114 |     needs_dlopen_none()
115 |     C = ffi.dlopen(None)
125 |     needs_dlopen_none()
126 |     C = ffi.dlopen(None)
136 |     needs_dlopen_none()
137 |     C = ffi.dlopen(None)
165 |     m = ffi.dlopen(lib_m)
182 |     m = ffi.dlopen(lib_m)
195 |     m = ffi.dlopen(lib_m)
226 |     needs_dlopen_none()
227 |     C = ffi.dlopen(None)
423 |     needs_dlopen_none()
424 |     C = ffi.dlopen(None)
514 |     needs_dlopen_none()
515 |     C = ffi.dlopen(None)
{% endraw %}

```
### testing/cffi0/test_unicode_literals.py

```python

{% raw %}
61 | def test_dlopen():
64 |     m = ffi.dlopen(lib_m)                           # unicode literal
{% endraw %}

```
### testing/cffi0/test_function.py

```python

{% raw %}
8 | from .backend_tests import needs_dlopen_none
31 |         m = ffi.dlopen(lib_m)
42 |         m = ffi.dlopen(lib_m)
54 |         needs_dlopen_none()
55 |         m = ffi.dlopen(None)
59 |     def test_dlopen_filename(self):
67 |         m = ffi.dlopen(path)
71 |         m = ffi.dlopen(os.path.basename(path))
75 |     def test_dlopen_flags(self):
80 |         m = ffi.dlopen(lib_m, ffi.RTLD_LAZY | ffi.RTLD_LOCAL)
84 |     def test_dlopen_constant(self):
91 |         m = ffi.dlopen(lib_m)
103 |         lib = ffi.dlopen('KERNEL32.DLL')
117 |         needs_dlopen_none()
118 |         ffi.C = ffi.dlopen(None)
134 |         needs_dlopen_none()
135 |         ffi.C = ffi.dlopen(None)
151 |         needs_dlopen_none()
152 |         ffi.C = ffi.dlopen(None)
178 |         needs_dlopen_none()
179 |         ffi.C = ffi.dlopen(None)
189 |         needs_dlopen_none()
190 |         ffi.C = ffi.dlopen(None)
213 |         needs_dlopen_none()
214 |         ffi.C = ffi.dlopen(None)
247 |         needs_dlopen_none()
248 |         ffi.C = ffi.dlopen(None)
260 |         needs_dlopen_none()
261 |         C = ffi.dlopen(None)
273 |         needs_dlopen_none()
274 |         ffi.C = ffi.dlopen(None)
290 |         needs_dlopen_none()
291 |         ffi.C = ffi.dlopen(None)
302 |         m = ffi.dlopen(lib_m)
312 |         needs_dlopen_none()
313 |         C = ffi.dlopen(None)
328 |         needs_dlopen_none()
329 |         lib = ffi.dlopen(None)
340 |         needs_dlopen_none()
341 |         lib = ffi.dlopen(None)
350 |         needs_dlopen_none()
351 |         lib = ffi.dlopen(None)
360 |         needs_dlopen_none()
361 |         lib = ffi.dlopen(None)
370 |         m = ffi.dlopen(lib_m)
384 |         m = ffi.dlopen(lib_m)
421 |         m = ffi.dlopen("Kernel32.dll")
438 |         m = ffi.dlopen("Kernel32.dll")
446 |         m = ffi.dlopen("Kernel32.dll")
454 |         m = ffi.dlopen("Kernel32.dll")
484 |         m = ffi.dlopen(lib_m)
493 |     def test_dir_on_dlopen_lib(self):
502 |         m = ffi.dlopen(lib_m)
510 |         lib = ffi.dlopen(lib_m)
{% endraw %}

```
### testing/cffi0/backend_tests.py

```python

{% raw %}
13 | def needs_dlopen_none():
15 |         py.test.skip("dlopen(None) cannot work on Windows for Python 3")
969 |         needs_dlopen_none()
970 |         lib = ffi.dlopen(None)
1908 |         needs_dlopen_none()
1909 |         lib = ffi.dlopen(None)
1938 |         needs_dlopen_none()
1939 |         lib = ffi.dlopen(None)
{% endraw %}

```
### testing/cffi0/test_ffi_backend.py

```python

{% raw %}
344 |         lib = ffi.dlopen("Kernel32.dll")
{% endraw %}

```
### testing/cffi0/test_ownlib.py

```python

{% raw %}
176 |         ownlib = ffi.dlopen(self.module)
192 |         ownlib = ffi.dlopen(self.module)
205 |         ownlib = ffi.dlopen(self.module)
227 |         ownlib = ffi.dlopen(self.module)
245 |         ownlib = ffi.dlopen(self.module)
263 |         ownlib = ffi.dlopen(self.module)
298 |         ownlib = ffi.dlopen(self.module)
324 |         lib = ffi.dlopen(self.module)
345 |         lib = ffi.dlopen(self.module)
366 |         lib = ffi.dlopen(self.module)
{% endraw %}

```
### testing/cffi0/test_verify.py

```python

{% raw %}
2135 |     lib = ffi.dlopen("Kernel32.dll")
2143 | def test_verify_dlopen_flags():
2149 |     ffi1.cdef("int foo_verify_dlopen_flags;")
2151 |     lib1 = ffi1.verify("int foo_verify_dlopen_flags;",
2155 |     lib1.foo_verify_dlopen_flags = 42
2156 |     assert lib2.foo_verify_dlopen_flags == 42
2157 |     lib2.foo_verify_dlopen_flags += 1
2158 |     assert lib1.foo_verify_dlopen_flags == 43
2163 |     ffi2.cdef("int foo_verify_dlopen_flags;")
2164 |     lib2 = ffi2.verify("int foo_verify_dlopen_flags;",
{% endraw %}

```
### cffi/api.py

```python

{% raw %}
33 |         C = ffi.dlopen(None)   # standard library
103 |         then be accessed via either 'ffi.dlopen()' or 'ffi.verify()'.
136 |     def dlopen(self, name, flags=0):
151 |         """Close a library obtained with ffi.dlopen().  After this call,
446 |         (including calling macros).  This is unlike 'ffi.dlopen()',
667 |                             "modules, not for dlopen()-style pure Python "
689 |                             "not for dlopen()-style pure Python modules")
700 |             raise TypeError("emit_python_code() is only for dlopen()-style "
816 |             raise OSError("dlopen(None) cannot work on Windows for Python 3 "
863 |                                   "accessed from a dlopen() library" % (name,))
{% endraw %}

```
### cffi/vengine_cpy.py

```python

{% raw %}
149 |             if hasattr(sys, "getdlopenflags"):
150 |                 previous_flags = sys.getdlopenflags()
152 |                 if hasattr(sys, "setdlopenflags") and flags is not None:
153 |                     sys.setdlopenflags(flags)
160 |                 if hasattr(sys, "setdlopenflags"):
161 |                     sys.setdlopenflags(previous_flags)
{% endraw %}

```
### cffi/verifier.py

```python

{% raw %}
93 |         objects returned by ffi.dlopen(), but that delegates all
{% endraw %}

```
### c/ffi_obj.c

```c

{% raw %}
850 | PyDoc_STRVAR(ffi_dlopen_doc,
860 | "Close a library obtained with ffi.dlopen().  After this call, access to\n"
864 | static PyObject *ffi_dlopen(PyObject *self, PyObject *args);  /* forward */
1108 |  {"dlopen",     (PyCFunction)ffi_dlopen,     METH_VARARGS, ffi_dlopen_doc},
{% endraw %}

```
### c/_cffi_backend.c

```c

{% raw %}
4371 | static void *b_do_dlopen(PyObject *args, const char **p_printable_filename,
4409 |             handle = dlopenW(filenameW);
4433 |     handle = dlopen(filename_or_null, flags);
4454 |     handle = b_do_dlopen(args, &printable_filename, &temp);
7690 | static struct { const char *name; int value; } all_dlopen_flags[] = {
7824 |     for (i = 0; all_dlopen_flags[i].name != NULL; i++) {
7826 |                                     all_dlopen_flags[i].name,
7827 |                                     all_dlopen_flags[i].value) < 0)
{% endraw %}

```
### c/lib_obj.c

```c

{% raw %}
30 |     void *l_libhandle;          /* the dlopen()ed handle, if any */
86 | static void cdlopen_close_ignore_errors(void *libhandle);  /* forward */
87 | static void *cdlopen_fetch(PyObject *libname, void *libhandle,
93 |     cdlopen_close_ignore_errors(lib->l_libhandle);
315 |             data = cdlopen_fetch(lib->l_libname, lib->l_libhandle, s);
369 |                 address = cdlopen_fetch(lib->l_libname, lib->l_libhandle, s);
396 |         void *address = cdlopen_fetch(lib->l_libname, lib->l_libhandle, s);
626 |                                    void *dlopen_libhandle)
648 |     lib->l_libhandle = dlopen_libhandle;
656 |     cdlopen_close_ignore_errors(dlopen_libhandle);
{% endraw %}

```
### c/test_c.py

```python

{% raw %}
68 |             py.test.skip("dlopen(None) cannot work on Windows with Python 3")
{% endraw %}

```
### c/cffi1_module.c

```c

{% raw %}
52 |         for (i = 0; all_dlopen_flags[i].name != NULL; i++) {
53 |             x = PyInt_FromLong(all_dlopen_flags[i].value);
57 |                                        all_dlopen_flags[i].name, x);
{% endraw %}

```
### c/cdlopen.c

```c

{% raw %}
2 | static void *cdlopen_fetch(PyObject *libname, void *libhandle,
23 | static void cdlopen_close_ignore_errors(void *libhandle)
29 | static int cdlopen_close(PyObject *libname, void *libhandle)
40 | static PyObject *ffi_dlopen(PyObject *self, PyObject *args)
46 |     handle = b_do_dlopen(args, &modname, &temp);
72 |         if (cdlopen_close(lib->l_libname, libhandle) < 0)
{% endraw %}

```
### c/misc_win32.h

```c

{% raw %}
192 | static void *dlopen(const char *filename, int flag)
197 | static void *dlopenW(const wchar_t *filename)
{% endraw %}

```