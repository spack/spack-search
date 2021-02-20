---
name: "py-onnx"
layout: package
next_package: py-openmc
previous_package: py-numpy
languages: ['c']
---
## 1.5.0
4 / 2584 files match, 1 filtered matches.

 - [onnx/onnxifi_loader.c](#onnxonnxifi_loaderc)

### onnx/onnxifi_loader.c

```c

{% raw %}
88 | #else
89 |   /* Clear libdl error state */
90 |   dlerror();
91 |   onnx->handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
92 | #endif
93 |   if (onnx->handle == NULL) {
{% endraw %}

```