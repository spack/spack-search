---
name: "rocksdb"
layout: package
next_package: cppcheck
previous_package: atompaw
languages: ['cpp']
---
## 6.7.3
2 / 1539 files match, 1 filtered matches.

 - [env/env_posix.cc](#envenv_posixcc)

### env/env_posix.cc

```cpp

{% raw %}
168 |       void* hndl = dlopen(NULL, RTLD_NOW);
185 |         void* hndl = dlopen(library_name.c_str(), RTLD_NOW);
196 |             void* hndl = dlopen(full_name.c_str(), RTLD_NOW);
{% endraw %}

```