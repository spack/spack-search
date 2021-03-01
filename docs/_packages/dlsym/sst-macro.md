---
name: "sst-macro"
layout: package
next_package: stat
previous_package: sqlite
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 10.1.0
5 / 2421 files match, 1 filtered matches.

 - [sstmac/software/process/app.cc](#sstmacsoftwareprocessappcc)

### sstmac/software/process/app.cc

```cpp

{% raw %}
171 |     }
172 | 
173 |     if (check_name){
174 |       void* name = dlsym(entry.handle, "exe_main_name");
175 |       if (name){
176 |         const char* str_name = (const char*) name;
{% endraw %}

```