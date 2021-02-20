---
name: "py-or-tools"
layout: package
next_package: py-osqp
previous_package: py-openmc
languages: ['c']
---
## 7.8
1 / 68418 files match, 1 filtered matches.

 - [ortools/base/dynamic_library.h](#ortoolsbasedynamic_libraryh)

### ortools/base/dynamic_library.h

```c

{% raw %}
49 | #if defined(_MSC_VER)
50 |     library_handle_ = static_cast<void *>(LoadLibrary(library_name.c_str()));
51 | #elif defined(__GNUC__)
52 |     library_handle_ = dlopen(library_name.c_str(), RTLD_NOW);
53 | #endif
54 |     return library_handle_ != nullptr;
{% endraw %}

```