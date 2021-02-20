---
name: "podio"
layout: package
next_package: polymake
previous_package: pocl
languages: ['cpp']
---
## master
2 / 135 files match, 1 filtered matches.

 - [src/SIOBlock.cc](#srcsioblockcc)

### src/SIOBlock.cc

```cpp

{% raw %}
142 |       return;
143 |     }
144 | 
145 |     void* libhandle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
146 |     if (libhandle) {
147 |       std::cout << "Loading SIOBlocks library \'" << libname << "\'" << std::endl;
{% endraw %}

```