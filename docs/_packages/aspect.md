---
name: "aspect"
layout: package
next_package: lua-luaposix
previous_package: julia
languages: ['cpp']
---
## 2.0.0
2 / 1995 files match

 - [CMakeLists.txt](#cmakeliststxt)
 - [source/main.cc](#sourcemaincc)

### CMakeLists.txt

```

{% raw %}
232 |   void *handle = dlopen (\"somelib.so\", RTLD_LAZY);
235 | " HAVE_DLOPEN)
238 | IF (NOT HAVE_DLOPEN)
239 |   MESSAGE(STATUS "dlopen() test failed, disabling dynamic plugin loading")
291 |   # some systems need to explicitly link to some libraries to use dlopen
{% endraw %}

```
### source/main.cc

```cpp

{% raw %}
204 | // dlopen them so that we can load plugins declared in them
231 |           void *handle = dlopen (shared_libs_list[i].c_str(), RTLD_LAZY);
{% endraw %}

```