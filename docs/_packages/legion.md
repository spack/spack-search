---
name: "legion"
layout: package
next_package: lftp
previous_package: lammps
languages: ['cpp']
---
## master
7 / 2126 files match, 3 filtered matches.

 - [runtime/realm/codedesc.cc](#runtimerealmcodedesccc)
 - [runtime/realm/module.cc](#runtimerealmmodulecc)
 - [runtime/realm/python/python_module.cc](#runtimerealmpythonpython_modulecc)

### runtime/realm/codedesc.cc

```cpp

{% raw %}
373 | 	handle = dlopen(*dso_name ? dso_name : 0, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### runtime/realm/module.cc

```cpp

{% raw %}
175 |       void *handle = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### runtime/realm/python/python_module.cc

```cpp

{% raw %}
163 |     handle = dlopen(python_lib, RTLD_GLOBAL | RTLD_LAZY);
{% endraw %}

```