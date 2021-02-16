---
name: "libxslt"
layout: package
next_package: libxsmm
previous_package: libxml2
languages: ['python']
---
## 1.1.33
3 / 2123 files match, 1 filtered matches.

 - [python/libxsl.py](#pythonlibxslpy)

### python/libxsl.py

```python

{% raw %}
6 | if not hasattr(sys,'getdlopenflags'):
41 |             flags = sys.getdlopenflags() 
42 |             sys.setdlopenflags(RTLD_GLOBAL | RTLD_NOW)
48 |                 sys.setdlopenflags(flags)
{% endraw %}

```