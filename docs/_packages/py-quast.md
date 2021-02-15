---
name: "py-quast"
layout: package
next_package: pax-utils
previous_package: nmap
languages: ['cpp']
---
## 4.6.1
2 / 2088 files match

 - [quast_libs/gnuplot/configure.in](#quast_libsgnuplotconfigurein)
 - [quast_libs/gnuplot/src/external.h](#quast_libsgnuplotsrcexternalh)

### quast_libs/gnuplot/configure.in

```

{% raw %}
242 |     AC_SEARCH_LIBS(dlopen, dl,
{% endraw %}

```
### quast_libs/gnuplot/src/external.h

```cpp

{% raw %}
100 | # define DLL_OPEN(f) dlopen((f), RTLD_NOW);
{% endraw %}

```