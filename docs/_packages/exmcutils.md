---
name: "exmcutils"
layout: package
next_package: botan
previous_package: openfast
languages: ['cpp']
---
## master
3 / 1903 files match

 - [turbine/code/src/tcl/python/tcl-python.c](#turbinecodesrctclpythontcl-pythonc)
 - [turbine/code/export/python.swift](#turbinecodeexportpythonswift)
 - [turbine/code/etc/turbine.supp](#turbinecodeetcturbinesupp)

### turbine/code/src/tcl/python/tcl-python.c

```cpp

{% raw %}
124 |   dlopen(str_python_lib, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### turbine/code/export/python.swift

```

{% raw %}
18 |    to use dlopen(..., RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### turbine/code/etc/turbine.supp

```

{% raw %}
142 |   tcl-dlopen-1
146 |   fun:TclpDlopen
350 |   glib-dlopen-1
356 |   fun:dlopen_doit
361 |   glib-dlopen-1
367 |   fun:dlopen_doit
{% endraw %}

```