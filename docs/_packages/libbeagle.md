---
name: "libbeagle"
layout: package
next_package: dimemas
previous_package: cc65
languages: ['c']
---
## 3.1.2
3 / 239 files match, 2 filtered matches.

 - [libhmsbeagle/plugin/LibtoolSharedLibrary.h](#libhmsbeaglepluginlibtoolsharedlibraryh)
 - [libhmsbeagle/plugin/UnixSharedLibrary.h](#libhmsbeaglepluginunixsharedlibraryh)

### libhmsbeagle/plugin/LibtoolSharedLibrary.h

```c

{% raw %}
57 |     m_handle = lt_dlopen(libname.c_str());
{% endraw %}

```
### libhmsbeagle/plugin/UnixSharedLibrary.h

```c

{% raw %}
52 |     m_handle = dlopen(libname.c_str(),RTLD_NOW|RTLD_GLOBAL);
{% endraw %}

```