---
name: "py-mypy"
layout: package
next_package: py-numpy
previous_package: py-mx
languages: ['python']
---
## 0.740
2 / 1601 files match, 2 filtered matches.

 - [mypy/typeshed/stdlib/3/sys.pyi](#mypytypeshedstdlib3syspyi)
 - [mypy/typeshed/stdlib/2/sys.pyi](#mypytypeshedstdlib2syspyi)

### mypy/typeshed/stdlib/3/sys.pyi

```python

{% raw %}
140 | def getdefaultencoding() -> str: ...
141 | if sys.platform != 'win32':
142 |     # Unix only
143 |     def getdlopenflags() -> int: ...
144 | def getfilesystemencoding() -> str: ...
145 | def getrefcount(arg: Any) -> int: ...
192 |     def breakpointhook(*args: Any, **kwargs: Any) -> Any: ...
193 | 
194 | def setcheckinterval(interval: int) -> None: ...  # deprecated
195 | def setdlopenflags(n: int) -> None: ...  # Linux only
196 | def setrecursionlimit(limit: int) -> None: ...
197 | def setswitchinterval(interval: float) -> None: ...
{% endraw %}

```
### mypy/typeshed/stdlib/2/sys.pyi

```python

{% raw %}
122 |     raise SystemExit()
123 | def getcheckinterval() -> int: ...  # deprecated
124 | def getdefaultencoding() -> str: ...
125 | def getdlopenflags() -> int: ...
126 | def getfilesystemencoding() -> str: ...  # In practice, never returns None
127 | def getrefcount(arg: Any) -> int: ...
130 | def getprofile() -> Optional[Any]: ...
131 | def gettrace() -> Optional[Any]: ...
132 | def setcheckinterval(interval: int) -> None: ...  # deprecated
133 | def setdlopenflags(n: int) -> None: ...
134 | def setdefaultencoding(encoding: Text) -> None: ...  # only exists after reload(sys)
135 | def setprofile(profilefunc: Any) -> None: ...  # TODO type
{% endraw %}

```