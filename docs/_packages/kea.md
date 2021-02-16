---
name: "kea"
layout: package
next_package: lumpy-sv
previous_package: ncftp
languages: ['cpp', 'c']
---
## 1.6.2
13 / 2822 files match

 - [src/lib/hooks/library_manager.cc](#srclibhookslibrary_managercc)
 - [src/lib/hooks/library_manager.h](#srclibhookslibrary_managerh)

### src/lib/hooks/library_manager.cc

```cpp

{% raw %}
75 |     dl_handle_ = dlopen(library_name_.c_str(), RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### src/lib/hooks/library_manager.h

```c

{% raw %}
215 |     void*       dl_handle_;     ///< Handle returned by dlopen
{% endraw %}

```