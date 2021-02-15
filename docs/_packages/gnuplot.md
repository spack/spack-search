---
name: "gnuplot"
layout: package
next_package: libpipeline
previous_package: py-pyarrow
languages: ['cpp']
---
## 5.0.1
2 / 726 files match

 - [configure.in](#configurein)
 - [src/external.h](#srcexternalh)

### configure.in

```

{% raw %}
241 |     AC_SEARCH_LIBS(dlopen, dl,
{% endraw %}

```
### src/external.h

```cpp

{% raw %}
100 | # define DLL_OPEN(f) dlopen((f), RTLD_NOW);
{% endraw %}

```