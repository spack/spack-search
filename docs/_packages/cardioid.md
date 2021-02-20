---
name: "cardioid"
layout: package
next_package: care
previous_package: caliper
languages: ['cpp']
---
## elecfem
1 / 1451 files match, 1 filtered matches.

 - [elec/reactionFactory.cc](#elecreactionfactorycc)

### elec/reactionFactory.cc

```cpp

{% raw %}
53 |    {
54 |       //try to load in the factory method
55 |       
56 |       void* handle = dlopen(filename.c_str(), RTLD_NOW|RTLD_LOCAL);
57 |       if (handle)
58 |       {
{% endraw %}

```