---
name: "hepmc3"
layout: package
next_package: stc
previous_package: amdfftw
languages: ['cpp']
---
## 3.2.2
3 / 373 files match, 2 filtered matches.

 - [src/WriterPlugin.cc](#srcwriterplugincc)
 - [src/ReaderPlugin.cc](#srcreaderplugincc)

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