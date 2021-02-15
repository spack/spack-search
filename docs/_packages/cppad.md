---
name: "cppad"
layout: package
next_package: cmake
previous_package: mesquite
languages: []
---
## develop
2 / 1308 files match

 - [configure.ac](#configureac)
 - [speed/sacado/CMakeLists.txt](#speedsacadocmakeliststxt)

### configure.ac

```

{% raw %}
436 |     [dlopen],
{% endraw %}

```
### speed/sacado/CMakeLists.txt

```

{% raw %}
59 | CHECK_LIBRARY_EXISTS( dl dlopen "${CMAKE_SYSTEM_LIBRARY_PATH}" dl_found )
{% endraw %}

```