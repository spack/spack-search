---
name: "cdo"
layout: package
next_package: gcc
previous_package: nnvm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 1.9.9
5 / 975 files match, 1 filtered matches.

 - [src/modules.cc](#srcmodulescc)

### src/modules.cc

```cpp

{% raw %}
570 |     }
571 | 
572 |   dlerror();
573 |   init_custom_module = (void (*)()) dlsym(lib_handle, "init_custom_module");
574 |   const char *dlsym_error = dlerror();
575 | 
576 |   if (dlsym_error)
577 |     {
578 |       std::cerr << "Cannot load symbol 'init_custom_module': " << dlsym_error << std::endl;
579 |       dlclose(lib_handle);
580 |       return;
{% endraw %}

```