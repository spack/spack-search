---
name: "rocksdb"
layout: package
next_package: cppcheck
previous_package: atompaw
languages: ['cpp']
---
## 6.7.3
2 / 1539 files match

 - [env/env_posix.cc](#envenv_posixcc)
 - [port/jemalloc_helper.h](#portjemalloc_helperh)

### env/env_posix.cc

```cpp

{% raw %}
168 |       void* hndl = dlopen(NULL, RTLD_NOW);
185 |         void* hndl = dlopen(library_name.c_str(), RTLD_NOW);
196 |             void* hndl = dlopen(full_name.c_str(), RTLD_NOW);
{% endraw %}

```
### port/jemalloc_helper.h

```cpp

{% raw %}
63 | // allocate memory and see if it is through jemalloc, to handle the dlopen()
{% endraw %}

```