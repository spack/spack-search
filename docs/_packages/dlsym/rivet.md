---
name: "rivet"
layout: package
next_package: mono
previous_package: wget
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 1.1.2
3 / 451 files match, 1 filtered matches.

 - [src/AnalysisLoader.cc](#srcanalysisloadercc)

### src/AnalysisLoader.cc

```cpp

{% raw %}
61 |     _handles.insert(handle);
62 | 
63 |     // Perform dodgy cast to factory function     
64 |     void* fnptr = dlsym(handle, "getAnalysisBuilders");
65 |     anabuilders_fn getBuilders = evil_cast<anabuilders_fn>(fnptr);
66 |     if (!getBuilders) {
{% endraw %}

```