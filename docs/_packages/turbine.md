---
name: "turbine"
layout: package
next_package: mercury
previous_package: folly
languages: ['cpp']
---
## 1.1.0
2 / 385 files match

 - [src/tcl/python/tcl-python.c](#srctclpythontcl-pythonc)
 - [export/python.swift](#exportpythonswift)

### src/tcl/python/tcl-python.c

```cpp

{% raw %}
103 |   dlopen(str_python_lib, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### export/python.swift

```

{% raw %}
18 |    to use dlopen(..., RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```