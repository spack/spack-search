---
name: "psi4"
layout: package
next_package: biobloom
previous_package: xz
languages: ['cpp']
---
## 1.3.2
1 / 6094 files match, 1 filtered matches.

 - [psi4/src/psi4/libplugin/load_plugin.cc](#psi4srcpsi4libpluginload_plugincc)

### psi4/src/psi4/libplugin/load_plugin.cc

```cpp

{% raw %}
47 |     info.plugin_handle = dlopen(plugin_pathname.c_str(), RTLD_LAZY);
{% endraw %}

```