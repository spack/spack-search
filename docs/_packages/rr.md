---
name: "rr"
layout: package
next_package: callflow
previous_package: gpdb
languages: ['cpp']
---
## 4.5.0
3 / 939 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [src/ThreadDb.cc](#srcthreaddbcc)
 - [src/test/dlopen.c](#srctestdlopenc)

### CMakeLists.txt

```

{% raw %}
804 |   dlopen
{% endraw %}

```
### src/ThreadDb.cc

```cpp

{% raw %}
215 |   thread_db_library = dlopen(LIBRARY_NAME, RTLD_NOW);
217 |     LOG(debug) << "load_library dlopen failed";
{% endraw %}

```
### src/test/dlopen.c

```cpp

{% raw %}
5 |   void* h = dlopen("libX11.so", RTLD_LAZY);
{% endraw %}

```