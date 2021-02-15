---
name: "henson"
layout: package
next_package: harminv
previous_package: ibm-databroker
languages: ['cpp']
---
## master
4 / 237 files match

 - [README.md](#readmemd)
 - [include/chaiscript/language/chaiscript_engine.hpp](#includechaiscriptlanguagechaiscript_enginehpp)
 - [include/henson/puppet.hpp](#includehensonpuppethpp)
 - [ext/pybind11/include/pybind11/detail/internals.h](#extpybind11includepybind11detailinternalsh)

### README.md

```

{% raw %}
73 | can be loaded using the [dynamic loading](https://en.wikipedia.org/wiki/Dynamic_loading) facilities `dlopen` and `dlsym`:
78 | void*       lib      = dlopen(fn.c_str(), RTLD_LAZY);
{% endraw %}

```
### include/chaiscript/language/chaiscript_engine.hpp

```

{% raw %}
74 |           : m_data(dlopen(t_filename.c_str(), RTLD_NOW))
{% endraw %}

```
### include/henson/puppet.hpp

```

{% raw %}
65 |                             void* lib = dlopen(filename_.c_str(), RTLD_LAZY);
{% endraw %}

```
### ext/pybind11/include/pybind11/detail/internals.h

```cpp

{% raw %}
49 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```