---
name: "moab"
layout: package
next_package: nix
previous_package: aml
languages: []
---
## 5.0.1
1 / 1807 files match

 - [configure.ac](#configureac)

### configure.ac

```

{% raw %}
68 | LT_INIT([dlopen])
180 | AC_CHECK_LIB(dl, dlopen, LIBS="$LIBS -ldl")
{% endraw %}

```