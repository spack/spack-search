---
name: "turbine"
layout: package
next_package: whizard
previous_package: grass
library_name: dlopen
matches: ['dlopen']
languages: ['c']
---
## 1.1.0
2 / 385 files match, 1 filtered matches.

 - [src/tcl/python/tcl-python.c](#srctclpythontcl-pythonc)

### src/tcl/python/tcl-python.c

```c

{% raw %}
100 | #elif defined __APPLE__
101 |   sprintf(str_python_lib, "libpython%d.%d.dylib", PY_MAJOR_VERSION, PY_MINOR_VERSION);
102 | #endif
103 |   dlopen(str_python_lib, RTLD_NOW | RTLD_GLOBAL);
104 | 
105 |   if (initialized) return TCL_OK;
{% endraw %}

```