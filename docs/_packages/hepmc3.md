---
name: "hepmc3"
layout: package
next_package: stc
previous_package: amdfftw
languages: ['cpp']
---
## 3.2.2
3 / 373 files match

 - [src/WriterPlugin.cc](#srcwriterplugincc)
 - [src/ReaderPlugin.cc](#srcreaderplugincc)
 - [python/include/pybind11/detail/internals.h](#pythonincludepybind11detailinternalsh)

### src/WriterPlugin.cc

```cpp

{% raw %}
42 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
66 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/ReaderPlugin.cc

```cpp

{% raw %}
41 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
65 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### python/include/pybind11/detail/internals.h

```cpp

{% raw %}
49 | // Python loads modules by default with dlopen with the RTLD_LOCAL flag; under libc++ and possibly
{% endraw %}

```