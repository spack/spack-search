---
name: "cdo"
layout: package
next_package: gcc
previous_package: nnvm
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 1.9.9
7 / 975 files match, 1 filtered matches.

 - [src/modules.cc](#srcmodulescc)

### src/modules.cc

```cpp

{% raw %}
561 | load_custom_module(std::string file_path)
562 | {
563 |   void (*init_custom_module)();
564 |   void *lib_handle = dlopen(file_path.c_str(), RTLD_LAZY);
565 |   custom_modules_lib_handles.push_back(lib_handle);
566 |   if (!lib_handle)
{% endraw %}

```