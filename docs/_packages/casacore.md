---
name: "casacore"
layout: package
next_package: catalyst
previous_package: care
languages: ['cpp']
---
## 3.3.0
3 / 3213 files match, 1 filtered matches.

 - [casa/OS/DynLib.cc](#casaosdynlibcc)

### casa/OS/DynLib.cc

```cpp

{% raw %}
109 |     itsHandle = dlopen (name.c_str(), RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```