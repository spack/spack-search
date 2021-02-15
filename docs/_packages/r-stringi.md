---
name: "r-stringi"
layout: package
next_package: varnish-cache
previous_package: portcullis
languages: []
---
## 1.1.3
1 / 1028 files match

 - [src/icu55/common/putil.cpp](#srcicu55commonputilcpp)

### src/icu55/common/putil.cpp

```

{% raw %}
135 | #    define HAVE_DLOPEN 0
140 | #   ifndef HAVE_DLOPEN
141 | #    define HAVE_DLOPEN 1
149 | #   define HAVE_DLOPEN 0
2060 | #if HAVE_DLOPEN && !U_PLATFORM_USES_ONLY_WIN32_API
2076 |   ret =  dlopen(libName, RTLD_NOW|RTLD_GLOBAL);
2079 |     printf("dlerror on dlopen(%s): %s\n", libName, dlerror());
{% endraw %}

```