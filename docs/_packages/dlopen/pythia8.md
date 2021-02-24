---
name: "pythia8"
layout: package
next_package: libtool
previous_package: dmtcp
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 8235
2 / 661 files match, 2 filtered matches.

 - [src/PartonDistributions.cc](#srcpartondistributionscc)
 - [include/Pythia8Plugins/PowhegProcs.h](#includepythia8pluginspowhegprocsh)

### src/PartonDistributions.cc

```cpp

{% raw %}
2616 |   map<string, pair<void*, int> >::iterator plugin =
2617 |     infoPtr->plugins.find(libName);
2618 |   if (plugin == infoPtr->plugins.end()) {
2619 |     lib   = dlopen(libName.c_str(), RTLD_LAZY);
2620 |     error = dlerror();
2621 |   }
{% endraw %}

```
### include/Pythia8Plugins/PowhegProcs.h

```c

{% raw %}
105 |   const char* error(0);
106 | 
107 |   // Load the library.
108 |   lib = dlopen(("libpythia8powheg" + proc + ".so").c_str(), RTLD_LAZY);
109 |   error = dlerror();
110 |   if (error) {
{% endraw %}

```