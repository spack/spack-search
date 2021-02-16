---
name: "root"
layout: package
next_package: gobject-introspection
previous_package: hadoop
languages: ['python', 'c']
---
## 6.22.06
26 / 18941 files match, 7 filtered matches.

 - [interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#interpreterllvmsrclibexecutionengineinteljiteventsjitprofilingc)
 - [bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py](#bindingspyrootpythonizationspythonroot_numbadeclarepy)
 - [bindings/pyroot_legacy/cppyy.py](#bindingspyroot_legacycppyypy)
 - [bindings/pyroot_legacy/JupyROOT/helpers/cppcompleter.py](#bindingspyroot_legacyjupyroothelperscppcompleterpy)
 - [bindings/jupyroot/python/JupyROOT/helpers/cppcompleter.py](#bindingsjupyrootpythonjupyroothelperscppcompleterpy)
 - [net/http/civetweb/civetweb.c](#nethttpcivetwebcivetwebc)
 - [builtins/glew/src/glew.c](#builtinsglewsrcglewc)

### interpreter/llvm/src/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```c

{% raw %}
349 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
358 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### bindings/pyroot/pythonizations/python/ROOT/_numbadeclare.py

```python

{% raw %}
191 |         C = ffi.dlopen(None)
{% endraw %}

```
### bindings/pyroot_legacy/cppyy.py

```python

{% raw %}
57 |       dlflags = sys.getdlopenflags()
58 |       sys.setdlopenflags( 0x100 | 0x2 )    # RTLD_GLOBAL | RTLD_NOW
64 |       sys.setdlopenflags( dlflags )
{% endraw %}

```
### bindings/pyroot_legacy/JupyROOT/helpers/cppcompleter.py

```python

{% raw %}
111 |             dlOpenRint = 'dlopen("libRint.so",RTLD_NOW);'
{% endraw %}

```
### bindings/jupyroot/python/JupyROOT/helpers/cppcompleter.py

```python

{% raw %}
111 |             dlOpenRint = 'dlopen("libRint.so",RTLD_NOW);'
{% endraw %}

```
### net/http/civetweb/civetweb.c

```c

{% raw %}
5533 | dlopen(const char *dll_name, int flags)
15280 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### builtins/glew/src/glew.c

```c

{% raw %}
88 |     if ((h = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL)) == NULL) return NULL;
114 |     image = dlopen("/System/Library/Frameworks/OpenGL.framework/Versions/Current/OpenGL", RTLD_LAZY);
{% endraw %}

```