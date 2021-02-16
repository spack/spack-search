---
name: "sst-macro"
layout: package
next_package: stacks
previous_package: sst-core
languages: ['cpp', 'c']
---
## 10.1.0
55 / 2421 files match, 6 filtered matches.

 - [sstmac/main/loadlib.cc](#sstmacmainloadlibcc)
 - [sstmac/software/launch/app_launcher.cc](#sstmacsoftwarelaunchapp_launchercc)
 - [sstmac/software/process/global.cc](#sstmacsoftwareprocessglobalcc)
 - [sstmac/software/process/app.h](#sstmacsoftwareprocessapph)
 - [sstmac/software/process/app.cc](#sstmacsoftwareprocessappcc)
 - [sstmac/replacements/dlfcn.h](#sstmacreplacementsdlfcnh)

### sstmac/main/loadlib.cc

```cpp

{% raw %}
106 |   void* handle = dlopen(fullpath.c_str(), RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### sstmac/software/launch/app_launcher.cc

```cpp

{% raw %}
81 |     App::dlopenCheck(lreq->aid(), app_params);
{% endraw %}

```
### sstmac/software/process/global.cc

```cpp

{% raw %}
190 | extern "C" void *sstmac_dlopen(const char* filename, int flag)
192 |   void* ret = dlopen(filename, flag);
{% endraw %}

```
### sstmac/software/process/app.h

```c

{% raw %}
229 |   static void dlopenCheck(int aid, SST::Params& params, bool check_name = true);
295 |   struct dlopen_entry {
300 |     dlopen_entry() : handle(nullptr), refcount(0), loaded(false) {}
303 |   static std::map<int, dlopen_entry> dlopens_;
{% endraw %}

```
### sstmac/software/process/app.cc

```cpp

{% raw %}
113 | std::map<int, App::dlopen_entry> App::dlopens_;
145 | static thread_lock dlopen_lock;
150 |   dlopen_entry& entry = dlopens_[aid];
161 | App::dlopenCheck(int aid, SST::Params& params, bool check_name)
164 |     dlopen_lock.lock();
166 |     dlopen_entry& entry = dlopens_[aid];
194 |     dlopen_lock.unlock();
203 |   dlopen_lock.lock();
204 |   auto iter = dlopens_.find(aid);
205 |   if (iter != dlopens_.end()){
206 |     dlopen_entry& entry = iter->second;
210 |       dlopens_.erase(iter);
213 |   dlopen_lock.unlock();
{% endraw %}

```
### sstmac/replacements/dlfcn.h

```c

{% raw %}
55 | void *sstmac_dlopen(const char *filename, int flag);
{% endraw %}

```