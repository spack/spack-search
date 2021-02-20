---
name: "py-scipy"
layout: package
next_package: py-setuptools
previous_package: py-rpy2
languages: ['c']
---
## 1.0.0
2 / 2587 files match, 1 filtered matches.

 - [scipy/_build_utils/src/apple_sgemv_fix.c](#scipy_build_utilssrcapple_sgemv_fixc)

### scipy/_build_utils/src/apple_sgemv_fix.c

```c

{% raw %}
91 |      * AVX and the OS version is Mavericks */
92 |     AVX_and_10_9 = AVX && MAVERICKS;
93 |     /* load vecLib */
94 |     veclib = dlopen(VECLIB_FILE, RTLD_LOCAL | RTLD_FIRST);
95 |     if (!veclib) {
96 |         veclib = NULL;
{% endraw %}

```