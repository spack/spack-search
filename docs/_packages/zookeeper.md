---
name: "zookeeper"
layout: package
next_package: zsh
previous_package: zfs
languages: ['cpp']
---
## 3.4.11
6 / 1552 files match, 1 filtered matches.

 - [src/c/tests/LibCSymTable.cc](#srcctestslibcsymtablecc)

### src/c/tests/LibCSymTable.cc

```cpp

{% raw %}
72 |     static void* handle=0;
73 |     if(!handle){
74 | #ifdef __CYGWIN__
75 |         handle=dlopen("cygwin1.dll",RTLD_LAZY);
76 |         assert("Unable to dlopen global sym table"&&handle);
77 | #else
78 |         handle=RTLD_NEXT;
{% endraw %}

```