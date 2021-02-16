---
name: "cppcheck"
layout: package
next_package: ffmpeg
previous_package: rocksdb
languages: ['c']
---
## 1.87
2 / 610 files match, 1 filtered matches.

 - [test/cfg/posix.c](#testcfgposixc)

### test/cfg/posix.c

```c

{% raw %}
337 |     void* lib = dlopen(libname, RTLD_NOW);
340 |     lib = dlopen(libname, RTLD_LAZY);
{% endraw %}

```