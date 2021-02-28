---
name: "aspect"
layout: package
next_package: clamav
previous_package: podio
library_name: dlopen
matches: ['dlopen']
languages: ['cpp']
---
## 2.0.0
2 / 1995 files match, 1 filtered matches.

 - [source/main.cc](#sourcemaincc)

### source/main.cc

```cpp

{% raw %}
228 |                       << shared_libs_list[i]
229 |                       << ">" << std::endl;
230 | 
231 |           void *handle = dlopen (shared_libs_list[i].c_str(), RTLD_LAZY);
232 |           AssertThrow (handle != NULL,
233 |                        ExcMessage (std::string("Could not successfully load shared library <")
{% endraw %}

```