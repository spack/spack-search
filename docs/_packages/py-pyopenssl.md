---
name: "py-pyopenssl"
layout: package
next_package: py-pysam
previous_package: py-pyjnius
languages: ['python']
---
## 19.0.0
1 / 61 files match, 1 filtered matches.

 - [tests/memdbg.py](#testsmemdbgpy)

### tests/memdbg.py

```python

{% raw %}
27 |     #include <stdlib.h>
28 |     #include <execinfo.h>
29 |     """, libraries=["crypto"])
30 | C = _ffi.dlopen(None)
31 | 
32 | verbose = False
{% endraw %}

```