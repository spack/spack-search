---
name: "psi4"
layout: package
next_package: psm
previous_package: prrte
languages: ['cpp']
---
## 1.3.2
1 / 6094 files match, 1 filtered matches.

 - [psi4/src/psi4/libplugin/load_plugin.cc](#psi4srcpsi4libpluginload_plugincc)

### psi4/src/psi4/libplugin/load_plugin.cc

```cpp

{% raw %}
44 | plugin_info plugin_load(std::string &plugin_pathname) {
45 |     plugin_info info;
46 | 
47 |     info.plugin_handle = dlopen(plugin_pathname.c_str(), RTLD_LAZY);
48 |     if (info.plugin_handle == nullptr) {
49 |         std::string msg = "load_plugin: Cannot open library: ";
{% endraw %}

```