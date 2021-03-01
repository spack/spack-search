---
name: "cdo"
layout: package
next_package: chrony
previous_package: casacore
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 1.9.5
5 / 916 files match, 1 filtered matches.

 - [src/modules.cc](#srcmodulescc)

### src/modules.cc

```cpp

{% raw %}
507 |     }
508 | 
509 |   dlerror();
510 |   init_custom_module = (void (*)()) dlsym(lib_handle, "init_custom_module");
511 |   const char *dlsym_error = dlerror();
512 | 
513 |   if (dlsym_error)
514 |     {
515 |       std::cerr << "Cannot load symbol 'init_custom_module': " << dlsym_error << std::endl;
516 |       dlclose(lib_handle);
517 |       return;
{% endraw %}

```