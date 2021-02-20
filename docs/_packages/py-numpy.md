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
93 |      * AVX and the OS version is Mavericks */
94 |     AVX_and_10_9 = AVX && MAVERICKS;
95 |     /* load vecLib */
96 |     veclib = dlopen(VECLIB_FILE, RTLD_LOCAL | RTLD_FIRST);
97 |     if (!veclib) {
98 |         veclib = NULL;
{% endraw %}

```