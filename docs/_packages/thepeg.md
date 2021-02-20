---
name: "thepeg"
layout: package
next_package: timemory
previous_package: tengine
languages: ['cpp']
---
## 2.2.1
7 / 917 files match, 1 filtered matches.

 - [Utilities/DynamicLoader.cc](#utilitiesdynamicloadercc)

### Utilities/DynamicLoader.cc

```cpp

{% raw %}
73 | #ifdef ThePEG_HAS_FENV
74 |   int oldfpe = fegetexcept();
75 | #endif
76 |   bool ret = dlopen(file.c_str(), RTLD_LAZY|RTLD_GLOBAL) != 0;
77 | #ifdef ThePEG_HAS_FENV
78 |   feenableexcept(oldfpe);
{% endraw %}

```