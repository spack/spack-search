---
name: "autoconf-archive"
layout: package
next_package: hipsycl
previous_package: libksba
languages: []
---
## 2019.01.06
2 / 1161 files match

 - [m4/ax_lua.m4](#m4ax_luam4)
 - [m4/ax_xercesc.m4](#m4ax_xercescm4)

### m4/ax_lua.m4

```

{% raw %}
614 |     AC_SEARCH_LIBS([dlopen], [dl])
621 |     AS_IF([test "x$ac_cv_search_dlopen" != 'xno' &&
622 |            test "x$ac_cv_search_dlopen" != 'xnone required'],
623 |       [_ax_lua_extra_libs="$_ax_lua_extra_libs $ac_cv_search_dlopen"])
{% endraw %}

```
### m4/ax_xercesc.m4

```

{% raw %}
353 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```