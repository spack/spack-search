---
name: "exmcutils"
layout: package
next_package: exodusii
previous_package: etcd
languages: ['c']
---
## master
3 / 1903 files match, 1 filtered matches.

 - [turbine/code/src/tcl/python/tcl-python.c](#turbinecodesrctclpythontcl-pythonc)

### turbine/code/src/tcl/python/tcl-python.c

```c

{% raw %}
121 | #elif defined __APPLE__
122 |   sprintf(str_python_lib, "lib%s.dylib", PYTHON_NAME);
123 | #endif
124 |   dlopen(str_python_lib, RTLD_NOW | RTLD_GLOBAL);
125 | 
126 |   if (initialized) return TCL_OK;
{% endraw %}

```