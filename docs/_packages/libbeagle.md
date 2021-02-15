---
name: "libbeagle"
layout: package
next_package: dimemas
previous_package: cc65
languages: ['cpp']
---
## 3.1.2
3 / 239 files match

 - [configure.ac](#configureac)
 - [libhmsbeagle/plugin/LibtoolSharedLibrary.h](#libhmsbeaglepluginlibtoolsharedlibraryh)
 - [libhmsbeagle/plugin/UnixSharedLibrary.h](#libhmsbeaglepluginunixsharedlibraryh)

### configure.ac

```

{% raw %}
86 |      AC_SEARCH_LIBS(dlopen,dl)
89 |   AC_SEARCH_LIBS(dlopen,dl)
{% endraw %}

```
### libhmsbeagle/plugin/LibtoolSharedLibrary.h

```cpp

{% raw %}
7 |  * the standard dlopen() interface
57 |     m_handle = lt_dlopen(libname.c_str());
{% endraw %}

```
### libhmsbeagle/plugin/UnixSharedLibrary.h

```cpp

{% raw %}
52 |     m_handle = dlopen(libname.c_str(),RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```