---
name: "nest"
layout: package
next_package: tar
previous_package: mpi-bash
languages: ['python']
---
## 2.14.0
2 / 1388 files match

 - [nestkernel/dynamicloader.cpp](#nestkerneldynamicloadercpp)
 - [pynest/nest/__init__.py](#pynestnest__init__py)

### nestkernel/dynamicloader.cpp

```

{% raw %}
185 |   const lt_dlhandle hModule = lt_dlopenext( new_module.name.c_str() );
{% endraw %}

```
### pynest/nest/__init__.py

```python

{% raw %}
46 |     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
55 |         sys.setdlopenflags(dl.RTLD_GLOBAL | dl.RTLD_NOW)
59 |             sys.setdlopenflags(DLFCN.RTLD_GLOBAL | DLFCN.RTLD_NOW)
63 |                 sys.setdlopenflags(ctypes.RTLD_GLOBAL | ctypes.RTLD_NOW)
67 |                 sys.setdlopenflags(ctypes.RTLD_GLOBAL)
{% endraw %}

```