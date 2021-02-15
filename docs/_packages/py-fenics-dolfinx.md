---
name: "py-fenics-dolfinx"
layout: package
next_package: py-billiard
previous_package: libxdmcp
languages: ['python']
---
## master
2 / 374 files match

 - [python/dolfinx/__init__.py](#pythondolfinx__init__py)
 - [python/test/unit/fem/test_custom_assembler.py](#pythontestunitfemtest_custom_assemblerpy)

### python/dolfinx/__init__.py

```python

{% raw %}
11 | stored_dlopen_flags = sys.getdlopenflags()
14 | # Fix dlopen flags (may need reorganising)
22 |     sys.setdlopenflags(RTLD_NOW | RTLD_GLOBAL)
26 | # sys.setdlopenflags(stored_dlopen_flags)
{% endraw %}

```
### python/test/unit/fem/test_custom_assembler.py

```python

{% raw %}
101 |     petsc_lib_cffi = ffi.dlopen(petsc_lib_name)
104 |         petsc_lib_cffi = ffi.dlopen(os.path.join(petsc_dir, petsc_arch, "lib", "libpetsc.so"))
106 |         petsc_lib_cffi = ffi.dlopen(os.path.join(petsc_dir, petsc_arch, "lib", "libpetsc.dylib"))
{% endraw %}

```