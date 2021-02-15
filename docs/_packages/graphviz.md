---
name: "graphviz"
layout: package
next_package: lvm2
previous_package: jemalloc
languages: ['cpp']
---
## 2.46.0
3 / 3596 files match

 - [configure.ac](#configureac)
 - [lib/gvc/gvplugin.c](#libgvcgvpluginc)
 - [m4/lib-link.m4](#m4lib-linkm4)

### configure.ac

```

{% raw %}
472 | LT_INIT([dlopen])
{% endraw %}

```
### lib/gvc/gvplugin.c

```cpp

{% raw %}
200 |     hndl = lt_dlopen(p);
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
380 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```