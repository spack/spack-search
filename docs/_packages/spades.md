---
name: "spades"
layout: package
next_package: mariadb-c-client
previous_package: frontier-client
languages: []
---
## 3.15.0
3 / 7828 files match

 - [ext/src/llvm/CMakeLists.txt](#extsrcllvmcmakeliststxt)
 - [ext/src/mimalloc/CMakeLists.txt](#extsrcmimalloccmakeliststxt)
 - [ext/src/googletest/googletest/cmake/libgtest.la.in](#extsrcgoogletestgoogletestcmakelibgtestlain)

### ext/src/llvm/CMakeLists.txt

```

{% raw %}
54 | check_library_exists(dl dlopen "" HAVE_LIBDL)
{% endraw %}

```
### ext/src/mimalloc/CMakeLists.txt

```

{% raw %}
18 | option(MI_LOCAL_DYNAMIC_TLS "Use slightly slower, dlopen-compatible TLS mechanism (Unix)" OFF)
{% endraw %}

```
### ext/src/googletest/googletest/cmake/libgtest.la.in

```

{% raw %}
15 | # Files to dlopen/dlpreopen
16 | dlopen=''
{% endraw %}

```