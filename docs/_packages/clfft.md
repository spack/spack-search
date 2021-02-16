---
name: "clfft"
layout: package
next_package: pkg-config
previous_package: gdk-pixbuf
languages: ['c']
---
## 2.12.2
3 / 159 files match, 1 filtered matches.

 - [src/include/sharedLibrary.h](#srcincludesharedlibraryh)

### src/include/sharedLibrary.h

```c

{% raw %}
41 | 	void* fileHandle = ::dlopen( linuxName.c_str( ), RTLD_NOW );
49 |   void* fileHandle = ::dlopen( appleName.c_str( ), RTLD_NOW );
57 |         void* fileHandle = ::dlopen( freebsdName.c_str( ), RTLD_NOW );
{% endraw %}

```