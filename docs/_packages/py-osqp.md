---
name: "py-osqp"
layout: package
next_package: py-petsc4py
previous_package: py-or-tools
languages: ['c']
---
## 0.6.1
1 / 159 files match, 1 filtered matches.

 - [osqp_sources/lin_sys/lib_handler.c](#osqp_sourceslin_syslib_handlerc)

### osqp_sources/lin_sys/lib_handler.c

```c

{% raw %}
22 |         #endif
23 |     }
24 | #else
25 |     h = dlopen (libName, RTLD_LAZY);
26 |     if (!h) {
27 |         #ifdef PRINTING
{% endraw %}

```