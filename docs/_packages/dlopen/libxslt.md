---
name: "libxslt"
layout: package
next_package: libpng
previous_package: silo
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['python']
---
## 1.1.33
3 / 2123 files match, 1 filtered matches.

 - [python/libxsl.py](#pythonlibxslpy)

### python/libxsl.py

```python

{% raw %}
3 | # loader to work in that mode if feasible
4 | #
5 | import sys
6 | if not hasattr(sys,'getdlopenflags'):
7 |     import libxml2mod
8 |     import libxsltmod
38 | 
39 |     if RTLD_GLOBAL != -1 and RTLD_NOW != -1:
40 |         try:
41 |             flags = sys.getdlopenflags() 
42 |             sys.setdlopenflags(RTLD_GLOBAL | RTLD_NOW)
43 |             try:
44 |                 import libxml2mod
45 |                 import libxsltmod
46 |                 import libxml2
47 |             finally:
48 |                 sys.setdlopenflags(flags)
49 |         except:
50 |             import libxml2mod
{% endraw %}

```