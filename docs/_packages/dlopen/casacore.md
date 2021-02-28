---
name: "casacore"
layout: package
next_package: openloops
previous_package: stat
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 3.3.0
3 / 3213 files match, 1 filtered matches.

 - [casa/OS/DynLib.cc](#casaosdynlibcc)

### casa/OS/DynLib.cc

```cpp

{% raw %}
106 |   void DynLib::open (const std::string& name)
107 |   {
108 | #ifdef HAVE_DLOPEN
109 |     itsHandle = dlopen (name.c_str(), RTLD_NOW | RTLD_GLOBAL);
110 |     if (itsHandle == 0) {
111 |       itsError += string(dlerror()) + '\n';
{% endraw %}

```