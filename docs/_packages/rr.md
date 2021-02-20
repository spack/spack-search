---
name: "rr"
layout: package
next_package: rsem
previous_package: rose
languages: ['cpp', 'c']
---
## 4.5.0
3 / 939 files match, 2 filtered matches.

 - [src/ThreadDb.cc](#srcthreaddbcc)
 - [src/test/dlopen.c](#srctestdlopenc)

### src/ThreadDb.cc

```cpp

{% raw %}
212 |     return loaded;
213 |   }
214 | 
215 |   thread_db_library = dlopen(LIBRARY_NAME, RTLD_NOW);
216 |   if (!thread_db_library) {
217 |     LOG(debug) << "load_library dlopen failed";
218 |     return false;
219 |   }
{% endraw %}

```
### src/test/dlopen.c

```c

{% raw %}
2 | #include "rrutil.h"
3 | 
4 | int main(void) {
5 |   void* h = dlopen("libX11.so", RTLD_LAZY);
6 |   if (h) {
7 |     dlclose(h);
{% endraw %}

```