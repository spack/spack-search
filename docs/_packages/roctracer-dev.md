---
name: "roctracer-dev"
layout: package
next_package: root
previous_package: rocprofiler-dev
languages: ['c']
---
## 3.10.0
2 / 71 files match, 1 filtered matches.

 - [src/core/loader.h](#srccoreloaderh)

### src/core/loader.h

```c

{% raw %}
52 |   private:
53 |   BaseLoader() {
54 |     const int flags = (to_load_ == true) ? RTLD_LAZY : RTLD_LAZY|RTLD_NOLOAD;
55 |     handle_ = dlopen(lib_name_, flags);
56 |     ONLD_TRACE("(" << lib_name_ << " = " << handle_ << ")");
57 |     if ((to_check_open_ == true) && (handle_ == NULL)) {
{% endraw %}

```