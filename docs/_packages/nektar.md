---
name: "nektar"
layout: package
next_package: mesquite
previous_package: mpe2
languages: ['cmake']
---
## 5.0.0
1 / 3267 files match

 - [cmake/ThirdPartyPython.cmake](#cmakethirdpartypythoncmake)

### cmake/ThirdPartyPython.cmake

```cmake

{% raw %}
144 |     FILE(WRITE ${CMAKE_BINARY_DIR}/NekPy/__init__.py "# Adjust dlopen flags to avoid OpenMPI issues
148 |     sys.setdlopenflags(dl.RTLD_NOW|dl.RTLD_GLOBAL)
{% endraw %}

```