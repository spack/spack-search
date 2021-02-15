---
name: "nnvm"
layout: package
next_package: libeatmydata
previous_package: foam-extend
languages: ['python']
---
## master
2 / 256 files match

 - [tests/python/frontend/darknet/test_forward.py](#testspythonfrontenddarknettest_forwardpy)
 - [tutorials/from_darknet.py](#tutorialsfrom_darknetpy)

### tests/python/frontend/darknet/test_forward.py

```python

{% raw %}
48 | LIB = __darknetffi__.dlopen('./' + DARKNET_LIB)
{% endraw %}

```
### tutorials/from_darknet.py

```python

{% raw %}
133 | darknet_lib = __darknetffi__.dlopen('./' + darknet_lib)
{% endraw %}

```