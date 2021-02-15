---
name: "py-tables"
layout: package
next_package: py-shiboken
previous_package: czmq
languages: ['cpp', 'python']
---
## 3.5.2
2 / 788 files match

 - [setup.py](#setuppy)
 - [src/utils.c](#srcutilsc)

### setup.py

```python

{% raw %}
229 |             # dlopen() won't tell us where the file is, just whether
{% endraw %}

```
### src/utils.c

```cpp

{% raw %}
55 |     hinstLib = dlopen(libname, RTLD_LAZY);
{% endraw %}

```