---
name: "py-cffi"
layout: package
next_package: py-chainer
previous_package: py-cairocffi
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
11 | 
12 | 
13 | # trying it out
14 | lib = ffi.dlopen(None)
15 | assert lib.AA == 0
16 | assert lib.BB == -1
{% endraw %}

```
### demo/readdir.py

```python

{% raw %}
5 |     raise Exception("Linux-only demo")
6 | 
7 | from _readdir import ffi
8 | lib = ffi.dlopen(None)
9 | 
10 | 
{% endraw %}

```
### demo/cffi-cocoa.py

```python

{% raw %}
47 |     
48 | ''')
49 | 
50 | objc = ffi.dlopen('objc')
51 | appkit = ffi.dlopen('AppKit')
52 | 
53 | nil = ffi.NULL
{% endraw %}

```
### testing/cffi1/test_verify1.py

```python

{% raw %}
2092 |         py.test.skip("win32-only test")
2093 |     ffi = FFI()
2094 |     ffi.cdef("void SetLastError(DWORD);")
2095 |     lib = ffi.dlopen("Kernel32.dll")
2096 |     @_run_in_multiple_threads
2097 |     def test1():
2100 |             lib.SetLastError(n)
2101 |             assert ffi.getwinerror()[0] == n
2102 | 
2103 | def test_verify_dlopen_flags():
2104 |     if not hasattr(sys, 'setdlopenflags'):
2105 |         py.test.skip("requires sys.setdlopenflags()")
2106 |     # Careful with RTLD_GLOBAL.  If by chance the FFI is not deleted
2107 |     # promptly, like on PyPy, then other tests may see the same
2108 |     # exported symbols as well.  So we must not export a simple name
2109 |     # like 'foo'!
2110 |     old = sys.getdlopenflags()
2111 |     try:
2112 |         ffi1 = FFI()
2113 |         ffi1.cdef("int foo_verify_dlopen_flags_1;")
2114 |         sys.setdlopenflags(ffi1.RTLD_GLOBAL | ffi1.RTLD_NOW)
2115 |         lib1 = ffi1.verify("int foo_verify_dlopen_flags_1;")
2116 |     finally:
2117 |         sys.setdlopenflags(old)
2118 | 
2119 |     ffi2 = FFI()
2120 |     ffi2.cdef("int *getptr(void);")
2121 |     lib2 = ffi2.verify("""
2122 |         extern int foo_verify_dlopen_flags_1;
2123 |         static int *getptr(void) { return &foo_verify_dlopen_flags_1; }
2124 |     """)
2125 |     p = lib2.getptr()
2126 |     assert ffi1.addressof(lib1, 'foo_verify_dlopen_flags_1') == p
2127 | 
2128 | def test_consider_not_implemented_function_type():
{% endraw %}

```
### testing/cffi1/test_dlopen_unicode_literals.py

```python

{% raw %}
2 | s = """from __future__ import unicode_literals
3 | """
4 | 
5 | with open(os.path.join(os.path.dirname(__file__), 'test_dlopen.py')) as f:
6 |     s += f.read()
7 | 
{% endraw %}

```
### testing/cffi1/test_re_python.py

```python

{% raw %}
95 | def test_function():
96 |     import _cffi_backend
97 |     from re_python_pysrc import ffi
98 |     lib = ffi.dlopen(extmod)
99 |     assert lib.add42(-10) == 32
100 |     assert type(lib.add42) is _cffi_backend.FFI.CData
102 | def test_function_with_varargs():
103 |     import _cffi_backend
104 |     from re_python_pysrc import ffi
105 |     lib = ffi.dlopen(extmod, 0)
106 |     assert lib.add43(45, ffi.cast("int", -5)) == 45
107 |     assert type(lib.add43) is _cffi_backend.FFI.CData
108 | 
109 | def test_dlopen_none():
110 |     import _cffi_backend
111 |     from re_python_pysrc import ffi
114 |         import ctypes.util
115 |         name = ctypes.util.find_msvcrt()
116 |         if name is None:
117 |             py.test.skip("dlopen(None) cannot work on Windows with Python 3")
118 |     lib = ffi.dlopen(name)
119 |     assert lib.strlen(b"hello") == 5
120 | 
121 | def test_dlclose():
122 |     import _cffi_backend
123 |     from re_python_pysrc import ffi
124 |     lib = ffi.dlopen(extmod)
125 |     ffi.dlclose(lib)
126 |     if type(extmod) is not str:   # unicode, on python 2
134 | 
135 | def test_constant_via_lib():
136 |     from re_python_pysrc import ffi
137 |     lib = ffi.dlopen(extmod)
138 |     assert lib.FOOBAR == -42
139 |     assert lib.FOOBAZ == -43
174 |     assert ffi.integer_const('FOOBAR') == -42
175 |     assert ffi.integer_const('FOOBAZ') == -43
176 |     assert ffi.integer_const('k2') == 121212
177 |     lib = ffi.dlopen(extmod)     # <- a random unrelated library would be fine
178 |     assert lib.FOOBAR == -42
179 |     assert lib.FOOBAZ == -43
184 | 
185 | def test_global_var():
186 |     from re_python_pysrc import ffi
187 |     lib = ffi.dlopen(extmod)
188 |     assert lib.globalvar42 == 1234
189 |     p = ffi.addressof(lib, 'globalvar42')
194 | 
195 | def test_global_const_int():
196 |     from re_python_pysrc import ffi
197 |     lib = ffi.dlopen(extmod)
198 |     assert lib.globalconst42 == 4321
199 |     py.test.raises(AttributeError, ffi.addressof, lib, 'globalconst42')
200 | 
201 | def test_global_const_nonint():
202 |     from re_python_pysrc import ffi
203 |     lib = ffi.dlopen(extmod)
204 |     assert ffi.string(lib.globalconsthello, 8) == b"hello"
205 |     py.test.raises(AttributeError, ffi.addressof, lib, 'globalconsthello')
212 | 
213 | def test_no_such_function_or_global_var():
214 |     from re_python_pysrc import ffi
215 |     lib = ffi.dlopen(extmod)
216 |     e = py.test.raises(ffi.error, getattr, lib, 'no_such_function')
217 |     assert str(e.value).startswith(
{% endraw %}

```
### testing/cffi0/test_parsing.py

```python

{% raw %}
1 | from cffi import FFI, FFIError, CDefError, VerificationError
2 | from .backend_tests import needs_dlopen_none
3 | 
4 | 
83 | def test_simple():
84 |     ffi = FFI(backend=FakeBackend())
85 |     ffi.cdef("double sin(double x);")
86 |     m = ffi.dlopen(lib_m)
87 |     func = m.sin    # should be a callable on real backends
88 |     assert func.name == 'sin'
91 | def test_pipe():
92 |     ffi = FFI(backend=FakeBackend())
93 |     ffi.cdef("int pipe(int pipefd[2]);")
94 |     needs_dlopen_none()
95 |     C = ffi.dlopen(None)
96 |     func = C.pipe
97 |     assert func.name == 'pipe'
100 | def test_vararg():
101 |     ffi = FFI(backend=FakeBackend())
102 |     ffi.cdef("short foo(int, ...);")
103 |     needs_dlopen_none()
104 |     C = ffi.dlopen(None)
105 |     func = C.foo
106 |     assert func.name == 'foo'
111 |     ffi.cdef("""
112 |         int foo(void);
113 |         """)
114 |     needs_dlopen_none()
115 |     C = ffi.dlopen(None)
116 |     assert C.foo.BType == '<func (), <int>, False>'
117 | 
122 |         typedef UInt UIntReally;
123 |         UInt foo(void);
124 |         """)
125 |     needs_dlopen_none()
126 |     C = ffi.dlopen(None)
127 |     assert str(ffi.typeof("UIntReally")) == '<unsigned int>'
128 |     assert C.foo.BType == '<func (), <unsigned int>, False>'
133 |         typedef struct { int a, b; } foo_t, *foo_p;
134 |         int foo(foo_p[]);
135 |         """)
136 |     needs_dlopen_none()
137 |     C = ffi.dlopen(None)
138 |     assert str(ffi.typeof("foo_t")) == '<int>a, <int>b'
139 |     assert str(ffi.typeof("foo_p")) == '<pointer to <int>a, <int>b>'
162 |         x, double/*several*//*comment*/y) /*on the same line*/
163 |         ;
164 |     """)
165 |     m = ffi.dlopen(lib_m)
166 |     func = m.sin
167 |     assert func.name == 'sin'
179 |                   etc
180 |         z(void);
181 |     """)
182 |     m = ffi.dlopen(lib_m)
183 |     m.x
184 |     m.y
192 |         #define BCD   \\
193 |             43
194 |     """)
195 |     m = ffi.dlopen(lib_m)
196 |     assert m.ABC == 42
197 |     assert m.BCD == 43
223 | 
224 | def test_override():
225 |     ffi = FFI(backend=FakeBackend())
226 |     needs_dlopen_none()
227 |     C = ffi.dlopen(None)
228 |     ffi.cdef("int foo(void);")
229 |     py.test.raises(FFIError, ffi.cdef, "long foo(void);")
420 |             XOR = 0xf ^ 0xa
421 |         };
422 |         """)
423 |     needs_dlopen_none()
424 |     C = ffi.dlopen(None)
425 |     assert C.POS == 1
426 |     assert C.TWO == 2
511 |                     hex_4=0x10L,
512 |                     hex_5=0x10ll,
513 |                     hex_6=0x10LL,};""")
514 |     needs_dlopen_none()
515 |     C = ffi.dlopen(None)
516 |     for base, expected_result in (('bin', 2), ('oct', 8), ('dec', 10), ('hex', 16)):
517 |         for index in range(7):
{% endraw %}

```
### testing/cffi0/test_unicode_literals.py

```python

{% raw %}
58 |     x = ffi.cast("enum foo_e", 1)
59 |     assert int(ffi.cast("int", x)) == 1
60 | 
61 | def test_dlopen():
62 |     ffi = FFI()
63 |     ffi.cdef("double sin(double x);")
64 |     m = ffi.dlopen(lib_m)                           # unicode literal
65 |     x = m.sin(1.23)
66 |     assert x == math.sin(1.23)
{% endraw %}

```
### testing/cffi0/test_function.py

```python

{% raw %}
5 | from cffi.backend_ctypes import CTypesBackend
6 | from testing.udir import udir
7 | from testing.support import FdWriteCapture
8 | from .backend_tests import needs_dlopen_none
9 | 
10 | try:
28 |         ffi.cdef("""
29 |             double sin(double x);
30 |         """)
31 |         m = ffi.dlopen(lib_m)
32 |         x = m.sin(1.23)
33 |         assert x == math.sin(1.23)
39 |         ffi.cdef("""
40 |             float sinf(float x);
41 |         """)
42 |         m = ffi.dlopen(lib_m)
43 |         x = m.sinf(1.23)
44 |         assert type(x) is float
51 |         ffi.cdef("""
52 |             void getenv(char *);
53 |         """)
54 |         needs_dlopen_none()
55 |         m = ffi.dlopen(None)
56 |         x = m.getenv(b"FOO")
57 |         assert x is None
58 | 
59 |     def test_dlopen_filename(self):
60 |         path = ctypes.util.find_library(lib_m)
61 |         if not path:
64 |         ffi.cdef("""
65 |             double cos(double x);
66 |         """)
67 |         m = ffi.dlopen(path)
68 |         x = m.cos(1.23)
69 |         assert x == math.cos(1.23)
70 | 
71 |         m = ffi.dlopen(os.path.basename(path))
72 |         x = m.cos(1.23)
73 |         assert x == math.cos(1.23)
74 | 
75 |     def test_dlopen_flags(self):
76 |         ffi = FFI(backend=self.Backend())
77 |         ffi.cdef("""
78 |             double cos(double x);
79 |         """)
80 |         m = ffi.dlopen(lib_m, ffi.RTLD_LAZY | ffi.RTLD_LOCAL)
81 |         x = m.cos(1.23)
82 |         assert x == math.cos(1.23)
83 | 
84 |     def test_dlopen_constant(self):
85 |         ffi = FFI(backend=self.Backend())
86 |         ffi.cdef("""
88 |             static const float baz = 42.5;   /* not visible */
89 |             double sin(double x);
90 |         """)
91 |         m = ffi.dlopen(lib_m)
92 |         assert m.FOOBAR == 42
93 |         with pytest.raises(NotImplementedError):
100 |             py.test.skip("ctypes complains on wrong calling conv")
101 |         ffi = FFI(backend=self.Backend())
102 |         ffi.cdef("long TlsAlloc(void); int TlsFree(long);")
103 |         lib = ffi.dlopen('KERNEL32.DLL')
104 |         x = lib.TlsAlloc()
105 |         assert x != 0
114 |             int fputs(const char *, void *);
115 |             void *stderr;
116 |         """)
117 |         needs_dlopen_none()
118 |         ffi.C = ffi.dlopen(None)
119 |         ffi.C.fputs   # fetch before capturing, for easier debugging
120 |         with FdWriteCapture() as fd:
131 |             int fputs(char *, void *);
132 |             void *stderr;
133 |         """)
134 |         needs_dlopen_none()
135 |         ffi.C = ffi.dlopen(None)
136 |         ffi.C.fputs   # fetch before capturing, for easier debugging
137 |         with FdWriteCapture() as fd:
148 |            int fprintf(void *, const char *format, ...);
149 |            void *stderr;
150 |         """)
151 |         needs_dlopen_none()
152 |         ffi.C = ffi.dlopen(None)
153 |         with FdWriteCapture() as fd:
154 |             ffi.C.fprintf(ffi.C.stderr, b"hello with no arguments\n")
175 |         ffi.cdef("""
176 |            int printf(const char *format, ...);
177 |         """)
178 |         needs_dlopen_none()
179 |         ffi.C = ffi.dlopen(None)
180 |         e = py.test.raises(TypeError, ffi.C.printf, b"hello %d\n", 42)
181 |         assert str(e.value) == ("argument 2 passed in the variadic part "
186 |         ffi.cdef("""
187 |             int puts(const char *);
188 |         """)
189 |         needs_dlopen_none()
190 |         ffi.C = ffi.dlopen(None)
191 |         fptr = ffi.C.puts
192 |         assert ffi.typeof(fptr) == ffi.typeof("int(*)(const char*)")
210 |             int fputs(const char *, void *);
211 |             void *stderr;
212 |         """)
213 |         needs_dlopen_none()
214 |         ffi.C = ffi.dlopen(None)
215 |         fptr = ffi.cast("int(*)(const char *txt, void *)", ffi.C.fputs)
216 |         assert fptr == ffi.C.fputs
244 |         ffi.cdef("""
245 |             int strlen(char[]);
246 |         """)
247 |         needs_dlopen_none()
248 |         ffi.C = ffi.dlopen(None)
249 |         p = ffi.new("char[]", b"hello")
250 |         res = ffi.C.strlen(p)
257 |         ffi.cdef("""
258 |             void *stdout;
259 |         """)
260 |         needs_dlopen_none()
261 |         C = ffi.dlopen(None)
262 |         pout = C.stdout
263 |         C.stdout = ffi.NULL
270 |         ffi.cdef("""
271 |             char *strchr(const char *s, int c);
272 |         """)
273 |         needs_dlopen_none()
274 |         ffi.C = ffi.dlopen(None)
275 |         p = ffi.new("char[]", b"hello world!")
276 |         q = ffi.C.strchr(p, ord('w'))
287 |             struct in_addr { unsigned int s_addr; };
288 |             char *inet_ntoa(struct in_addr in);
289 |         """)
290 |         needs_dlopen_none()
291 |         ffi.C = ffi.dlopen(None)
292 |         ina = ffi.new("struct in_addr *", [0x04040404])
293 |         a = ffi.C.inet_ntoa(ina[0])
299 |             typedef double func_t(double);
300 |             func_t sin;
301 |         """)
302 |         m = ffi.dlopen(lib_m)
303 |         x = m.sin(1.23)
304 |         assert x == math.sin(1.23)
309 |         filename = str(udir.join('fputs_custom_FILE'))
310 |         ffi = FFI(backend=self.Backend())
311 |         ffi.cdef("int fputs(const char *, FILE *);")
312 |         needs_dlopen_none()
313 |         C = ffi.dlopen(None)
314 |         with open(filename, 'wb') as f:
315 |             f.write(b'[')
325 |         ffi = FFI(backend=self.Backend())
326 |         ffi.cdef("""enum foo_e { AA, BB, CC=5, DD };
327 |                     typedef enum { EE=-5, FF } some_enum_t;""")
328 |         needs_dlopen_none()
329 |         lib = ffi.dlopen(None)
330 |         assert lib.AA == 0
331 |         assert lib.BB == 1
337 |     def test_void_star_accepts_string(self):
338 |         ffi = FFI(backend=self.Backend())
339 |         ffi.cdef("""int strlen(const void *);""")
340 |         needs_dlopen_none()
341 |         lib = ffi.dlopen(None)
342 |         res = lib.strlen(b"hello")
343 |         assert res == 5
347 |             py.test.skip("not supported by the ctypes backend")
348 |         ffi = FFI(backend=self.Backend())
349 |         ffi.cdef("""int strlen(signed char *);""")
350 |         needs_dlopen_none()
351 |         lib = ffi.dlopen(None)
352 |         res = lib.strlen(b"hello")
353 |         assert res == 5
357 |             py.test.skip("not supported by the ctypes backend")
358 |         ffi = FFI(backend=self.Backend())
359 |         ffi.cdef("""int strlen(unsigned char *);""")
360 |         needs_dlopen_none()
361 |         lib = ffi.dlopen(None)
362 |         res = lib.strlen(b"hello")
363 |         assert res == 5
367 |         ffi.cdef("""
368 |             int nonexistent();
369 |         """)
370 |         m = ffi.dlopen(lib_m)
371 |         assert not hasattr(m, 'nonexistent')
372 | 
381 |             def wrapper(*args):
382 |                 return f(*args) + 100
383 |             return wrapper
384 |         m = ffi.dlopen(lib_m)
385 |         sin100 = my_decorator(m.sin)
386 |         x = sin100(1.23)
418 |         ffi.cdef("""
419 |             BOOL QueryPerformanceFrequency(LONGLONG *lpFrequency);
420 |         """)
421 |         m = ffi.dlopen("Kernel32.dll")
422 |         p_freq = ffi.new("LONGLONG *")
423 |         res = m.QueryPerformanceFrequency(p_freq)
435 |         ffi.cdef("""
436 |             BOOL QueryPerformanceFrequency(LONGLONG *lpFrequency);
437 |         """)
438 |         m = ffi.dlopen("Kernel32.dll")
439 |         tp = ffi.typeof(m.QueryPerformanceFrequency)
440 |         assert str(tp) == "<ctype 'int(*)(long long *)'>"
443 |         ffi.cdef("""
444 |             BOOL __cdecl QueryPerformanceFrequency(LONGLONG *lpFrequency);
445 |         """)
446 |         m = ffi.dlopen("Kernel32.dll")
447 |         tpc = ffi.typeof(m.QueryPerformanceFrequency)
448 |         assert tpc is tp
451 |         ffi.cdef("""
452 |             BOOL WINAPI QueryPerformanceFrequency(LONGLONG *lpFrequency);
453 |         """)
454 |         m = ffi.dlopen("Kernel32.dll")
455 |         tps = ffi.typeof(m.QueryPerformanceFrequency)
456 |         if win64:
481 |     def test_stdcall_only_on_windows(self):
482 |         ffi = FFI(backend=self.Backend())
483 |         ffi.cdef("double __stdcall sin(double x);")     # stdcall ignored
484 |         m = ffi.dlopen(lib_m)
485 |         if (sys.platform == 'win32' and sys.maxsize < 2**32 and
486 |                 self.Backend is not CTypesBackend):
490 |         x = m.sin(1.23)
491 |         assert x == math.sin(1.23)
492 | 
493 |     def test_dir_on_dlopen_lib(self):
494 |         ffi = FFI(backend=self.Backend())
495 |         ffi.cdef("""
499 |             const double myconst;
500 |             #define MYFOO 42
501 |         """)
502 |         m = ffi.dlopen(lib_m)
503 |         assert dir(m) == ['MYE1', 'MYE2', 'MYFOO', 'myconst', 'myfunc', 'myvar']
504 | 
507 |             py.test.skip("not with the ctypes backend")
508 |         ffi = FFI(backend=self.Backend())
509 |         ffi.cdef("int foobar(void); int foobaz;")
510 |         lib = ffi.dlopen(lib_m)
511 |         ffi.dlclose(lib)
512 |         e = py.test.raises(ValueError, getattr, lib, 'foobar')
{% endraw %}

```
### testing/cffi0/backend_tests.py

```python

{% raw %}
10 | SIZE_OF_PTR   = ctypes.sizeof(ctypes.c_void_p)
11 | SIZE_OF_WCHAR = ctypes.sizeof(ctypes.c_wchar)
12 | 
13 | def needs_dlopen_none():
14 |     if sys.platform == 'win32' and sys.version_info >= (3,):
15 |         py.test.skip("dlopen(None) cannot work on Windows for Python 3")
16 | 
17 | 
966 |     def test_enum_partial(self):
967 |         ffi = FFI(backend=self.Backend())
968 |         ffi.cdef(r"enum foo {A, ...}; enum bar { B, C };")
969 |         needs_dlopen_none()
970 |         lib = ffi.dlopen(None)
971 |         assert lib.B == 0
972 |         py.test.raises(VerificationMissing, getattr, lib, "A")
1905 |             #define DOT_UL 1000UL
1906 |             enum foo {AA, BB=DOT, CC};
1907 |         """)
1908 |         needs_dlopen_none()
1909 |         lib = ffi.dlopen(None)
1910 |         assert ffi.string(ffi.cast("enum foo", 100)) == "BB"
1911 |         assert lib.DOT_0 == 0
1935 |         ffi = FFI()
1936 |         ffi.include(ffi1)
1937 |         ffi.cdef("enum { EE2, EE3 };")
1938 |         needs_dlopen_none()
1939 |         lib = ffi.dlopen(None)
1940 |         assert lib.EE1 == 0
1941 |         assert lib.EE2 == 0
{% endraw %}

```
### testing/cffi0/test_ffi_backend.py

```python

{% raw %}
341 |         assert message == ("No application is associated with the "
342 |                            "specified file for this operation")
343 |         ffi.cdef("void SetLastError(int);")
344 |         lib = ffi.dlopen("Kernel32.dll")
345 |         lib.SetLastError(2)
346 |         code, message = ffi.getwinerror()
{% endraw %}

```
### testing/cffi0/test_ownlib.py

```python

{% raw %}
173 |         ffi.cdef("""
174 |             int test_getting_errno(void);
175 |         """)
176 |         ownlib = ffi.dlopen(self.module)
177 |         res = ownlib.test_getting_errno()
178 |         assert res == -1
189 |         ffi.cdef("""
190 |             int test_setting_errno(void);
191 |         """)
192 |         ownlib = ffi.dlopen(self.module)
193 |         ffi.errno = 42
194 |         res = ownlib.test_setting_errno()
202 |         ffi.cdef("""
203 |             int my_array[7];
204 |         """)
205 |         ownlib = ffi.dlopen(self.module)
206 |         for i in range(7):
207 |             assert ownlib.my_array[i] == i
224 |         ffi.cdef("""
225 |             int my_array[];
226 |         """)
227 |         ownlib = ffi.dlopen(self.module)
228 |         for i in range(7):
229 |             assert ownlib.my_array[i] == i
242 |         ffi.cdef("""
243 |             int test_getting_errno(void);
244 |         """)
245 |         ownlib = ffi.dlopen(self.module)
246 |         ffi_r = weakref.ref(ffi)
247 |         ownlib_r = weakref.ref(ownlib)
260 |         ffi.cdef("""
261 |             int test_getting_errno(void);
262 |         """)
263 |         ownlib = ffi.dlopen(self.module)
264 |         ffi_r = weakref.ref(ffi)
265 |         ownlib_r = weakref.ref(ownlib)
295 |             RECT ReturnRect(int i, RECT ar, RECT* br, POINT cp, RECT dr,
296 |                         RECT *er, POINT fp, RECT gr);
297 |         """)
298 |         ownlib = ffi.dlopen(self.module)
299 | 
300 |         rect = ffi.new('RECT[1]')
321 |             py.test.skip("not implemented with the ctypes backend")
322 |         ffi = FFI(backend=self.Backend())
323 |         ffi.cdef("long left; int test_getting_errno(void);")
324 |         lib = ffi.dlopen(self.module)
325 |         lib.left = 123456
326 |         p = ffi.addressof(lib, "left")
342 |             char16_t foo_2bytes(char16_t);
343 |             char32_t foo_4bytes(char32_t);
344 |         """)
345 |         lib = ffi.dlopen(self.module)
346 |         assert lib.foo_2bytes(u+'\u1234') == u+'\u125e'
347 |         assert lib.foo_4bytes(u+'\u1234') == u+'\u125e'
363 | 
364 |             void modify_struct_value(RECT r);
365 |         """)
366 |         lib = ffi.dlopen(self.module)
367 |         s = ffi.new("RECT *", [11, 22, 33, 44])
368 |         lib.modify_struct_value(s[0])
{% endraw %}

```
### testing/cffi0/test_verify.py

```python

{% raw %}
2132 |         py.test.skip("win32-only test")
2133 |     ffi = FFI()
2134 |     ffi.cdef("void SetLastError(DWORD);")
2135 |     lib = ffi.dlopen("Kernel32.dll")
2136 |     @_run_in_multiple_threads
2137 |     def test1():
2140 |             lib.SetLastError(n)
2141 |             assert ffi.getwinerror()[0] == n
2142 | 
2143 | def test_verify_dlopen_flags():
2144 |     # Careful with RTLD_GLOBAL.  If by chance the FFI is not deleted
2145 |     # promptly, like on PyPy, then other tests may see the same
2146 |     # exported symbols as well.  So we must not export a simple name
2147 |     # like 'foo'!
2148 |     ffi1 = FFI()
2149 |     ffi1.cdef("int foo_verify_dlopen_flags;")
2150 | 
2151 |     lib1 = ffi1.verify("int foo_verify_dlopen_flags;",
2152 |                        flags=ffi1.RTLD_GLOBAL | ffi1.RTLD_LAZY)
2153 |     lib2 = get_second_lib()
2154 | 
2155 |     lib1.foo_verify_dlopen_flags = 42
2156 |     assert lib2.foo_verify_dlopen_flags == 42
2157 |     lib2.foo_verify_dlopen_flags += 1
2158 |     assert lib1.foo_verify_dlopen_flags == 43
2159 | 
2160 | def get_second_lib():
2161 |     # Hack, using modulename makes the test fail
2162 |     ffi2 = FFI()
2163 |     ffi2.cdef("int foo_verify_dlopen_flags;")
2164 |     lib2 = ffi2.verify("int foo_verify_dlopen_flags;",
2165 |                        flags=ffi2.RTLD_GLOBAL | ffi2.RTLD_LAZY)
2166 |     return lib2
{% endraw %}

```
### cffi/api.py

```python

{% raw %}
30 |             int printf(const char *, ...);
31 |         """)
32 | 
33 |         C = ffi.dlopen(None)   # standard library
34 |         -or-
35 |         C = ffi.verify()  # use a C compiler: verify the decl above is right
100 |     def cdef(self, csource, override=False, packed=False, pack=None):
101 |         """Parse the given C source.  This registers all declared functions,
102 |         types, and global variables.  The functions and global variables can
103 |         then be accessed via either 'ffi.dlopen()' or 'ffi.verify()'.
104 |         The types can be used in 'ffi.new()' and other functions.
105 |         If 'packed' is specified as True, all structs declared inside this
133 |                 for tp in finishlist:
134 |                     tp.finish_backend_type(self, finishlist)
135 | 
136 |     def dlopen(self, name, flags=0):
137 |         """Load and return a dynamic library identified by 'name'.
138 |         The standard C library can be loaded by passing None.
148 |         return lib
149 | 
150 |     def dlclose(self, lib):
151 |         """Close a library obtained with ffi.dlopen().  After this call,
152 |         access to functions or variables from the library will fail
153 |         (possibly with a segmentation fault).
443 |         library can be used to call functions and access global
444 |         variables declared in this 'ffi'.  The library is compiled
445 |         by the C compiler: it gives you C-level API compatibility
446 |         (including calling macros).  This is unlike 'ffi.dlopen()',
447 |         which requires binary compatibility in the signatures.
448 |         """
664 |         module_name, source, source_extension, kwds = self._assigned_source
665 |         if source is None:
666 |             raise TypeError("distutils_extension() is only for C extension "
667 |                             "modules, not for dlopen()-style pure Python "
668 |                             "modules")
669 |         mkpath(tmpdir)
686 |         module_name, source, source_extension, kwds = self._assigned_source
687 |         if source is None:
688 |             raise TypeError("emit_c_code() is only for C extension modules, "
689 |                             "not for dlopen()-style pure Python modules")
690 |         recompile(self, module_name, source,
691 |                   c_file=filename, call_c_compiler=False, **kwds)
697 |             raise ValueError("set_source() must be called before emit_c_code()")
698 |         module_name, source, source_extension, kwds = self._assigned_source
699 |         if source is not None:
700 |             raise TypeError("emit_python_code() is only for dlopen()-style "
701 |                             "pure Python modules, not for C extension modules")
702 |         recompile(self, module_name, source,
813 |     path = ctypes.util.find_library(name)
814 |     if path is None:
815 |         if name == "c" and sys.platform == "win32" and sys.version_info >= (3,):
816 |             raise OSError("dlopen(None) cannot work on Windows for Python 3 "
817 |                           "(see http://bugs.python.org/issue23606)")
818 |         msg = ("ctypes.util.find_library() did not manage "
860 |     #
861 |     def accessor_constant(name):
862 |         raise NotImplementedError("non-integer constant '%s' cannot be "
863 |                                   "accessed from a dlopen() library" % (name,))
864 |     #
865 |     def accessor_int_constant(name):
{% endraw %}

```
### cffi/vengine_cpy.py

```python

{% raw %}
146 |         # import it as a new extension module
147 |         imp.acquire_lock()
148 |         try:
149 |             if hasattr(sys, "getdlopenflags"):
150 |                 previous_flags = sys.getdlopenflags()
151 |             try:
152 |                 if hasattr(sys, "setdlopenflags") and flags is not None:
153 |                     sys.setdlopenflags(flags)
154 |                 module = imp.load_dynamic(self.verifier.get_module_name(),
155 |                                           self.verifier.modulefilename)
157 |                 error = "importing %r: %s" % (self.verifier.modulefilename, e)
158 |                 raise VerificationError(error)
159 |             finally:
160 |                 if hasattr(sys, "setdlopenflags"):
161 |                     sys.setdlopenflags(previous_flags)
162 |         finally:
163 |             imp.release_lock()
{% endraw %}

```
### cffi/verifier.py

```python

{% raw %}
90 |     def load_library(self):
91 |         """Get a C module from this Verifier instance.
92 |         Returns an instance of a FFILibrary class that behaves like the
93 |         objects returned by ffi.dlopen(), but that delegates all
94 |         operations to the C module.  If necessary, the C code is written
95 |         and compiled first.
{% endraw %}

```
### c/ffi_obj.c

```c

{% raw %}
847 |     return 0;
848 | }
849 | 
850 | PyDoc_STRVAR(ffi_dlopen_doc,
851 | "Load and return a dynamic library identified by 'name'.  The standard\n"
852 | "C library can be loaded by passing None.\n"
857 | "first access.");
858 | 
859 | PyDoc_STRVAR(ffi_dlclose_doc,
860 | "Close a library obtained with ffi.dlopen().  After this call, access to\n"
861 | "functions or variables from the library will fail (possibly with a\n"
862 | "segmentation fault).");
863 | 
864 | static PyObject *ffi_dlopen(PyObject *self, PyObject *args);  /* forward */
865 | static PyObject *ffi_dlclose(PyObject *self, PyObject *args);  /* forward */
866 | 
1105 |  {"callback",   (PyCFunction)ffi_callback,   METH_VKW,     ffi_callback_doc},
1106 |  {"cast",       (PyCFunction)ffi_cast,       METH_VARARGS, ffi_cast_doc},
1107 |  {"dlclose",    (PyCFunction)ffi_dlclose,    METH_VARARGS, ffi_dlclose_doc},
1108 |  {"dlopen",     (PyCFunction)ffi_dlopen,     METH_VARARGS, ffi_dlopen_doc},
1109 |  {"from_buffer",(PyCFunction)ffi_from_buffer,METH_VKW,     ffi_from_buffer_doc},
1110 |  {"from_handle",(PyCFunction)ffi_from_handle,METH_O,       ffi_from_handle_doc},
{% endraw %}

```
### c/_cffi_backend.c

```c

{% raw %}
4368 |     dl_methods,                         /* tp_methods */
4369 | };
4370 | 
4371 | static void *b_do_dlopen(PyObject *args, const char **p_printable_filename,
4372 |                          PyObject **p_temp)
4373 | {
4406 |             if (*p_printable_filename == NULL)
4407 |                 return NULL;
4408 | 
4409 |             handle = dlopenW(filenameW);
4410 |             goto got_handle;
4411 |         }
4430 |     if ((flags & (RTLD_NOW | RTLD_LAZY)) == 0)
4431 |         flags |= RTLD_NOW;
4432 | 
4433 |     handle = dlopen(filename_or_null, flags);
4434 | 
4435 | #ifdef MS_WIN32
4451 |     void *handle;
4452 |     DynLibObject *dlobj = NULL;
4453 | 
4454 |     handle = b_do_dlopen(args, &printable_filename, &temp);
4455 |     if (handle == NULL)
4456 |         goto error;
7687 |     _cffi_from_c_wchar3216_t,
7688 | };
7689 | 
7690 | static struct { const char *name; int value; } all_dlopen_flags[] = {
7691 |     { "RTLD_LAZY",     RTLD_LAZY     },
7692 |     { "RTLD_NOW",      RTLD_NOW      },
7821 |         0)
7822 |       INITERROR;
7823 | 
7824 |     for (i = 0; all_dlopen_flags[i].name != NULL; i++) {
7825 |         if (PyModule_AddIntConstant(m,
7826 |                                     all_dlopen_flags[i].name,
7827 |                                     all_dlopen_flags[i].value) < 0)
7828 |             INITERROR;
7829 |     }
{% endraw %}

```
### c/lib_obj.c

```c

{% raw %}
27 |     PyObject *l_dict;           /* content, built lazily */
28 |     PyObject *l_libname;        /* some string that gives the name of the lib */
29 |     FFIObject *l_ffi;           /* reference back to the ffi object */
30 |     void *l_libhandle;          /* the dlopen()ed handle, if any */
31 | };
32 | 
83 |     return _cpyextfunc_type(lib, exf);
84 | }
85 | 
86 | static void cdlopen_close_ignore_errors(void *libhandle);  /* forward */
87 | static void *cdlopen_fetch(PyObject *libname, void *libhandle,
88 |                            const char *symbol);
89 | 
90 | static void lib_dealloc(LibObject *lib)
91 | {
92 |     PyObject_GC_UnTrack(lib);
93 |     cdlopen_close_ignore_errors(lib->l_libhandle);
94 |     Py_DECREF(lib->l_dict);
95 |     Py_DECREF(lib->l_libname);
312 |         if (g->address == NULL) {
313 |             /* for dlopen() style */
314 |             assert(_CFFI_GETOP(g->type_op) == _CFFI_OP_DLOPEN_CONST);
315 |             data = cdlopen_fetch(lib->l_libname, lib->l_libhandle, s);
316 |             if (data == NULL)
317 |                 return NULL;
366 |             void *address = g->address;
367 |             if (address == NULL) {
368 |                 /* for dlopen() style */
369 |                 address = cdlopen_fetch(lib->l_libname, lib->l_libhandle, s);
370 |                 if (address == NULL)
371 |                     return NULL;
393 |            the specified type.
394 |         */
395 |         PyObject *ct1;
396 |         void *address = cdlopen_fetch(lib->l_libname, lib->l_libhandle, s);
397 |         if (address == NULL)
398 |             return NULL;
623 | };
624 | 
625 | static LibObject *lib_internal_new(FFIObject *ffi, const char *module_name,
626 |                                    void *dlopen_libhandle)
627 | {
628 |     LibObject *lib;
645 |     lib->l_libname = libname;
646 |     Py_INCREF(ffi);
647 |     lib->l_ffi = ffi;
648 |     lib->l_libhandle = dlopen_libhandle;
649 |     return lib;
650 | 
653 |  err2:
654 |     Py_DECREF(libname);
655 |  err1:
656 |     cdlopen_close_ignore_errors(dlopen_libhandle);
657 |     return NULL;
658 | }
{% endraw %}

```
### c/test_c.py

```python

{% raw %}
65 |         if path is None and name == 'c':
66 |             assert sys.platform == 'win32'
67 |             assert sys.version_info >= (3,)
68 |             py.test.skip("dlopen(None) cannot work on Windows with Python 3")
69 |     return load_library(path, flags)
70 | 
{% endraw %}

```
### c/cffi1_module.c

```c

{% raw %}
49 |                                  (PyObject *)&MiniBuffer_Type) < 0)
50 |             return -1;
51 | 
52 |         for (i = 0; all_dlopen_flags[i].name != NULL; i++) {
53 |             x = PyInt_FromLong(all_dlopen_flags[i].value);
54 |             if (x == NULL)
55 |                 return -1;
56 |             res = PyDict_SetItemString(FFI_Type.tp_dict,
57 |                                        all_dlopen_flags[i].name, x);
58 |             Py_DECREF(x);
59 |             if (res < 0)
{% endraw %}

```
### c/cdlopen.c

```c

{% raw %}
1 | 
2 | static void *cdlopen_fetch(PyObject *libname, void *libhandle,
3 |                            const char *symbol)
4 | {
20 |     return address;
21 | }
22 | 
23 | static void cdlopen_close_ignore_errors(void *libhandle)
24 | {
25 |     if (libhandle != NULL)
26 |         dlclose(libhandle);
27 | }
28 | 
29 | static int cdlopen_close(PyObject *libname, void *libhandle)
30 | {
31 |     if (libhandle != NULL && dlclose(libhandle) != 0) {
37 |     return 0;
38 | }
39 | 
40 | static PyObject *ffi_dlopen(PyObject *self, PyObject *args)
41 | {
42 |     const char *modname;
43 |     PyObject *temp, *result = NULL;
44 |     void *handle;
45 | 
46 |     handle = b_do_dlopen(args, &modname, &temp);
47 |     if (handle != NULL)
48 |     {
69 |            again, and fail because the library was closed. */
70 |         PyDict_Clear(lib->l_dict);
71 | 
72 |         if (cdlopen_close(lib->l_libname, libhandle) < 0)
73 |             return NULL;
74 |     }
{% endraw %}

```
### c/misc_win32.h

```c

{% raw %}
189 | #define RTLD_GLOBAL 0
190 | #define RTLD_LOCAL  0
191 | 
192 | static void *dlopen(const char *filename, int flag)
193 | {
194 |     return (void *)LoadLibraryA(filename);
195 | }
196 | 
197 | static void *dlopenW(const wchar_t *filename)
198 | {
199 |     return (void *)LoadLibraryW(filename);
{% endraw %}

```