---
name: "osqp"
layout: package
next_package: libid3tag
previous_package: fpocket
languages: ['cpp']
---
## master
2 / 240 files match

 - [.valgrind-suppress.supp](#valgrind-suppresssupp)
 - [lin_sys/lib_handler.c](#lin_syslib_handlerc)

### .valgrind-suppress.supp

```

{% raw %}
37 |    fun:dlopen_doit
40 |    fun:dlopen@@GLIBC_2.2.5
{% endraw %}

```
### lin_sys/lib_handler.c

```cpp

{% raw %}
25 |     h = dlopen (libName, RTLD_LAZY);
{% endraw %}

```