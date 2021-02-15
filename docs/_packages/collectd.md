---
name: "collectd"
layout: package
next_package: erne
previous_package: gridlab-d
languages: ['cpp']
---
## 5.10.0
2 / 489 files match

 - [configure.ac](#configureac)
 - [src/daemon/plugin.c](#srcdaemonpluginc)

### configure.ac

```

{% raw %}
13 | LT_INIT([dlopen disable-static])
64 | if test "x$lt_cv_dlopen" = "xno"; then
65 |   AC_MSG_ERROR([Your system does not support dlopen])
68 | AC_SUBST([DLOPEN_LIBS], [$lt_cv_dlopen_libs])
{% endraw %}

```
### src/daemon/plugin.c

```cpp

{% raw %}
415 |   void *dlh = dlopen(file, flags);
420 |              "dlopen(\"%s\") failed: %s. "
{% endraw %}

```