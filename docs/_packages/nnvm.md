---
name: "nnvm"
layout: package
next_package: node-js
previous_package: nmap
languages: ['python']
---
## master
2 / 256 files match, 2 filtered matches.

 - [tests/python/frontend/darknet/test_forward.py](#testspythonfrontenddarknettest_forwardpy)
 - [tutorials/from_darknet.py](#tutorialsfrom_darknetpy)

### tests/python/frontend/darknet/test_forward.py

```python

{% raw %}
45 | DARKNETLIB_URL = 'https://github.com/siju-samuel/darknet/blob/master/lib/' \
46 |                                     + DARKNET_LIB + '?raw=true'
47 | _download(DARKNETLIB_URL, DARKNET_LIB)
48 | LIB = __darknetffi__.dlopen('./' + DARKNET_LIB)
49 | 
50 | def test_forward(net):
{% endraw %}

```
### tutorials/from_darknet.py

```python

{% raw %}
130 | if os.path.isfile('./' + darknet_lib) is False:
131 |     exit(0)
132 | 
133 | darknet_lib = __darknetffi__.dlopen('./' + darknet_lib)
134 | cfg = "./" + str(cfg_name)
135 | weights = "./" + str(weights_name)
{% endraw %}

```