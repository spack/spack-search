---
name: "cppcheck"
layout: package
next_package: cpprestsdk
previous_package: conduit
languages: ['c']
---
## 1.87
2 / 610 files match, 1 filtered matches.

 - [test/cfg/posix.c](#testcfgposixc)

### test/cfg/posix.c

```c

{% raw %}
334 | 
335 | void dl(const char* libname, const char* func)
336 | {
337 |     void* lib = dlopen(libname, RTLD_NOW);
338 |     // cppcheck-suppress resourceLeak
339 |     // cppcheck-suppress redundantAssignment
340 |     lib = dlopen(libname, RTLD_LAZY);
341 |     const char* funcname;
342 |     // cppcheck-suppress uninitvar
{% endraw %}

```