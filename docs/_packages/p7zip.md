---
name: "p7zip"
layout: package
next_package: at-spi2-atk
previous_package: quota
languages: []
---
## 16.02
1 / 1236 files match

 - [CPP/Windows/DLL.cpp](#cppwindowsdllcpp)

### CPP/Windows/DLL.cpp

```

{% raw %}
11 | #include <dlfcn.h>  // dlopen ...
131 |   int options_dlopen = 0;
133 |   options_dlopen |= RTLD_LOCAL;
136 |   options_dlopen |= RTLD_NOW;
140 |   options_dlopen |= RTLD_GROUP; // mainly for solaris but not for HPUX
143 |   TRACEN((printf("CLibrary::Load - dlopen(%s,0x%d)\n",name,options_dlopen)))
144 |   handler = dlopen(name,options_dlopen);
{% endraw %}

```