---
name: "osqp"
layout: package
next_package: p11-kit
previous_package: openwsman
languages: ['c']
---
## master
2 / 240 files match, 1 filtered matches.

 - [lin_sys/lib_handler.c](#lin_syslib_handlerc)

### lin_sys/lib_handler.c

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