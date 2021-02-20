---
name: "py-jedi"
layout: package
next_package: py-jpype1
previous_package: py-grpcio
languages: ['python']
---
## 0.10.0
1 / 286 files match, 1 filtered matches.

 - [test/test_evaluate/test_extension.py](#testtest_evaluatetest_extensionpy)

### test/test_evaluate/test_extension.py

```python

{% raw %}
17 |         func = 'LoadLibrary'
18 |         params = 1
19 |     else:
20 |         func = 'dlopen'
21 |         params = 2
22 |     s = jedi.Script('import _ctypes; _ctypes.%s(' % (func,))
{% endraw %}

```