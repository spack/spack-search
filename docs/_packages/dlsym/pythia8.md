---
name: "pythia8"
layout: package
next_package: bcftools
previous_package: zfs
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 8235
7 / 661 files match, 3 filtered matches.

 - [src/PartonDistributions.cc](#srcpartondistributionscc)
 - [include/Pythia8Plugins/PowhegProcs.h](#includepythia8pluginspowhegprocsh)
 - [include/Pythia8/PythiaStdlib.h](#includepythia8pythiastdlibh)

### src/PartonDistributions.cc

```cpp

{% raw %}
2684 |   if (!infoPtr) return sym;
2685 | 
2686 |   // Load the symbol.
2687 |   sym = (Symbol)dlsym(lib, symName.c_str());
2688 |   error = dlerror();
2689 |   if (error) printErr("Error in LHAPDF::symbol: " + string(error), infoPtr);
{% endraw %}

```
### include/Pythia8Plugins/PowhegProcs.h

```c

{% raw %}
115 |   dlerror();
116 | 
117 |   // Load the LHAup pointer.
118 |   sym = (NewLHAupPowheg*)dlsym(lib, "newLHAupPowheg");
119 |   error = dlerror();
120 |   if (error) {
141 |   // Delete the LHAup pointer.
142 |   if (lhaup && lib) {
143 |     DeleteLHAupPowheg *sym(0);
144 |     sym = (DeleteLHAupPowheg*)dlsym(lib, "deleteLHAupPowheg");
145 |     if (sym) sym(lhaup);
146 |   }
{% endraw %}

```
### include/Pythia8/PythiaStdlib.h

```c

{% raw %}
28 | #undef dlsym
29 | 
30 | // Redefine dlsym to suppress compiler warnings.
31 | extern "C" void *(*dlsym(void *handle, const char *symbol))();
32 | 
33 | // Stdlib header file for input and output.
{% endraw %}

```