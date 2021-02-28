---
name: "treelite"
layout: package
next_package: libunwind
previous_package: pnmpi
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 0.93
1 / 216 files match, 1 filtered matches.

 - [src/predictor/predictor.cc](#srcpredictorpredictorcc)

### src/predictor/predictor.cc

```cpp

{% raw %}
74 | #ifdef _WIN32
75 |   FARPROC func_handle = GetProcAddress(static_cast<HMODULE>(lib_handle), name);
76 | #else
77 |   void* func_handle = dlsym(static_cast<void*>(lib_handle), name);
78 | #endif
79 |   return static_cast<HandleType>(func_handle);
{% endraw %}

```