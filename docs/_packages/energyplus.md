---
name: "energyplus"
layout: package
next_package: erlang
previous_package: emboss
languages: ['python']
---
## 9.3.0
1 / 1700 files match, 1 filtered matches.

 - [python_standard_lib/ctypes/__init__.py](#python_standard_libctypes__init__py)

### python_standard_lib/ctypes/__init__.py

```python

{% raw %}
103 |         return CFunctionType
104 | 
105 | if _os.name == "nt":
106 |     from _ctypes import LoadLibrary as _dlopen
107 |     from _ctypes import FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL
108 | 
129 |         WINFUNCTYPE.__doc__ = CFUNCTYPE.__doc__.replace("CFUNCTYPE", "WINFUNCTYPE")
130 | 
131 | elif _os.name == "posix":
132 |     from _ctypes import dlopen as _dlopen
133 | 
134 | from _ctypes import sizeof, byref, addressof, alignment, resize
344 |         self._FuncPtr = _FuncPtr
345 | 
346 |         if handle is None:
347 |             self._handle = _dlopen(self._name, mode)
348 |         else:
349 |             self._handle = handle
{% endraw %}

```