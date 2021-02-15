---
name: "icu4c"
layout: package
next_package: dbus
previous_package: polymake
languages: []
---
## 67.1
3 / 2302 files match

 - [source/configure.ac](#sourceconfigureac)
 - [source/common/putil.cpp](#sourcecommonputilcpp)
 - [source/test/depstest/dependencies.txt](#sourcetestdepstestdependenciestxt)

### source/configure.ac

```

{% raw %}
475 |    AC_SEARCH_LIBS([dlopen], [dl])
476 |    AC_CHECK_FUNCS([dlopen])
478 |    if test "x$ac_cv_func_dlopen" != xyes; then
479 |       CONFIG_CPPFLAGS="$CONFIG_CPPFLAGS -DHAVE_DLOPEN=0"
{% endraw %}

```
### source/common/putil.cpp

```

{% raw %}
142 | #    define HAVE_DLOPEN 0
147 | #   ifndef HAVE_DLOPEN
148 | #    define HAVE_DLOPEN 1
156 | #   define HAVE_DLOPEN 0
2290 | #if U_ENABLE_DYLOAD && HAVE_DLOPEN && !U_PLATFORM_USES_ONLY_WIN32_API
2305 |   ret =  dlopen(libName, RTLD_NOW|RTLD_GLOBAL);
2308 |     printf("dlerror on dlopen(%s): %s\n", libName, dlerror());
{% endraw %}

```
### source/test/depstest/dependencies.txt

```

{% raw %}
113 |     dlopen dlclose dlsym  # called by putil.o only for icuplug.o
{% endraw %}

```