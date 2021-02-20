---
name: "fermisciencetools"
layout: package
next_package: ferret
previous_package: fenics-dolfinx
languages: ['python', 'c']
---
## 11r5p3
16 / 15648 files match, 4 filtered matches.

 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/test/test_sys.py](#x86_64-unknown-linux-gnu-libc217libpython27testtest_syspy)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/distutils/tests/setuptools_build_ext.py](#x86_64-unknown-linux-gnu-libc217libpython27distutilstestssetuptools_build_extpy)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/__init__.py](#x86_64-unknown-linux-gnu-libc217libpython27ctypes__init__py)
 - [x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pystate.h](#x86_64-unknown-linux-gnu-libc217includepython27pystateh)

### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/test/test_sys.py

```python

{% raw %}
245 |         #  still has 5 elements
246 |         maj, min, buildno, plat, csd = sys.getwindowsversion()
247 | 
248 |     @unittest.skipUnless(hasattr(sys, "setdlopenflags"),
249 |                          'test needs sys.setdlopenflags()')
250 |     def test_dlopenflags(self):
251 |         self.assertTrue(hasattr(sys, "getdlopenflags"))
252 |         self.assertRaises(TypeError, sys.getdlopenflags, 42)
253 |         oldflags = sys.getdlopenflags()
254 |         self.assertRaises(TypeError, sys.setdlopenflags)
255 |         sys.setdlopenflags(oldflags+1)
256 |         self.assertEqual(sys.getdlopenflags(), oldflags+1)
257 |         sys.setdlopenflags(oldflags)
258 | 
259 |     def test_refcount(self):
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/distutils/tests/setuptools_build_ext.py

```python

{% raw %}
220 |                 "   del __bootstrap__",
221 |                 "   if '__loader__' in globals():",
222 |                 "       del __loader__",
223 |                 if_dl("   old_flags = sys.getdlopenflags()"),
224 |                 "   old_dir = os.getcwd()",
225 |                 "   try:",
226 |                 "     os.chdir(os.path.dirname(__file__))",
227 |                 if_dl("     sys.setdlopenflags(dl.RTLD_NOW)"),
228 |                 "     imp.load_dynamic(__name__,__file__)",
229 |                 "   finally:",
230 |                 if_dl("     sys.setdlopenflags(old_flags)"),
231 |                 "     os.chdir(old_dir)",
232 |                 "__bootstrap__()",
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/__init__.py

```python

{% raw %}
108 |         return CFunctionType
109 | 
110 | if _os.name in ("nt", "ce"):
111 |     from _ctypes import LoadLibrary as _dlopen
112 |     from _ctypes import FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL
113 |     if _os.name == "ce":
137 |         WINFUNCTYPE.__doc__ = CFUNCTYPE.__doc__.replace("CFUNCTYPE", "WINFUNCTYPE")
138 | 
139 | elif _os.name == "posix":
140 |     from _ctypes import dlopen as _dlopen
141 | 
142 | from _ctypes import sizeof, byref, addressof, alignment, resize
361 |         self._FuncPtr = _FuncPtr
362 | 
363 |         if handle is None:
364 |             self._handle = _dlopen(self._name, mode)
365 |         else:
366 |             self._handle = handle
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pystate.h

```c

{% raw %}
27 |     PyObject *codec_error_registry;
28 | 
29 | #ifdef HAVE_DLOPEN
30 |     int dlopenflags;
31 | #endif
32 | #ifdef WITH_TSC
{% endraw %}

```