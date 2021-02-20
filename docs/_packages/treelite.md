---
name: "treelite"
layout: package
next_package: trilinos
previous_package: tpm2-tss
languages: ['cpp']
---
## 0.93
1 / 216 files match, 1 filtered matches.

 - [src/predictor/predictor.cc](#srcpredictorpredictorcc)

### src/predictor/predictor.cc

```cpp

{% raw %}
55 | #ifdef _WIN32
56 |   HMODULE handle = LoadLibraryA(name);
57 | #else
58 |   void* handle = dlopen(name, RTLD_LAZY | RTLD_LOCAL);
59 | #endif
60 |   return static_cast<treelite::Predictor::LibraryHandle>(handle);
{% endraw %}

```