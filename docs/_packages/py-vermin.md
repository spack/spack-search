---
name: "py-vermin"
layout: package
next_package: pythia8
previous_package: py-uwsgi
languages: ['python']
---
## 1.0.3
2 / 62 files match, 2 filtered matches.

 - [vermin/rules.py](#verminrulespy)
 - [tests/function.py](#testsfunctionpy)

### vermin/rules.py

```python

{% raw %}
1369 |     "sys.getallocatedblocks": (None, (3, 4)),
1370 |     "sys.getandroidapilevel": (None, (3, 7)),
1371 |     "sys.getcheckinterval": ((2, 3), (3, 0)),
1372 |     "sys.getdlopenflags": ((2, 2), (3, 0)),
1373 |     "sys.getfilesystemencodeerrors": (None, (3, 6)),
1374 |     "sys.getfilesystemencoding": ((2, 3), (3, 0)),
1381 |     "sys.set_asyncgen_hooks": (None, (3, 6)),
1382 |     "sys.set_coroutine_origin_tracking_depth": (None, (3, 7)),
1383 |     "sys.setdefaultencoding": ((2, 0), None),
1384 |     "sys.setdlopenflags": ((2, 2), (3, 0)),
1385 |     "sys.setswitchinterval": (None, (3, 2)),
1386 |     "sys.settscdump": ((2, 4), None),
{% endraw %}

```
### tests/function.py

```python

{% raw %}
6 |   def test_getcheckinterval_of_sys(self):
7 |     self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from sys import getcheckinterval"))
8 | 
9 |   def test_getdlopenflags_of_sys(self):
10 |     self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from sys import getdlopenflags"))
11 | 
12 |   def test_getfilesystemencoding_of_sys(self):
3493 |   def test_setdefaultencoding_from_sys(self):
3494 |     self.assertOnlyIn((2, 0), self.detect("import sys\nsys.setdefaultencoding()"))
3495 | 
3496 |   def test_setdlopenflags_from_sys(self):
3497 |     self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import sys\nsys.setdlopenflags()"))
3498 | 
3499 |   def test_setswitchinterval_from_sys(self):
{% endraw %}

```