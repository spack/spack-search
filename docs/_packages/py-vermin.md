---
name: "py-vermin"
layout: package
next_package: heppdt
previous_package: openmpi
languages: ['python']
---
## 1.0.3
2 / 62 files match, 2 filtered matches.

 - [vermin/rules.py](#verminrulespy)
 - [tests/function.py](#testsfunctionpy)

### vermin/rules.py

```python

{% raw %}
1372 |     "sys.getdlopenflags": ((2, 2), (3, 0)),
1384 |     "sys.setdlopenflags": ((2, 2), (3, 0)),
{% endraw %}

```
### tests/function.py

```python

{% raw %}
9 |   def test_getdlopenflags_of_sys(self):
10 |     self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from sys import getdlopenflags"))
3496 |   def test_setdlopenflags_from_sys(self):
3497 |     self.assertOnlyIn(((2, 2), (3, 0)), self.detect("import sys\nsys.setdlopenflags()"))
{% endraw %}

```