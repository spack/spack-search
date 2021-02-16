---
name: "py-numpy"
layout: package
next_package: py-onnx
previous_package: py-mypy
languages: ['c']
---
## 1.10.4
1 / 1215 files match, 1 filtered matches.

 - [numpy/_build_utils/src/apple_sgemv_fix.c](#numpy_build_utilssrcapple_sgemv_fixc)

### numpy/_build_utils/src/apple_sgemv_fix.c

```c

{% raw %}
96 |     veclib = dlopen(VECLIB_FILE, RTLD_LOCAL | RTLD_FIRST);
{% endraw %}

```