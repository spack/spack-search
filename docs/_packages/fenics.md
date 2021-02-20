---
name: "fenics"
layout: package
next_package: fenics-dolfinx
previous_package: fakexrandr
languages: ['python']
---
## 1.6.0
3 / 2235 files match, 2 filtered matches.

 - [site-packages/dolfin/__init__.py](#site-packagesdolfin__init__py)
 - [site-packages/dolfin/importhandler/__init__.py](#site-packagesdolfinimporthandler__init__py)

### site-packages/dolfin/__init__.py

```python

{% raw %}
18 | 
19 | # Reset dl open flags
20 | import sys
21 | sys.setdlopenflags(dolfin.importhandler.stored_dlopen_flags)
22 | del sys
23 | 
{% endraw %}

```
### site-packages/dolfin/importhandler/__init__.py

```python

{% raw %}
15 | import io
16 | 
17 | # Store dl open flags to restore them after import
18 | stored_dlopen_flags = sys.getdlopenflags()
19 | 
20 | # A try to get rid of problems with dynamic_cast of types defined in different
29 |     except ImportError:
30 |         RTLD_NOW = 2
31 |         RTLD_GLOBAL = 256
32 |     sys.setdlopenflags(RTLD_NOW | RTLD_GLOBAL)
33 | 
34 | # Check for runtime dependencies
{% endraw %}

```