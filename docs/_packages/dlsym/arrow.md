---
name: "arrow"
layout: package
next_package: fio
previous_package: multiverso
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 0.9.0
1 / 1133 files match, 1 filtered matches.

 - [cpp/src/arrow/io/hdfs-internal.cc](#cppsrcarrowiohdfs-internalcc)

### cpp/src/arrow/io/hdfs-internal.cc

```cpp

{% raw %}
254 | static inline void* GetLibrarySymbol(void* handle, const char* symbol) {
255 |   if (handle == NULL) return NULL;
256 | #ifndef _WIN32
257 |   return dlsym(handle, symbol);
258 | #else
259 | 
{% endraw %}

```