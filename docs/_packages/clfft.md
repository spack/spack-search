---
name: "clfft"
layout: package
next_package: pkg-config
previous_package: gdk-pixbuf
languages: ['cpp']
---
## 2.12.2
3 / 159 files match

 - [src/include/sharedLibrary.h](#srcincludesharedlibraryh)
 - [src/callback-client/CMakeLists.txt](#srccallback-clientcmakeliststxt)
 - [src/client/CMakeLists.txt](#srcclientcmakeliststxt)

### src/include/sharedLibrary.h

```cpp

{% raw %}
41 | 	void* fileHandle = ::dlopen( linuxName.c_str( ), RTLD_NOW );
49 |   void* fileHandle = ::dlopen( appleName.c_str( ), RTLD_NOW );
57 |         void* fileHandle = ::dlopen( freebsdName.c_str( ), RTLD_NOW );
{% endraw %}

```
### src/callback-client/CMakeLists.txt

```

{% raw %}
38 | 	# To use the dlopen() and dlclose() functions, we should link with libdl
{% endraw %}

```
### src/client/CMakeLists.txt

```

{% raw %}
36 | 	# To use the dlopen() and dlclose() functions, we should link with libdl
{% endraw %}

```