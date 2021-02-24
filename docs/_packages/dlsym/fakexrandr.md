---
name: "fakexrandr"
layout: package
next_package: ghostscript
previous_package: polymake
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['python']
---
## master
1 / 16 files match, 1 filtered matches.

 - [make_skeleton.py](#make_skeletonpy)

### make_skeleton.py

```python

{% raw %}
66 | 
67 | defns = []
68 | for function in functions:
69 |     defns.append("_{fn} = dlsym(xrandr_lib, \"{fn}\")".format(fn=function[1]))
70 | print("#define FUNCTION_POINTER_INITIALIZATIONS {defns}".format(
71 |     defns="; ".join(defns)))
{% endraw %}

```