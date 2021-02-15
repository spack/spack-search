---
name: "arrayfire"
layout: package
next_package: perl-dbd-mysql
previous_package: libmesh
languages: ['cpp']
---
## 3.7.0
3 / 4691 files match

 - [src/backend/common/module_loading_unix.cpp](#srcbackendcommonmodule_loading_unixcpp)
 - [extern/forge/extern/glad/src/glad.c](#externforgeexterngladsrcgladc)
 - [extern/glad/src/glad.c](#externgladsrcgladc)

### src/backend/common/module_loading_unix.cpp

```

{% raw %}
24 |     return dlopen(library_name, RTLD_LAZY);
{% endraw %}

```
### extern/forge/extern/glad/src/glad.c

```cpp

{% raw %}
896 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### extern/glad/src/glad.c

```cpp

{% raw %}
896 |         libGL = dlopen(NAMES[index], RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```