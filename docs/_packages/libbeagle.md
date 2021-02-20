---
name: "libbeagle"
layout: package
next_package: libcanberra
previous_package: lftp
languages: ['c']
---
## 3.1.2
3 / 239 files match, 2 filtered matches.

 - [libhmsbeagle/plugin/LibtoolSharedLibrary.h](#libhmsbeaglepluginlibtoolsharedlibraryh)
 - [libhmsbeagle/plugin/UnixSharedLibrary.h](#libhmsbeaglepluginunixsharedlibraryh)

### libhmsbeagle/plugin/LibtoolSharedLibrary.h

```c

{% raw %}
54 |     libname += ".0.0";
55 | #endif
56 | 
57 |     m_handle = lt_dlopen(libname.c_str());
58 |     if (m_handle == 0)
59 |     {
{% endraw %}

```
### libhmsbeagle/plugin/UnixSharedLibrary.h

```c

{% raw %}
49 |     libname += ".0.0";
50 | #endif
51 | 
52 |     m_handle = dlopen(libname.c_str(),RTLD_NOW|RTLD_GLOBAL);
53 |     if (m_handle == 0)
54 |     {
{% endraw %}

```