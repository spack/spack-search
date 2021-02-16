---
name: "rr"
layout: package
next_package: callflow
previous_package: gpdb
languages: ['cpp', 'c']
---
## 4.5.0
3 / 939 files match

 - [src/ThreadDb.cc](#srcthreaddbcc)
 - [src/test/dlopen.c](#srctestdlopenc)

### src/ThreadDb.cc

```cpp

{% raw %}
215 |   thread_db_library = dlopen(LIBRARY_NAME, RTLD_NOW);
217 |     LOG(debug) << "load_library dlopen failed";
{% endraw %}

```
### src/test/dlopen.c

```c

{% raw %}
5 |   void* h = dlopen("libX11.so", RTLD_LAZY);
{% endraw %}

```