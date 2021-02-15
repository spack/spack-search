---
name: "wcs"
layout: package
next_package: whizard
previous_package: postgresql
languages: []
---
## develop
1 / 192 files match

 - [src/utils/graph_factory.hpp](#srcutilsgraph_factoryhpp)

### src/utils/graph_factory.hpp

```

{% raw %}
16 | #include <dlfcn.h> //dlopen
244 |   void* handle = dlopen(("./" + library_file).c_str(), RTLD_LAZY);
{% endraw %}

```