---
name: "zookeeper"
layout: package
next_package: pcre
previous_package: botan
languages: ['cpp']
---
## 3.4.11
6 / 1552 files match

 - [src/c/tests/LibCSymTable.cc](#srcctestslibcsymtablecc)

### src/c/tests/LibCSymTable.cc

```cpp

{% raw %}
75 |         handle=dlopen("cygwin1.dll",RTLD_LAZY);
76 |         assert("Unable to dlopen global sym table"&&handle);
{% endraw %}

```