---
name: "pythia8"
layout: package
next_package: masurca
previous_package: dbus
languages: ['cpp', 'c']
---
## 8235
2 / 661 files match, 2 filtered matches.

 - [src/PartonDistributions.cc](#srcpartondistributionscc)
 - [include/Pythia8Plugins/PowhegProcs.h](#includepythia8pluginspowhegprocsh)

### src/PartonDistributions.cc

```cpp

{% raw %}
2619 |     lib   = dlopen(libName.c_str(), RTLD_LAZY);
{% endraw %}

```
### include/Pythia8Plugins/PowhegProcs.h

```c

{% raw %}
108 |   lib = dlopen(("libpythia8powheg" + proc + ".so").c_str(), RTLD_LAZY);
{% endraw %}

```