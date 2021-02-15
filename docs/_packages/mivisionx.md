---
name: "mivisionx"
layout: package
next_package: libssh2
previous_package: masurca
languages: ['cpp', 'python']
---
## 3.8.0
4 / 1738 files match

 - [rali/rali_pybind/third_party_lib/pybind11/include/pybind11/detail/internals.h](#ralirali_pybindthird_party_libpybind11includepybind11detailinternalsh)
 - [model_compiler/python/nnir_to_clib.py](#model_compilerpythonnnir_to_clibpy)
 - [apps/cloud_inference/server_app/inference.cpp](#appscloud_inferenceserver_appinferencecpp)
 - [amd_openvx/openvx/ago/ago_platform.cpp](#amd_openvxopenvxagoago_platformcpp)

### rali/rali_pybind/third_party_lib/pybind11/include/pybind11/detail/internals.h

```cpp

{% raw %}
49 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```
### model_compiler/python/nnir_to_clib.py

```python

{% raw %}
1209 |     libHandle = dlopen(library_name, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### apps/cloud_inference/server_app/inference.cpp

```

{% raw %}
634 |         moduleHandle = dlopen(modulePath.c_str(), RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### amd_openvx/openvx/ago/ago_platform.cpp

```

{% raw %}
92 | 	return (ago_module) dlopen(libFileName, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```