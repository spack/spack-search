---
name: "py-onnx"
layout: package
next_package: freexl
previous_package: gobject-introspection
languages: ['cpp']
---
## 1.5.0
4 / 2584 files match

 - [third_party/pybind11/include/pybind11/detail/internals.h](#third_partypybind11includepybind11detailinternalsh)
 - [third_party/pybind11/docs/faq.rst](#third_partypybind11docsfaqrst)
 - [onnx/onnxifi_loader.c](#onnxonnxifi_loaderc)
 - [onnx/onnxifi_loader.h](#onnxonnxifi_loaderh)

### third_party/pybind11/include/pybind11/detail/internals.h

```cpp

{% raw %}
20 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```
### third_party/pybind11/docs/faq.rst

```

{% raw %}
172 | typically using ``dlopen`` with the ``RTLD_LOCAL`` flag), this Python default
{% endraw %}

```
### onnx/onnxifi_loader.c

```cpp

{% raw %}
91 |   onnx->handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### onnx/onnxifi_loader.h

```cpp

{% raw %}
30 |    * dlopen (on other operating systems and environments).
{% endraw %}

```