---
name: "podio"
layout: package
next_package: libxaw
previous_package: xcb-util-renderutil
languages: ['cpp']
---
## master
2 / 135 files match

 - [src/SIOBlock.cc](#srcsioblockcc)
 - [include/podio/SIOBlock.h](#includepodiosioblockh)

### src/SIOBlock.cc

```cpp

{% raw %}
145 |     void* libhandle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### include/podio/SIOBlock.h

```cpp

{% raw %}
133 |      * Load a library with the given name via dlopen
{% endraw %}

```