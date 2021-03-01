---
name: "cdo"
layout: package
next_package: clamav
previous_package: casacore
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 1.9.5
7 / 916 files match, 1 filtered matches.

 - [src/modules.cc](#srcmodulescc)

### src/modules.cc

```cpp

{% raw %}
498 | load_custom_module(std::string file_path)
499 | {
500 |   void (*init_custom_module)();
501 |   void *lib_handle = dlopen(file_path.c_str(), RTLD_LAZY);
502 |   custom_modules_lib_handles.push_back(lib_handle);
503 |   if (!lib_handle)
{% endraw %}

```