---
name: "nim"
layout: package
next_package: opari2
previous_package: biobloom
languages: ['c']
---
## 0.19.6
9 / 7503 files match, 1 filtered matches.

 - [tests/realtimeGC/cmain.c](#testsrealtimegccmainc)

### tests/realtimeGC/cmain.c

```c

{% raw %}
31 |     hndl = (void*) dlopen((char const*)"./tests/realtimeGC/libshared.so", RTLD_LAZY);
{% endraw %}

```