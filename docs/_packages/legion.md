---
name: "legion"
layout: package
next_package: gmt
previous_package: libnsl
languages: ['cpp']
---
## master
7 / 2126 files match

 - [bindings/python/legion_cffi.py.in](#bindingspythonlegion_cffipyin)
 - [runtime/realm/codedesc.cc](#runtimerealmcodedesccc)
 - [runtime/realm/module.cc](#runtimerealmmodulecc)
 - [runtime/realm/python/python_module.cc](#runtimerealmpythonpython_modulecc)
 - [runtime/legion/runtime.cc](#runtimelegionruntimecc)
 - [language/src/regent/cudahelper.t](#languagesrcregentcudahelpert)
 - [language/src/regent/openmphelper.t](#languagesrcregentopenmphelpert)

### bindings/python/legion_cffi.py.in

```

{% raw %}
29 | lib = ffi.dlopen(None)
{% endraw %}

```
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
162 |     // life is so much easier if we use dlopen (but we only get one copy then)
163 |     handle = dlopen(python_lib, RTLD_GLOBAL | RTLD_LAZY);
{% endraw %}

```
### runtime/legion/runtime.cc

```cpp

{% raw %}
12353 |           // This is a little scary, we could still be inside of dlopen when
17672 |       // Converting the DSO reference could call dlopen and might block
{% endraw %}

```
### language/src/regent/cudahelper.t

```

{% raw %}
97 |         var lib = dlfcn.dlopen([&int8](0), dlfcn.RTLD_LAZY)
{% endraw %}

```
### language/src/regent/openmphelper.t

```

{% raw %}
32 |     var lib = dlfcn.dlopen([&int8](0), dlfcn.RTLD_LAZY)
{% endraw %}

```