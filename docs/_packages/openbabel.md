---
name: "openbabel"
layout: package
next_package: py-easybuild-framework
previous_package: aria2
languages: []
---
## 2.4.0
3 / 1131 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [src/dlhandler_unix.cpp](#srcdlhandler_unixcpp)
 - [scripts/CMakeLists.txt](#scriptscmakeliststxt)

### CMakeLists.txt

```

{% raw %}
233 | check_library_exists(dl dlopen "" HAVE_LIBDL)
{% endraw %}

```
### src/dlhandler_unix.cpp

```

{% raw %}
164 |   bool success = (dlopen(lib_name.c_str(), RTLD_LAZY | RTLD_GLOBAL) != 0);
{% endraw %}

```
### scripts/CMakeLists.txt

```

{% raw %}
87 |               COMMAND ${CMAKE_COMMAND} -E echo "  sys.setdlopenflags(sys.getdlopenflags() | dl.RTLD_GLOBAL)" >> ob.py
{% endraw %}

```