---
name: "gatepet2stir"
layout: package
next_package: gawk
previous_package: fuse-overlayfs
languages: ['c']
---
## 1.3.2
1 / 2303 files match, 1 filtered matches.

 - [include/root/Reflex/SharedLibrary.h](#includerootreflexsharedlibraryh)

### include/root/Reflex/SharedLibrary.h

```c

{% raw %}
101 |    ::SetErrorMode(0);
102 |    fHandle = ::LoadLibrary(fLibName.c_str());
103 | #else
104 |    fHandle = ::dlopen(fLibName.c_str(), RTLD_LAZY | RTLD_GLOBAL);
105 | #endif
106 | 
{% endraw %}

```