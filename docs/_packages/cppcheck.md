---
name: "cppcheck"
layout: package
next_package: ffmpeg
previous_package: rocksdb
languages: ['cpp']
---
## 1.87
2 / 610 files match

 - [cfg/posix.cfg](#cfgposixcfg)
 - [test/cfg/posix.c](#testcfgposixc)

### cfg/posix.cfg

```

{% raw %}
79 |     <alloc>dlopen</alloc>
117 |   <!-- see http://pubs.opengroup.org/onlinepubs/9699919799/functions/dlopen.html -->
118 |   <function name="dlopen">
{% endraw %}

```
### test/cfg/posix.c

```cpp

{% raw %}
337 |     void* lib = dlopen(libname, RTLD_NOW);
340 |     lib = dlopen(libname, RTLD_LAZY);
{% endraw %}

```