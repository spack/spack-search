---
name: "sst-macro"
layout: package
next_package: sst-transports
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
103 |   // This is a little weird, but always try the last path - if we
104 |   // didn't succeed in the stat, we'll get a file not found error
105 |   // from dlopen, which is a useful error message for the user.
106 |   void* handle = dlopen(fullpath.c_str(), RTLD_NOW|RTLD_LOCAL);
107 |   if (NULL == handle) {
108 |     spkt_abort_printf("Opening library %s failed\n:%s", libname.c_str(), dlerror());
{% endraw %}

```
### sstmac/software/launch/app_launcher.cc

```cpp

{% raw %}
78 | 
79 |     SoftwareId sid(lreq->aid(), lreq->tid());
80 |     SST::Params app_params = lreq->appParams();
81 |     App::dlopenCheck(lreq->aid(), app_params);
82 |     auto app_name = app_params.find<std::string>("name");
83 |     App* theapp = sprockit::create<App>("macro", app_name, app_params, sid, os_);
{% endraw %}

```
### sstmac/software/process/global.cc

```cpp

{% raw %}
187 | 
188 | #include <dlfcn.h>
189 | 
190 | extern "C" void *sstmac_dlopen(const char* filename, int flag)
191 | {
192 |   void* ret = dlopen(filename, flag);
193 |   return ret;
194 | }
{% endraw %}

```
### sstmac/software/process/app.h

```c

{% raw %}
226 |     unique_name_ = name;
227 |   }
228 | 
229 |   static void dlopenCheck(int aid, SST::Params& params, bool check_name = true);
230 | 
231 |   static void dlcloseCheck(int aid);
292 | 
293 |   int rc_;
294 | 
295 |   struct dlopen_entry {
296 |     void* handle;
297 |     int refcount;
298 |     bool loaded;
299 |     std::string name;
300 |     dlopen_entry() : handle(nullptr), refcount(0), loaded(false) {}
301 |   };
302 | 
303 |   static std::map<int, dlopen_entry> dlopens_;
304 | 
305 |   static int app_rc_;
{% endraw %}

```
### sstmac/software/process/app.cc

```cpp

{% raw %}
110 | std::map<std::string, App::empty_main_fxn>* UserAppCxxEmptyMain::empty_main_fxns_init_ = nullptr;
111 | std::map<AppId, UserAppCxxFullMain::argv_entry> UserAppCxxFullMain::argv_map_;
112 | 
113 | std::map<int, App::dlopen_entry> App::dlopens_;
114 | int App::app_rc_ = 0;
115 | 
142 | }
143 | 
144 | 
145 | static thread_lock dlopen_lock;
146 | 
147 | void
148 | App::lockDlopen(int aid)
149 | {
150 |   dlopen_entry& entry = dlopens_[aid];
151 |   entry.refcount++;
152 | }
158 | }
159 | 
160 | void
161 | App::dlopenCheck(int aid, SST::Params& params, bool check_name)
162 | {
163 |   if (params.contains("exe")){
164 |     dlopen_lock.lock();
165 |     std::string libname = params.find<std::string>("exe");
166 |     dlopen_entry& entry = dlopens_[aid];
167 |     entry.name = libname;
168 |     if (entry.refcount == 0 || !entry.loaded){
191 | 
192 |     ++entry.refcount;
193 |     sstmac_app_loaded(aid);
194 |     dlopen_lock.unlock();
195 |   }
196 |   UserAppCxxEmptyMain::aliasMains();
200 | void
201 | App::dlcloseCheck(int aid)
202 | {
203 |   dlopen_lock.lock();
204 |   auto iter = dlopens_.find(aid);
205 |   if (iter != dlopens_.end()){
206 |     dlopen_entry& entry = iter->second;
207 |     --entry.refcount;
208 |     if (entry.refcount == 0 && entry.loaded){
209 |       unloadExternLibrary(entry.handle);
210 |       dlopens_.erase(iter);
211 |     }
212 |   }
213 |   dlopen_lock.unlock();
214 | }
215 | 
{% endraw %}

```
### sstmac/replacements/dlfcn.h

```c

{% raw %}
52 | extern "C" {
53 | #endif
54 | 
55 | void *sstmac_dlopen(const char *filename, int flag);
56 | 
57 | #ifdef __cplusplus
{% endraw %}

```