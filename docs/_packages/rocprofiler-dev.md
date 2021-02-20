---
name: "rocprofiler-dev"
layout: package
next_package: roctracer-dev
previous_package: rocm-openmp-extras
languages: ['c']
---
## 3.9.0
5 / 152 files match, 1 filtered matches.

 - [roctracer/src/core/loader.h](#roctracersrccoreloaderh)

### roctracer/src/core/loader.h

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