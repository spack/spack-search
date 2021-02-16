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

### src/SIOBlock.cc

```cpp

{% raw %}
145 |     void* libhandle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```