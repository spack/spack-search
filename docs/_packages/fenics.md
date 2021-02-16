---
name: "fenics"
layout: package
next_package: ecflow
previous_package: kibana
languages: ['python']
---
## 1.6.0
3 / 2235 files match, 2 filtered matches.

 - [site-packages/dolfin/__init__.py](#site-packagesdolfin__init__py)
 - [site-packages/dolfin/importhandler/__init__.py](#site-packagesdolfinimporthandler__init__py)

### site-packages/dolfin/__init__.py

```python

{% raw %}
21 | sys.setdlopenflags(dolfin.importhandler.stored_dlopen_flags)
{% endraw %}

```
### site-packages/dolfin/importhandler/__init__.py

```python

{% raw %}
18 | stored_dlopen_flags = sys.getdlopenflags()
32 |     sys.setdlopenflags(RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```