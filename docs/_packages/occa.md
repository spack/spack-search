---
name: "occa"
layout: package
next_package: libfs
previous_package: r-rmpi
languages: []
---
## 1.0.9
3 / 604 files match

 - [src/modes/serial/device.cpp](#srcmodesserialdevicecpp)
 - [src/tools/sys.cpp](#srctoolssyscpp)
 - [include/occa/tools/sys.hpp](#includeoccatoolssyshpp)

### src/modes/serial/device.cpp

```

{% raw %}
337 |       k.dlHandle = sys::dlopen(filename);
{% endraw %}

```
### src/tools/sys.cpp

```

{% raw %}
749 |     void* dlopen(const std::string &filename,
753 |       void *dlHandle = ::dlopen(filename.c_str(), RTLD_NOW);
759 |           OCCA_FORCE_ERROR("Error loading binary [" << io::shortname(filename) << "] with dlopen: " << error);
761 |           OCCA_FORCE_ERROR("Error loading binary [" << io::shortname(filename) << "] with dlopen");
{% endraw %}

```
### include/occa/tools/sys.hpp

```

{% raw %}
92 |     void* dlopen(const std::string &filename,
{% endraw %}

```