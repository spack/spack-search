---
name: "fermisciencetools"
layout: package
next_package: fastx-toolkit
previous_package: timemory
languages: ['python', 'c']
---
## 11r5p3
16 / 15648 files match

 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/test/test_sys.py](#x86_64-unknown-linux-gnu-libc217libpython27testtest_syspy)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/distutils/tests/setuptools_build_ext.py](#x86_64-unknown-linux-gnu-libc217libpython27distutilstestssetuptools_build_extpy)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/__init__.py](#x86_64-unknown-linux-gnu-libc217libpython27ctypes__init__py)
 - [x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pystate.h](#x86_64-unknown-linux-gnu-libc217includepython27pystateh)

### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/test/test_sys.py

```python

{% raw %}
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
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/distutils/tests/setuptools_build_ext.py

```python

{% raw %}
223 |                 if_dl("   old_flags = sys.getdlopenflags()"),
227 |                 if_dl("     sys.setdlopenflags(dl.RTLD_NOW)"),
230 |                 if_dl("     sys.setdlopenflags(old_flags)"),
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/__init__.py

```python

{% raw %}
111 |     from _ctypes import LoadLibrary as _dlopen
140 |     from _ctypes import dlopen as _dlopen
364 |             self._handle = _dlopen(self._name, mode)
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pystate.h

```c

{% raw %}
30 |     int dlopenflags;
{% endraw %}

```