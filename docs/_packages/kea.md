---
name: "kea"
layout: package
next_package: keepalived
previous_package: kcov
languages: ['cpp', 'c']
---
## 1.6.2
13 / 2822 files match, 2 filtered matches.

 - [src/lib/hooks/library_manager.cc](#srclibhookslibrary_managercc)
 - [src/lib/hooks/library_manager.h](#srclibhookslibrary_managerh)

### src/lib/hooks/library_manager.cc

```cpp

{% raw %}
72 | 
73 |     // Open the library.  We'll resolve names now, so that if there are any
74 |     // issues we don't bugcheck in the middle of apparently unrelated code.
75 |     dl_handle_ = dlopen(library_name_.c_str(), RTLD_NOW | RTLD_LOCAL);
76 |     if (dl_handle_ == NULL) {
77 |         LOG_ERROR(hooks_logger, HOOKS_OPEN_ERROR).arg(library_name_)
{% endraw %}

```
### src/lib/hooks/library_manager.h

```c

{% raw %}
212 | 
213 |     // Member variables
214 | 
215 |     void*       dl_handle_;     ///< Handle returned by dlopen
216 |     int         index_;         ///< Index associated with this library
217 |     boost::shared_ptr<CalloutManager> manager_;
{% endraw %}

```