---
name: "py-fenics-dolfinx"
layout: package
next_package: py-gevent
previous_package: py-cyvcf2
languages: ['python']
---
## master
2 / 374 files match, 2 filtered matches.

 - [python/dolfinx/__init__.py](#pythondolfinx__init__py)
 - [python/test/unit/fem/test_custom_assembler.py](#pythontestunitfemtest_custom_assemblerpy)

### python/dolfinx/__init__.py

```python

{% raw %}
8 | 
9 | # Store dl open flags to restore them after import
10 | import sys
11 | stored_dlopen_flags = sys.getdlopenflags()
12 | 
13 | # Developer note: below is related to OpenMPI
19 |     except ImportError:
20 |         RTLD_NOW = 2
21 |         RTLD_GLOBAL = 256
22 |     sys.setdlopenflags(RTLD_NOW | RTLD_GLOBAL)
23 | del sys
24 | 
{% endraw %}

```
### python/test/unit/fem/test_custom_assembler.py

```python

{% raw %}
98 | 
99 | 
100 | if petsc_lib_name is not None:
101 |     petsc_lib_cffi = ffi.dlopen(petsc_lib_name)
102 | else:
103 |     try:
104 |         petsc_lib_cffi = ffi.dlopen(os.path.join(petsc_dir, petsc_arch, "lib", "libpetsc.so"))
105 |     except OSError:
106 |         petsc_lib_cffi = ffi.dlopen(os.path.join(petsc_dir, petsc_arch, "lib", "libpetsc.dylib"))
107 |     except OSError:
108 |         print("Could not load PETSc library for CFFI (ABI mode).")
{% endraw %}

```